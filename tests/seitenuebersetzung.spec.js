import { test, expect } from '@playwright/test';
import { readFileSync } from 'fs';
import { setCodeMirrorContent } from './helpers/codemirror.js';

const lessons = JSON.parse(readFileSync(new URL('../content/web-erste-website/lessons.json', import.meta.url), 'utf-8'));

// Seitenuebersetzer (Edge/Chrome) bauen jeden uebersetzbaren Absatz satzweise neu auf und ersetzen
// dabei auch die Inline-Elemente durch Kopien. Vue haelt danach Verweise auf abgehaengte Knoten und
// stuerzte beim naechsten v-if-Wechsel ab („Cannot read properties of null (reading 'insertBefore')“,
// z. B. ○ → ✓ nach „Pruefen“). Simulation: nur Elemente, die laut translate-Attribut uebersetzt werden.
const simulateTranslation = (page) => page.evaluate(() => {
  const translatable = (el) => el.closest('[translate]')?.getAttribute('translate') !== 'no';
  const blocks = [...document.querySelectorAll('#app *')].filter((el) =>
    [...el.childNodes].some((n) => n.nodeType === Node.TEXT_NODE && n.nodeValue.trim()));
  let rebuilt = 0;
  for (const el of blocks.reverse()) {
    if (!el.isConnected || !translatable(el) || el.querySelector('[translate="no"]')) continue;
    el.replaceChildren(...[...el.childNodes].map((n) =>
      (n.nodeType === Node.TEXT_NODE && n.nodeValue.trim() ? document.createTextNode(`[EN] ${n.nodeValue}`) : n.cloneNode(true))));
    rebuilt += 1;
  }
  return rebuilt;
});

test('Seitenübersetzung: Lerntext wird übersetzt, „Prüfen“ funktioniert trotzdem', async ({ page }) => {
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  await page.goto('/kurs/web-erste-website?stufe=einfach');
  await page.locator('.btn-start-course').click();
  await page.locator('.lesson-item').nth(0).click();
  const idx = lessons[0].tasks.findIndex((t) => !t.example);
  const block = page.locator('.task-block').nth(idx);
  await expect(block.locator('.task-pending')).toBeVisible();

  expect(await simulateTranslation(page)).toBeGreaterThan(0);
  await expect(page.locator('.lesson-content')).toContainText('[EN]');

  await block.locator('.btn-check').click();
  await expect(block.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
  await setCodeMirrorContent(block.locator('.cm-host'), lessons[0].tasks[idx].solution);
  await block.locator('.btn-check').click();
  await expect(block.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  await expect(block.locator('.task-done')).toBeVisible();
  // Re-Rendern nach dem Pruefen darf den uebersetzten Aufgabentext nicht zuruecksetzen.
  await expect(block.locator('.task-instruction')).toContainText('[EN]');
  expect(errors).toEqual([]);
  await expect(block.locator('.btn-check')).not.toContainText('[EN]');
});

test('Seitenübersetzung: Code in Lerntexten bleibt unübersetzt', async ({ page }) => {
  await page.goto('/kurs/web-erste-website?stufe=einfach');
  await page.locator('.btn-start-course').click();
  await page.locator('.lesson-item').nth(0).click();
  const code = page.locator('.lesson-content code').first();
  await expect(code).toBeVisible();
  await expect(code).toHaveAttribute('translate', 'no');
});
