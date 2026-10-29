import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { slugify } from '../src/utils/slug.js';

const SHEET = fs.readFileSync(path.join('content', 'microbit-spickzettel', 'spickzettel.md'), 'utf8');
const BEGRIFFE = JSON.parse(fs.readFileSync(path.join('content', 'begriffe.json'), 'utf8'));
const STERNE = JSON.parse(fs.readFileSync(path.join('content', 'microbit-sterne', 'lessons.json'), 'utf8'));
const STERNE_KEY = 'ue-hacker-interactive-progress-microbit-sterne';
const MODES = ['bloecke', 'python', 'javascript'];

// Abschnitte des Spickzettels: Überschrift `##` bis zur nächsten.
const sections = SHEET.split(/^## /m).slice(1).map((s) => ({ title: s.split('\n')[0].trim(), body: s }));

test.describe('micro:bit-Spickzettel und Begriffs-Links in den micro:bit-Kursen', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      if (sessionStorage.getItem('spickzettel-test-init')) return;
      sessionStorage.setItem('spickzettel-test-init', '1');
      localStorage.clear();
    });
  });

  test('Inhalt: jeder Begriff hat seinen Abschnitt, jeder Abschnitt alle drei Ansichten', () => {
    const anchors = sections.map((s) => slugify(s.title));
    const list = BEGRIFFE.microbit;
    expect(list.length).toBeGreaterThan(10);
    for (const c of list) {
      expect(c.kurs, c.begriff).toBe('microbit-spickzettel');
      expect(anchors, `${c.begriff}: Überschrift für #${c.anker} fehlt im Spickzettel`).toContain(c.anker);
      expect(SHEET, `${c.begriff}: fehlt im Inhaltsverzeichnis`).toContain(`](#${c.anker})`);
    }
    // Umgekehrt: kein Abschnitt, auf den nichts verlinkt.
    expect(anchors.filter((a) => !list.some((c) => c.anker === a))).toEqual([]);
    for (const s of sections) {
      for (const mode of MODES) {
        expect((s.body.match(new RegExp(`^:::${mode}$`, 'gm')) || []).length, `${s.title}: ${mode}`).toBeGreaterThan(0);
      }
    }
  });

  test('Spickzettel: Sprung zum Abschnitt, Umschalter, keine Haken und kein gespeicherter Fortschritt', async ({ page }) => {
    await page.goto('/microbit/spickzettel#funk');
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toHaveText('micro:bit-Spickzettel', { timeout: 15000 });
    await expect(content.locator('h2#funk')).toBeInViewport();
    await expect(page.locator('.guide-mode-btn')).toHaveCount(3);
    await expect(page.locator('.guide-task')).toHaveCount(0);

    await expect(content.locator('#funk ~ .variante-bloecke .mc-funk').first()).toBeVisible();
    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(content.locator('.variante-python pre', { hasText: 'radio.config(group=x)' })).toBeVisible();

    // Inhaltsverzeichnis springt innerhalb der Seite.
    await content.locator('a[href="#variable"]').click();
    await expect(content.locator('h2#variable')).toBeInViewport();
    // Der Spickzettel verlinkt nicht auf sich selbst.
    await expect(content.locator('a.concept-link')).toHaveCount(0);

    const stored = await page.evaluate(() => Object.keys(localStorage).filter((k) => k.includes('spickzettel')));
    expect(stored).toEqual([]);
  });

  async function openSterne(page, lessonId) {
    const idx = STERNE.findIndex((l) => l.id === lessonId);
    const done = STERNE.slice(0, idx).map((l) => l.id);
    await page.addInitScript(([key, ids]) => localStorage.setItem(
      key, JSON.stringify({ variant: 'microbit-sterne', completedLessonIds: ids }),
    ), [STERNE_KEY, done]);
    await page.goto('/kurs/projekt-microbit-sterne');
    await page.locator('.btn-start-course').click();
    await page.locator('.lessons-list .lesson-item').nth(idx).click();
    await expect(page.locator('.guide-lesson .lesson-content h1')).toHaveText(STERNE[idx].title, { timeout: 15000 });
  }

  test('Fang den Stern, Werkstatt: „Funk“ kommt nur in der Ampel vor und verlinkt auf den Spickzettel', async ({ page }) => {
    await openSterne(page, 'lektion-05');
    const content = page.locator('.guide-lesson .lesson-content');
    const link = content.locator('a.concept-link[href="/microbit/spickzettel#funk"]');
    await expect(link).toHaveCount(1);
    await expect(link).toBeVisible();
    await expect(link).toHaveText('Funk');
    await expect(link).toHaveAttribute('target', '_blank');
    await expect(link).toHaveAttribute('title', /Funkgruppe\. – micro:bit-Spickzettel$/);

    const box = content.locator('.concept-box');
    await expect(box).toContainText('Neu oder unklar? Hier lest ihr mehr darüber');
    const item = box.locator('.concept-box-item', { hasText: 'Funk' });
    await expect(item.locator('a.concept-box-link')).toHaveAttribute('href', '/microbit/spickzettel#funk');
    await expect(item).toContainText('micro:bit-Spickzettel');
  });

  test('Links und Kasten richten sich nach der gewählten Ansicht', async ({ page }) => {
    await openSterne(page, 'lektion-02');
    const content = page.locator('.guide-lesson .lesson-content');
    const visible = (anchor) => content.locator(`a.concept-link[href="/microbit/spickzettel#${anchor}"]:visible`);
    const box = content.locator('.concept-box');

    // Blöcke: Die Variable wird im gemeinsamen Text erklärt, „wenn“ ist ein Block-Name im Fettdruck.
    await expect(visible('variable')).toHaveCount(1);
    await expect(visible('bedingung')).toHaveCount(1);
    await expect(visible('bedingung')).toHaveText('wenn');
    // „Schleife“ steht nur im Python-Teil: weder Link noch Eintrag im Kasten.
    await expect(visible('schleife')).toHaveCount(0);
    const term = (name) => box.locator('.concept-box-item strong', { hasText: new RegExp(`^${name}$`) });
    await expect(term('Variable')).toHaveCount(1);
    const names = await box.locator('.concept-box-item strong').allTextContents();
    expect(names).not.toContain('Schleife');
    expect(new Set(names).size).toBe(names.length);

    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(visible('schleife')).toHaveCount(1);
    await expect(visible('variable')).toHaveCount(1);
    await expect(term('Schleife')).toHaveCount(1);
  });

  test('Verlinkung: Block-Namen nur als ganzer Fettdruck, je Ansicht beim ersten Vorkommen', async ({ page }) => {
    await page.goto('/');
    const result = await page.evaluate(async () => {
      const { linkConceptsByMode } = await import('/src/composables/useConcepts.js');
      const html = [
        '<p>Rot oder Gelb. Nimm den Block <strong>oder</strong>.</p>',
        '<p>:::bloecke</p>', '<p>Eine Variable im Blöcke-Teil.</p>', '<p>:::</p>',
        '<p>:::python</p>', '<p>Eine Variable im Python-Teil, noch eine Variable.</p>', '<p>:::</p>',
        '<p>Gemeinsam: Variable.</p>',
      ].join('');
      const r = linkConceptsByMode(html, { language: 'microbit' }, ['bloecke', 'python', 'javascript']);
      const links = [...r.html.matchAll(/href="[^"]*#([^"]+)"[^>]*>([^<]*)</g)].map((m) => `${m[1]}:${m[2]}`);
      return { links, found: Object.fromEntries(Object.entries(r.found).map(([k, v]) => [k, v.map((c) => c.anker)])) };
    });
    // Das „oder“ im Satz bleibt Text, nur der fett gedruckte Block wird ein Link.
    // Die Variable bekommt je Ansicht einen Link, der gemeinsame Satz danach keinen mehr.
    // JavaScript fehlt in diesem Text und zählt deshalb nicht mit.
    expect(result.links).toEqual(['und-oder:oder', 'variable:Variable', 'variable:Variable']);
    expect(result.found.bloecke).toEqual(['und-oder', 'variable']);
    expect(result.found.python).toEqual(['und-oder', 'variable']);
    expect(result.found.javascript).toEqual([]);
  });
});
