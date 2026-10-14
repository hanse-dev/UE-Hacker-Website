import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { readFileSync } from 'fs';

const lessons = JSON.parse(readFileSync(new URL('../content/js-memory/lessons.json', import.meta.url), 'utf-8'));

const STORAGE_KEY = 'ue-hacker-interactive-progress-js-memory';
const COURSE_URL = '/kurs/projekt-js-memory';

// Projekt "Memory": erstes DOM-Projekt (kein Canvas). Der Kurs laeuft in der JS-Sandbox im
// DOM-Modus (`"sandboxMode": "dom"` in kurse.json) - die Uebungsflaeche aus js-grundkurs Woche 7
// ist sichtbar, das Canvas nicht. Die Sandbox ist eine gemeinsame Arbeitsflaeche pro Lektion
// (`.js-workspace`, siehe tests/js-spielewerkstatt.spec.js).
test.describe('Projekt Memory (JS-Sandbox im DOM-Modus)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  const unlockAll = (page) =>
    page.addInitScript(
      ({ key, ids }) => {
        localStorage.setItem(
          key,
          JSON.stringify({ version: 1, courseId: 'projekt-js-memory', variant: 'js-memory', completedLessonIds: ids })
        );
      },
      { key: STORAGE_KEY, ids: lessons.map((l) => l.id) }
    );

  const openCourse = async (page) => {
    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
  };

  const openLesson = async (page, lessonIdx) => {
    await page.locator('.lesson-item').nth(lessonIdx).click();
    await expect(page.locator('.lesson-item.active')).toContainText(lessons[lessonIdx].title);
    await expect(page.locator('.task-block')).toHaveCount(lessons[lessonIdx].tasks.length);
  };

  test('Kurs laedt, zeigt die DOM-Uebungsflaeche statt des Canvas und Lektion 1 schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(30000);
    await page.addInitScript((key) => localStorage.removeItem(key), STORAGE_KEY);
    await page.goto(COURSE_URL);
    await expect(page.locator('.course-description')).toContainText('Memory');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(7, { timeout: 15000 });
    await expect(page.locator('.btn-kernel')).toHaveCount(0);

    // Beispiel 1: Ausfuehren reicht. In der Sandbox ist die Uebungsflaeche sichtbar (DOM-Modus),
    // das Canvas nicht - und die per createElement gebaute Karte haengt wirklich in der Seite.
    const task0 = page.locator('.task-block').nth(0);
    await task0.locator('.btn-run').click();
    await expect(task0.locator('.task-done')).toBeVisible({ timeout: 10000 });
    const frame0 = page.frameLocator('.js-workspace iframe.js-sandbox');
    await expect(frame0.locator('#dom-uebung')).toBeVisible();
    await expect(frame0.locator('canvas')).toBeHidden();
    await expect(frame0.locator('#ueberschrift')).toHaveText('Memory');
    await expect(frame0.locator('#dom-uebung button', { hasText: '🐶' })).toBeVisible();

    const task1 = page.locator('.task-block').nth(1);
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.task-done')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task2.locator('.cm-host'), lessons[0].tasks[2].solution);
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Canvas-Projekte bleiben im Canvas-Modus (kein sandboxMode in kurse.json)', async ({ page }) => {
    await page.goto('/kurs/projekt-js-snake');
    await page.locator('.btn-start-course').click();
    const task0 = page.locator('.task-block').nth(0);
    await expect(task0).toBeVisible({ timeout: 15000 });
    await task0.locator('.btn-run').click();
    await expect(task0.locator('.task-done')).toBeVisible({ timeout: 10000 });
    const frame0 = page.frameLocator('.js-workspace iframe.js-sandbox');
    await expect(frame0.locator('canvas')).toBeVisible();
    await expect(frame0.locator('#dom-uebung')).toBeHidden();
  });

  test('dom_click_text mit ID-Liste: Paar-Vergleich wird ueber mehrere verschiedene Karten geprueft', async ({ page }) => {
    test.setTimeout(30000);
    await unlockAll(page);
    await openCourse(page);
    await openLesson(page, 4);

    // Lektion 5, Aufgabe 3: Die Pruefung klickt karte2, karte6 (Paar), dann karte0, karte1 (kein
    // Paar). Eine "Loesung", die immer "Paar gefunden!" meldet, darf nicht bestehen.
    const task = page.locator('.task-block').nth(2);
    const wrong = lessons[4].tasks[2].solution.replace("'Leider kein Paar.'", "'Paar gefunden!'");
    expect(wrong).not.toBe(lessons[4].tasks[2].solution);
    await setCodeMirrorContent(task.locator('.cm-host'), wrong);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(task.locator('.cm-host'), lessons[4].tasks[2].solution);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Fertiges Memory ist wirklich spielbar: aufdecken, zurueckdrehen, Zuege zaehlen, gewinnen', async ({ page }) => {
    test.setTimeout(60000);
    await unlockAll(page);
    await openCourse(page);
    await openLesson(page, 6);

    // Lektion 7, Aufgabe 3 (Gewinn-Erkennung): Karten liegen ungemischt, Paare sind i und i + 4.
    const task = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task.locator('.cm-host'), lessons[6].tasks[2].solution);
    await task.locator('.btn-run').click();
    await expect(page.locator('.js-workspace .output-display')).toBeVisible({ timeout: 10000 });

    const frame = page.frameLocator('.js-workspace iframe.js-sandbox');
    const karte = (i) => frame.locator(`#karte${i}`);
    await expect(frame.locator('#dom-uebung button')).toHaveCount(8);
    await expect(karte(0)).toHaveText('❓');

    // Falsches Paar: beide Karten liegen kurz offen, drehen sich dann von allein zurueck.
    await karte(0).click();
    await expect(karte(0)).toHaveText('🐶');
    await karte(1).click();
    await expect(karte(1)).toHaveText('🐱');
    await expect(frame.locator('#text')).toHaveText('Leider kein Paar.');
    await expect(frame.locator('#anzeige')).toHaveText('Züge: 1');
    await expect(karte(0)).toHaveText('❓', { timeout: 5000 });
    await expect(karte(1)).toHaveText('❓');

    // Alle vier Paare: bleiben offen, am Ende steht die Gewinn-Meldung mit der Zahl der Zuege.
    for (const [i, symbol] of ['🐶', '🐱', '🦊', '🐸'].entries()) {
      await karte(i).click();
      await karte(i + 4).click();
      await expect(karte(i)).toHaveText(symbol);
      await expect(karte(i + 4)).toHaveText(symbol);
    }
    await expect(frame.locator('#anzeige')).toHaveText('Züge: 5');
    await expect(frame.locator('#text')).toHaveText('Gewonnen in 5 Zügen!');
  });

  test('Kompletter Durchlauf: jede Musterlösung besteht ihre Prüfung, keine unveränderte Vorlage besteht', async ({ page }) => {
    test.setTimeout(240000);
    await unlockAll(page);
    await openCourse(page);

    for (const [lessonIdx, lesson] of lessons.entries()) {
      await openLesson(page, lessonIdx);

      for (const [taskIdx, task] of lesson.tasks.entries()) {
        const block = page.locator('.task-block').nth(taskIdx);
        const label = `${lesson.id} Aufgabe ${taskIdx}`;

        if (task.example) {
          // Beispiele haben keinen Pruefen-Button - ein fehlerfreier Lauf zaehlt.
          await expect(block.locator('.btn-check'), label).toHaveCount(0);
          await block.locator('.btn-run').click();
          await expect(block.locator('.task-done'), label).toBeVisible({ timeout: 10000 });
          await expect(page.locator('.js-workspace .output-content'), label).not.toContainText('Fehler');
          continue;
        }

        expect(task.solution, `${label}: keine Musterlösung`).toBeTruthy();
        expect(task.validation?.type, `${label}: keine Prüfung`).toBeTruthy();

        // Die Vorlage allein darf nie bestehen - sonst prueft die Aufgabe nichts.
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-error'), `${label}: Vorlage besteht`).toBeVisible({ timeout: 10000 });

        await setCodeMirrorContent(block.locator('.cm-host'), task.solution);
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-success'), label).toBeVisible({ timeout: 10000 });
      }
    }
  });
});
