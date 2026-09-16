import { test, expect } from '@playwright/test';

const TOUR_URL = '/experiment/wochen-tour';

test.describe('Experiment: Wochen-Tour', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('zeigt alle 12 Wochen, Variantenwahl öffnet die Tour auf Lektion', async ({ page }) => {
    await page.goto(TOUR_URL);
    await expect(page.locator('.week-chip')).toHaveCount(12);

    await page.locator('.week-chip[data-week="1"]').click();
    const variantBtn = page.locator('.variant-selector .variant-btn').first();
    await expect(variantBtn).toBeVisible();
    await expect(page.locator('.variant-selector .variant-btn')).toHaveCount(3);

    await variantBtn.click();
    await expect(page.locator('.tour-tab.active')).toContainText('Lektion');
    await expect(page.locator('.tour-content .cell-markdown').first()).toBeVisible();
  });

  test('"Weiter"-Button schaltet Lektion -> Debug -> Missionen -> Boss-Quest -> Check der Reihe nach weiter', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=abenteuer`);
    await expect(page.locator('.tour-tab.active')).toContainText('Lektion');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.tour-tab.active')).toContainText('Debug');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.tour-tab.active')).toContainText('Missionen');
    // Kein Missionen-Punkte-Widget in der Tour
    await expect(page.locator('.missionen-panel')).toHaveCount(0);

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.tour-tab.active')).toContainText('Boss-Quest');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.tour-tab.active')).toContainText('Check');
    await expect(page.locator('.week-check-panel')).toBeVisible();

    // Letzter Schritt: kein "Weiter"-Button mehr, stattdessen Abschluss-Hinweis
    await expect(page.locator('.tour-next-btn')).toHaveCount(0);
    await expect(page.locator('.tour-done-msg')).toBeVisible();
  });

  test('Seitenmenü: Sprung zu einem Unterabschnitt scrollt zur passenden Zelle', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=abenteuer`);
    const heading = page.locator('.side-menu-heading').first();
    await expect(heading).toBeVisible();
    const headingText = await heading.textContent();
    await heading.click();

    // Die Zelle mit derselben Überschrift muss danach im Viewport sichtbar sein
    const targetCell = page.locator('.cell-markdown', { hasText: headingText.trim() }).first();
    await expect(targetCell).toBeInViewport();
  });

  test('Seitenmenü: Glossar öffnen und zurück zur Tour behält den Fortschritt', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=abenteuer`);
    await page.locator('.tour-next-btn').click(); // -> Debug
    await expect(page.locator('.tour-tab.active')).toContainText('Debug');

    await page.locator('[data-reference-key="0_glossar"]').click();
    await expect(page.locator('.tour-reference-banner')).toBeVisible();
    await expect(page.locator('.tour-tab.active')).toHaveCount(0);

    await page.locator('.tour-back-btn').click();
    await expect(page.locator('.tour-tab.active')).toContainText('Debug');
  });
});
