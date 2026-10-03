import { test, expect } from '@playwright/test';
import { devSkipPorts } from '../playwright.devskip.config.js';

// Eigene Config (playwright.devskip.config.js): beide Server laufen mit VITE_DEV_SKIP_CHECKS=1.
// Der Modus wirkt zentral (src/composables/devSkipChecks.js) - getestet wird je eine Stelle pro
// Pruef-Art: Python-Lektion, JS-Lektion, Lektions-Freischaltung, Wochen-Check (Quiz + Coding).
const BUILD = `http://localhost:${devSkipPorts.build}`;

test.describe('Dev-Modus "Prüfungen überspringen" (npm run dev:skip-checks)', () => {
  test('Hinweis-Banner auf jeder Seite', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('.dev-skip-banner')).toBeVisible();
    await page.goto('/projekte');
    await expect(page.locator('.dev-skip-banner')).toBeVisible();
  });

  test('Python-Lektion: "Prüfen" besteht mit unverändertem Code, ohne auf den Kernel zu warten', async ({ page }) => {
    await page.goto('/kurs/python-12-wochen-grundkurs?week=1&variant=abenteuer');
    const task = page.locator('.task-block', { has: page.locator('.btn-check') }).first();
    await expect(task.locator('.btn-check')).toBeEnabled({ timeout: 15000 });
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('JS-Lektion: "Prüfen" besteht mit unverändertem (leerem) Spielfeld', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await page.locator('.btn-start-course').click();
    const task = page.locator('.task-block').nth(2);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Alle Lektionen sind ohne Vorarbeit freigeschaltet', async ({ page }) => {
    await page.goto('/kurs/projekt-morsecode');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });
    await expect(page.locator('.lessons-list .lesson-item.locked')).toHaveCount(0);
    await page.locator('.lessons-list .lesson-item').last().click();
    await expect(page.locator('.lesson-item.active')).toContainText('Der komplette Übersetzer');
  });

  test('Wochen-Check: beliebige Quiz-Antworten und unveränderter Coding-Code bestehen', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/ki-labor?week=1');
    await page.locator('[data-open-check]').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

    const cards = page.locator('.quiz-question');
    await expect(cards.first()).toBeVisible({ timeout: 20000 });
    const count = await cards.count();
    for (let i = 0; i < count; i++) {
      await cards.nth(i).locator('.option-btn').first().click();
    }
    await page.locator('.btn-check-quiz').click();
    await expect(page.locator('.quiz-result.quiz-pass')).toBeVisible();

    const challenges = page.locator('.code-challenge');
    const challengeCount = await challenges.count();
    expect(challengeCount).toBeGreaterThan(0);
    for (let i = 0; i < challengeCount; i++) {
      const challenge = challenges.nth(i);
      await challenge.locator('.btn-check').click();
      await expect(challenge.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
    }
    await expect(page.locator('.certificate-reveal')).toBeVisible();
  });

  test('Produktions-Build: der Modus wirkt trotz gesetzter Variable nicht', async ({ page }) => {
    await page.goto(`${BUILD}/kurs/projekt-js-spielewerkstatt`);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.dev-skip-banner')).toHaveCount(0);
    await expect(page.locator('.lessons-list .lesson-item.locked').first()).toBeVisible({ timeout: 15000 });

    const task = page.locator('.task-block').nth(2);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
  });
});
