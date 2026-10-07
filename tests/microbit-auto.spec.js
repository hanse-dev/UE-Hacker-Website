import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const CONTENT_DIR = path.join('content', 'microbit-auto');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));

test.describe('micro:bit-Kurs: Roboterauto (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      // Nur beim ersten Laden leeren, damit der Reload-Test den gespeicherten Stand sieht.
      if (sessionStorage.getItem('microbit-test-init')) return;
      sessionStorage.setItem('microbit-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem('ue-hacker-interactive-progress-microbit-auto');
    });
  });

  async function openCourse(page) {
    await page.goto('/kurs/projekt-microbit-auto');
    await expect(page.locator('.course-description')).toContainText('Roboterauto');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, und jeder Abschnitt gibt es für Blöcke und Python', () => {
    for (const lesson of lessons) {
      expect(lesson.tasks.some((task) => !task.isBonus), lesson.id).toBe(true);
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      const opened = md.match(/^:::(bloecke|python)$/gm) || [];
      const closed = md.match(/^:::$/gm) || [];
      expect(closed.length, `${lesson.file}: Abschnitte geschlossen`).toBe(opened.length);
      expect(opened.filter((m) => m === ':::bloecke').length, `${lesson.file}: Blöcke und Python gleich oft`)
        .toBe(opened.filter((m) => m === ':::python').length);
      // Ein Block-Listing ausserhalb eines :::bloecke-Abschnitts waere auch in der Python-Ansicht sichtbar.
      const outside = md.replace(/^:::(bloecke|python)$[\s\S]*?^:::$/gm, '');
      expect(outside, `${lesson.file}: Code nur innerhalb der Abschnitte`).not.toMatch(/```(bloecke|python)/);
    }
  });

  test('Umschalter zeigt Blöcke oder Python und merkt sich die Wahl', async ({ page }) => {
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');

    await expect(content.locator('.mc-blocks').first()).toBeVisible();
    await expect(content.locator('.mc-block.mc-grundlagen').first()).toHaveText('beim Start');
    await expect(content.locator('pre code.language-python').first()).toBeHidden();
    await expect(content).not.toContainText(':::');

    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(content.locator('pre code.language-python').first()).toBeVisible();
    await expect(content.locator('pre code.language-python').first()).toContainText('display.show(Image.HEART)');
    await expect(content.locator('.mc-blocks').first()).toBeHidden();

    // Nach dem Neuladen bleibt der Kurs geoeffnet (?started=1).
    await page.reload();
    await expect(page.locator('.guide-mode-btn[data-mode="python"]')).toHaveClass(/active/);
    await expect(page.locator('.guide-lesson .lesson-content pre code.language-python').first()).toBeVisible();
  });

  test('Pflichtaufgaben abhaken schließt die Stufe ab und schaltet die nächste frei, Bonus ist freiwillig', async ({ page }) => {
    await openCourse(page);
    // Kein Python-Kernel und kein Code-Editor: die Aufgaben werden am echten Auto ausprobiert.
    await expect(page.locator('.btn-kernel')).toHaveCount(0);
    // Offline-ZIPs gibt es nur fuer Pyodide-Projekte - hier waeren es tote Links.
    await expect(page.locator('.offline-downloads')).toHaveCount(0);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);

    const required = lessons[0].tasks.filter((task) => !task.isBonus).length;
    const tasks = page.locator('.guide-task');
    await expect(tasks).toHaveCount(lessons[0].tasks.length);
    await expect(tasks.locator('.task-bonus-badge')).toHaveCount(lessons[0].tasks.length - required);

    for (let i = 0; i < required - 1; i++) await tasks.nth(i).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toHaveCount(0);
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);

    await tasks.nth(required - 1).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);

    await page.locator('.btn-next').click();
    await expect(page.locator('.guide-lesson .lesson-content h1')).toContainText('Stufe 1');
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(0);

    // Abgeschlossene Stufe bleibt nach dem Neuladen abgehakt.
    await page.reload();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1, { timeout: 15000 });
    await page.locator('.lesson-item').first().click();
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(required);
  });

  test('Projekte-Übersicht zeigt den Kurs mit micro:bit-Label und Robotik-Tag', async ({ page }) => {
    await page.goto('/projekte');
    const card = page.locator('a.projekt-card[href="/kurs/projekt-microbit-auto"]');
    await expect(card).toBeVisible({ timeout: 15000 });
    await expect(card.locator('.badge-language')).toHaveText('micro:bit');
    await expect(card.locator('.tag-chip')).toHaveText('Robotik');
  });

  test('Bibliothek für Python wird zum Download ausgeliefert', async ({ page }) => {
    const res = await page.request.get('/microbit/keyes_MiniCar.py');
    expect(res.status()).toBe(200);
    expect(await res.text()).toContain('class MiniCar');
  });
});
