import { test, expect } from '@playwright/test';
import { startKernel } from './helpers/kernel.js';

test.describe('Projekte-Übersicht', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-progress-morsecode');
    });
  });

  test('zeigt alle Projekt-Karten', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(5, { timeout: 15000 });
    await expect(page.locator('a[href="/kurs/projekt-caesar-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-morsecode"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-zahlendetektiv"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-js-spielewerkstatt"]')).toBeVisible();
  });

  test('Level-Filter "Fortgeschritten" reduziert auf Zahlen-Detektiv und Vigenère-Chiffre', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(5, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Fortgeschritten' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(2);
    await expect(page.locator('a[href="/kurs/projekt-zahlendetektiv"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
  });

  test('Tag-Filter "Kryptografie" zeigt Cäsar- und Vigenère-Chiffre', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(5, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Kryptografie' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(2);
    await expect(page.locator('a[href="/kurs/projekt-caesar-chiffre"]')).toBeVisible();
    await expect(page.locator('a[href="/kurs/projekt-vigenere-chiffre"]')).toBeVisible();
  });

  test('Sprach-Filter "JavaScript" zeigt nur die Spielewerkstatt', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(5, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'JavaScript' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(1);
    await expect(page.locator('a[href="/kurs/projekt-js-spielewerkstatt"]')).toBeVisible();
  });

  test('Zurücksetzen-Button stellt alle Projekte wieder her', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card')).toHaveCount(5, { timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Fortgeschritten' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(2);

    await page.locator('.filter-reset').click();
    await expect(page.locator('.projekt-card')).toHaveCount(5);
  });

  test('Morsecode-Projekt lädt und Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-morsecode');
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });
    await expect(page.locator('.course-description')).toContainText('Morsecode');

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
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });
    await expect(page.locator('.course-description')).toContainText('Vigenère');

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
});
