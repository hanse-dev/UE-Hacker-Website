import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const VARIANT_KEYS = ['abenteuer', 'pferde', 'scifi'];

test('Kursseite: 12 Wochen, 3 Varianten, 5 Tour-Schritte + Nachschlagewerke', async ({ page }) => {
  await page.goto(COURSE_URL);
  await expect(page.locator('.week-tile')).toHaveCount(12);

  // Woche 1 ist im Lektions-Format (python-woche1-lektionen.spec.js) - Notebook-Schritte: Woche 12
  await page.locator('.week-tile[data-week="12"]').click();
  await expect(page.locator('.variant-tile')).toHaveCount(3);

  await page.locator('.variant-tile').nth(1).click();
  // Alle 5 Tour-Schritte (Lektion/Debug/Missionen/Extra-Herausforderung/Check) + Nachschlagewerke
  await expect(page.locator('.stepper-step')).toHaveCount(5);
  expect(await page.locator('.side-menu-reference').count()).toBeGreaterThanOrEqual(2);
});

test('Woche 1: Notebook lädt, Schritt- und Varianten-Wechsel', async ({ page }) => {
  await page.goto(`${COURSE_URL}?week=12&variant=scifi&step=1_lektion`);
  await page.locator('.cell').first().waitFor({ state: 'visible', timeout: 15000 });
  await expect(page.locator('.error')).not.toBeVisible();

  await page.locator('.stepper-step[data-step-key="2_debug"]').click();
  await page.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
  await expect(page.locator('.error')).not.toBeVisible();

  // Thema wechseln über den Breadcrumb (statt Varianten-Buttons wie in der alten UI)
  await page.locator('.tour-breadcrumb .breadcrumb-link').nth(1).click();
  await expect(page.locator('.variant-tile')).toHaveCount(3);
  await page.locator('.variant-tile', { hasText: 'Pferde' }).click();
  await page.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
  await expect(page.locator('.error')).not.toBeVisible();
});

// Smoke-Test: jede Woche/Variante-Kombination lädt fehlerfrei - über alle Tour-Schritte, beide
// Zweige der Missionen-Verzweigung und jedes Nachschlagewerk (Glossar/Lösungen/Cheat-Sheets).
async function sweepWeekVariant(page, weekNumber, variantKey) {
  await page.goto(`${COURSE_URL}?week=${weekNumber}&variant=${variantKey}&step=1_lektion`);
  await page.locator('.cell').first().waitFor({ state: 'visible', timeout: 15000 });
  await expect(page.locator('.error')).toHaveCount(0);

  const stepKeys = await page.locator('.stepper-step').evaluateAll((els) => els.map((el) => el.dataset.stepKey));
  for (const key of stepKeys) {
    await page.locator(`.stepper-step[data-step-key="${key}"]`).click();
    await page.waitForTimeout(150);
    await expect(page.locator('.error')).toHaveCount(0);
  }

  // Verzweigung nach den Missionen: Extra-Herausforderung-Zweig separat anklicken.
  if (stepKeys.includes('3_missionen') && stepKeys.includes('5_boss') && stepKeys.includes('4_check')) {
    await page.locator('.stepper-step[data-step-key="3_missionen"]').click();
    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await page.locator('[data-branch="5_boss"]').click();
    await page.waitForTimeout(150);
    await expect(page.locator('.error')).toHaveCount(0);
  }

  const refKeys = await page.locator('.side-menu-reference').evaluateAll((els) => els.map((el) => el.dataset.referenceKey));
  for (const key of refKeys) {
    await page.locator(`[data-reference-key="${key}"]`).click();
    await page.waitForTimeout(150);
    await expect(page.locator('.error')).toHaveCount(0);
    await page.locator('.tour-back-btn').click();
  }
}

// Wochen im Lektions-Format (content/python-woche{N}-*/) haben keine Notebook-Schritte mehr und
// werden in python-lektionen-format.spec.js geprüft.
const lessonWeeks = new Set(
  fs.readdirSync(path.join(process.cwd(), 'content'))
    .map((d) => d.match(/^python-woche(\d+)-/)?.[1]).filter(Boolean).map(Number)
);
for (const weekNumber of [4, 6, 12].filter((w) => !lessonWeeks.has(w))) {
  for (const variantKey of VARIANT_KEYS) {
    test(`Woche ${weekNumber}/${variantKey}: alle Schritte, Verzweigung und Nachschlagewerke fehlerfrei`, async ({ page }) => {
      test.setTimeout(60000);
      await sweepWeekVariant(page, weekNumber, variantKey);
    });
  }
}
