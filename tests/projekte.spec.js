import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';
import { startKernel } from './helpers/kernel.js';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// Prueft die drei Offline-Download-Links (Notebooks, eine Python-Datei, Einzeldateien je Lektion):
// richtige URL und die Datei wird wirklich als ZIP ausgeliefert (erzeugt von
// scripts/pack_notebooks.py, vor jedem Lauf sichergestellt durch scripts/ensure-test-prereqs.mjs).
async function expectOfflineZips(page, links, base) {
  await expect(links).toHaveCount(3);
  for (const [i, format] of ['notebooks', 'komplett', 'einzeln'].entries()) {
    const href = `${base}-${format}.zip`;
    await expect(links.nth(i)).toHaveAttribute('href', href);
    const res = await page.request.get(href);
    expect(res.status(), href).toBe(200);
    expect((await res.body()).subarray(0, 2).toString(), href).toBe('PK');
  }
}

test.describe('Projekte-Übersicht', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-progress-morsecode');
    });
  });

  test('zeigt alle Projekt-Karten', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });
    await expect(page.locator('a[href="/kurs/projekt-caesar-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-haeufigkeitsanalyse"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-morsecode"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-zahlendetektiv"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-spielewerkstatt"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-snake"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-memory"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-quiz"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-text-adventure"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-microbit-auto"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-microbit-ampel"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-microbit-sterne"]')).toBeVisible();
  });

  test('Projekt-Karte ist ganzflächig klickbar, nicht nur der "Jetzt starten"-Link', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });

    await page.locator('a.projekt-card[href="/kurs/projekt-caesar-chiffre"] h3').click();
    await expect(page).toHaveURL(/projekt-caesar-chiffre/);
  });

  test('Level-Filter "Fortgeschritten" reduziert auf Zahlen-Detektiv, Vigenère-Chiffre, Häufigkeitsanalyse, Snake, Quiz-Generator und Text-Adventure', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Fortgeschritten' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(6);
    await expect(page.locator('a[href="/kurs/projekt-zahlendetektiv"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-haeufigkeitsanalyse"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-snake"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-quiz"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-text-adventure"]')).toBeVisible();
  });

  test('Tag-Filter "Kryptografie" zeigt Cäsar-, Vigenère-Chiffre und Häufigkeitsanalyse', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Kryptografie' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(3);
    await expect(page.locator('a[href="/kurs/projekt-caesar-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-haeufigkeitsanalyse"]')).toBeVisible();
  });

  test('Sprach-Filter "JavaScript" zeigt Spielewerkstatt, Snake, Memory und Quiz-Generator', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'JavaScript' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(4);
    await expect(page.locator('a[href="/kurs/projekt-js-spielewerkstatt"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-snake"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-memory"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-quiz"]')).toBeVisible();
  });

  test('Zurücksetzen-Button stellt alle Projekte wieder her', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(13, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Fortgeschritten' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(6);

    await page.locator('.filter-reset').click();
    await expect(page.locator('.projekt-card')).toHaveCount(13);
  });

  test('Morsecode-Projekt lädt und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-morsecode');
    await expect(page.locator('.course-description')).toContainText('Morsecode');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });

    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    const task1 = page.locator('.task-block').nth(0);
    await task1.locator('.code-editor').fill(
      "MORSE = {'a': '.-', 'b': '-...', 's': '...', 'o': '---'}\nprint(MORSE['s'])"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(1);
    await task2.locator('.code-editor').fill(
      "MORSE = {'a': '.-', 'b': '-...', 's': '...', 'o': '---'}\nprint(MORSE['o'])"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Vigenère-Chiffre-Projekt lädt und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-vigenere-chiffre');
    await expect(page.locator('.course-description')).toContainText('Vigenère');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });

    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    const task1 = page.locator('.task-block').nth(0);
    await task1.locator('.code-editor').fill("print(ord('m') - ord('a'))");
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(1);
    await task2.locator('.code-editor').fill("print(ord('z') - ord('a'))");
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Häufigkeitsanalyse-Projekt lädt und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-interactive-progress-haeufigkeitsanalyse');
    });
    await page.goto('/kurs/projekt-haeufigkeitsanalyse');
    await expect(page.locator('.course-description')).toContainText('Geheimnachricht');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(8, { timeout: 15000 });
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);

    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    // Die unveränderte Vorlage (zählt nichts, gibt 0 aus) darf die Prüfung nicht bestehen.
    const task1 = page.locator('.task-block').nth(0);
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await task1.locator('.code-editor').fill(
      'satz = "jeder mensch lebt gerne in frieden"\nanzahl = 0\nfor zeichen in satz:\n    if zeichen == "e":\n        anzahl = anzahl + 1\n\nprint(anzahl)'
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    // Bonus: der abgefangene Geheimtext steht in der Vorlage, nur die Schleife fehlt.
    const task2 = page.locator('.task-block').nth(1);
    const vorlage = await task2.locator('.code-editor').inputValue();
    expect(vorlage).toContain('dboppox gsb exc roedo');
    await task2.locator('.code-editor').fill(
      vorlage.replace('# deine Schleife hier', "for zeichen in geheimtext:\n    if zeichen == 'o':\n        anzahl = anzahl + 1")
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Häufigkeitsanalyse: jede Musterlösung aus lessons.json besteht in Pyodide ihre eigene Prüfung', async ({ page }) => {
    test.setTimeout(180000);
    const lessons = JSON.parse(
      fs.readFileSync(path.join(process.cwd(), 'content', 'haeufigkeitsanalyse', 'lessons.json'), 'utf-8')
    );
    expect(lessons).toHaveLength(8);
    // Alle Lektionen als abgeschlossen vormerken, damit jede direkt anklickbar ist.
    await page.addInitScript((ids) => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-haeufigkeitsanalyse',
        JSON.stringify({ version: 1, courseId: 'projekt-haeufigkeitsanalyse', variant: 'haeufigkeitsanalyse', completedLessonIds: ids })
      );
    }, lessons.map((l) => l.id));
    await page.goto('/kurs/projekt-haeufigkeitsanalyse');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(8, { timeout: 15000 });

    for (const [lessonIdx, lesson] of lessons.entries()) {
      await page.locator('.lesson-item').nth(lessonIdx).click();
      await expect(page.locator('.lesson-item.active')).toContainText(lesson.title);
      await expect(page.locator('.task-block')).toHaveCount(lesson.tasks.length);
      // Erst wenn die Vorlage der neuen Lektion im Editor steht, ist der Wechsel wirklich durch.
      await expect(page.locator('.task-block').nth(0).locator('.code-editor')).toHaveValue(lesson.tasks[0].codeTemplate);
      await startKernel(page);
      await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

      for (const [taskIdx, task] of lesson.tasks.entries()) {
        expect(task.solution, `${lesson.id} Aufgabe ${taskIdx + 1}: keine Musterlösung`).toBeTruthy();
        expect(task.validation.expected, `${lesson.id} Aufgabe ${taskIdx + 1}: kein expected`).toBeTruthy();
        const block = page.locator('.task-block').nth(taskIdx);
        await block.locator('.code-editor').fill(task.solution);
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-success'), `${lesson.id} Aufgabe ${taskIdx + 1}`).toBeVisible({ timeout: 15000 });
      }
    }
  });

  test('Python-Projekt zeigt die drei Offline-Downloads, JS-Projekt nicht', async ({ page }) => {
    await page.goto('/kurs/projekt-morsecode');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 15000 });
    await expectOfflineZips(page, page.locator('.offline-downloads a'), '/projekt-zips/morsecode');

    await page.goto('/kurs/projekt-js-snake');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.offline-downloads')).toHaveCount(0);
  });

  test('Snake-Projekt lädt mit der JS-Sandbox-Engine und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(30000);
    await page.goto('/kurs/projekt-js-snake');
    await expect(page.locator('.course-description')).toContainText('Schlange');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(6, { timeout: 15000 });
    await expect(page.locator('.btn-kernel')).toHaveCount(0);

    // Lektion 1: zwei Beispiele (nur Ausführen), dann die eigene Zeichenaufgabe (Prüfen).
    const task0 = page.locator('.task-block').nth(0);
    await task0.locator('.btn-run').click();
    await expect(task0.locator('.task-done')).toBeVisible({ timeout: 10000 });

    const task1 = page.locator('.task-block').nth(1);
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.task-done')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(
      task2.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nconst groesse = 20;\nctx.fillStyle = 'limegreen';\nctx.fillRect(2 * groesse, 2 * groesse, groesse, groesse);"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Text-Adventure-Projekt lädt und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-text-adventure');
    await expect(page.locator('.course-description')).toContainText('Fluchtraum');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(6, { timeout: 15000 });

    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    const task1 = page.locator('.task-block').nth(0);
    await task1.locator('.code-editor').fill(
      'raum = {\n    "beschreibung": "Du wachst in einer alten Bibliothek auf. Ein Vorhängeschloss versperrt die Tür nach Norden.",\n    "ausgaenge": {"westen": "arbeitszimmer"}\n}\nprint(raum["beschreibung"])\nprint(raum["ausgaenge"]["westen"])'
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(1);
    await task2.locator('.code-editor').fill(
      'raum2 = {\n    "beschreibung": "Ein dunkler Keller.",\n    "ausgaenge": {"treppe": "bibliothek"}\n}\nprint(raum2["ausgaenge"]["treppe"])'
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });
});
