import { test, expect } from '@playwright/test';

// Begriffe in Projekt-Kursen verlinken auf die Grundkurs-Woche, in der sie erklärt werden
// (useConcepts.js, content/begriffe.json): im Lektionstext beim ersten Vorkommen als Link, am Ende
// der Lektion als Kasten "Neu oder unklar? Hier lernst du mehr darüber".
const openProject = async (page, courseId) => {
  await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
  await page.goto(`/kurs/${courseId}`);
  await page.locator('.btn-start-course').click();
  await expect(page.locator('.lesson-content h1').first()).toBeVisible({ timeout: 15000 });
};

test.describe('Begriffe in Projekten verlinken auf die Grundkurse', () => {
  test('JS-Projekt: "Array" verlinkt auf JS-Grundkurs Woche 5, Kasten am Lektionsende', async ({ page }) => {
    await openProject(page, 'projekt-js-quiz');
    const content = page.locator('.lesson-content');

    const arrayLinks = content.locator('a.concept-link[href="/kurs/js-grundkurs?week=5"]');
    // Nur das erste Vorkommen ist ein Link, auch wenn "Array" öfter im Text steht.
    await expect(arrayLinks).toHaveCount(1);
    await expect(arrayLinks).toHaveText(/^Arrays?$/);
    await expect(arrayLinks).toHaveAttribute('target', '_blank');
    await expect(arrayLinks).toHaveAttribute('title', /Woche 5/);
    // Nie in Code-Blöcken oder Überschriften.
    await expect(content.locator('pre a.concept-link, code a.concept-link, h1 a.concept-link')).toHaveCount(0);

    const box = content.locator('.concept-box');
    await expect(box).toContainText('Neu oder unklar?');
    // Jeder Begriff nur einmal im Kasten, auch wenn er in Text und Aufgaben vorkommt.
    const items = box.locator('.concept-box-item');
    const names = await items.locator('strong').allTextContents();
    expect(names.length).toBeGreaterThan(1);
    expect(new Set(names).size).toBe(names.length);
    const item = box.locator('.concept-box-item', { hasText: 'Array' }).first();
    await expect(item.locator('a.concept-box-link')).toHaveAttribute('href', '/kurs/js-grundkurs?week=5');
    await expect(item).toContainText('JavaScript-Grundkurs, Woche 5');
  });

  test('Python-Projekt: "Dictionary" verlinkt auf den Python-Grundkurs Woche 8', async ({ page }) => {
    await openProject(page, 'projekt-morsecode');
    const content = page.locator('.lesson-content');
    await expect(content.locator('a.concept-link[href="/kurs/python-12-wochen-grundkurs?week=8"]')).toHaveCount(1);
    await expect(content.locator('.concept-box')).toContainText('Python-Grundkurs (12 Wochen), Woche 8');
  });

  test('der Link landet in der richtigen Grundkurs-Woche', async ({ page }) => {
    await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
    await page.goto('/kurs/js-grundkurs?week=5');
    await expect(page.getByText('Arrays: mehrere Werte in einer Variable').first()).toBeVisible({ timeout: 15000 });
  });

  test('Grundkurse selbst bekommen keine Begriffs-Links', async ({ page }) => {
    await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
    await page.goto('/kurs/js-grundkurs?week=5');
    await expect(page.locator('.lesson-content h1').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.lesson-content')).toContainText('Array');
    await expect(page.locator('a.concept-link')).toHaveCount(0);
    await expect(page.locator('.concept-box')).toHaveCount(0);
  });
});
