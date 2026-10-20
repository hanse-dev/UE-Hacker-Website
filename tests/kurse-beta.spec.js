import { test, expect } from '@playwright/test';
import fs from 'node:fs';

const kurse = JSON.parse(fs.readFileSync('public/kurse.json', 'utf8'));
// Noch nicht im Unterricht durchgegangen (Entscheidung Eike, 15.10.2026): alle Projekte außer dem
// Roboterauto, dazu JS-Grundkurs, KI-Labor und Ferienkurse. Die Ampelanlage hat Eike am 20.10.2026
// gelesen und als geprüft markiert (bleibt aber bis zum Test mit echten Teilen nicht verlinkt).
const NICHT_BETA = ['python-einstufung', 'python-grundlagen-interaktiv', 'python-12-wochen-grundkurs', 'projekt-microbit-auto', 'projekt-microbit-ampel'];

test.describe('Beta-Kennzeichnung', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
  });

  test('kurse.json: genau die noch nicht erprobten Kurse sind Beta', () => {
    for (const kurs of kurse) {
      expect(!!kurs.beta, kurs.id).toBe(!NICHT_BETA.includes(kurs.id));
    }
  });

  test('Projekte-Übersicht zeigt Beta an der Karte', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-caesar-chiffre"] .beta-badge')).toHaveText('Beta: neu, noch nicht vollständig getestet', { timeout: 15000 });
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-microbit-auto"]')).toBeVisible();
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-microbit-auto"] .beta-badge')).toHaveCount(0);
  });

  test('Startseite zeigt Beta an den Kurskarten', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('a.course-card[href="/kurs/js-grundkurs"] .beta-badge')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('a.course-card[href="/kurs/python-12-wochen-grundkurs"]')).toBeVisible();
    await expect(page.locator('a.course-card[href="/kurs/python-12-wochen-grundkurs"] .beta-badge')).toHaveCount(0);
  });

  test('Kursseite zeigt Beta mit Erklärung, auch nach dem Start', async ({ page }) => {
    await page.goto('/kurs/projekt-caesar-chiffre');
    await expect(page.locator('.beta-hint .beta-badge')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.beta-hint')).toContainText('Beta heißt: Dieser Kurs ist schon fertig, aber noch neu und noch nicht vollständig getestet.');
    // Der Titel selbst bleibt unverändert.
    await expect(page.locator('.course-detail > h1')).toHaveText('Projekt: Cäsar-Chiffre');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.beta-hint .beta-badge')).toBeVisible();

    await page.goto('/kurs/projekt-microbit-auto');
    await expect(page.locator('.course-description')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.beta-badge')).toHaveCount(0);
    await expect(page.locator('.beta-hint')).toHaveCount(0);

    await page.goto('/kurs/projekt-microbit-ampel');
    await expect(page.locator('.course-description')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.beta-badge')).toHaveCount(0);
  });
});
