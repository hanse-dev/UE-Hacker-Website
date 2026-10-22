import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { expectGuideContent } from './helpers/guide-content.js';

const CONTENT_DIR = path.join('content', 'microbit-sterne');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const STORAGE_KEY = 'ue-hacker-interactive-progress-microbit-sterne';
const IMAGE_DIR = path.join('public', 'microbit', 'sterne');

test.describe('micro:bit-Kurs: Fang den Stern (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      if (sessionStorage.getItem('microbit-test-init')) return;
      sessionStorage.setItem('microbit-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
  });

  async function openCourse(page, completedLessonIds = []) {
    if (completedLessonIds.length) {
      await page.addInitScript(([key, ids]) => localStorage.setItem(
        key, JSON.stringify({ variant: 'microbit-sterne', completedLessonIds: ids }),
      ), [STORAGE_KEY, completedLessonIds]);
    }
    await page.goto('/kurs/projekt-microbit-sterne');
    await expect(page.locator('.course-description')).toContainText('Korb');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, und jeden Abschnitt gibt es für Blöcke, Python und JavaScript', () => {
    expectGuideContent(CONTENT_DIR);
    for (const lesson of lessons) {
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      expect((md.match(/^:::javascript$/gm) || []).length, lesson.file).toBeGreaterThan(0);
    }
  });

  test('Jedes erzeugte Bild wird in einer Lektion gezeigt, jede Lektion hat mindestens ein Bild', () => {
    const used = new Set();
    for (const lesson of lessons) {
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      const imgs = [...md.matchAll(/<img src="\/microbit\/sterne\/([^"]+)" alt="[^"]{20,}"/g)].map((m) => m[1]);
      expect(imgs.length, `${lesson.file}: Bilder mit Alt-Text`).toBeGreaterThan(0);
      imgs.forEach((name) => used.add(name));
    }
    for (const file of fs.readdirSync(IMAGE_DIR)) expect([...used], file).toContain(file);
  });

  test('Startklar: Bilder laden und passen auf ein Handy, Hilfe beim Verbinden und Plan B sind da', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 800 });
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content).toContainText('Chrome');
    await expect(content).toContainText('Edge');
    await expect(content.locator('h2', { hasText: 'Verbindet sich nicht?' })).toBeVisible();
    await expect(content.locator('h2', { hasText: 'Plan B' })).toBeVisible();

    const images = content.locator('img');
    await expect(images).toHaveCount(5);
    for (let i = 0; i < 5; i++) {
      const img = images.nth(i);
      await img.scrollIntoViewIfNeeded();
      await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth)).toBeGreaterThan(0);
      const [imgBox, contentBox] = [await img.boundingBox(), await content.boundingBox()];
      expect(imgBox.x + imgBox.width).toBeLessThanOrEqual(contentBox.x + contentBox.width);
    }
    await expect(content.locator('img[src="/microbit/sterne/hilfe.svg"]')).toBeVisible();
  });

  test('LED-Blöcke haben die MakeCode-Farbe, alle drei Ansichten stehen zur Wahl', async ({ page }) => {
    await openCourse(page);
    await expect(page.locator('.guide-mode-btn')).toHaveCount(3);
    const led = page.locator('.guide-lesson .mc-block.mc-led').first();
    await expect(led).toHaveText('Zeichne x 2 y 0');
    await expect(led).toHaveCSS('background-color', 'rgb(92, 45, 145)');

    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(page.locator('.guide-lesson pre code.language-python').first()).toContainText('display.set_pixel(2, 0, 9)');
    await expect(page.locator('.guide-lesson .mc-blocks').first()).toBeHidden();
  });

  test('Stufe 1: Knopf A ist vorgegeben, Knopf B steckt nur in der eingeklappten Lösung', async ({ page }) => {
    await openCourse(page, ['lektion-01']);
    await page.locator('.lesson-item').nth(1).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toContainText('Stufe 1');
    await expect(content.locator('.mc-block:visible', { hasText: 'wenn Knopf B geklickt' })).toHaveCount(0);

    const solution = content.locator('details', { has: page.locator('summary', { hasText: 'Lösung anzeigen' }) });
    await solution.locator('summary').click();
    await expect(solution.locator('.mc-block', { hasText: 'wenn Knopf B geklickt' })).toBeVisible();
    await expect(solution.locator('.mc-block', { hasText: 'wenn korb < 4 dann' })).toBeVisible();
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

  test('Kurs ist in der Projekte-Übersicht verlinkt, der Filter Spiele zeigt ihn mit Beta-Kennzeichen', async ({ page }) => {
    await page.goto('/projekte');
    const card = page.locator('a.projekt-card[href="/kurs/projekt-microbit-sterne"]');
    await expect(card).toBeVisible({ timeout: 15000 });
    await expect(card.locator('.beta-badge')).toBeVisible();
    await page.locator('.filter-chip', { hasText: 'Spiele' }).click();
    await expect(card).toBeVisible();
    await card.click();
    await expect(page.locator('.course-description')).toContainText('Chrome');
    await expect(page.locator('.btn-start-course')).toBeVisible();
  });
});
