import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { expectGuideContent } from './helpers/guide-content.js';

const CONTENT_DIR = path.join('content', 'microbit-einfuehrung');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const kurse = JSON.parse(fs.readFileSync(path.join('public', 'kurse.json'), 'utf8'));
const INTRO_ID = 'projekt-microbit-einfuehrung';
const STORAGE_KEY = 'ue-hacker-interactive-progress-microbit-einfuehrung';
const MICROBIT_KURSE = kurse.filter((k) => k.language === 'microbit' && k.id !== INTRO_ID).map((k) => k.id);

test.describe('micro:bit: Einführung vor jedem micro:bit-Kurs', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      if (sessionStorage.getItem('microbit-test-init')) return;
      sessionStorage.setItem('microbit-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
  });

  test('Inhalt: Anleitungs-Regeln, jedes Bild im Ordner wird gezeigt, am Ende Links zu allen micro:bit-Kursen', () => {
    expectGuideContent(CONTENT_DIR);
    const all = lessons.map((l) => fs.readFileSync(path.join(CONTENT_DIR, l.file), 'utf8')).join('\n');
    for (const file of fs.readdirSync(path.join('public', 'microbit', 'einfuehrung'))) {
      expect(all, file).toContain(`/microbit/einfuehrung/${file}`);
    }
    const last = fs.readFileSync(path.join(CONTENT_DIR, lessons.at(-1).file), 'utf8');
    expect(MICROBIT_KURSE.length).toBeGreaterThanOrEqual(3);
    for (const id of MICROBIT_KURSE) expect(last, id).toContain(`(/kurs/${id})`);
  });

  for (const id of ['projekt-microbit-sterne', 'projekt-microbit-ampel', 'projekt-microbit-auto']) {
    test(`${id}: Startseite verweist Neue auf die Einführung, „Kurs starten“ überspringt sie`, async ({ page }) => {
      await page.goto(`/kurs/${id}`);
      const banner = page.locator('.microbit-intro-banner');
      await expect(banner).toContainText('Neu beim micro:bit?', { timeout: 15000 });
      await expect(banner.locator('a')).toHaveAttribute('href', `/kurs/${INTRO_ID}`);
      await expect(page.locator('.btn-start-course')).toBeVisible();
    });
  }

  test('Link führt in die Einführung; sie hat selbst keinen Verweis und fehlt in der Projekte-Übersicht', async ({ page }) => {
    await page.goto('/kurs/projekt-microbit-sterne');
    await page.locator('.microbit-intro-banner a').click();
    await expect(page).toHaveURL(new RegExp(`/kurs/${INTRO_ID}$`));
    await expect(page.locator('.course-description')).toContainText('noch nie mit dem micro:bit');
    await expect(page.locator('.microbit-intro-banner')).toHaveCount(0);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.guide-lesson img[src="/microbit/einfuehrung/vorderseite.svg"]')).toBeVisible();

    await page.goto('/projekte');
    await expect(page.locator('.projekt-card').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator(`a[href="/kurs/${INTRO_ID}"]`)).toHaveCount(0);
  });

  test('Andere Kurse zeigen keinen micro:bit-Hinweis', async ({ page }) => {
    await page.goto('/kurs/projekt-caesar-chiffre');
    await expect(page.locator('.course-description')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.microbit-intro-banner')).toHaveCount(0);
  });

  test('Nach der abgeschlossenen Einführung steht im Kasten nur noch ein Haken', async ({ page }) => {
    await page.addInitScript(([key, ids]) => localStorage.setItem(
      key, JSON.stringify({ variant: 'microbit-einfuehrung', completedLessonIds: ids }),
    ), [STORAGE_KEY, lessons.map((l) => l.id)]);
    await page.goto('/kurs/projekt-microbit-ampel');
    const banner = page.locator('.microbit-intro-banner');
    await expect(banner).toContainText('Einführung geschafft', { timeout: 15000 });
    await expect(banner.locator('a')).toHaveCount(0);
  });
});
