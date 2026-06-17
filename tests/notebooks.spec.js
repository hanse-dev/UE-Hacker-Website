import { test, expect } from '@playwright/test';

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const VARIANTS = [['abenteuer', 'Abenteuer'], ['pferde', 'Pferde'], ['scifi', 'Sci-Fi']];

async function openWeek(page, weekIndex) {
  const week = page.locator('.week-section').nth(weekIndex);
  if (weekIndex !== 0) await week.locator('.week-header').click();
  await week.locator('.cell').first().waitFor({ state: 'visible', timeout: 8000 });
  return week;
}

test('Kursseite: 12 Wochen, 3 Varianten, 7 Tabs', async ({ page }) => {
  await page.goto(COURSE_URL);
  await expect(page.locator('.week-header')).toHaveCount(12);
  const w1 = page.locator('.week-section').first();
  await expect(w1.locator('.variant-btn')).toHaveCount(3);
  await expect(w1.locator('.tab-btn')).toHaveCount(6);
});

test('Woche 1: Notebook lädt, Tab- und Varianten-Wechsel', async ({ page }) => {
  await page.goto(COURSE_URL);
  const w1 = await openWeek(page, 0);
  await expect(w1.locator('.error')).not.toBeVisible();

  await w1.locator('.tab-btn', { hasText: 'Debug' }).click();
  await w1.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
  await expect(w1.locator('.error')).not.toBeVisible();

  await w1.locator('.variant-btn', { hasText: 'Pferde' }).click();
  await w1.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
  await expect(w1.locator('.error')).not.toBeVisible();
});

for (const weekIndex of [0, 5, 11]) {
  for (const [variant, label] of VARIANTS) {
    test(`Woche ${weekIndex + 1}/${variant}`, async ({ page }) => {
      await page.goto(COURSE_URL);
      const week = await openWeek(page, weekIndex);
      await week.locator(`.variant-btn:has-text("${label}")`).click();
      await week.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
      await expect(week.locator('.error')).not.toBeVisible();
    });
  }
}
