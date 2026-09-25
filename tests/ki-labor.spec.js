import { test, expect } from '@playwright/test';
import checks from '../content/ki-labor-checks/index.mjs';

// KI-Labor (Route /kurs/ki-labor, echter Kurs mit kurse.json-Eintrag, ueber CourseDetail.vue
// eingebunden wie js-grundkurs). 8 Wochen, siehe KURSPLAN.md "KI-Track: KI-Grundlagen". Nutzt
// dieselbe Wochenauswahl (KiLaborTour.vue, Kopie von JsGrundkursTour.vue) und dieselbe generische
// Wochen-Tour (JsCourseTour.vue), aber engine="pyodide" (LessonView.vue) statt js-sandbox - wie
// im 12-Wochen-Python-Kurs. Algorithmen werden komplett in reinem Python selbst geschrieben, kein
// scikit-learn. Bislang sind Woche 1-5 umgesetzt, Wochen 6-8 sind "kommt noch".
//
// Quiz + Zertifikat nutzen dasselbe System wie der 12-Wochen-Kurs (useWeekChecks.js/
// WeekCheckPanel.vue/CodeChallenge.vue/useCertificatePdf.js), jetzt um einen courseKey-Parameter
// generalisiert ('ki-labor' statt dem Default 'python') - eigener Storage-Key
// ('ue-hacker-week-checks-ki-labor') und eigener Content-Ordner (content/ki-labor-checks/), damit
// Woche 1 im KI-Labor nicht mit Woche 1 im Python-Kurs kollidiert (siehe HANDOFF.md).
const PROGRESS_KEY = 'ue-hacker-interactive-progress-ki-labor-woche1';
const PROGRESS_KEY_WEEK2 = 'ue-hacker-interactive-progress-ki-labor-woche2';
const PROGRESS_KEY_WEEK3 = 'ue-hacker-interactive-progress-ki-labor-woche3';
const PROGRESS_KEY_WEEK4 = 'ue-hacker-interactive-progress-ki-labor-woche4';
const PROGRESS_KEY_WEEK5 = 'ue-hacker-interactive-progress-ki-labor-woche5';

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

  test('Wochenauswahl: 8 Kacheln, Woche 1-5 verfügbar, Rest "kommt noch"', async ({ page }) => {
    await page.goto('/kurs/ki-labor');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.week-tile')).toHaveCount(8);
    for (let i = 0; i < 5; i++) {
      await expect(page.locator('.week-tile').nth(i)).not.toBeDisabled();
    }
    for (let i = 5; i < 8; i++) {
      await expect(page.locator('.week-tile').nth(i)).toBeDisabled();
    }
    await expect(page.locator('.week-tile-badge')).toHaveCount(3);
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

  test('Deep-Link ?week=3 öffnet direkt die Wochen-Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=3');
    // 10 Lektionen (5 Lektion + Debug + Mission + 3 Extra-Herausforderung) + 1 Check-Punkt, da
    // content/ki-labor-checks/week-3.json existiert (hasCheck=true).
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 3');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Nächste Nachbarn');
  });

  test('Deep-Link ?week=4 öffnet direkt die Wochen-Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=4');
    // 10 Lektionen (5 Lektion + Debug + Mission + 3 Extra-Herausforderung) + 1 Check-Punkt, da
    // content/ki-labor-checks/week-4.json existiert (hasCheck=true).
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 4');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Training & Test');
  });

  test('Deep-Link ?week=5 öffnet direkt die Wochen-Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=5');
    // 10 Lektionen (5 Lektion + Debug + Mission + 3 Extra-Herausforderung) + 1 Check-Punkt, da
    // content/ki-labor-checks/week-5.json existiert (hasCheck=true).
    await expect(page.locator('.stepper-step')).toHaveCount(11, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 5');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Entscheidungsbäume');
  });

  test('Deep-Link ?week=6 (noch nicht verfügbar) zeigt die Wochenauswahl statt der Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=6');
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

  test('Woche 3: Debug-Lektion mit fehlendem return/falschem Vergleich/fehlendem Zähl-Standardwert', async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, PROGRESS_KEY_WEEK3);
    await page.goto('/kurs/ki-labor?week=3');
    await page.locator('.stepper-step').nth(5).click();
    await initKernel(page);

    const first = page.locator('.task-block').first();
    await first.locator('.btn-check').click();
    await expect(first.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    const naechsterNachbarFixed = 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2)\n\ndef naechster_nachbar(trainingsdaten, neu):\n    bester_abstand = None\n    naechster = None\n    for beispiel in trainingsdaten:\n        d = abstand(neu, beispiel)\n        if bester_abstand is None or d < bester_abstand:\n            bester_abstand = d\n            naechster = beispiel\n    return naechster["art"]\n\ntrainingsdaten = [\n    {"x": 0, "y": 0, "art": "A"},\n    {"x": 10, "y": 10, "art": "B"},\n    {"x": 1, "y": 1, "art": "C"},\n]\n\nprint(naechster_nachbar(trainingsdaten, {"x": 0, "y": 1}))';

    await solve(page, [
      naechsterNachbarFixed,
      naechsterNachbarFixed,
      'def zaehle_labels(labels):\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    return anzahl_je_kategorie\n\nlabels = ["Saeugetier", "Vogel", "Saeugetier"]\nprint(zaehle_labels(labels))',
    ]);
  });

  test('Kompletter Durchlauf Woche 3: alle Lektionen, Extra-Herausforderungen und der Wochen-Check', async ({ page }) => {
    test.setTimeout(120000);
    await page.goto('/kurs/ki-labor?week=3');
    await initKernel(page);

    await solve(page, [null, null, 'print(abs(160 - 145))\nprint(abs(160 - 200))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await solve(page, [null, null, 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2)\n\nprint(abstand({"x": 0, "y": 0}, {"x": 3, "y": 4}))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await solve(page, [
      null,
      null,
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef naechster_nachbar(trainingsdaten, neu):\n    bester_abstand = None\n    naechster = None\n    for beispiel in trainingsdaten:\n        d = abstand(neu, beispiel)\n        if bester_abstand is None or d < bester_abstand:\n            bester_abstand = d\n            naechster = beispiel\n    return naechster["art"]\n\ntrainingsdaten = [{"beine": 4, "gewicht": 30, "art": "Saeugetier"}, {"beine": 2, "gewicht": 0.03, "art": "Vogel"}, {"beine": 8, "gewicht": 0.0002, "art": "Spinnentier"}]\nprint(naechster_nachbar(trainingsdaten, {"beine": 8, "gewicht": 0.0001}))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await solve(page, [
      null,
      null,
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ntrainingsdaten = [{"beine": 4, "gewicht": 30, "art": "Saeugetier"}, {"beine": 2, "gewicht": 0.03, "art": "Vogel"}, {"beine": 4, "gewicht": 25, "art": "Saeugetier"}, {"beine": 2, "gewicht": 0.02, "art": "Vogel"}]\nneu = {"beine": 3, "gewicht": 20}\n\ndef abstand_zu_neu(beispiel):\n    return abstand(neu, beispiel)\n\nsortiert = sorted(trainingsdaten, key=abstand_zu_neu)\nnaechste = sortiert[:3]\n\nzaehl = {}\nfor beispiel in naechste:\n    label = beispiel["art"]\n    zaehl[label] = zaehl.get(label, 0) + 1\nprint(zaehl)',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    const knnKlassifiziere = 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ntrainingsdaten = [{"beine": 4, "gewicht": 30, "art": "Saeugetier"}, {"beine": 2, "gewicht": 0.03, "art": "Vogel"}, {"beine": 4, "gewicht": 25, "art": "Saeugetier"}, {"beine": 2, "gewicht": 0.02, "art": "Vogel"}]\n';
    await solve(page, [
      null,
      `${knnKlassifiziere}print(knn_klassifiziere(trainingsdaten, {"beine": 4, "gewicht": 27}, 3))`,
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await page.locator('.btn-next').click();

    // Debug-Lektion (fixe Loesungen, s.o.).
    const naechsterNachbarFixed = 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2)\n\ndef naechster_nachbar(trainingsdaten, neu):\n    bester_abstand = None\n    naechster = None\n    for beispiel in trainingsdaten:\n        d = abstand(neu, beispiel)\n        if bester_abstand is None or d < bester_abstand:\n            bester_abstand = d\n            naechster = beispiel\n    return naechster["art"]\n\ntrainingsdaten = [\n    {"x": 0, "y": 0, "art": "A"},\n    {"x": 10, "y": 10, "art": "B"},\n    {"x": 1, "y": 1, "art": "C"},\n]\n\nprint(naechster_nachbar(trainingsdaten, {"x": 0, "y": 1}))';
    await solve(page, [
      naechsterNachbarFixed,
      naechsterNachbarFixed,
      'def zaehle_labels(labels):\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    return anzahl_je_kategorie\n\nlabels = ["Saeugetier", "Vogel", "Saeugetier"]\nprint(zaehle_labels(labels))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    // Mission: eigener Frucht-Datensatz + 1-NN.
    await solve(page, [
      'trainingsdaten = [{"suesse": 8, "groesse": 3, "frucht": "Kirsche"}, {"suesse": 3, "groesse": 15, "frucht": "Zitrone"}, {"suesse": 9, "groesse": 4, "frucht": "Kirsche"}]\n\ndef namen_liste(trainingsdaten):\n    return [t["frucht"] for t in trainingsdaten]\n\nprint(namen_liste(trainingsdaten))',
      'import math\n\ntrainingsdaten = [{"suesse": 8, "groesse": 3, "frucht": "Kirsche"}, {"suesse": 3, "groesse": 15, "frucht": "Zitrone"}, {"suesse": 9, "groesse": 4, "frucht": "Kirsche"}]\n\ndef abstand(a, b):\n    return math.sqrt((a["suesse"] - b["suesse"]) ** 2 + (a["groesse"] - b["groesse"]) ** 2)\n\nprint(abstand(trainingsdaten[0], trainingsdaten[1]))',
      'import math\n\ntrainingsdaten = [{"suesse": 8, "groesse": 3, "frucht": "Kirsche"}, {"suesse": 3, "groesse": 15, "frucht": "Zitrone"}, {"suesse": 9, "groesse": 4, "frucht": "Kirsche"}]\n\ndef abstand(a, b):\n    return math.sqrt((a["suesse"] - b["suesse"]) ** 2 + (a["groesse"] - b["groesse"]) ** 2)\n\ndef naechster_nachbar(trainingsdaten, neu):\n    bester_abstand = None\n    naechster = None\n    for beispiel in trainingsdaten:\n        d = abstand(neu, beispiel)\n        if bester_abstand is None or d < bester_abstand:\n            bester_abstand = d\n            naechster = beispiel\n    return naechster["frucht"]\n\nprint(naechster_nachbar(trainingsdaten, {"suesse": 9, "groesse": 5}))',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');

    // Mission abgeschlossen, danach folgt ein Boss-Abschnitt (Extra-Herausforderung) UND ein
    // Check -> "Weiter" zeigt eine Wahl-Seite statt direkt zum Check zu springen.
    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="boss"]').click();

    // Boss 1: gewichteter Nachbar.
    await solve(page, [
      'def gewicht(abstand):\n    if abstand == 0:\n        return 1000000\n    return 1 / abstand\n\nprint(gewicht(2))\nprint(gewicht(0))',
      'def gewicht(abstand):\n    if abstand == 0:\n        return 1000000\n    return 1 / abstand\n\ndef gewichtete_stimmen(nachbarn_mit_abstand):\n    stimmen = {}\n    for label, abstand in nachbarn_mit_abstand:\n        stimmen[label] = stimmen.get(label, 0) + gewicht(abstand)\n    return stimmen\n\nprint(gewichtete_stimmen([("A", 1), ("B", 2), ("A", 4)]))',
      'def gewicht(abstand):\n    if abstand == 0:\n        return 1000000\n    return 1 / abstand\n\ndef gewichtete_stimmen(nachbarn_mit_abstand):\n    stimmen = {}\n    for label, abstand in nachbarn_mit_abstand:\n        stimmen[label] = stimmen.get(label, 0) + gewicht(abstand)\n    return stimmen\n\ndef gewichteter_sieger(nachbarn_mit_abstand):\n    stimmen = gewichtete_stimmen(nachbarn_mit_abstand)\n    beste = None\n    bester_wert = -1\n    for label in stimmen:\n        if stimmen[label] > bester_wert:\n            bester_wert = stimmen[label]\n            beste = label\n    return beste\n\nprint(gewichteter_sieger([("A", 1), ("B", 2), ("A", 4)]))',
    ]);
    await page.locator('.btn-next').click();

    // Boss 2: der richtige Wert fuer k.
    await solve(page, [
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\nprint(ist_richtig("Katze", "Katze"))\nprint(ist_richtig("Katze", "Hund"))',
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nprint(genauigkeit(["Katze", "Hund", "Katze", "Vogel"], ["Katze", "Katze", "Katze", "Vogel"]))',
      'def beste_genauigkeit(ergebnisse_je_k):\n    bestes_k = None\n    bester_wert = -1\n    for k in ergebnisse_je_k:\n        if ergebnisse_je_k[k] > bester_wert:\n            bester_wert = ergebnisse_je_k[k]\n            bestes_k = k\n    return bestes_k\n\nprint(beste_genauigkeit({1: 60, 3: 80, 5: 75}))',
    ]);
    await page.locator('.btn-next').click();

    // Boss 3: mehr als zwei Klassen.
    await solve(page, [
      'def sammle_kategorien(trainingsdaten):\n    kategorien = []\n    for beispiel in trainingsdaten:\n        if beispiel["art"] not in kategorien:\n            kategorien.append(beispiel["art"])\n    return kategorien\n\nprint(sammle_kategorien([{"art": "Hund"}, {"art": "Katze"}, {"art": "Hund"}, {"art": "Vogel"}]))',
      'def ist_unentschieden(anzahl_je_kategorie):\n    werte = list(anzahl_je_kategorie.values())\n    bester_wert = -1\n    for wert in werte:\n        if wert > bester_wert:\n            bester_wert = wert\n    anzahl_bester = 0\n    for wert in werte:\n        if wert == bester_wert:\n            anzahl_bester += 1\n    return anzahl_bester >= 2\n\nprint(ist_unentschieden({"Hund": 2, "Katze": 2, "Vogel": 1}))\nprint(ist_unentschieden({"Hund": 3, "Katze": 1}))',
      'def ist_unentschieden(anzahl_je_kategorie):\n    werte = list(anzahl_je_kategorie.values())\n    bester_wert = -1\n    for wert in werte:\n        if wert > bester_wert:\n            bester_wert = wert\n    anzahl_bester = 0\n    for wert in werte:\n        if wert == bester_wert:\n            anzahl_bester += 1\n    return anzahl_bester >= 2\n\ndef entscheide(anzahl_je_kategorie, sortierte_nachbarn):\n    if ist_unentschieden(anzahl_je_kategorie):\n        return sortierte_nachbarn[0]["art"]\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\nprint(entscheide({"Hund": 2, "Katze": 2}, [{"art": "Katze"}, {"art": "Hund"}, {"art": "Hund"}, {"art": "Katze"}]))',
    ]);
    // Letzte Lektion (boss-03) abgeschlossen, kein weiterer Boss -> "Weiter" springt direkt zum
    // Wochen-Check (kein Mission->Boss-Uebergang mehr, also keine erneute Wahl-Seite).
    await page.locator('.btn-next').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    await passWeekQuiz(page);
    await passCodingChallenge(page, 0, 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2)\n\nprint(abstand({"x": 0, "y": 0}, {"x": 6, "y": 8}))');
    await passCodingChallenge(
      page,
      1,
      'labels = ["Hund", "Katze", "Hund", "Hund", "Katze"]\n\nanzahl_je_kategorie = {}\nfor label in labels:\n    anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n\nprint(anzahl_je_kategorie)'
    );

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
  });


  test('Woche 4: Debug-Lektion mit fehlender Zählung/überschneidender Aufteilung/falschem Vergleich', async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, PROGRESS_KEY_WEEK4);
    await page.goto('/kurs/ki-labor?week=4');
    await page.locator('.stepper-step').nth(5).click();
    await initKernel(page);

    const first = page.locator('.task-block').first();
    await first.locator('.btn-check').click();
    await expect(first.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await solve(page, [
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nvorhersagen = ["A", "B", "A"]\nerwartete_werte = ["A", "B", "B"]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'daten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n]\nsplit = 4\ntrainingsdaten = daten[:split]\ntestdaten = daten[split:]\nprint(len(trainingsdaten))\nprint(len(testdaten))',
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nvorhersagen = ["Saeugetier", "Vogel"]\nerwartete_werte = ["Saeugetier", "Saeugetier"]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
    ]);
  });

  test('Kompletter Durchlauf Woche 4: alle Lektionen, Extra-Herausforderungen und der Wochen-Check', async ({ page }) => {
    test.setTimeout(120000);
    await page.goto('/kurs/ki-labor?week=4');
    await initKernel(page);

    await solve(page, [null, null, 'daten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 6, "gewicht": 0.001, "art": "Insekt"},\n    {"beine": 8, "gewicht": 0.0002, "art": "Spinnentier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n]\ntrainingsdaten = daten[:5]\ntestdaten = daten[5:]\nprint(len(trainingsdaten))\nprint(len(testdaten))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await solve(page, [null, null, 'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nvorhersagen = [\'A\', \'B\', \'A\', \'A\']\nerwartete_werte = [\'A\', \'B\', \'B\', \'A\']\nprint(genauigkeit(vorhersagen, erwartete_werte))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await solve(page, [null, null, 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ntrainingsdaten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n]\ntestdaten = [\n    {"beine": 4, "gewicht": 26, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 4.5, "art": "Vogel"},\n]\nvorhersagen = []\nfor beispiel in testdaten:\n    vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, 3))\nprint(vorhersagen)']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await solve(page, [null, 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ndef trainiere_und_teste(daten, split, k):\n    trainingsdaten = daten[:split]\n    testdaten = daten[split:]\n    vorhersagen = []\n    for beispiel in testdaten:\n        vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, k))\n    erwartete_werte = [beispiel["art"] for beispiel in testdaten]\n    return genauigkeit(vorhersagen, erwartete_werte)\n\ndaten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 20, "art": "Vogel"},\n]\nprint(trainiere_und_teste(daten, 5, 1))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await solve(page, [null, 'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ntrainingsdaten = [\n    {"beine": 4, "gewicht": 5, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 30, "art": "Vogel"},\n]\ntestdaten = [\n    {"beine": 4, "gewicht": 32, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 2, "art": "Vogel"},\n]\nvorhersagen = [knn_klassifiziere(trainingsdaten, b, 1) for b in testdaten]\nerwartete_werte = [b["art"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))']);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await page.locator('.btn-next').click();

    // Debug-Lektion (fixe Loesungen, s.o.).
    await solve(page, [
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nvorhersagen = ["A", "B", "A"]\nerwartete_werte = ["A", "B", "B"]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'daten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n]\nsplit = 4\ntrainingsdaten = daten[:split]\ntestdaten = daten[split:]\nprint(len(trainingsdaten))\nprint(len(testdaten))',
      'def ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nvorhersagen = ["Saeugetier", "Vogel"]\nerwartete_werte = ["Saeugetier", "Saeugetier"]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    // Mission: eigener Frucht-Datensatz aufteilen, vorhersagen, Genauigkeit messen.
    await solve(page, [
      'daten = [\n    {"suesse": 8, "groesse": 3, "frucht": "Kirsche"},\n    {"suesse": 9, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 15, "frucht": "Zitrone"},\n    {"suesse": 2, "groesse": 16, "frucht": "Zitrone"},\n    {"suesse": 8, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 14, "frucht": "Zitrone"},\n]\ntrainingsdaten = daten[:4]\ntestdaten = daten[4:]\nprint(len(trainingsdaten))\nprint(len(testdaten))',
      'import math\ndaten = [\n    {"suesse": 8, "groesse": 3, "frucht": "Kirsche"},\n    {"suesse": 9, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 15, "frucht": "Zitrone"},\n    {"suesse": 2, "groesse": 16, "frucht": "Zitrone"},\n    {"suesse": 8, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 14, "frucht": "Zitrone"},\n]\ntrainingsdaten = daten[:4]\ntestdaten = daten[4:]\n\ndef abstand(a, b):\n    return math.sqrt((a["suesse"] - b["suesse"]) ** 2 + (a["groesse"] - b["groesse"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["frucht"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\nvorhersagen = []\nfor beispiel in testdaten:\n    vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, 3))\nprint(vorhersagen)',
      'import math\ndaten = [\n    {"suesse": 8, "groesse": 3, "frucht": "Kirsche"},\n    {"suesse": 9, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 15, "frucht": "Zitrone"},\n    {"suesse": 2, "groesse": 16, "frucht": "Zitrone"},\n    {"suesse": 8, "groesse": 4, "frucht": "Kirsche"},\n    {"suesse": 3, "groesse": 14, "frucht": "Zitrone"},\n]\ntrainingsdaten = daten[:4]\ntestdaten = daten[4:]\n\ndef abstand(a, b):\n    return math.sqrt((a["suesse"] - b["suesse"]) ** 2 + (a["groesse"] - b["groesse"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["frucht"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\nvorhersagen = []\nfor beispiel in testdaten:\n    vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, 3))\n\nerwartete_werte = [beispiel["frucht"] for beispiel in testdaten]\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nprint(genauigkeit(vorhersagen, erwartete_werte))',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');

    // Mission abgeschlossen, danach folgt ein Boss-Abschnitt (Extra-Herausforderung) UND ein
    // Check -> "Weiter" zeigt eine Wahl-Seite statt direkt zum Check zu springen.
    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="boss"]').click();

    // Boss 1: ein stoerrischer Ausreisser.
    await solve(page, [
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef sammle_vorhersagen(trainingsdaten, testdaten, k):\n    vorhersagen = []\n    for beispiel in testdaten:\n        vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, k))\n    return vorhersagen\n\ntrainingsdaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 3, "gewicht": 9, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\n\nprint(sammle_vorhersagen(trainingsdaten, testdaten, 1))',
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef sammle_vorhersagen(trainingsdaten, testdaten, k):\n    vorhersagen = []\n    for beispiel in testdaten:\n        vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, k))\n    return vorhersagen\n\ntrainingsdaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 3, "gewicht": 9, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\n\nprint(sammle_vorhersagen(trainingsdaten, testdaten, 3))',
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef sammle_vorhersagen(trainingsdaten, testdaten, k):\n    vorhersagen = []\n    for beispiel in testdaten:\n        vorhersagen.append(knn_klassifiziere(trainingsdaten, beispiel, k))\n    return vorhersagen\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ntrainingsdaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 3, "gewicht": 9, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\nerwartete_werte = [beispiel["art"] for beispiel in testdaten]\n\nvorhersagen_k1 = sammle_vorhersagen(trainingsdaten, testdaten, 1)\nvorhersagen_k3 = sammle_vorhersagen(trainingsdaten, testdaten, 3)\nprint(genauigkeit(vorhersagen_k1, erwartete_werte))\nprint(genauigkeit(vorhersagen_k3, erwartete_werte))',
    ]);
    await page.locator('.btn-next').click();

    // Boss 2: mehr Trainingsdaten, bessere Vorhersage?
    await solve(page, [
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ndaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\n\ntrainingsdaten = daten[:2]\nvorhersagen = [knn_klassifiziere(trainingsdaten, b, 1) for b in testdaten]\nerwartete_werte = [b["art"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ndaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\n\ntrainingsdaten = daten[:6]\nvorhersagen = [knn_klassifiziere(trainingsdaten, b, 1) for b in testdaten]\nerwartete_werte = [b["art"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ndef vergleiche_trainingsgroessen(daten, split_klein, split_gross, testdaten, k):\n    erwartete_werte = [b["art"] for b in testdaten]\n\n    trainingsdaten_klein = daten[:split_klein]\n    vorhersagen_klein = [knn_klassifiziere(trainingsdaten_klein, b, k) for b in testdaten]\n    genauigkeit_klein = genauigkeit(vorhersagen_klein, erwartete_werte)\n\n    trainingsdaten_gross = daten[:split_gross]\n    vorhersagen_gross = [knn_klassifiziere(trainingsdaten_gross, b, k) for b in testdaten]\n    genauigkeit_gross = genauigkeit(vorhersagen_gross, erwartete_werte)\n\n    return (genauigkeit_klein, genauigkeit_gross)\n\ndaten = [\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n    {"beine": 2, "gewicht": 4, "art": "Vogel"},\n    {"beine": 2, "gewicht": 5, "art": "Vogel"},\n    {"beine": 4, "gewicht": 25, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 28, "art": "Saeugetier"},\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n]\ntestdaten = [\n    {"beine": 3, "gewicht": 10, "art": "Vogel"},\n    {"beine": 4, "gewicht": 27, "art": "Saeugetier"},\n]\n\nprint(vergleiche_trainingsgroessen(daten, 2, 6, testdaten, 1))',
    ]);
    await page.locator('.btn-next').click();

    // Boss 3: erkennt Overfitting.
    await solve(page, [
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ntrainingsdaten = [\n    {"beine": 4, "gewicht": 5, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 30, "art": "Vogel"},\n]\nvorhersagen = [knn_klassifiziere(trainingsdaten, b, 1) for b in trainingsdaten]\nerwartete_werte = [b["art"] for b in trainingsdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'import math\n\ndef abstand(a, b):\n    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)\n\ndef knn_klassifiziere(trainingsdaten, neu, k):\n    def abstand_zu_neu(beispiel):\n        return abstand(neu, beispiel)\n    sortiert = sorted(trainingsdaten, key=abstand_zu_neu)\n    naechste = sortiert[:k]\n    labels = [beispiel["art"] for beispiel in naechste]\n    anzahl_je_kategorie = {}\n    for label in labels:\n        anzahl_je_kategorie[label] = anzahl_je_kategorie.get(label, 0) + 1\n    beste_kategorie = None\n    bester_wert = -1\n    for kategorie in anzahl_je_kategorie:\n        anzahl = anzahl_je_kategorie[kategorie]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_kategorie = kategorie\n    return beste_kategorie\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\ntrainingsdaten = [\n    {"beine": 4, "gewicht": 5, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 30, "art": "Vogel"},\n]\ntestdaten = [\n    {"beine": 4, "gewicht": 30, "art": "Saeugetier"},\n    {"beine": 2, "gewicht": 3, "art": "Vogel"},\n]\nvorhersagen = [knn_klassifiziere(trainingsdaten, b, 1) for b in testdaten]\nerwartete_werte = [b["art"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      'def ist_overfitting(trainings_genauigkeit, test_genauigkeit, schwelle):\n    return (trainings_genauigkeit - test_genauigkeit) > schwelle\n\nprint(ist_overfitting(100, 0, 20))',
    ]);
    // Letzte Lektion (boss-03) abgeschlossen, kein weiterer Boss -> "Weiter" springt direkt zum
    // Wochen-Check (kein Mission->Boss-Uebergang mehr, also keine erneute Wahl-Seite).
    await page.locator('.btn-next').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    await passWeekQuiz(page);
    await passCodingChallenge(page, 0, 'def ist_richtig(v, e):\n    return v == e\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\nprint(genauigkeit([\'Hund\', \'Katze\', \'Hund\', \'Vogel\'], [\'Hund\', \'Hund\', \'Hund\', \'Vogel\']))');
    await passCodingChallenge(
      page,
      1,
      'daten = [{\'x\': 1}, {\'x\': 2}, {\'x\': 3}, {\'x\': 4}, {\'x\': 5}, {\'x\': 6}]\ntrainingsdaten = daten[:4]\ntestdaten = daten[4:]\nprint(len(trainingsdaten))\nprint(len(testdaten))'
    );

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
  });

  test('Woche 5: Debug-Lektion mit fehlender Zählung/falscher Vergleichsrichtung/falschem Vergleich', async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, PROGRESS_KEY_WEEK5);
    await page.goto('/kurs/ki-labor?week=5');
    await page.locator('.stepper-step').nth(5).click();
    await initKernel(page);

    const first = page.locator('.task-block').first();
    await first.locator('.btn-check').click();
    await expect(first.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await solve(page, [
      'def mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\nteil = [{"schirm": "nein"}, {"schirm": "ja"}, {"schirm": "ja"}]\nprint(mehrheitsklasse(teil))',
      'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndaten = [{"regen": 10}, {"regen": 50}, {"regen": 90}]\nlinks, rechts = teile_bei_schwellenwert(daten, "regen", 50)\nprint(len(links))\nprint(len(rechts))',
      'def mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\nteil = [{"schirm": "ja"}, {"schirm": "ja"}, {"schirm": "nein"}]\nprint(anzahl_falsch(teil))',
    ]);
  });

  test('Kompletter Durchlauf Woche 5: alle Lektionen, Extra-Herausforderungen und der Wochen-Check', async ({ page }) => {
    test.setTimeout(120000);
    await page.goto('/kurs/ki-labor?week=5');
    await initKernel(page);

    // Lektion 1: Was ist ein Entscheidungsbaum?
    await solve(page, [null, null, 'def party_drinnen(temperatur):\n    if temperatur < 15:\n        return "drinnen"\n    else:\n        return "draußen"\n\nprint(party_drinnen(10))\nprint(party_drinnen(25))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    // Lektion 2: Wie gut ist eine Aufteilung?
    await solve(page, [null, null, 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndaten = [\n    {"regen": 80, "temperatur": 18, "schirm": "ja"},\n    {"regen": 90, "temperatur": 25, "schirm": "ja"},\n    {"regen": 70, "temperatur": 10, "schirm": "ja"},\n    {"regen": 60, "temperatur": 30, "schirm": "ja"},\n    {"regen": 20, "temperatur": 22, "schirm": "nein"},\n    {"regen": 10, "temperatur": 15, "schirm": "nein"},\n    {"regen": 30, "temperatur": 28, "schirm": "nein"},\n    {"regen": 15, "temperatur": 12, "schirm": "nein"},\n]\n\nlinks25, rechts25 = teile_bei_schwellenwert(daten, "regen", 25)\nprint(anzahl_falsch(links25) + anzahl_falsch(rechts25))\nlinks45, rechts45 = teile_bei_schwellenwert(daten, "regen", 45)\nprint(anzahl_falsch(links45) + anzahl_falsch(rechts45))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    // Lektion 3: Automatisch den besten Trennwert finden.
    await solve(page, [null, 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["bestanden"]] = anzahl_je_klasse.get(beispiel["bestanden"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["bestanden"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\ndaten = [\n    {"punkte": 20, "bestanden": "nein"},\n    {"punkte": 35, "bestanden": "nein"},\n    {"punkte": 60, "bestanden": "ja"},\n    {"punkte": 75, "bestanden": "ja"},\n]\nprint(bester_schwellenwert(daten, "punkte"))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    // Lektion 4: Der Baum selbst.
    await solve(page, [null, 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\ndef baue_baum(daten, merkmal):\n    schwelle, _ = bester_schwellenwert(daten, merkmal)\n    links, rechts = teile_bei_schwellenwert(daten, merkmal, schwelle)\n    return {\n        "merkmal": merkmal,\n        "schwelle": schwelle,\n        "links": mehrheitsklasse(links),\n        "rechts": mehrheitsklasse(rechts),\n    }\n\ndaten = [\n    {"regen": 80, "temperatur": 18, "schirm": "ja"},\n    {"regen": 90, "temperatur": 25, "schirm": "ja"},\n    {"regen": 70, "temperatur": 10, "schirm": "ja"},\n    {"regen": 60, "temperatur": 30, "schirm": "ja"},\n    {"regen": 20, "temperatur": 22, "schirm": "nein"},\n    {"regen": 10, "temperatur": 15, "schirm": "nein"},\n    {"regen": 30, "temperatur": 28, "schirm": "nein"},\n    {"regen": 15, "temperatur": 12, "schirm": "nein"},\n]\n\nprint(baue_baum(daten, "temperatur"))']);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    // Lektion 5: Das beste Merkmal wählen.
    await solve(page, [null, 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\ndef bestes_merkmal(daten, merkmale):\n    bestes = None\n    wenigste_fehler = None\n    for merkmal in merkmale:\n        _, fehler = bester_schwellenwert(daten, merkmal)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            bestes = merkmal\n    return bestes\n\ndaten = [\n    {"regen": 80, "temperatur": 18, "schirm": "ja"},\n    {"regen": 90, "temperatur": 25, "schirm": "ja"},\n    {"regen": 70, "temperatur": 10, "schirm": "ja"},\n    {"regen": 60, "temperatur": 30, "schirm": "ja"},\n    {"regen": 20, "temperatur": 22, "schirm": "nein"},\n    {"regen": 10, "temperatur": 15, "schirm": "nein"},\n    {"regen": 30, "temperatur": 28, "schirm": "nein"},\n    {"regen": 15, "temperatur": 12, "schirm": "nein"},\n]\n\nprint(bestes_merkmal(daten, ["temperatur", "regen"]))']);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await page.locator('.btn-next').click();

    // Debug-Lektion (fixe Loesungen, s.o.).
    await solve(page, [
      'def mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\nteil = [{"schirm": "nein"}, {"schirm": "ja"}, {"schirm": "ja"}]\nprint(mehrheitsklasse(teil))',
      'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndaten = [{"regen": 10}, {"regen": 50}, {"regen": 90}]\nlinks, rechts = teile_bei_schwellenwert(daten, "regen", 50)\nprint(len(links))\nprint(len(rechts))',
      'def mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\nteil = [{"schirm": "ja"}, {"schirm": "ja"}, {"schirm": "nein"}]\nprint(anzahl_falsch(teil))',
    ]);
    await page.locator('.btn-next').click();
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    // Mission: eigener Pflanzen-Datensatz aufteilen, besten Trennwert finden, Baum bauen.
    await solve(page, [
      'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\npflanzen = [\n    {"bodenfeuchtigkeit": 10, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 15, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 20, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 70, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 80, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 75, "giessen": "nein"},\n]\nlinks, rechts = teile_bei_schwellenwert(pflanzen, "bodenfeuchtigkeit", 40)\nprint(len(links))\nprint(len(rechts))',
      'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["giessen"]] = anzahl_je_klasse.get(beispiel["giessen"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["giessen"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\npflanzen = [\n    {"bodenfeuchtigkeit": 10, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 15, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 20, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 70, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 80, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 75, "giessen": "nein"},\n]\nprint(bester_schwellenwert(pflanzen, "bodenfeuchtigkeit"))',
      'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["giessen"]] = anzahl_je_klasse.get(beispiel["giessen"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["giessen"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\ndef baue_baum(daten, merkmal):\n    schwelle, _ = bester_schwellenwert(daten, merkmal)\n    links, rechts = teile_bei_schwellenwert(daten, merkmal, schwelle)\n    return {\n        "merkmal": merkmal,\n        "schwelle": schwelle,\n        "links": mehrheitsklasse(links),\n        "rechts": mehrheitsklasse(rechts),\n    }\n\ndef klassifiziere(baum, beispiel):\n    if beispiel[baum["merkmal"]] < baum["schwelle"]:\n        return baum["links"]\n    else:\n        return baum["rechts"]\n\npflanzen = [\n    {"bodenfeuchtigkeit": 10, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 15, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 20, "giessen": "ja"},\n    {"bodenfeuchtigkeit": 70, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 80, "giessen": "nein"},\n    {"bodenfeuchtigkeit": 75, "giessen": "nein"},\n]\nbaum = baue_baum(pflanzen, "bodenfeuchtigkeit")\nprint(klassifiziere(baum, {"bodenfeuchtigkeit": 5}))\nprint(klassifiziere(baum, {"bodenfeuchtigkeit": 90}))',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');

    // Mission abgeschlossen, danach folgt ein Boss-Abschnitt (Extra-Herausforderung) UND ein
    // Check -> "Weiter" zeigt eine Wahl-Seite statt direkt zum Check zu springen.
    await page.locator('.btn-next').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="boss"]').click();

    const helferFunktionen = 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["schirm"]] = anzahl_je_klasse.get(beispiel["schirm"], 0) + 1\n    beste_klasse = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        anzahl = anzahl_je_klasse[klasse]\n        if anzahl > bester_wert:\n            bester_wert = anzahl\n            beste_klasse = klasse\n    return beste_klasse\n\ndef anzahl_falsch(teil):\n    mehrheit = mehrheitsklasse(teil)\n    falsch = 0\n    for beispiel in teil:\n        if beispiel["schirm"] != mehrheit:\n            falsch += 1\n    return falsch\n\ndef bester_schwellenwert(daten, merkmal):\n    werte = sorted(set(b[merkmal] for b in daten))\n    beste_schwelle = None\n    wenigste_fehler = None\n    for i in range(len(werte) - 1):\n        kandidat = (werte[i] + werte[i + 1]) / 2\n        links, rechts = teile_bei_schwellenwert(daten, merkmal, kandidat)\n        fehler = anzahl_falsch(links) + anzahl_falsch(rechts)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            beste_schwelle = kandidat\n    return beste_schwelle, wenigste_fehler\n\ndef bestes_merkmal(daten, merkmale):\n    bestes = None\n    wenigste_fehler = None\n    for merkmal in merkmale:\n        _, fehler = bester_schwellenwert(daten, merkmal)\n        if wenigste_fehler is None or fehler < wenigste_fehler:\n            wenigste_fehler = fehler\n            bestes = merkmal\n    return bestes\n\n';
    const datenB1 = 'daten = [\n    {"regen": 80, "temperatur": 18, "wochentag": 3, "schirm": "ja"},\n    {"regen": 90, "temperatur": 25, "wochentag": 6, "schirm": "ja"},\n    {"regen": 70, "temperatur": 10, "wochentag": 1, "schirm": "ja"},\n    {"regen": 60, "temperatur": 30, "wochentag": 5, "schirm": "ja"},\n    {"regen": 20, "temperatur": 22, "wochentag": 2, "schirm": "nein"},\n    {"regen": 10, "temperatur": 15, "wochentag": 7, "schirm": "nein"},\n    {"regen": 30, "temperatur": 28, "wochentag": 4, "schirm": "nein"},\n    {"regen": 15, "temperatur": 12, "wochentag": 1, "schirm": "nein"},\n]\n';

    // Boss 1: drei Merkmale, nur eines zaehlt.
    await solve(page, [
      helferFunktionen + datenB1 + 'print(bestes_merkmal(daten, ["temperatur", "wochentag", "regen"]))',
      helferFunktionen + datenB1 + 'print(bestes_merkmal(daten, ["wochentag", "regen", "temperatur"]))',
      helferFunktionen + datenB1 + 'print(bester_schwellenwert(daten, "regen")[1])\nprint(bester_schwellenwert(daten, "temperatur")[1])\nprint(bester_schwellenwert(daten, "wochentag")[1])',
    ]);
    await page.locator('.btn-next').click();

    const baumFunktionen = helferFunktionen + 'def baue_baum(daten, merkmal):\n    schwelle, _ = bester_schwellenwert(daten, merkmal)\n    links, rechts = teile_bei_schwellenwert(daten, merkmal, schwelle)\n    return {\n        "merkmal": merkmal,\n        "schwelle": schwelle,\n        "links": mehrheitsklasse(links),\n        "rechts": mehrheitsklasse(rechts),\n    }\n\ndef klassifiziere(baum, beispiel):\n    if beispiel[baum["merkmal"]] < baum["schwelle"]:\n        return baum["links"]\n    return baum["rechts"]\n\ndef ist_richtig(vorhersage, erwartet):\n    return vorhersage == erwartet\n\ndef genauigkeit(vorhersagen, erwartete_werte):\n    richtig = 0\n    for i in range(len(vorhersagen)):\n        if ist_richtig(vorhersagen[i], erwartete_werte[i]):\n            richtig += 1\n    return round(richtig / len(vorhersagen) * 100)\n\n';
    const trainingsdatenB2 = 'trainingsdaten = [\n    {"regen": 80, "temperatur": 18, "schirm": "ja"},\n    {"regen": 90, "temperatur": 25, "schirm": "ja"},\n    {"regen": 70, "temperatur": 10, "schirm": "ja"},\n    {"regen": 20, "temperatur": 22, "schirm": "nein"},\n    {"regen": 10, "temperatur": 15, "schirm": "nein"},\n    {"regen": 30, "temperatur": 28, "schirm": "nein"},\n]\n';
    const testdatenB2 = 'testdaten = [\n    {"regen": 65, "temperatur": 20, "schirm": "ja"},\n    {"regen": 12, "temperatur": 18, "schirm": "nein"},\n]\n';

    // Boss 2: Baum trainieren, auf echten Testdaten pruefen.
    await solve(page, [
      baumFunktionen + trainingsdatenB2 + 'bestes = bestes_merkmal(trainingsdaten, ["regen", "temperatur"])\nbaum = baue_baum(trainingsdaten, bestes)\nprint(baum)',
      baumFunktionen + trainingsdatenB2 + testdatenB2 + 'bestes = bestes_merkmal(trainingsdaten, ["regen", "temperatur"])\nbaum = baue_baum(trainingsdaten, bestes)\nvorhersagen = [klassifiziere(baum, b) for b in testdaten]\nerwartete_werte = [b["schirm"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      baumFunktionen + trainingsdatenB2 + testdatenB2 + 'baum = baue_baum(trainingsdaten, "temperatur")\nvorhersagen = [klassifiziere(baum, b) for b in testdaten]\nerwartete_werte = [b["schirm"] for b in testdaten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
    ]);
    await page.locator('.btn-next').click();

    const datenB3 = 'daten = [\n    {"regen": 80, "schirm": "ja"},\n    {"regen": 75, "schirm": "ja"},\n    {"regen": 55, "schirm": "ja"},\n    {"regen": 45, "schirm": "nein"},\n    {"regen": 40, "schirm": "ja"},\n    {"regen": 35, "schirm": "nein"},\n    {"regen": 20, "schirm": "nein"},\n    {"regen": 15, "schirm": "nein"},\n]\n';

    // Boss 3: wenn keine Schwelle perfekt trennt.
    await solve(page, [
      helferFunktionen + datenB3 + 'print(bester_schwellenwert(daten, "regen"))',
      baumFunktionen + datenB3 + 'baum = baue_baum(daten, "regen")\nvorhersagen = [klassifiziere(baum, b) for b in daten]\nerwartete_werte = [b["schirm"] for b in daten]\nprint(genauigkeit(vorhersagen, erwartete_werte))',
      baumFunktionen + datenB3 + 'baum = baue_baum(daten, "regen")\nvorhersagen = [klassifiziere(baum, b) for b in daten]\nerwartete_werte = [b["schirm"] for b in daten]\nprint(genauigkeit(vorhersagen, erwartete_werte))\nbaseline = [mehrheitsklasse(daten) for _ in daten]\nprint(genauigkeit(baseline, erwartete_werte))',
    ]);
    // Letzte Lektion (boss-03) abgeschlossen, kein weiterer Boss -> "Weiter" springt direkt zum
    // Wochen-Check (kein Mission->Boss-Uebergang mehr, also keine erneute Wahl-Seite).
    await page.locator('.btn-next').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    await passWeekQuiz(page);
    await passCodingChallenge(page, 0, 'def teile_bei_schwellenwert(daten, merkmal, schwelle):\n    links = [b for b in daten if b[merkmal] < schwelle]\n    rechts = [b for b in daten if b[merkmal] >= schwelle]\n    return links, rechts\n\ndef mehrheitsklasse(teil):\n    anzahl_je_klasse = {}\n    for beispiel in teil:\n        anzahl_je_klasse[beispiel["wert"]] = anzahl_je_klasse.get(beispiel["wert"], 0) + 1\n    beste = None\n    bester_wert = -1\n    for klasse in anzahl_je_klasse:\n        if anzahl_je_klasse[klasse] > bester_wert:\n            bester_wert = anzahl_je_klasse[klasse]\n            beste = klasse\n    return beste\n\ndaten = [{"x": 10, "wert": "A"}, {"x": 20, "wert": "A"}, {"x": 50, "wert": "B"}, {"x": 60, "wert": "B"}]\nlinks, rechts = teile_bei_schwellenwert(daten, "x", 35)\nprint(mehrheitsklasse(links))\nprint(mehrheitsklasse(rechts))');
    await passCodingChallenge(
      page,
      1,
      'def klassifiziere(baum, beispiel):\n    if beispiel[baum["merkmal"]] < baum["schwelle"]:\n        return baum["links"]\n    return baum["rechts"]\n\nbaum = {"merkmal": "x", "schwelle": 35, "links": "A", "rechts": "B"}\nprint(klassifiziere(baum, {"x": 15}))\nprint(klassifiziere(baum, {"x": 80}))'
    );

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
  });
});
