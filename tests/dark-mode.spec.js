import { test, expect } from '@playwright/test';

// Dark Mode: data-theme auf <html> (useTheme.js + Inline-Skript in index.html), Farben über
// CSS-Tokens in src/style.css. Werte hier = --bg-page / --surface aus style.css.
const LIGHT_BG = 'rgb(244, 246, 248)';
const DARK_BG = 'rgb(21, 18, 27)';
const DARK_SURFACE = 'rgb(31, 26, 39)';
const DARK_TINT = 'rgb(44, 34, 56)'; // --surface-tint, Hintergrund der Code-Bereiche

// WCAG-Kontrast zwischen einer Farbe des Elements und dem ersten nicht transparenten Hintergrund
// (das Element selbst oder ein Vorfahre).
const contrast = (locator, prop, against = 'parent') => locator.evaluate((el, [prop, against]) => {
  const rgb = (c) => c.match(/[\d.]+/g).map(Number);
  const lum = ([r, g, b]) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  let bgEl = against === 'self' ? el : el.parentElement;
  while (bgEl && rgb(getComputedStyle(bgEl).backgroundColor)[3] === 0) bgEl = bgEl.parentElement;
  const [a, b] = [lum(rgb(getComputedStyle(el)[prop])), lum(rgb(getComputedStyle(bgEl).backgroundColor))];
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}, [prop, against]);

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

  test('Inhaltsbereiche haben in beiden Modi ihre Fläche (--surface)', async ({ page }) => {
    // Regression: Ein kaputter Variablenname (var(--var(--surface))) ließ .app-main section
    // durchsichtig werden - auch im hellen Modus.
    const section = page.locator('.app-main section:not(#hero)').first();
    await page.emulateMedia({ colorScheme: 'light' });
    await page.goto('/');
    await expect(section).toHaveCSS('background-color', 'rgb(255, 255, 255)');
    await page.emulateMedia({ colorScheme: 'dark' });
    await expect(section).toHaveCSS('background-color', DARK_SURFACE);

    await page.goto('/kurs/projekt-caesar-chiffre?started=1');
    await expect(page.locator('.course-layout').first()).toHaveCSS('background-color', DARK_SURFACE, { timeout: 15000 });
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

  test('Lektion: Aufgaben und Beispiele sind deutlich markiert', async ({ page }) => {
    // Regression: Beispiel-Streifen (--border-strong) und Badge-Schrift (--text-faint) waren auf
    // dunklem Grund kaum zu sehen (Kontrast ~1,9 bzw. ~4).
    await page.emulateMedia({ colorScheme: 'dark' });
    await page.goto('/kurs/js-grundkurs?week=1');
    const example = page.locator('.task-block.task-example').first();
    const required = page.locator('.task-block.task-required').first();
    await expect(example).toBeVisible({ timeout: 20000 });
    expect(await contrast(example, 'borderLeftColor')).toBeGreaterThanOrEqual(3);
    expect(await contrast(required, 'borderLeftColor')).toBeGreaterThanOrEqual(3);
    expect(await contrast(example.locator('.badge-example'), 'color', 'self')).toBeGreaterThanOrEqual(7);
    expect(await contrast(required.locator('.badge-required'), 'color', 'self')).toBeGreaterThanOrEqual(7);

    // Python-Lektionsansicht (LessonView.vue) nutzt dieselben Tokens.
    await page.goto('/kurs/python-grundlagen-interaktiv');
    await page.locator('.btn-start-course').click();
    await page.locator('.variant-card').first().click();
    const pyExample = page.locator('.task-block.task-example').first();
    await expect(pyExample).toBeVisible({ timeout: 20000 });
    expect(await contrast(pyExample, 'borderLeftColor')).toBeGreaterThanOrEqual(3);
    expect(await contrast(pyExample.locator('.task-badge'), 'color', 'self')).toBeGreaterThanOrEqual(7);
  });
});
