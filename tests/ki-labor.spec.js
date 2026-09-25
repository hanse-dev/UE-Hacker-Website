import { test, expect } from '@playwright/test';
import checks from '../content/ki-labor-checks/index.mjs';

// KI-Labor (Route /kurs/ki-labor, echter Kurs mit kurse.json-Eintrag, ueber CourseDetail.vue
// eingebunden wie js-grundkurs). 8 Wochen, siehe KURSPLAN.md "KI-Track: KI-Grundlagen". Nutzt
// dieselbe Wochenauswahl (KiLaborTour.vue, Kopie von JsGrundkursTour.vue) und dieselbe generische
// Wochen-Tour (JsCourseTour.vue), aber engine="pyodide" (LessonView.vue) statt js-sandbox - wie
// im 12-Wochen-Python-Kurs. Algorithmen werden komplett in reinem Python selbst geschrieben, kein
// scikit-learn. Bislang ist nur Woche 1 ("Was ist KI?") umgesetzt, Wochen 2-8 sind "kommt noch".
//
// Quiz + Zertifikat nutzen dasselbe System wie der 12-Wochen-Kurs (useWeekChecks.js/
// WeekCheckPanel.vue/CodeChallenge.vue/useCertificatePdf.js), jetzt um einen courseKey-Parameter
// generalisiert ('ki-labor' statt dem Default 'python') - eigener Storage-Key
// ('ue-hacker-week-checks-ki-labor') und eigener Content-Ordner (content/ki-labor-checks/), damit
// Woche 1 im KI-Labor nicht mit Woche 1 im Python-Kurs kollidiert (siehe HANDOFF.md).
const PROGRESS_KEY = 'ue-hacker-interactive-progress-ki-labor-woche1';
const PROGRESS_KEY_WEEK2 = 'ue-hacker-interactive-progress-ki-labor-woche2';

function findQuestion(text) {
  const normalized = text.replace(/^\d+\.\s*/, '').trim();
  for (const week of Object.values(checks.weeks)) {
    for (const q of week.questions) {
      if (q.question === normalized) return q;
    }
  }
  return null;
}

function correctOptionTexts(q) {
  if (q.type === 'multiple_select') return q.correctIndices.map((i) => q.options[i]);
  return [q.options[q.correctIndex]];
}

async function clickOptionByExactText(card, opt) {
  const buttons = card.locator('.option-btn');
  const count = await buttons.count();
  for (let i = 0; i < count; i++) {
    const text = (await buttons.nth(i).innerText()).replace(/^[☐☑]\s*/, '').trim();
    if (text === opt) {
      await buttons.nth(i).click();
      return;
    }
  }
  throw new Error(`Option not found: ${opt}`);
}

async function passWeekQuiz(page) {
  const cards = page.locator('.quiz-question');
  await expect(cards.first()).toBeVisible({ timeout: 20000 });
  const count = await cards.count();
  for (let i = 0; i < count; i++) {
    const card = cards.nth(i);
    const raw = await card.locator('.question-text').innerText();
    const q = findQuestion(raw);
    expect(q, `Unbekannte Frage: ${raw}`).toBeTruthy();
    for (const opt of correctOptionTexts(q)) {
      await clickOptionByExactText(card, opt);
    }
  }
  await page.locator('.btn-check-quiz').click();
}

async function passCodingChallenge(page, challengeIndex, code) {
  const challenge = page.locator(`.code-challenge[data-challenge-index="${challengeIndex}"]`);
  await challenge.locator('.btn-kernel').click({ force: true });
  await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });
  await challenge.locator('.code-editor').fill(code);
  await challenge.locator('.btn-check').click();
  await expect(challenge.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
}

test.describe('KI-Labor (Wochenauswahl)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem(key);
      localStorage.removeItem('ue-hacker-week-checks-ki-labor');
    }, PROGRESS_KEY);
  });

  test('Wochenauswahl: 8 Kacheln, Woche 1+2 verfügbar, Rest "kommt noch"', async ({ page }) => {
    await page.goto('/kurs/ki-labor');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.week-tile')).toHaveCount(8);
    await expect(page.locator('.week-tile').nth(0)).not.toBeDisabled();
    await expect(page.locator('.week-tile').nth(1)).not.toBeDisabled();
    for (let i = 2; i < 8; i++) {
      await expect(page.locator('.week-tile').nth(i)).toBeDisabled();
    }
    await expect(page.locator('.week-tile-badge')).toHaveCount(6);
  });

  test('Woche 1 anklicken öffnet die Wochen-Tour, "Andere Woche wählen" führt zurück', async ({ page }) => {
    await page.goto('/kurs/ki-labor');
    await page.locator('.btn-start-course').click();
    await page.locator('.week-tile').nth(0).click();
    // 10 Lektionen (5 Lektion + Debug + Mission + 3 Extra-Herausforderung) + 1 Check-Punkt, da
    // content/ki-labor-checks/week-1.json existiert (hasCheck=true).
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');

    await page.locator('.breadcrumb-back').click();
    await expect(page.locator('.week-tile')).toHaveCount(8);
    await expect(page.locator('.stepper-step')).toHaveCount(0);
  });

  test('Deep-Link ?week=1 öffnet direkt die Wochen-Tour, gruppierte Kullern Lektion/Debug/Mission/Extra-Herausforderung/Check', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=1');
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Was ist KI?');

    const groupLabels = page.locator('.stepper-group-label');
    await expect(groupLabels).toHaveCount(5);
    await expect(groupLabels.nth(0)).toHaveText(/lektion/i);
    await expect(groupLabels.nth(1)).toHaveText(/debug/i);
    await expect(groupLabels.nth(2)).toHaveText(/mission/i);
    await expect(groupLabels.nth(3)).toHaveText(/extra-herausforderung/i);
    await expect(page.locator('[data-open-check]')).toBeVisible();
  });

  test('Deep-Link ?week=2 öffnet direkt die Wochen-Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=2');
    // 10 Lektionen (5 Lektion + Debug + Mission + 3 Extra-Herausforderung) + 1 Check-Punkt, da
    // content/ki-labor-checks/week-2.json existiert (hasCheck=true).
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 2');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Daten sind alles');
  });

  test('Deep-Link ?week=3 (noch nicht verfügbar) zeigt die Wochenauswahl statt der Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=3');
    await expect(page.locator('.week-tile')).toHaveCount(8);
    await expect(page.locator('.stepper-step')).toHaveCount(0);
  });

  async function initKernel(page) {
    await page.locator('.btn-kernel').click({ force: true });
    await expect(page.locator('.btn-kernel')).toBeDisabled({ timeout: 60000 });
  }

  // codes[i] === null: Beispiel-Aufgabe (nur "Ausfuehren", kein "Pruefen"), sonst Loesung + Pruefen.
  async function solve(page, codes) {
    for (let i = 0; i < codes.length; i++) {
      const task = page.locator('.task-block').nth(i);
      if (codes[i] === null) {
        await expect(task.locator('.btn-check')).toHaveCount(0);
        await task.locator('.btn-run').click();
        await expect(task.locator('.task-done')).toBeVisible({ timeout: 10000 });
        continue;
      }
      await task.locator('.code-editor').fill(codes[i]);
      await task.locator('.btn-check').click();
      await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
    }
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  }

  test('Lektion 1: falsche Loesung schlaegt fehl, richtige besteht', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=1');
    await initKernel(page);
    const task2 = page.locator('.task-block').nth(2);
    await task2.locator('.code-editor').fill('def ist_bestanden(punkte):\n    return "falsch"');
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await task2.locator('.code-editor').fill(
      'def ist_bestanden(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    else:\n        return "nicht bestanden"\n\nprint(ist_bestanden(70))\nprint(ist_bestanden(30))'
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Debug-Lektion: kaputter Code besteht erst nach dem Fix', async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, PROGRESS_KEY);
    await page.goto('/kurs/ki-labor?week=1');
    await page.locator('.stepper-step').nth(5).click();
    await initKernel(page);

    const first = page.locator('.task-block').first();
    await first.locator('.btn-check').click();
    await expect(first.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await solve(page, [
      'def einschaetzung(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    else:\n        return "nicht heiß"\n\nprint(einschaetzung(30))',
      'def ist_bestanden(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    else:\n        return "nicht bestanden"\n\nprint(ist_bestanden(50))',
      'def note_beschreibung(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    elif punkte >= 0:\n        return "mangelhaft"\n    else:\n        return "unbekannt"\n\nprint(note_beschreibung(80))',
    ]);
  });

  test('Kompletter Durchlauf Woche 1: alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/ki-labor?week=1');
    await initKernel(page);

    await solve(page, [
      null,
      null,
      'def ist_bestanden(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    else:\n        return "nicht bestanden"\n\nprint(ist_bestanden(70))\nprint(ist_bestanden(30))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await solve(page, [
      null,
      null,
      'def klassifiziere_tier(beine):\n    if beine == 4:\n        return "Vierbeiner"\n    elif beine == 2:\n        return "Zweibeiner"\n    elif beine == 6:\n        return "Insekt"\n    elif beine == 8:\n        return "Spinnentier"\n    elif beine == 0:\n        return "Ohne Beine"\n    else:\n        return "Unbekannt"\n\nprint(klassifiziere_tier(0))\nprint(klassifiziere_tier(100))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await solve(page, [
      null,
      'def finde_antwort(frage, beispiele):\n    for eingabe, antwort in beispiele:\n        if eingabe == frage:\n            return antwort\n    return "unbekannt"\n\neigene_beispiele = [("apfel", "Obst"), ("karotte", "Gemüse"), ("banane", "Obst")]\nprint(finde_antwort("apfel", eigene_beispiele))\nprint(finde_antwort("brot", eigene_beispiele))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await solve(page, [
      null,
      'eigenes_modell = {"hund": "Tier", "katze": "Tier", "rose": "Pflanze"}\nprint(eigenes_modell.get("hund", "unbekannt"))\nprint(eigenes_modell.get("auto", "unbekannt"))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await solve(page, [
      null,
      'def vorhersage_sicherheit(modell, eingabe):\n    if eingabe in modell:\n        return f"Sicher: {modell[eingabe]}"\n    else:\n        return "Unsicher: unbekannt"\n\nmein_modell = {"sonne": "Stern"}\nprint(vorhersage_sicherheit(mein_modell, "sonne"))\nprint(vorhersage_sicherheit(mein_modell, "mond"))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await solve(page, [
      'def einschaetzung(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    else:\n        return "nicht heiß"\n\nprint(einschaetzung(30))',
      'def ist_bestanden(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    else:\n        return "nicht bestanden"\n\nprint(ist_bestanden(50))',
      'def note_beschreibung(punkte):\n    if punkte >= 50:\n        return "bestanden"\n    elif punkte >= 0:\n        return "mangelhaft"\n    else:\n        return "unbekannt"\n\nprint(note_beschreibung(80))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await solve(page, [
      'def temperatur_gefuehl(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    elif temperatur < 5:\n        return "kalt"\n    else:\n        return "mild"\n\nprint(f"Gefühl: {temperatur_gefuehl(30)}")\nprint(f"Gefühl: {temperatur_gefuehl(2)}")',
      'def kleidungs_tipp(temperatur, regen):\n    if regen:\n        return "Regenjacke"\n    elif temperatur > 25:\n        return "T-Shirt"\n    elif temperatur < 5:\n        return "Winterjacke"\n    else:\n        return "Pullover"\n\nprint(f"Tipp: {kleidungs_tipp(30, False)}")\nprint(f"Tipp: {kleidungs_tipp(2, True)}")',
      'def temperatur_gefuehl(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    elif temperatur < 5:\n        return "kalt"\n    else:\n        return "mild"\n\ndef kleidungs_tipp(temperatur, regen):\n    if regen:\n        return "Regenjacke"\n    elif temperatur > 25:\n        return "T-Shirt"\n    elif temperatur < 5:\n        return "Winterjacke"\n    else:\n        return "Pullover"\n\ndef wetterbericht(temperatur, regen):\n    gefuehl = temperatur_gefuehl(temperatur)\n    tipp = kleidungs_tipp(temperatur, regen)\n    return f"Es ist {gefuehl}. Trage: {tipp}"\n\nprint(wetterbericht(30, False))\nprint(wetterbericht(2, True))',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();

    // Mission abgeschlossen, danach folgt ein Boss-Abschnitt (Extra-Herausforderung) UND ein
    // Check -> "Weiter" zeigt eine Wahl-Seite statt direkt zum Check zu springen.
    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="check"]').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });
  });

  test('Extra-Herausforderung: Wahl-Seite führt zu den 3 Boss-Lektionen, alle 3 loesen schaltet den Check frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05', 'debug-01'],
      }));
    }, PROGRESS_KEY);
    await page.goto('/kurs/ki-labor?week=1');
    // Mission (noch nicht abgeschlossen) frisch lösen, das triggert onLessonCompleted -> Wahl-Seite.
    await page.locator('.stepper-step').nth(6).click();
    await initKernel(page);
    await solve(page, [
      'def temperatur_gefuehl(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    elif temperatur < 5:\n        return "kalt"\n    else:\n        return "mild"\n\nprint(f"Gefühl: {temperatur_gefuehl(30)}")\nprint(f"Gefühl: {temperatur_gefuehl(2)}")',
      'def kleidungs_tipp(temperatur, regen):\n    if regen:\n        return "Regenjacke"\n    elif temperatur > 25:\n        return "T-Shirt"\n    elif temperatur < 5:\n        return "Winterjacke"\n    else:\n        return "Pullover"\n\nprint(f"Tipp: {kleidungs_tipp(30, False)}")\nprint(f"Tipp: {kleidungs_tipp(2, True)}")',
      'def temperatur_gefuehl(temperatur):\n    if temperatur > 25:\n        return "heiß"\n    elif temperatur < 5:\n        return "kalt"\n    else:\n        return "mild"\n\ndef kleidungs_tipp(temperatur, regen):\n    if regen:\n        return "Regenjacke"\n    elif temperatur > 25:\n        return "T-Shirt"\n    elif temperatur < 5:\n        return "Winterjacke"\n    else:\n        return "Pullover"\n\ndef wetterbericht(temperatur, regen):\n    gefuehl = temperatur_gefuehl(temperatur)\n    tipp = kleidungs_tipp(temperatur, regen)\n    return f"Es ist {gefuehl}. Trage: {tipp}"\n\nprint(wetterbericht(30, False))\nprint(wetterbericht(2, True))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="boss"]').click();

    await solve(page, [
      'def note(punkte):\n    if punkte >= 90:\n        return "A"\n    elif punkte >= 75:\n        return "B"\n    elif punkte >= 60:\n        return "C"\n    elif punkte >= 40:\n        return "D"\n    else:\n        return "F"\n\nprint(note(95))\nprint(note(65))\nprint(note(10))',
      'def note(punkte):\n    if punkte >= 90:\n        return "A"\n    elif punkte >= 75:\n        return "B"\n    elif punkte >= 60:\n        return "C"\n    elif punkte >= 40:\n        return "D"\n    else:\n        return "F"\n\ndef bestehensquote(punkte_liste):\n    bestanden = 0\n    for punkte in punkte_liste:\n        if note(punkte) != "F":\n            bestanden += 1\n    return round(bestanden / len(punkte_liste) * 100)\n\nprint(bestehensquote([95, 65, 10, 80]))',
      'def note(punkte):\n    if punkte >= 90:\n        return "A"\n    elif punkte >= 75:\n        return "B"\n    elif punkte >= 60:\n        return "C"\n    elif punkte >= 40:\n        return "D"\n    else:\n        return "F"\n\ndef bestehensquote(punkte_liste):\n    bestanden = 0\n    for punkte in punkte_liste:\n        if note(punkte) != "F":\n            bestanden += 1\n    return round(bestanden / len(punkte_liste) * 100)\n\ndef zusammenfassung(punkte, punkte_liste):\n    eigene_note = note(punkte)\n    quote = bestehensquote(punkte_liste)\n    return f"Note: {eigene_note}, Klasse bestanden: {quote}%"\n\nprint(zusammenfassung(95, [95, 65, 10, 80]))',
    ]);
    await page.locator('.btn-next').click();

    await solve(page, [
      'beispiele = [("hund", "Tier"), ("katze", "Tier"), ("spinne", "Tier"), ("rose", "Pflanze"), ("baum", "Pflanze")]\n\ndef finde_antwort(frage, beispiele):\n    for eingabe, antwort in beispiele:\n        if eingabe == frage:\n            return antwort\n    return "unbekannt"\n\nprint(finde_antwort("hund", beispiele))\nprint(finde_antwort("stein", beispiele))',
      'beispiele = [("hund", "Tier"), ("katze", "Tier"), ("spinne", "Tier"), ("rose", "Pflanze"), ("baum", "Pflanze")]\n\ndef zaehle_kategorie(beispiele, kategorie):\n    anzahl = 0\n    for eingabe, antwort in beispiele:\n        if antwort == kategorie:\n            anzahl += 1\n    return anzahl\n\nprint(zaehle_kategorie(beispiele, "Tier"))\nprint(zaehle_kategorie(beispiele, "Pflanze"))',
      'beispiele = [("hund", "Tier"), ("katze", "Tier"), ("spinne", "Tier"), ("rose", "Pflanze"), ("baum", "Pflanze")]\n\ndef zaehle_kategorie(beispiele, kategorie):\n    anzahl = 0\n    for eingabe, antwort in beispiele:\n        if antwort == kategorie:\n            anzahl += 1\n    return anzahl\n\ndef haeufigste_kategorie(beispiele):\n    kategorien = set(antwort for _, antwort in beispiele)\n    beste = None\n    bester_wert = -1\n    for kategorie in kategorien:\n        anzahl = zaehle_kategorie(beispiele, kategorie)\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste = kategorie\n    return beste\n\nprint(haeufigste_kategorie(beispiele))',
    ]);
    await page.locator('.btn-next').click();

    await solve(page, [
      'modell = {"hund": "Tier", "katze": "Tier", "rose": "Pflanze", "baum": "Pflanze"}\n\ndef vorhersage_sicherheit(modell, eingabe):\n    if eingabe in modell:\n        return f"Sicher: {modell[eingabe]}"\n    else:\n        return "Unsicher: unbekannt"\n\nprint(vorhersage_sicherheit(modell, "hund"))\nprint(vorhersage_sicherheit(modell, "vogel"))',
      'modell = {"hund": "Tier", "katze": "Tier", "rose": "Pflanze", "baum": "Pflanze"}\n\ndef teste_modell(modell, testfaelle):\n    richtig = 0\n    for eingabe, erwartet in testfaelle:\n        if modell.get(eingabe, "unbekannt") == erwartet:\n            richtig += 1\n    return richtig\n\nprint(teste_modell(modell, [("hund", "Tier"), ("rose", "Pflanze"), ("vogel", "Tier")]))',
      'modell = {"hund": "Tier", "katze": "Tier", "rose": "Pflanze", "baum": "Pflanze"}\n\ndef teste_modell(modell, testfaelle):\n    richtig = 0\n    for eingabe, erwartet in testfaelle:\n        if modell.get(eingabe, "unbekannt") == erwartet:\n            richtig += 1\n    return richtig\n\ndef genauigkeit(modell, testfaelle):\n    richtig = teste_modell(modell, testfaelle)\n    prozent = round(richtig / len(testfaelle) * 100)\n    return f"Genauigkeit: {prozent}%"\n\nprint(genauigkeit(modell, [("hund", "Tier"), ("rose", "Pflanze"), ("vogel", "Tier")]))',
    ]);
    // Letzte Lektion (boss-03) abgeschlossen, kein weiterer Boss -> "Weiter" springt direkt zum
    // Wochen-Check (kein Mission->Boss-Uebergang mehr, also keine erneute Wahl-Seite).
    await page.locator('.btn-next').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });
  });

  test('Wochen-Check: Quiz allein reicht nicht, Quiz + beide Coding-Aufgaben verleiht das Zertifikat', async ({ page }) => {
    test.setTimeout(60000);
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05', 'debug-01', 'mission-01'],
      }));
    }, PROGRESS_KEY);
    await page.goto('/kurs/ki-labor?week=1');
    await page.locator('[data-open-check]').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    await passWeekQuiz(page);
    await expect(page.locator('.certificate-reveal')).toHaveCount(0);

    await passCodingChallenge(page, 0, 'def ist_erwachsen(alter):\n    return alter >= 18\n\nprint(ist_erwachsen(20))\nprint(ist_erwachsen(15))');
    await expect(page.locator('.certificate-reveal')).toHaveCount(0);

    await passCodingChallenge(
      page,
      1,
      'modell = {"hund": "Tier", "baum": "Pflanze"}\n\ndef klassifiziere(eingabe, modell):\n    return modell.get(eingabe, "unbekannt")\n\nprint(klassifiziere("hund", modell))\nprint(klassifiziere("stein", modell))'
    );

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.certificate-login-hint')).toBeVisible();
    await expect(page.locator('.btn-certificate-pdf')).toHaveCount(0);
  });

  test('Woche 2: Debug-Lektion mit fehlendem return/falschem Vergleich/fehlendem .get()-Standardwert', async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, PROGRESS_KEY_WEEK2);
    await page.goto('/kurs/ki-labor?week=2');
    await page.locator('.stepper-step').nth(5).click();
    await initKernel(page);

    const first = page.locator('.task-block').first();
    await first.locator('.btn-check').click();
    await expect(first.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await solve(page, [
      'def durchschnittsgewicht(tiere):\n    summe = 0\n    for tier in tiere:\n        summe += tier["gewicht"]\n    return summe / len(tiere)\n\ntiere = [{"gewicht": 10}, {"gewicht": 20}, {"gewicht": 30}]\nprint(durchschnittsgewicht(tiere))',
      'def zaehle_vierbeiner(tiere):\n    anzahl = 0\n    for tier in tiere:\n        if tier["beine"] >= 4:\n            anzahl += 1\n    return anzahl\n\ntiere = [{"beine": 4}, {"beine": 4}, {"beine": 2}]\nprint(zaehle_vierbeiner(tiere))',
      'def gewicht_oder_unbekannt(tier):\n    return tier.get("gewicht", "unbekannt")\n\nvogel = {"name": "Spatz"}\nprint(gewicht_oder_unbekannt(vogel))',
    ]);
  });

  test('Kompletter Durchlauf Woche 2: alle Lektionen, Extra-Herausforderungen und der Wochen-Check', async ({ page }) => {
    test.setTimeout(120000);
    await page.goto('/kurs/ki-labor?week=2');
    await initKernel(page);

    await solve(page, [null, null, 'fahrzeuge = [{"name": "Auto", "raeder": 4}, {"name": "Motorrad", "raeder": 2}, {"name": "Lkw", "raeder": 6}]\nfor f in fahrzeuge:\n    print(f"{f[\'name\']} hat {f[\'raeder\']} Räder")']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await solve(page, [null, null, 'personen = [{"name": "Anna", "alter": 12, "grosse": 150}, {"name": "Ben", "alter": 15, "grosse": 170}]\nfor p in personen:\n    print(f"{p[\'name\']}: {p[\'alter\']} Jahre, {p[\'grosse\']}cm")']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await solve(page, [null, null, 'schueler = [{"name": "Anna", "note": 2}, {"name": "Ben", "note": 4}, {"name": "Cem", "note": 1}]\nprint([s["name"] for s in schueler if s["note"] < 3])']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await solve(page, [null, null, 'autos = [{"marke": "VW", "ps": 90}, {"marke": "Audi"}, {"marke": "BMW", "ps": 150}]\nfor a in autos:\n    print(f"{a[\'marke\']}: {a.get(\'ps\', \'unbekannt\')}")']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await solve(page, [null, null, 'pflanzen = [{"hoehe": 30, "typ": "Blume"}, {"hoehe": 200, "typ": "Baum"}, {"hoehe": 15, "typ": "Blume"}]\nhoehen = [p["hoehe"] for p in pflanzen]\ntypen = [p["typ"] for p in pflanzen]\nprint(hoehen)\nprint(typen)']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await solve(page, [
      'def durchschnittsgewicht(tiere):\n    summe = 0\n    for tier in tiere:\n        summe += tier["gewicht"]\n    return summe / len(tiere)\n\ntiere = [{"gewicht": 10}, {"gewicht": 20}, {"gewicht": 30}]\nprint(durchschnittsgewicht(tiere))',
      'def zaehle_vierbeiner(tiere):\n    anzahl = 0\n    for tier in tiere:\n        if tier["beine"] >= 4:\n            anzahl += 1\n    return anzahl\n\ntiere = [{"beine": 4}, {"beine": 4}, {"beine": 2}]\nprint(zaehle_vierbeiner(tiere))',
      'def gewicht_oder_unbekannt(tier):\n    return tier.get("gewicht", "unbekannt")\n\nvogel = {"name": "Spatz"}\nprint(gewicht_oder_unbekannt(vogel))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await solve(page, [
      'tiere = [{"name": "Hund", "beine": 4, "gewicht": 30}, {"name": "Spatz", "beine": 2, "gewicht": 0.03}, {"name": "Biene", "beine": 6, "gewicht": 0.001}]\ndef namen_liste(tiere):\n    return [t["name"] for t in tiere]\n\nprint(namen_liste(tiere))',
      'tiere = [{"name": "Hund", "beine": 4, "gewicht": 30}, {"name": "Spatz", "beine": 2, "gewicht": 0.03}, {"name": "Biene", "beine": 6, "gewicht": 0.001}]\ndef durchschnitt(tiere, merkmal):\n    summe = 0\n    for t in tiere:\n        summe += t[merkmal]\n    return summe / len(tiere)\n\nprint(durchschnitt(tiere, "beine"))',
      'tiere = [{"name": "Hund", "beine": 4, "gewicht": 30}, {"name": "Spatz", "beine": 2, "gewicht": 0.03}, {"name": "Biene", "beine": 6, "gewicht": 0.001}]\ndef ueber_schwelle(tiere, merkmal, schwelle):\n    return [t["name"] for t in tiere if t[merkmal] > schwelle]\n\nprint(ueber_schwelle(tiere, "gewicht", 1))',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');

    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="boss"]').click();

    await solve(page, [
      'def maximum(tiere, merkmal):\n    hoechster = tiere[0][merkmal]\n    for tier in tiere:\n        if tier[merkmal] > hoechster:\n            hoechster = tier[merkmal]\n    return hoechster\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz", "beine": 2}, {"name": "Spinne", "beine": 8}]\nprint(maximum(tiere, "beine"))',
      'def minimum(tiere, merkmal):\n    kleinster = tiere[0][merkmal]\n    for tier in tiere:\n        if tier[merkmal] < kleinster:\n            kleinster = tier[merkmal]\n    return kleinster\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz", "beine": 2}, {"name": "Spinne", "beine": 8}]\nprint(minimum(tiere, "beine"))',
      'def maximum(tiere, merkmal):\n    hoechster = tiere[0][merkmal]\n    for tier in tiere:\n        if tier[merkmal] > hoechster:\n            hoechster = tier[merkmal]\n    return hoechster\n\ndef minimum(tiere, merkmal):\n    kleinster = tiere[0][merkmal]\n    for tier in tiere:\n        if tier[merkmal] < kleinster:\n            kleinster = tier[merkmal]\n    return kleinster\n\ndef spannweite(tiere, merkmal):\n    return maximum(tiere, merkmal) - minimum(tiere, merkmal)\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz", "beine": 2}, {"name": "Spinne", "beine": 8}]\nprint(spannweite(tiere, "beine"))',
    ]);
    await page.locator('.btn-next').click();

    await solve(page, [
      'def zaehle_uebereinstimmungen(a, b):\n    anzahl = 0\n    for schluessel in a:\n        if schluessel in b and a[schluessel] == b[schluessel]:\n            anzahl += 1\n    return anzahl\n\na = {"beine": 4, "farbe": "braun", "laut": "Wuff"}\nb = {"beine": 4, "farbe": "braun", "laut": "Miau"}\nprint(zaehle_uebereinstimmungen(a, b))',
      'def zaehle_uebereinstimmungen(a, b):\n    anzahl = 0\n    for schluessel in a:\n        if schluessel in b and a[schluessel] == b[schluessel]:\n            anzahl += 1\n    return anzahl\n\ndef aehnlichstes_tier(ziel, tiere):\n    bestes = None\n    beste_anzahl = -1\n    for tier in tiere:\n        anzahl = zaehle_uebereinstimmungen(ziel, tier)\n        if anzahl > beste_anzahl:\n            beste_anzahl = anzahl\n            bestes = tier["name"]\n    return bestes\n\ntiere = [{"name": "Katze", "beine": 4, "farbe": "schwarz"}, {"name": "Hund", "beine": 4, "farbe": "braun"}]\nziel = {"beine": 4, "farbe": "braun"}\nprint(aehnlichstes_tier(ziel, tiere))',
      'def zaehle_uebereinstimmungen(a, b):\n    anzahl = 0\n    for schluessel in a:\n        if schluessel in b and a[schluessel] == b[schluessel]:\n            anzahl += 1\n    return anzahl\n\ndef aehnlichkeit_prozent(a, b):\n    anzahl = zaehle_uebereinstimmungen(a, b)\n    return round(anzahl / len(a) * 100)\n\na = {"beine": 4, "farbe": "braun", "laut": "Wuff"}\nb = {"beine": 4, "farbe": "braun", "laut": "Miau"}\nprint(aehnlichkeit_prozent(a, b))',
    ]);
    await page.locator('.btn-next').click();

    await solve(page, [
      'def fehlt_merkmal(tiere, merkmal):\n    return [t["name"] for t in tiere if merkmal not in t]\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz"}, {"name": "Biene", "beine": 6}]\nprint(fehlt_merkmal(tiere, "beine"))',
      'def fehlt_merkmal(tiere, merkmal):\n    return [t["name"] for t in tiere if merkmal not in t]\n\ndef vollstaendigkeit(tiere, merkmal):\n    fehlend = len(fehlt_merkmal(tiere, merkmal))\n    return round((len(tiere) - fehlend) / len(tiere) * 100)\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz"}, {"name": "Biene", "beine": 6}]\nprint(vollstaendigkeit(tiere, "beine"))',
      'def fehlt_merkmal(tiere, merkmal):\n    return [t["name"] for t in tiere if merkmal not in t]\n\ndef namen_ohne_luecke(tiere, merkmal):\n    fehlende_namen = fehlt_merkmal(tiere, merkmal)\n    return [t["name"] for t in tiere if t["name"] not in fehlende_namen]\n\ntiere = [{"name": "Hund", "beine": 4}, {"name": "Spatz"}, {"name": "Biene", "beine": 6}]\nprint(namen_ohne_luecke(tiere, "beine"))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    await passWeekQuiz(page);
    await passCodingChallenge(page, 0, 'def ist_erwachsen(alter):\n    return alter >= 18\n\nprint(ist_erwachsen(20))\nprint(ist_erwachsen(15))');
    await passCodingChallenge(
      page,
      1,
      'tiere = [{"name": "Hund", "gewicht": 30}, {"name": "Spatz"}, {"name": "Katze", "gewicht": 4}]\n\ndef namen_mit_merkmal(tiere, merkmal):\n    return [t["name"] for t in tiere if merkmal in t]\n\nprint(namen_mit_merkmal(tiere, "gewicht"))'
    );

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
  });
});
