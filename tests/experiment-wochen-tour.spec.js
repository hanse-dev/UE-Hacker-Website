import { test, expect } from '@playwright/test';

const TOUR_URL = '/experiment/wochen-tour';

test.describe('Experiment: Wochen-Tour', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Kachel-Flow: Woche wählen -> Thema wählen -> Tour startet auf Lektion', async ({ page }) => {
    await page.goto(TOUR_URL);
    await expect(page.locator('.week-tile')).toHaveCount(12);

    await page.locator('.week-tile[data-week="1"]').click();
    await expect(page.locator('.week-tile')).toHaveCount(0); // Wochen-Seite verlassen
    await expect(page.locator('.variant-tile')).toHaveCount(3);

    await page.locator('.variant-tile').first().click();
    await expect(page.locator('.variant-tile')).toHaveCount(0); // Themen-Seite verlassen
    await expect(page.locator('.stepper-step.current')).toContainText('Lektion');
    await expect(page.locator('.tour-content .cell-markdown').first()).toBeVisible();
  });

  test('Breadcrumb springt zurück zur Wochen- bzw. Themen-Seite', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=2&variant=abenteuer`);
    await expect(page.locator('.tour-breadcrumb')).toBeVisible();

    await page.locator('.tour-breadcrumb .breadcrumb-link').nth(1).click(); // Thema wechseln
    await expect(page.locator('.variant-tile')).toHaveCount(3);

    await page.locator('.breadcrumb-back').click(); // zurück zur Wochen-Seite
    await expect(page.locator('.week-tile')).toHaveCount(12);
  });

  test('"Weiter"-Button schaltet Lektion -> Debug -> Missionen -> Boss-Quest -> Check der Reihe nach weiter', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=abenteuer`);
    await expect(page.locator('.stepper-step.current')).toContainText('Lektion');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Debug');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Missionen');
    // Kein Missionen-Punkte-Widget in der Tour
    await expect(page.locator('.missionen-panel')).toHaveCount(0);

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Boss-Quest');

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Check');
    await expect(page.locator('.week-check-panel')).toBeVisible();

    // Letzter Schritt: kein "Weiter"-Button mehr, stattdessen Abschluss-Hinweis
    await expect(page.locator('.tour-next-btn')).toHaveCount(0);
    await expect(page.locator('.tour-done-msg')).toBeVisible();
  });

  test('Seitenmenü lässt sich ein- und ausklappen', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=abenteuer`);
    await expect(page.locator('.tour-side-menu')).toBeVisible();

    await page.locator('.side-menu-toggle').click();
    await expect(page.locator('.tour-side-menu')).toHaveCount(0);

    await page.locator('.side-menu-toggle').click();
    await expect(page.locator('.tour-side-menu')).toBeVisible();
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
    await expect(page.locator('.stepper-step.current')).toContainText('Debug');

    await page.locator('[data-reference-key="0_glossar"]').click();
    await expect(page.locator('.tour-reference-banner')).toBeVisible();
    await expect(page.locator('.stepper-step.current')).toHaveCount(0);

    await page.locator('.tour-back-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Debug');
  });
});
