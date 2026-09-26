import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// JavaScript-Grundkurs (Route /kurs/js-grundkurs, echter Kurs mit kurse.json-Eintrag, ueber
// CourseDetail.vue eingebunden wie jeder andere Kurs). 9 Wochen, siehe KURSPLAN.md
// "JavaScript-Track: Grundkurs". Nutzt dieselbe, bereits getestete JS-Sandbox-Engine wie
// js-spielewerkstatt.spec.js. Struktur pro Woche angelehnt an den 12-Wochen-Python-Kurs
// (Lektion/Debug/Mission als gruppierte Abschnitte, ohne Zertifikat/Quiz - bewusste
// Nutzer-Entscheidung fuer dieses leichte Format), zusaetzlich eine Wochenauswahl
// (JsGrundkursTour.vue) vor dem eigentlichen Wochen-Stepper (JsCourseTour.vue).
// Wochen sind frei anklickbar (kein Gating zwischen Wochen) - nur die Lektionen INNERHALB einer
// Woche sind sequenziell freigeschaltet (ProjectCourse.vue-Muster).
//
// Beispiel-Aufgaben (`"example": true` in lessons.json, bereits fertiger unveraenderter
// codeTemplate) haben keinen "Pruefen"-Button - nur "Ausfuehren", ein erfolgreicher Lauf zaehlt
// automatisch als erledigt (siehe JsLessonView.vue markExampleDone). `taskCodes` ist ein Array mit
// einem Eintrag pro Aufgabe der Lektion: `null` heisst "Beispiel, unveraendert ausfuehren", ein
// String ersetzt den Editor-Inhalt vor dem Pruefen der echten Aufgabe.
async function completeLesson(page, taskCodes) {
  for (let i = 0; i < taskCodes.length; i++) {
    const task = page.locator('.task-block').nth(i);
    if (taskCodes[i] === null) {
      await task.locator('.btn-run').click();
      await expect(task.locator('.task-done')).toBeVisible({ timeout: 10000 });
    } else {
      await setCodeMirrorContent(task.locator('.cm-host'), taskCodes[i]);
      await task.locator('.btn-check').click();
      await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
    }
  }

  // Erst der "Weiter"-Button (im lesson-complete-box) schaltet tatsächlich zur nächsten Lektion um.
  await expect(page.locator('.lesson-complete-box')).toBeVisible({ timeout: 5000 });
  await page.locator('.btn-next').click();
}

// Loest alle Aufgaben einer reinen Pflichtaufgaben-Lektion (kein Beispiel dabei) nacheinander per
// Code + "Pruefen" - fuer Debug- und Missions-Lektionen, deren Aufgaben alle ohne `example` sind.
async function completeAllRequired(page, fixes) {
  for (let i = 0; i < fixes.length; i++) {
    const task = page.locator('.task-block').nth(i);
    await setCodeMirrorContent(task.locator('.cm-host'), fixes[i]);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  }
  await expect(page.locator('.lesson-complete-box')).toBeVisible({ timeout: 5000 });
  await page.locator('.btn-next').click();
}

test.describe('JS-Grundkurs (Wochenauswahl)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche1');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche2');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche3');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche4');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche5');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche6');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche7');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche8');
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche9');
    });
  });

  test('Wochenauswahl: alle 9 Wochen verfügbar, keine "kommt noch"-Kachel mehr', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.week-tile')).toHaveCount(9);

    for (let i = 0; i < 9; i++) {
      await expect(page.locator('.week-tile').nth(i)).not.toBeDisabled();
    }
    await expect(page.locator('.week-tile-badge')).toHaveCount(0);
  });

  test('Woche 1 anklicken öffnet die Wochen-Tour, "Andere Woche wählen" führt zurück', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs');
    await page.locator('.btn-start-course').click();
    await page.locator('.week-tile').nth(0).click();
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');

    await page.locator('.breadcrumb-back').click();
    await expect(page.locator('.week-tile')).toHaveCount(9);
    await expect(page.locator('.stepper-step')).toHaveCount(0);
  });

  test('Deep-Link ?week=2 öffnet direkt die Wochen-Tour für Woche 2', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=2');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 2');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Bedingungen');
  });

  test('Deep-Link ?week=3 öffnet direkt die Wochen-Tour für Woche 3', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=3');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 3');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Schleifen');
  });

  test('Deep-Link ?week=4 öffnet direkt die Wochen-Tour für Woche 4', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=4');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 4');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Funktionen');
  });

  test('Deep-Link ?week=5 öffnet direkt die Wochen-Tour für Woche 5', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=5');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 5');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Arrays');
  });

  test('Deep-Link ?week=6 öffnet direkt die Wochen-Tour für Woche 6', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=6');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 6');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Objekte');
  });

  test('Deep-Link ?week=7 öffnet direkt die Wochen-Tour für Woche 7, Sandbox mit DOM-Übungsfläche sichtbar', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=7');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 7');
    await expect(page.locator('.tour-breadcrumb')).toContainText('DOM');

    // Woche 7 ist die erste Woche, die das Sandbox-iframe sichtbar zeigt (DOM-Übungsfläche).
    const task0 = page.locator('.task-block').first();
    await task0.locator('.btn-run').click();
    await expect(task0.locator('iframe.js-sandbox')).toBeVisible();
    await expect(task0.locator('.sandbox-toolbar')).toBeVisible();
  });

  test('Deep-Link ?week=8 öffnet direkt die Wochen-Tour für Woche 8', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=8');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 8');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Objekte als Blaupause');
  });

  test('Deep-Link ?week=9 öffnet direkt die Wochen-Tour für Woche 9', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=9');
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 9');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Abschlussprojekt');
  });

  test('Seite laedt mit Stepper (7 Kullern in 3 Abschnitten Lektion/Debug/Mission) und Breadcrumb, ohne sichtbares Canvas', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs');
    await page.locator('.btn-start-course').click();
    await page.locator('.week-tile').nth(0).click();
    await expect(page.locator('.stepper-step')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.btn-kernel')).toHaveCount(0);
    // Nur Lektion 1 ist zu Beginn freigeschaltet (aktueller Kuller), der Rest ist gesperrt.
    await expect(page.locator('.stepper-step').nth(0)).toHaveClass(/current/);
    await expect(page.locator('.stepper-step').nth(1)).toHaveClass(/locked/);
    await expect(page.locator('.stepper-step').nth(1)).toBeDisabled();

    const groupLabels = page.locator('.stepper-group-label');
    await expect(groupLabels).toHaveCount(3);
    await expect(groupLabels.nth(0)).toHaveText(/lektion/i);
    await expect(groupLabels.nth(1)).toHaveText(/debug/i);
    await expect(groupLabels.nth(2)).toHaveText(/mission/i);

    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 1');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Lektion 1');

    // Lektion 1: zwei Beispiele (nur Ausfuehren) zuerst, dann die Pflichtaufgabe (Ausfuehren +
    // Pruefen) als letzte - "Pruefen" ist immer die letzte Aufgabe einer Lektion.
    const task0 = page.locator('.task-block').nth(0);
    await expect(task0).toHaveClass(/task-example/);
    await expect(task0.locator('.badge-example')).toBeVisible();
    await expect(task0.locator('.btn-check')).toHaveCount(0);

    const task1 = page.locator('.task-block').nth(1);
    await expect(task1).toHaveClass(/task-example/);
    await expect(task1.locator('.btn-check')).toHaveCount(0);

    const task2 = page.locator('.task-block').nth(2);
    await expect(task2).toHaveClass(/task-required/);
    await expect(task2.locator('.badge-required')).toBeVisible();
    await expect(task2.locator('.btn-check')).toBeVisible();

    // show-canvas="false": das iframe existiert (ist die Ausfuehrungsumgebung), bleibt aber
    // unsichtbar - dieser Kurs zeichnet nie etwas, die Ausgabe-Box unter dem Editor reicht.
    await task0.locator('.btn-run').click();
    await expect(task0.locator('iframe.js-sandbox')).toBeAttached();
    await expect(task0.locator('iframe.js-sandbox')).toBeHidden();
    await expect(task0.locator('.sandbox-toolbar')).toBeHidden();
    // Ein erfolgreicher Lauf einer Beispiel-Aufgabe zaehlt automatisch als erledigt.
    await expect(task0.locator('.task-done')).toBeVisible({ timeout: 10000 });
  });

  test('Lektion 1: falsche Loesung schlaegt fehl, richtige besteht', async ({ page }) => {
    await page.goto('/kurs/js-grundkurs?week=1');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    // Die Pflichtaufgabe ist die letzte Aufgabe der Lektion (Index 2, nach den zwei Beispielen).
    const task2 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task2.locator('.cm-host'), "console.log('Hallo Welt!');");
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(task2.locator('.cm-host'), "console.log('Ich lerne JavaScript!');");
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Debug: kaputter Code schlaegt fehl, reparierter Code besteht', async ({ page }) => {
    // Debug-Abschnitt ist erst frei, wenn alle 5 Lektionen abgeschlossen sind.
    await page.addInitScript(() => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-js-grundkurs-woche1',
        JSON.stringify({
          version: 1,
          courseId: 'js-grundkurs-woche1',
          variant: 'js-grundkurs-woche1',
          completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
        })
      );
    });
    await page.goto('/kurs/js-grundkurs?week=1');
    await page.locator('.stepper-step[title="Fehlersuche"]').click();
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    // Erste Debug-Aufgabe unveraendert (kaputt) ausgeführt - muss fehlschlagen.
    const task0 = page.locator('.task-block').nth(0);
    await task0.locator('.btn-check').click();
    await expect(task0.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(task0.locator('.cm-host'), "console.log('Willkommen');");
    await task0.locator('.btn-check').click();
    await expect(task0.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Mission: in Lektionsaufgaben zaehlt nur die Ausgabe, auch hart codiert', async ({ page }) => {
    // Bewusste Entscheidung (siehe useTaskValidation.js `structuralChecksOk`): normale
    // Lektions-/Missionsaufgaben pruefen nur die Ausgabe, nicht ob dafuer echte Variablen
    // angelegt wurden - das gilt nur noch fuer den zertifikatsrelevanten Wochen-Check.
    await page.addInitScript(() => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-js-grundkurs-woche1',
        JSON.stringify({
          version: 1,
          courseId: 'js-grundkurs-woche1',
          variant: 'js-grundkurs-woche1',
          completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05', 'debug-01'],
        })
      );
    });
    await page.goto('/kurs/js-grundkurs?week=1');
    await page.locator('.stepper-step[title="Deine Mission"]').click();
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task0 = page.locator('.task-block').nth(0);
    await setCodeMirrorContent(task0.locator('.cm-host'), "console.log('umfang: 32, flaeche: 48');");
    await task0.locator('.btn-check').click();
    await expect(task0.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Kompletter Durchlauf Woche 1: alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=1');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [null, null, "console.log('Ich lerne JavaScript!');"]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    // Lektion 2 wird automatisch als naechste Lektion angezeigt (onLessonCompleted).
    await expect(page.locator('.task-block').nth(1)).toBeVisible();
    // Lektion 2 hat nur 2 Aufgaben (Demo + Variablen-Check) - die frühere dritte Aufgabe (const-
    // Fehler-Demo) ist jetzt Teil des Lektionstexts, nicht mehr eine eigene Aufgabe.
    await completeLesson(page, [null, 'let lieblingszahl = 7;']);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      null,
      "let zahl = 42;\nlet text = 'Katze';\nlet wahrheitswert = true;",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      null,
      'let summe = 15 + 27;\nconsole.log(`Summe: ${summe}`);',
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      'let breite = 9;\nlet hoehe = 6;\n\nlet flaeche = breite * hoehe;\nconsole.log(`Fläche: ${flaeche}`);',
      'let minuten = 24 * 60;\nconsole.log(`Ein Tag hat ${minuten} Minuten`);',
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "console.log('Willkommen');",
      'const zahl = 10;\nconsole.log(zahl);',
      "let text = 'Hund';\nconsole.log(text);",
      "let a = 5;\nlet b = 3;\nconsole.log('Summe: ' + (a + b));",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'let breite = 12;\nlet hoehe = 4;\n\nlet umfang = 2 * (breite + hoehe);\nlet flaeche = breite * hoehe;',
      'let fahrenheit = 50;\n\nlet celsius = (fahrenheit - 32) * 5 / 9;',
      'let ergebnis = 8 * 6;\nconsole.log(`Ergebnis: ${ergebnis}`);',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 2 (Bedingungen): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=2');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [null, 'let alter = 20;\nlet istVolljaehrig = alter >= 18;']);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      "let zahl = 7;\nif (zahl % 2 === 0) {\n  console.log(`${zahl} ist gerade`);\n} else {\n  console.log(`${zahl} ist ungerade`);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      "let temperatur = 5;\nif (temperatur < 10) {\n  console.log(`${temperatur} Grad: kalt`);\n} else if (temperatur < 20) {\n  console.log(`${temperatur} Grad: mild`);\n} else {\n  console.log(`${temperatur} Grad: warm`);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      'let alter = 14;\nlet groesse = 150;\n\nlet darfFahren = alter >= 12 && groesse >= 140;',
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      "let strom = true;\nlet schluessel = false;\n\nif (strom) {\n  if (schluessel) {\n    console.log('Maschine startet');\n  } else {\n    console.log('Schlüssel fehlt');\n  }\n} else {\n  console.log('Kein Strom');\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "let zahl = 5;\nif (zahl === 10) {\n  console.log('zehn');\n} else {\n  console.log('nicht zehn');\n}",
      "let signal = 'rot';\n\nif (signal === 'rot') {\n  console.log('Stopp');\n} else if (signal === 'gruen') {\n  console.log('Los');\n} else {\n  console.log('Vorsicht');\n}",
      "let hatTicket = true;\nlet hatAusweis = false;\n\nif (hatTicket || hatAusweis) {\n  console.log('Einlass gewährt');\n} else {\n  console.log('Einlass verweigert');\n}",
      "let antwort = 42;\n\nif (antwort === 42) {\n  console.log('Richtig!');\n} else {\n  console.log('Falsch, versuch es nochmal.');\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'let einkaufswert = 80;\n\nlet rabatt = 0;\nif (einkaufswert >= 50) {\n  rabatt = einkaufswert * 0.1;\n}',
      'let alter = 15;\nlet groesse = 170;\n\nlet darfTeilnehmen = alter >= 16 && groesse >= 150;',
      "let farbe = 'gelb';\n\nif (farbe === 'rot') {\n  console.log('Stopp!');\n} else if (farbe === 'gelb') {\n  console.log('Achtung!');\n} else if (farbe === 'gruen') {\n  console.log('Los!');\n} else {\n  console.log('Unbekanntes Signal');\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 3 (Schleifen): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=3');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      'let summe = 0;\nfor (let i = 1; i <= 10; i++) {\n  summe += i;\n}',
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      'let summe = 0;\nlet schritte = 0;\nwhile (summe < 20) {\n  summe += 3;\n  schritte++;\n}',
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      "for (let i = 1; i <= 10; i++) {\n  if (i === 5) {\n    continue;\n  }\n  console.log(i);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "let wort = 'banane';\nlet anzahl = 0;\nfor (const zeichen of wort) {\n  if (zeichen === 'a') {\n    anzahl++;\n  }\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      'let anzahl = 0;\nfor (let i = 1; i <= 20; i++) {\n  if (i % 3 === 0) {\n    anzahl++;\n  }\n}',
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      'for (let i = 1; i <= 5; i++) {\n  console.log(i);\n}',
      "let i = 0;\nwhile (i < 3) {\n  console.log('Piep');\n  i++;\n}",
      "for (let i = 1; i <= 5; i++) {\n  if (i === 3) {\n    continue;\n  }\n  console.log(i);\n}",
      "let wort = 'Baum';\nfor (const zeichen of wort) {\n  console.log(zeichen);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'let summe = 0;\nfor (let i = 1; i <= 20; i++) {\n  if (i % 2 === 0) {\n    summe += i;\n  }\n}',
      'let zahl = 100;\nlet versuche = 0;\nwhile (zahl >= 0) {\n  zahl -= 7;\n  versuche++;\n}',
      "for (let i = 1; i <= 15; i++) {\n  if (i % 3 === 0) {\n    continue;\n  }\n  console.log(i);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 4 (Funktionen): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=4');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      'function quadriere(zahl) {\n  return zahl * zahl;\n}\nconsole.log(quadriere(6));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      'function rechteckFlaeche(breite, hoehe) {\n  return breite * hoehe;\n}\nconsole.log(rechteckFlaeche(6, 3));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      'function istGerade(zahl) {\n  return zahl % 2 === 0;\n}\nconsole.log(istGerade(8));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      'const halbiere = (zahl) => zahl / 2;\nlet ergebnis = halbiere(10);\nconsole.log(ergebnis);',
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      'function summeBis(n) {\n  let summe = 0;\n  for (let i = 1; i <= n; i++) {\n    summe += i;\n  }\n  return summe;\n}\nconsole.log(summeBis(10));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      'function verdreifache(zahl) {\n  return zahl * 3;\n}\n\nconsole.log(verdreifache(4));',
      'function teile(zaehler, nenner) {\n  return zaehler / nenner;\n}\n\nconsole.log(teile(10, 2));',
      "function nenneFarbe() {\n  return 'Blau';\n}\n\nconsole.log(nenneFarbe());",
      'const verdopple = (zahl) => {\n  return zahl * 2;\n};\n\nconsole.log(verdopple(5));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'function kubik(zahl) {\n  return zahl * zahl * zahl;\n}\nconsole.log(kubik(3));',
      'function maximum(a, b, c) {\n  let max = a;\n  if (b > max) max = b;\n  if (c > max) max = c;\n  return max;\n}\nconsole.log(maximum(3, 9, 5));',
      "function zaehleVorkommen(text, zeichen) {\n  let anzahl = 0;\n  for (const c of text) {\n    if (c === zeichen) anzahl++;\n  }\n  return anzahl;\n}\nconsole.log(zaehleVorkommen('banane', 'a'));",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 5 (Arrays): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=5');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      "let zahlen = [10, 20, 30];\nlet mittlererWert = zahlen[1];",
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      "let warteschlange = [];\nwarteschlange.push('Anna');\nwarteschlange.push('Ben');\nwarteschlange.push('Cem');\nwarteschlange.pop();\nlet laenge = warteschlange.length;",
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      "let namen = ['Lea', 'Tom', 'Mia', 'Jan', 'Zoe'];\nlet anzahl = namen.length;\nlet letzter = namen[namen.length - 1];",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "let staedte = ['Berlin', 'Hamburg', 'Koeln'];\nfor (const stadt of staedte) {\n  console.log(`${stadt} ist dabei!`);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      'let preise = [5, 12, 8, 20, 15, 3];\nlet summe = 0;\nfor (const preis of preise) {\n  if (preis >= 10) {\n    summe += preis;\n  }\n}',
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "let obst = ['Apfel', 'Birne', 'Kirsche'];\nconsole.log(obst[0]);",
      "let farben = ['rot', 'gruen', 'blau'];\nconsole.log(farben[farben.length - 1]);",
      "let liste = ['a', 'b'];\nlet ergebnis = liste.push('c');\nconsole.log(liste);",
      'let noten = [2, 3, 1, 4];\nfor (let i = 0; i < noten.length; i++) {\n  console.log(noten[i]);\n}',
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'function summeArray(zahlen) {\n  let summe = 0;\n  for (const zahl of zahlen) {\n    summe += zahl;\n  }\n  return summe;\n}\nconsole.log(summeArray([3, 7, 2]));',
      'function groesstesElement(zahlen) {\n  let max = zahlen[0];\n  for (const zahl of zahlen) {\n    if (zahl > max) {\n      max = zahl;\n    }\n  }\n  return max;\n}\nconsole.log(groesstesElement([4, 9, 2, 15, 6]));',
      'function zaehleUeber(zahlen, grenze) {\n  let anzahl = 0;\n  for (const zahl of zahlen) {\n    if (zahl > grenze) {\n      anzahl++;\n    }\n  }\n  return anzahl;\n}\nconsole.log(zaehleUeber([5, 12, 8, 20, 3], 10));',
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 6 (Objekte): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=6');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      "let haustier = { art: 'Hund', alter: 3 };",
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      'let konto = { stand: 100 };\nkonto.stand += 50;',
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      'let wuerfel = {\n  seitenlaenge: 4,\n  volumen() {\n    return this.seitenlaenge * this.seitenlaenge * this.seitenlaenge;\n  }\n};\nconsole.log(wuerfel.volumen());',
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "let team = [\n  { name: 'Lea', punkte: 12 },\n  { name: 'Tom', punkte: 7 },\n  { name: 'Mia', punkte: 19 },\n];\nfor (const person of team) {\n  console.log(`${person.name} hat ${person.punkte} Punkte`);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      "let bestellungen = [\n  { artikel: 'Buch', preis: 12 },\n  { artikel: 'Stift', preis: 2 },\n  { artikel: 'Buch', preis: 8 },\n  { artikel: 'Heft', preis: 3 },\n];\nlet summe = 0;\nfor (const b of bestellungen) {\n  if (b.artikel === 'Buch') {\n    summe += b.preis;\n  }\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "let person = { name: 'Alex', alter: 12 };\nlet eigenschaft = 'alter';\nconsole.log(person[eigenschaft]);",
      'let rechner = {\n  wert: 10,\n  verdoppeln() {\n    return this.wert * 2;\n  }\n};\n\nconsole.log(rechner.verdoppeln());',
      "let buch = { name: 'Harry Potter', seiten: 320 };\nconsole.log(buch.name);",
      "let team = [\n  { name: 'Lea', punkte: 12 },\n  { name: 'Tom', punkte: 7 },\n];\n\nfor (const person of team) {\n  console.log(person.name);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      "function vorstellen(person) {\n  return `${person.name} ist ${person.alter} Jahre alt`;\n}\nconsole.log(vorstellen({ name: 'Mia', alter: 11 }));",
      'function gesamtPreis(artikel) {\n  let summe = 0;\n  for (const a of artikel) {\n    summe += a.preis;\n  }\n  return summe;\n}\nconsole.log(gesamtPreis([{ preis: 5 }, { preis: 12 }, { preis: 3 }]));',
      "function zaehleArt(tiere, gesuchteArt) {\n  let anzahl = 0;\n  for (const tier of tiere) {\n    if (tier.art === gesuchteArt) {\n      anzahl++;\n    }\n  }\n  return anzahl;\n}\nconsole.log(zaehleArt([{ art: 'Hund' }, { art: 'Katze' }, { art: 'Hund' }], 'Hund'));",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 7 (DOM & Interaktivität): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=7');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      "let inhalt = document.querySelector('#text').textContent;",
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      "document.querySelector('#text').textContent = 'Ich habe das geändert!';",
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      "let knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = 'Danke fürs Klicken!';\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "let zaehlerWert = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  zaehlerWert += 5;\n  document.querySelector('#anzeige').textContent = zaehlerWert;\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      "let zaehlerWert = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  zaehlerWert++;\n  if (zaehlerWert >= 5) {\n    document.querySelector('#anzeige').textContent = 'Maximum erreicht!';\n  } else {\n    document.querySelector('#anzeige').textContent = zaehlerWert;\n  }\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "let ueberschrift = document.querySelector('#ueberschrift');\nueberschrift.textContent = 'Neu!';",
      "let knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = 'Erfolg!';\n});",
      "let knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = 'Geklickt!';\n});",
      "let zaehlerWert = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  zaehlerWert++;\n  document.querySelector('#anzeige').textContent = zaehlerWert;\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      "document.querySelector('#ueberschrift').textContent = 'Mission gestartet!';",
      "let knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#text').textContent = 'Mission erfüllt!';\n});",
      "let zaehlerWert = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  zaehlerWert += 2;\n  if (zaehlerWert >= 6) {\n    document.querySelector('#anzeige').textContent = 'Fertig!';\n  } else {\n    document.querySelector('#anzeige').textContent = zaehlerWert;\n  }\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 8 (Objekte als Blaupause): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=8');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    await completeLesson(page, [
      null,
      "class Buch {\n  constructor(titel, seiten) {\n    this.titel = titel;\n    this.seiten = seiten;\n  }\n}\n\nlet meinBuch = new Buch('Der Hobbit', 310);",
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      'class Kreis {\n  constructor(radius) {\n    this.radius = radius;\n  }\n  flaeche() {\n    return Math.round(Math.PI * this.radius * this.radius);\n  }\n}\n\nlet k = new Kreis(4);\nconsole.log(k.flaeche());',
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      "class Konto {\n  constructor(inhaber, stand) {\n    this.inhaber = inhaber;\n    this.stand = stand;\n  }\n  einzahlen(betrag) {\n    this.stand += betrag;\n    return this.stand;\n  }\n}\n\nlet konto1 = new Konto('Alex', 100);\nlet konto2 = new Konto('Sam', 50);\nconsole.log(konto1.einzahlen(30));",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "class Produkt {\n  constructor(name, preis) {\n    this.name = name;\n    this.preis = preis;\n  }\n}\n\nlet produkte = [\n  new Produkt('Apfel', 2),\n  new Produkt('Brot', 3),\n  new Produkt('Milch', 1),\n];\n\nfor (const p of produkte) {\n  console.log(`${p.name}: ${p.preis}€`);\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      "class Produkt {\n  constructor(name, preis) {\n    this.name = name;\n    this.preis = preis;\n  }\n}\n\nlet produkte = [\n  new Produkt('Apfel', 2),\n  new Produkt('Buch', 15),\n  new Produkt('Brot', 3),\n  new Produkt('Kopfhoerer', 25),\n];\n\nlet summe = 0;\nfor (const p of produkte) {\n  if (p.preis >= 10) {\n    summe += p.preis;\n  }\n}",
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      "class Person {\n  constructor(name, alter) {\n    this.name = name;\n    this.alter = alter;\n  }\n}\n\nlet p = new Person('Alex', 12);\nconsole.log(p.name, p.alter);",
      "class Hund {\n  constructor(name) {\n    this.name = name;\n  }\n}\n\nlet mein = new Hund('Rex');\nconsole.log(mein.name);",
      'class Zaehler {\n  constructor() {\n    this.wert = 0;\n  }\n  erhoehen() {\n    this.wert++;\n    return this.wert;\n  }\n}\n\nlet z = new Zaehler();\nconsole.log(z.erhoehen());',
      'class Rechteck {\n  constructor(breite, hoehe) {\n    this.breite = breite;\n    this.hoehe = hoehe;\n  }\n  flaeche() {\n    return this.breite * this.hoehe;\n  }\n}\n\nlet r = new Rechteck(4, 5);\nconsole.log(r.flaeche());',
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      "class Auto {\n  constructor(marke, tempo) {\n    this.marke = marke;\n    this.tempo = tempo;\n  }\n  beschleunigen() {\n    this.tempo += 10;\n    return this.tempo;\n  }\n}\n\nlet a = new Auto('Tesla', 50);\na.beschleunigen();\nconsole.log(a.beschleunigen());",
      "class Vorrat {\n  constructor(name, menge) {\n    this.name = name;\n    this.menge = menge;\n  }\n  istLeer() {\n    return this.menge === 0;\n  }\n}\n\nlet v = new Vorrat('Mehl', 0);\nconsole.log(v.istLeer());",
      "class Bestellung {\n  constructor(artikel, menge) {\n    this.artikel = artikel;\n    this.menge = menge;\n  }\n}\n\nlet bestellungen = [\n  new Bestellung('Schrauben', 12),\n  new Bestellung('Naegel', 3),\n  new Bestellung('Bretter', 6),\n];\n\nlet anzahl = 0;\nfor (const b of bestellungen) {\n  if (b.menge >= 5) {\n    anzahl++;\n  }\n}\nconsole.log(anzahl);",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });

  test('Kompletter Durchlauf Woche 9 (Abschlussprojekt): alle 7 Lektionen loesen schaltet die Woche frei', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/kurs/js-grundkurs?week=9');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const frageClass = "class Frage {\n  constructor(frage, antwort) {\n    this.frage = frage;\n    this.antwort = antwort;\n  }\n}\n\n";

    await completeLesson(page, [
      null,
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n  new Frage('2 + 2?', '4'),\n  new Frage('Farbe des Himmels?', 'blau'),\n];\n\nfunction gibAntwort(index) {\n  return fragen[index].antwort;\n}\nconsole.log(gibAntwort(1));",
    ]);
    await expect(page.locator('.progress-count')).toContainText('1 abgeschlossen');

    await completeLesson(page, [
      null,
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n  new Frage('2 + 2?', '4'),\n  new Frage('Farbe des Himmels?', 'blau'),\n];\n\ndocument.querySelector('#text').textContent = fragen[2].frage;",
    ]);
    await expect(page.locator('.progress-count')).toContainText('2 abgeschlossen');

    await completeLesson(page, [
      null,
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n  new Frage('2 + 2?', '4'),\n  new Frage('Farbe des Himmels?', 'blau'),\n];\n\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = fragen[1].antwort;\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('3 abgeschlossen');

    await completeLesson(page, [
      null,
      "let namen = ['Anna', 'Ben'];\nlet index = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  if (index < namen.length) {\n    document.querySelector('#anzeige').textContent = namen[index];\n    index++;\n  } else {\n    document.querySelector('#anzeige').textContent = 'Ende!';\n  }\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('4 abgeschlossen');

    await completeLesson(page, [
      null,
      "let ergebnisse = [\n  { richtig: false },\n  { richtig: true },\n  { richtig: true },\n  { richtig: true },\n];\n\nfunction zaehleRichtige(liste) {\n  let anzahl = 0;\n  for (const e of liste) {\n    if (e.richtig) {\n      anzahl++;\n    }\n  }\n  return anzahl;\n}\n\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = zaehleRichtige(ergebnisse);\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('5 abgeschlossen');

    await completeAllRequired(page, [
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n];\n\ndocument.querySelector('#text').textContent = fragen[0].frage;",
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n  new Frage('2 + 2?', '4'),\n];\n\nlet index = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#text').textContent = fragen[index].frage;\n  index++;\n});",
      "function zaehleRichtige(liste) {\n  let anzahl = 0;\n  for (const a of liste) {\n    if (a.richtig) {\n      anzahl++;\n    }\n  }\n  return anzahl;\n}\n\nlet antworten = [{ richtig: true }, { richtig: true }];\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  document.querySelector('#anzeige').textContent = zaehleRichtige(antworten);\n});",
      frageClass + "let fragen = [\n  new Frage('Hauptstadt von Frankreich?', 'Paris'),\n  new Frage('2 + 2?', '4'),\n];\n\nlet index = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  if (index < fragen.length) {\n    document.querySelector('#text').textContent = fragen[index].frage;\n    index++;\n  } else {\n    document.querySelector('#text').textContent = 'Fertig!';\n  }\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('6 abgeschlossen');

    await completeAllRequired(page, [
      'function anzahlBestanden(personen) {\n  let anzahl = 0;\n  for (const p of personen) {\n    if (p.punkte >= 50) {\n      anzahl++;\n    }\n  }\n  return anzahl;\n}\nconsole.log(anzahlBestanden([{ punkte: 80 }, { punkte: 30 }, { punkte: 60 }]));',
      "let mitglieder = ['Lea', 'Tom', 'Mia'];\nlet index = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  if (index < mitglieder.length) {\n    document.querySelector('#text').textContent = mitglieder[index];\n    index++;\n  } else {\n    document.querySelector('#text').textContent = 'Alle vorgestellt!';\n  }\n});",
      "let punktestand = 0;\nlet knopf = document.querySelector('#knopf');\nknopf.addEventListener('click', () => {\n  punktestand += 10;\n  if (punktestand >= 30) {\n    document.querySelector('#anzeige').textContent = 'Level geschafft!';\n  } else {\n    document.querySelector('#anzeige').textContent = punktestand;\n  }\n});",
    ]);
    await expect(page.locator('.progress-count')).toContainText('7 abgeschlossen');
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
  });
});
