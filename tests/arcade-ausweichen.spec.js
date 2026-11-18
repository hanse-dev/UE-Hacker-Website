import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { expectGuideContent } from './helpers/guide-content.js';

// Anleitungs-Kurs für MakeCode Arcade: Der Kurs steht auf der Seite, programmiert und gespielt
// wird auf arcade.makecode.com. Blöcke tragen die Farben der Arcade-Werkzeugleiste.
const CONTENT_DIR = path.join('content', 'arcade-ausweichen');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const STORAGE_KEY = 'ue-hacker-interactive-progress-arcade-ausweichen';
const IMAGE_DIR = path.join('public', 'arcade', 'ausweichen');

test.describe('MakeCode Arcade: Ausweichen (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      if (sessionStorage.getItem('arcade-test-init')) return;
      sessionStorage.setItem('arcade-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
  });

  async function openCourse(page, completedLessonIds = []) {
    if (completedLessonIds.length) {
      await page.addInitScript(([key, ids]) => localStorage.setItem(
        key, JSON.stringify({ variant: 'arcade-ausweichen', completedLessonIds: ids }),
      ), [STORAGE_KEY, completedLessonIds]);
    }
    await page.goto('/kurs/projekt-arcade-ausweichen');
    await expect(page.locator('.course-description')).toContainText('arcade.makecode.com');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, jeden Abschnitt gibt es für Blöcke, Python und JavaScript', () => {
    expectGuideContent(CONTENT_DIR);
    for (const lesson of lessons) {
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      expect((md.match(/^:::javascript$/gm) || []).length, lesson.file).toBeGreaterThan(0);
      // Arcade-Blöcke heißen anders als micro:bit-Blöcke: keine micro:bit-Kategorien.
      expect(md, lesson.file).not.toMatch(/^\s*\[(grundlagen|eingabe|led|musik|pins|funk|minicar)\] /m);
    }
    const used = new Set();
    for (const lesson of lessons) {
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      for (const [, name] of md.matchAll(/<img src="\/arcade\/ausweichen\/([^"]+)" alt="[^"]{20,}"/g)) used.add(name);
    }
    for (const file of fs.readdirSync(IMAGE_DIR)) expect([...used], file).toContain(file);
  });

  test('Startklar: Link zum Editor öffnet einen neuen Tab, Bild passt aufs Handy, Hinweis nennt Arcade', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 800 });
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    const link = content.locator('a[href="https://arcade.makecode.com"]');
    await expect(link).toHaveAttribute('target', '_blank');
    await expect(link).toHaveAttribute('rel', /noopener/);
    await expect(content.locator('h2', { hasText: 'Plan B' })).toBeVisible();

    const img = content.locator('img[src="/arcade/ausweichen/bildschirm.svg"]');
    await img.scrollIntoViewIfNeeded();
    await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth)).toBeGreaterThan(0);
    const [imgBox, contentBox] = [await img.boundingBox(), await content.boundingBox()];
    expect(imgBox.x + imgBox.width).toBeLessThanOrEqual(contentBox.x + contentBox.width);

    await expect(page.locator('.guide-tasks .editor-hint')).toContainText('MakeCode Arcade');
    await expect(page.locator('.guide-tasks .editor-hint')).not.toContainText('micro:bit');
  });

  test('Blöcke haben die Arcade-Farben, alle drei Ansichten stehen zur Wahl', async ({ page }) => {
    await openCourse(page);
    await expect(page.locator('.guide-mode-btn')).toHaveCount(3);
    const sprite = page.locator('.guide-lesson .mc-block.mc-sprites').first();
    await expect(sprite).toHaveText('setze mySprite auf Sprite [Bild] vom Typ Player');
    await expect(sprite).toHaveCSS('background-color', 'rgb(75, 123, 236)');
    // „beim Start“ liegt in Arcade unter Schleifen, und die sind dort heller grün als beim micro:bit.
    await expect(page.locator('.guide-lesson .mc-block.mc-schleifen').first()).toHaveCSS('background-color', 'rgb(32, 191, 107)');

    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(page.locator('.guide-lesson pre code.language-python').first()).toContainText('sprites.create(img("""');
    await expect(page.locator('.guide-lesson .mc-blocks').first()).toBeHidden();
    await page.locator('.guide-mode-btn[data-mode="javascript"]').click();
    await expect(page.locator('.guide-lesson pre code.language-javascript').first()).toContainText('SpriteKind.Player');
  });

  test('Stufe 4: Tempo-Variable in allen drei Ansichten, Python erklärt global', async ({ page }) => {
    const index = lessons.findIndex((lesson) => lesson.id === 'lektion-punkte');
    await openCourse(page, lessons.slice(0, index).map((lesson) => lesson.id));
    await page.locator('.lesson-item').nth(index).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toContainText('Stufe 4');
    await expect(content.locator('.mc-block.mc-variablen:visible', { hasText: 'ändere tempo um 5' })).toHaveCount(1);
    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(content.locator('pre code.language-python:visible', { hasText: 'global tempo' })).toHaveCount(1);
  });

  test('Werkstatt: Pläne sind in Worten, ohne Code', async ({ page }) => {
    const index = lessons.findIndex((lesson) => lesson.id === 'lektion-werkstatt');
    await openCourse(page, lessons.slice(0, index).map((lesson) => lesson.id));
    await page.locator('.lesson-item').nth(index).click();
    const plans = page.locator('.guide-lesson .lesson-content details', { has: page.locator('summary', { hasText: 'Plan anzeigen' }) });
    await expect(plans).toHaveCount(3);
    for (let i = 0; i < 3; i++) {
      await plans.nth(i).locator('summary').click();
      await expect(plans.nth(i).locator('ol').first()).toBeVisible();
      await expect(plans.nth(i).locator('pre, .mc-block')).toHaveCount(0);
    }
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

  test('Projekte-Seite: Karte mit Sprache „MakeCode Arcade“', async ({ page }) => {
    await page.goto('/projekte');
    const card = page.locator('a.projekt-card[href="/kurs/projekt-arcade-ausweichen"]');
    await expect(card).toBeVisible({ timeout: 15000 });
    await expect(card).toContainText('MakeCode Arcade');
  });
});
