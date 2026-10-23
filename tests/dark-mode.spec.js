import { test, expect } from '@playwright/test';

// Dark Mode: data-theme auf <html> (useTheme.js + Inline-Skript in index.html), Farben über
// CSS-Tokens in src/style.css. Werte hier = --bg-page / --surface aus style.css.
const LIGHT_BG = 'rgb(244, 246, 248)';
const DARK_BG = 'rgb(21, 18, 27)';
const DARK_TINT = 'rgb(44, 34, 56)'; // --surface-tint, Hintergrund der Code-Bereiche

const bodyBg = (page) => page.evaluate(() => getComputedStyle(document.body).backgroundColor);

test.describe('Dark Mode', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      if (!sessionStorage.getItem('theme-test-init')) {
        localStorage.removeItem('ue-hacker-theme');
        sessionStorage.setItem('theme-test-init', '1');
      }
    });
  });

  test('folgt ohne Auswahl der Systemeinstellung', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.goto('/');
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
    expect(await bodyBg(page)).toBe(DARK_BG);

    await page.emulateMedia({ colorScheme: 'light' });
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
    expect(await bodyBg(page)).toBe(LIGHT_BG);
  });

  test('Auswahl in den Optionen gilt sofort und bleibt nach dem Neuladen', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'light' });
    await page.goto('/');
    await page.getByRole('button', { name: 'Optionen' }).click();
    const dialog = page.getByRole('dialog');
    await expect(dialog.locator('[data-theme-option="system"]')).toHaveAttribute('aria-pressed', 'true');

    await dialog.getByRole('button', { name: 'Dunkel' }).click();
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
    expect(await bodyBg(page)).toBe(DARK_BG);

    await page.reload();
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
    expect(await bodyBg(page)).toBe(DARK_BG);

    await page.getByRole('button', { name: 'Optionen' }).click();
    await expect(page.getByRole('dialog').locator('[data-theme-option="dark"]')).toHaveAttribute('aria-pressed', 'true');
    await page.getByRole('dialog').getByRole('button', { name: 'System' }).click();
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  });

  test('„Hell“ bleibt hell, auch wenn das System dunkel ist', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.goto('/');
    await page.getByRole('button', { name: 'Optionen' }).click();
    await page.getByRole('dialog').getByRole('button', { name: 'Hell' }).click();
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
    expect(await bodyBg(page)).toBe(LIGHT_BG);
  });

  test('Inline-Skript setzt das Theme schon vor der App (kein helles Aufblitzen)', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'light' });
    await page.addInitScript(() => localStorage.setItem('ue-hacker-theme', 'dark'));
    // App-Code blockieren: dann kann nur das Inline-Skript in index.html data-theme gesetzt haben.
    await page.route('**/src/main.js', (route) => route.abort());
    await page.goto('/');
    await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  });

  test('Lektion: Textflächen und Code-Editor werden dunkel', async ({ page }) => {
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.goto('/kurs/js-grundkurs?week=1');
    const editor = page.locator('.cm-editor').first();
    await expect(editor).toBeVisible({ timeout: 20000 });
    await expect(page.locator('.cm-host').first()).toHaveCSS('background-color', DARK_TINT);
    // Normaler Text im Editor ist hell (--text), nicht das Schwarz des CodeMirror-Standards.
    await expect(editor).toHaveCSS('color', 'rgb(230, 225, 236)');
    await expect(page.locator('.lesson-content').first()).not.toHaveCSS('background-color', 'rgb(255, 255, 255)');
  });
});
