import { test, expect } from '@playwright/test';

// KI-Labor (Route /kurs/ki-labor, echter Kurs mit kurse.json-Eintrag, ueber CourseDetail.vue
// eingebunden wie js-grundkurs). 8 Wochen, siehe KURSPLAN.md "KI-Track: KI-Grundlagen". Nutzt
// dieselbe Wochenauswahl (KiLaborTour.vue, Kopie von JsGrundkursTour.vue) und dieselbe generische
// Wochen-Tour (JsCourseTour.vue), aber engine="pyodide" (LessonView.vue) statt js-sandbox - wie
// im 12-Wochen-Python-Kurs. Algorithmen werden komplett in reinem Python selbst geschrieben, kein
// scikit-learn. Bislang ist nur Woche 1 ("Was ist KI?") umgesetzt, Wochen 2-8 sind "kommt noch".
const PROGRESS_KEY = 'ue-hacker-interactive-progress-ki-labor-woche1';

test.describe('KI-Labor (Wochenauswahl)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem(key);
    }, PROGRESS_KEY);
  });

  test('Wochenauswahl: 8 Kacheln, nur Woche 1 verfügbar, Rest "kommt noch"', async ({ page }) => {
    await page.goto('/kurs/ki-labor');
    await expect(page.locator('.week-tile')).toHaveCount(8);
    await expect(page.locator('.week-tile').nth(0)).not.toBeDisabled();
    for (let i = 1; i < 8; i++) {
      await expect(page.locator('.week-tile').nth(i)).toBeDisabled();
    }
    await expect(page.locator('.week-tile-badge')).toHaveCount(7);
  });

  test('Woche 1 anklicken öffnet die Wochen-Tour, "Andere Woche wählen" führt zurück', async ({ page }) => {
    await page.goto('/kurs/ki-labor');
    await page.locator('.week-tile').nth(0).click();
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');

    await page.locator('.breadcrumb-back').click();
    await expect(page.locator('.week-tile')).toHaveCount(8);
    await expect(page.locator('.stepper-step')).toHaveCount(0);
  });

  test('Deep-Link ?week=1 öffnet direkt die Wochen-Tour, gruppierte Kullern Lektion/Debug/Mission', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=1');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Was ist KI?');

    const groupLabels = page.locator('.stepper-group-label');
    await expect(groupLabels).toHaveCount(3);
    await expect(groupLabels.nth(0)).toHaveText(/lektion/i);
    await expect(groupLabels.nth(1)).toHaveText(/debug/i);
    await expect(groupLabels.nth(2)).toHaveText(/mission/i);
  });

  test('Deep-Link ?week=2 (noch nicht verfügbar) zeigt die Wochenauswahl statt der Tour', async ({ page }) => {
    await page.goto('/kurs/ki-labor?week=2');
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
  });
});
