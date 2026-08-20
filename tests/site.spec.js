import { test, expect } from '@playwright/test';

const INTERACTIVE_URL = '/kurs/python-grundlagen-interaktiv';
const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const PLACEMENT_URL = '/kurs/python-einstufung';

test.describe('Home & Navigation', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Home zeigt CTAs und Kern-Kurse', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#hero')).toBeVisible();
    await expect(page.locator('.cta-button')).toHaveCount(3);
    await expect(page.locator('a.cta-button[href="/kurs/python-einstufung"]')).toBeVisible();
    await expect(page.locator('a.cta-button[href="/kurs/python-12-wochen-grundkurs"]')).toBeVisible();
    await expect(page.locator('a.cta-button[href="/kurs/python-grundlagen-interaktiv"]')).toBeVisible();

    // Home filtert Kurse: 12-Wochen + Interaktiv immer; andere nur mit Termin
    await expect(page.locator('#kurse-uebersicht .course-card')).toHaveCount(2);
    await expect(page.locator('a.course-link[href="/kurs/python-12-wochen-grundkurs"]')).toBeVisible();
    await expect(page.locator('a.course-link[href="/kurs/python-grundlagen-interaktiv"]')).toBeVisible();
  });

  test('Home-CTA Einstufung öffnet Placement-Kurs', async ({ page }) => {
    await page.goto('/');
    await page.locator('a.cta-button[href="/kurs/python-einstufung"]').click();
    await expect(page).toHaveURL(/python-einstufung/);
    await expect(page.locator('.course-detail > h1')).toHaveText(/Einstufung|Placement/);
    await expect(page.locator('.placement-intro, .placement-results, .quiz-question').first()).toBeVisible({
      timeout: 15000,
    });
  });

  test('Sprachumschaltung DE → EN', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#hero h2')).toContainText(/Willkommen|Übergangshacker/i);
    await page.locator('.lang-switcher button', { hasText: 'EN' }).click();
    await expect(page.locator('a.cta-button[href="/kurs/python-einstufung"]')).toContainText(/Placement/i);
    await expect(page.locator('#kurse-uebersicht h2')).toContainText(/Course/i);
    await expect(page.locator('#kurse-uebersicht .course-card').first()).toContainText(/Week|Interactive|Basics/i);
  });
});

test.describe('12-Wochen-Kurs UI', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Placement-Banner verlinkt zur Einstufung', async ({ page }) => {
    await page.goto(COURSE_URL);
    await expect(page.locator('.placement-banner')).toBeVisible({ timeout: 20000 });
    await page.locator('.placement-banner-link').click();
    await expect(page).toHaveURL(/python-einstufung/);
  });

  test('Kursstruktur erklärt Tabs inkl. Check', async ({ page }) => {
    await page.goto(COURSE_URL);
    await expect(page.locator('.course-structure')).toBeVisible({ timeout: 20000 });
    await expect(page.locator('.course-structure-tab')).toHaveCount(7);
    await expect(page.locator('.course-structure-tab', { hasText: 'Check' })).toBeVisible();
  });

  test('Missionen-Panel lässt sich aufklappen', async ({ page }) => {
    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-content')).toBeVisible({ timeout: 20000 });
    const panel = week.locator('.missionen-panel');
    await expect(panel).toBeVisible();
    await panel.locator('.missionen-panel-header').click();
    await expect(panel.locator('.missionen-panel-content')).toBeVisible();
    await expect(panel.locator('.mission-item').first()).toBeVisible();
  });
});

test.describe('Interaktiver Kurs', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-variant');
    });
  });

  test('Variantwahl Kinder → Lektion wird geladen', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(INTERACTIVE_URL);
    await expect(page.locator('.variant-card').first()).toBeVisible({ timeout: 15000 });
    await page.locator('.variant-card').first().click();
    await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 20000 });
    await expect(page.locator('.lesson-view, .lesson-content, .lesson-main').first()).toBeVisible();
    await expect(page.locator('.lesson-content, .code-editor, .editor-hint').first()).toBeVisible({
      timeout: 20000,
    });
  });

  test('Placement-Banner auch auf Interaktiv-Kurs', async ({ page }) => {
    await page.goto(INTERACTIVE_URL);
    await expect(page.locator('.placement-banner')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.placement-banner-link')).toHaveAttribute('href', '/kurs/python-einstufung');
  });
});

test.describe('Weitere Kursseiten', () => {
  test('Ferienkurs-Seite lädt ohne Fehler', async ({ page }) => {
    await page.goto('/kurs/ferienkurse');
    await expect(page.locator('.course-detail > h1, .course-loading')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.course-error')).toHaveCount(0);
  });
});
