import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { expectGuideContent } from './helpers/guide-content.js';

const CONTENT_DIR = path.join('content', 'microbit-ampel');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const STORAGE_KEY = 'ue-hacker-interactive-progress-microbit-ampel';
const PLAN_DIR = path.join('public', 'microbit', 'ampel');
const PLANS = ['breadboard', 'erste-led-3v3', 'stufe-0', 'stufe-1', 'stufe-2', 'taster'];

// Am Extension Board ist nur eine Stiftleiste erreichbar: 3.3V, GND, GND, P20, P19, P16 … P10, 3.3V.
// P10 hängt an der LED-Anzeige, P11 an Knopf B, P19 bleibt frei - genutzt werden nur diese Pins.
const PINS_IM_KURS = ['P12', 'P13', 'P14', 'P15', 'P16', 'P20'];

test.describe('micro:bit-Kurs: Ampelanlage (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      // Nur beim ersten Laden leeren, damit der Reload-Test den gespeicherten Stand sieht.
      if (sessionStorage.getItem('microbit-test-init')) return;
      sessionStorage.setItem('microbit-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
  });

  async function openCourse(page, completedLessonIds = []) {
    if (completedLessonIds.length) {
      await page.addInitScript(([key, ids]) => localStorage.setItem(
        key, JSON.stringify({ variant: 'microbit-ampel', completedLessonIds: ids }),
      ), [STORAGE_KEY, completedLessonIds]);
    }
    await page.goto('/kurs/projekt-microbit-ampel');
    await expect(page.locator('.course-description')).toContainText('Ampelanlage');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, und jeder Abschnitt gibt es für Blöcke und Python', () => {
    expectGuideContent(CONTENT_DIR);
  });

  test('Steckpläne werden ausgeliefert und passen auch auf ein Handy', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 800 });
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    const images = content.locator('img');
    await expect(images).toHaveCount(3);
    for (let i = 0; i < 3; i++) {
      const img = images.nth(i);
      await img.scrollIntoViewIfNeeded();
      await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth)).toBeGreaterThan(0);
      const [imgBox, contentBox] = [await img.boundingBox(), await content.boundingBox()];
      expect(imgBox.x + imgBox.width).toBeLessThanOrEqual(contentBox.x + contentBox.width);
    }
    for (const name of PLANS) {
      const res = await page.request.get(`/microbit/ampel/${name}.svg`);
      expect(res.status(), name).toBe(200);
      expect(await res.text(), name).toContain('<svg');
    }
  });

  test('Startklar: Die erste LED leuchtet zuerst an 3.3V, erst danach kommen P13 und das Programm', async ({ page }) => {
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    const srcs = await content.locator('img').evaluateAll((imgs) => imgs.map((img) => img.getAttribute('src')));
    expect(srcs.indexOf('/microbit/ampel/erste-led-3v3.svg')).toBeGreaterThan(-1);
    expect(srcs.indexOf('/microbit/ampel/erste-led-3v3.svg')).toBeLessThan(srcs.indexOf('/microbit/ampel/stufe-0.svg'));

    // Der 3.3V-Steckplan steht vor dem ersten Programm, und beide Fälle nach dem Umstecken sind erklärt.
    const headings = await content.locator('h2').allTextContents();
    const umstecken = headings.findIndex((h) => h.includes('P13'));
    expect(umstecken, headings.join(' | ')).toBeGreaterThan(-1);
    expect(umstecken).toBeLessThan(headings.indexOf('Das erste Programm'));
    await expect(content).toContainText('altes Programm');
    await expect(content).toContainText('noch kein Programm');
    await expect(page.locator('.guide-task').first()).toContainText('3.3V');
  });

  test('Pin- und Funk-Blöcke haben die MakeCode-Farben, der Hinweis passt zu jedem micro:bit-Kurs', async ({ page }) => {
    await openCourse(page, lessons.slice(0, 5).map((l) => l.id));
    await expect(page.locator('.guide-tasks .editor-hint')).toContainText('micro:bit');
    await expect(page.locator('.guide-tasks .editor-hint')).not.toContainText('Auto');

    await page.locator('.lesson-item').first().click();
    const pins = page.locator('.mc-block.mc-pins').first();
    await expect(pins).toHaveText('schreibe digitalen Wert von Pin P13 auf 1');
    await expect(pins).toHaveCSS('background-color', 'rgb(178, 34, 34)');

    await page.locator('.lesson-item').nth(5).click();
    const funk = page.locator('.mc-block.mc-funk').first();
    await expect(funk).toHaveText('setze Funkgruppe auf x');
    await expect(funk).toHaveCSS('background-color', 'rgb(227, 0, 140)');
  });

  test('Nur Pins aus der erreichbaren Stiftleiste, in Text, Code und Steckplänen', () => {
    const pinsIn = (text) => [...text.matchAll(/\b(?:P|pin|DigitalPin\.P|AnalogPin\.P)(\d+)\b/g)].map((m) => `P${m[1]}`);
    for (const lesson of lessons) {
      // Die Abbildung der ganzen Stiftleiste (Startklar) nennt bewusst alle Pins.
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8').replace(/^.*3\.3V · GND · GND.*$/m, '');
      for (const pin of pinsIn(md)) expect(PINS_IM_KURS, `${lesson.file}: ${pin}`).toContain(pin);
    }
    for (const name of PLANS) {
      const svg = fs.readFileSync(path.join(PLAN_DIR, `${name}.svg`), 'utf8');
      for (const pin of pinsIn(svg)) expect(PINS_IM_KURS, `${name}.svg: ${pin}`).toContain(pin);
    }
  });

  test('Steckpläne: höchstens zwei Kabel zu GND, jede LED mit Brücke in eine GND-Reihe', () => {
    for (const name of PLANS.filter((n) => n !== 'breadboard')) {
      const svg = fs.readFileSync(path.join(PLAN_DIR, `${name}.svg`), 'utf8');
      const leds = (svg.match(/<circle [^>]*r="15"/g) || []).length;
      const bridges = (svg.match(/stroke="#1e88e5"/g) || []).length;
      expect((svg.match(/>GND<\/text>/g) || []).length, `${name}: GND-Kabel`).toBeLessThanOrEqual(2);
      expect(bridges, `${name}: Brücken`).toBeGreaterThanOrEqual(leds);
    }
  });

  test('JavaScript-Ansicht zeigt MakeCode-JavaScript und merkt sich die Wahl', async ({ page }) => {
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(page.locator('.guide-mode-btn')).toHaveCount(3);
    await page.locator('.guide-mode-btn[data-mode="javascript"]').click();
    const js = content.locator('pre code.language-javascript').first();
    await expect(js).toBeVisible();
    await expect(js).toContainText('pins.digitalWritePin(DigitalPin.P13, 1)');
    await expect(content.locator('.mc-blocks').first()).toBeHidden();
    await expect(content.locator('pre code.language-python').first()).toBeHidden();

    await page.reload();
    await expect(page.locator('.guide-mode-btn[data-mode="javascript"]')).toHaveClass(/active/);
    await expect(page.locator('.guide-lesson .lesson-content pre code.language-javascript').first()).toBeVisible();
  });

  test('Gemerkte JavaScript-Wahl: ein Kurs ohne JavaScript zeigt Blöcke statt einer leeren Seite', async ({ page }) => {
    await page.addInitScript(() => localStorage.setItem('ue-hacker-guide-mode', 'javascript'));
    await page.goto('/kurs/projekt-microbit-auto');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.guide-mode-btn')).toHaveCount(2);
    await expect(page.locator('.guide-mode-btn[data-mode="bloecke"]')).toHaveClass(/active/);
    await expect(page.locator('.guide-lesson .lesson-content .mc-blocks').first()).toBeVisible();
  });

  test('Stufe 1: Das Gerüst ist sichtbar, die fertige Lösung ist eingeklappt', async ({ page }) => {
    await openCourse(page, ['lektion-01']);
    await page.locator('.lesson-item').nth(1).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toContainText('Stufe 1');
    await expect(content.locator('.mc-block:visible', { hasText: 'pausiere (ms) 5000' })).toHaveCount(0);

    const solution = content.locator('details', { has: page.locator('summary', { hasText: 'Lösung anzeigen' }) });
    await solution.locator('summary').click();
    await expect(solution.locator('.mc-block', { hasText: 'pausiere (ms) 5000' })).toBeVisible();
    await expect(solution.locator('pre code.language-python')).toBeHidden();
  });

  test('Pflichtaufgaben abhaken schließt die Stufe ab und schaltet die nächste frei', async ({ page }) => {
    await openCourse(page);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);
    const tasks = page.locator('.guide-task');
    for (const [i, task] of lessons[0].tasks.entries()) {
      if (!task.isBonus) await tasks.nth(i).locator('.guide-task-check').check();
    }
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Kurs ist in der Projekte-Übersicht verlinkt, der Filter Elektronik zeigt ihn', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-microbit-ampel"]')).toBeVisible({ timeout: 15000 });
    await page.locator('.filter-chip', { hasText: 'Elektronik' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(1);
    await page.locator('a.projekt-card[href="/kurs/projekt-microbit-ampel"]').click();
    await expect(page.locator('.course-description')).toContainText('Breadboard');
    await expect(page.locator('.btn-start-course')).toBeVisible();
  });
});
