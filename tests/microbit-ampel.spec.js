import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { expectGuideContent } from './helpers/guide-content.js';

const CONTENT_DIR = path.join('content', 'microbit-ampel');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const STORAGE_KEY = 'ue-hacker-interactive-progress-microbit-ampel';

test.describe('micro:bit-Kurs: Ampelanlage (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
  });

  async function openCourse(page, completedLessonIds = []) {
    if (completedLessonIds.length) {
      await page.addInitScript(([key, ids]) => localStorage.setItem(
        key, JSON.stringify({ variant: 'microbit-ampel', completedLessonIds: ids }),
      ), [STORAGE_KEY, completedLessonIds]);
    }
    await page.goto('/kurs/projekt-microbit-ampel');
    await expect(page.locator('.course-description')).toContainText('Ampelanlage');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, und jeder Abschnitt gibt es für Blöcke und Python', () => {
    expectGuideContent(CONTENT_DIR);
  });

  test('Steckpläne werden ausgeliefert und passen auch auf ein Handy', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 800 });
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    const images = content.locator('img');
    await expect(images).toHaveCount(2);
    for (let i = 0; i < 2; i++) {
      const img = images.nth(i);
      await img.scrollIntoViewIfNeeded();
      await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth)).toBeGreaterThan(0);
      const [imgBox, contentBox] = [await img.boundingBox(), await content.boundingBox()];
      expect(imgBox.x + imgBox.width).toBeLessThanOrEqual(contentBox.x + contentBox.width);
    }
    for (const name of ['breadboard', 'stufe-0', 'stufe-1', 'stufe-2', 'taster']) {
      const res = await page.request.get(`/microbit/ampel/${name}.svg`);
      expect(res.status(), name).toBe(200);
      expect(await res.text(), name).toContain('<svg');
    }
  });

  test('Pin- und Funk-Blöcke haben die MakeCode-Farben, der Hinweis passt zu jedem micro:bit-Kurs', async ({ page }) => {
    await openCourse(page, lessons.slice(0, 5).map((l) => l.id));
    await expect(page.locator('.guide-tasks .editor-hint')).toContainText('micro:bit');
    await expect(page.locator('.guide-tasks .editor-hint')).not.toContainText('Auto');

    await page.locator('.lesson-item').first().click();
    const pins = page.locator('.mc-block.mc-pins').first();
    await expect(pins).toHaveText('schreibe digitalen Wert von Pin P13 auf 1');
    await expect(pins).toHaveCSS('background-color', 'rgb(178, 34, 34)');

    await page.locator('.lesson-item').nth(5).click();
    const funk = page.locator('.mc-block.mc-funk').first();
    await expect(funk).toHaveText('setze Funkgruppe auf 7');
    await expect(funk).toHaveCSS('background-color', 'rgb(227, 0, 140)');
  });

  test('Stufe 1: Das Gerüst ist sichtbar, die fertige Lösung ist eingeklappt', async ({ page }) => {
    await openCourse(page, ['lektion-01']);
    await page.locator('.lesson-item').nth(1).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toContainText('Stufe 1');
    await expect(content.locator('.mc-block:visible', { hasText: 'pausiere (ms) 5000' })).toHaveCount(0);

    const solution = content.locator('details', { has: page.locator('summary', { hasText: 'Lösung anzeigen' }) });
    await solution.locator('summary').click();
    await expect(solution.locator('.mc-block', { hasText: 'pausiere (ms) 5000' })).toBeVisible();
    await expect(solution.locator('pre code.language-python')).toBeHidden();
  });

  test('Pflichtaufgaben abhaken schließt die Stufe ab und schaltet die nächste frei', async ({ page }) => {
    await openCourse(page);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);
    const tasks = page.locator('.guide-task');
    for (const [i, task] of lessons[0].tasks.entries()) {
      if (!task.isBonus) await tasks.nth(i).locator('.guide-task-check').check();
    }
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Kurs ist in der Projekte-Übersicht verlinkt, mit eigenem Filter für Elektronik', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-microbit-ampel"]')).toBeVisible({ timeout: 15000 });
    await page.locator('.filter-chip', { hasText: 'Elektronik' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(1);
    await page.locator('a.projekt-card[href="/kurs/projekt-microbit-ampel"]').click();
    await expect(page.locator('.course-description')).toContainText('Breadboard');
  });
});
