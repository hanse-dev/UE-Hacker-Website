import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// Spiel-Projekt "Ausweichen" (engine "spiel"): Bloecke oder Python, beides laeuft ueber
// src/spiel/spiel.py in Pyodide; Pruefen spielt das Spiel unsichtbar durch (validation.checks).
const CONTENT_DIR = path.join('content', 'ausweichen');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));
const PROGRESS_KEY = 'ue-hacker-interactive-progress-ausweichen';
const BLOCKS_KEY = 'ue-hacker-lesson-code-ausweichen-bloecke';
const MODE_KEY = 'ue-hacker-guide-mode';
const KERNEL_TIMEOUT = 90000;

// Python -> Blockly-JSON mit demselben Uebersetzer, den die Seite in Pyodide nutzt.
function zuBloecken(codes) {
  const script = [
    'import json, sys',
    "sys.path.insert(0, 'src/spiel')",
    'from zu_bloecken import zu_bloecken',
    'print(json.dumps([zu_bloecken(c) for c in json.load(sys.stdin)]))',
  ].join('\n');
  return JSON.parse(execFileSync('python3', ['-c', script], { input: JSON.stringify(codes), encoding: 'utf8' }));
}

async function openLesson(page, lessonIdx, { mode = 'python', blocks = null } = {}) {
  const done = lessons.slice(0, lessonIdx).map((l) => l.id);
  await page.addInitScript(([progressKey, modeKey, blocksKey, ids, m, b, lessonId]) => {
    if (sessionStorage.getItem('spiel-test-init')) return;
    sessionStorage.setItem('spiel-test-init', '1');
    localStorage.removeItem('ue-hacker-lang');
    localStorage.setItem(modeKey, m);
    localStorage.setItem(progressKey, JSON.stringify({ version: 1, courseId: 'projekt-ausweichen', variant: 'ausweichen', completedLessonIds: ids }));
    localStorage.removeItem('ue-hacker-lesson-code-ausweichen');
    if (b) localStorage.setItem(blocksKey, JSON.stringify({ [lessonId]: { savedAt: Date.now(), codes: b } }));
    else localStorage.removeItem(blocksKey);
  }, [PROGRESS_KEY, MODE_KEY, BLOCKS_KEY, done, mode, blocks, lessons[lessonIdx].id]);
  await page.goto(`/kurs/projekt-ausweichen?started=1&lesson=${lessons[lessonIdx].id}`);
  await expect(page.locator('.spiel-lesson h1')).toHaveText(lessons[lessonIdx].title, { timeout: 15000 });
  await expect(page.locator('.btn-spielen').first()).toBeEnabled({ timeout: KERNEL_TIMEOUT });
}

/** x der linken Kante des blauen Spielers in Zeile y (Canvas-Pixel), -1 wenn keiner da ist. */
async function spielerX(page, y = 370) {
  return page.locator('.spiel-canvas').evaluate((canvas, zeile) => {
    const data = canvas.getContext('2d').getImageData(0, zeile, canvas.width, 1).data;
    for (let x = 0; x < canvas.width; x++) {
      const [r, g, b] = data.slice(x * 4, x * 4 + 3);
      if (b > 200 && r < 120 && g > 100 && g < 160) return x;
    }
    return -1;
  }, y);
}

test.describe('Spiel-Projekt: Ausweichen', () => {
  test('Lösungen bestehen, Vorlagen fallen durch, alles lässt sich in Blöcke übersetzen (CPython)', () => {
    const out = execFileSync('python3', ['scripts/check_spiel_loesungen.py'], { encoding: 'utf8' });
    expect(out).toContain('0 Fehler');
  });

  test('Inhalt: jede Lektion hat Blöcke- und Python-Abschnitte, jede Aufgabe eine Spiel-Prüfung mit Hinweisen', () => {
    for (const lesson of lessons) {
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      const bloecke = (md.match(/^:::bloecke$/gm) || []).length;
      expect(bloecke, `${lesson.file}: :::bloecke`).toBeGreaterThan(0);
      expect((md.match(/^:::python$/gm) || []).length, `${lesson.file}: gleich viele :::python`).toBe(bloecke);
      // Python-Code nur in Python-Abschnitten, Block-Listings nur in Blöcke-Abschnitten.
      const ausserhalb = md.replace(/^:::(bloecke|python)$[\s\S]*?^:::$/gm, '');
      expect(ausserhalb, `${lesson.file}: Code außerhalb von :::bloecke/:::python`).not.toMatch(/```(python|bloecke)/);
      for (const task of lesson.tasks) {
        expect(task.validation?.type).toBe('spiel');
        for (const check of task.validation.checks) expect(check.hint, JSON.stringify(check)).toBeTruthy();
        if (!task.example) expect(task.solution, task.instruction).toBeTruthy();
      }
    }
  });

  test('Kurs steht auf der Projekte-Seite und startet mit Blöcken', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card[href="/kurs/projekt-ausweichen"]')).toBeVisible();
    await openLesson(page, 0, { mode: 'bloecke' });
    await expect(page.locator('.spiel-mode-btn[data-mode="bloecke"]')).toHaveAttribute('aria-pressed', 'true');
    await expect(page.locator('.spiel-bloecke-flaeche .blocklySvg').first()).toBeVisible({ timeout: 30000 });
    // Nur der Blöcke-Abschnitt des Lektionstexts ist sichtbar.
    await expect(page.locator('.lesson-content .variante-bloecke').first()).toBeVisible();
    await expect(page.locator('.lesson-content .variante-python').first()).toBeHidden();
    // Die Vorlage als Blöcke ergibt wieder das Python der Vorlage.
    await page.locator('.spiel-python-ansehen summary').first().click();
    await expect(page.locator('.spiel-python-ansehen pre').first()).toHaveText(/spieler = figur\(180, 200, 40, 20, "blau"\)/);
  });

  test('Ansicht wechseln: Python zeigt den Editor und merkt sich die Wahl', async ({ page }) => {
    await openLesson(page, 0, { mode: 'bloecke' });
    await page.locator('.spiel-mode-btn[data-mode="python"]').click();
    await expect(page.locator('.task-block .cm-content').first()).toContainText('figur(180, 200');
    await expect(page.locator('.lesson-content .variante-python').first()).toBeVisible();
    expect(await page.evaluate((key) => localStorage.getItem(key), MODE_KEY)).toBe('python');
  });

  test('Python: Vorlage fällt mit Hinweis durch, Lösung besteht und schaltet die nächste Lektion frei', async ({ page }) => {
    test.setTimeout(150000);
    await openLesson(page, 1);
    const task = page.locator('.task-block').nth(1);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toContainText('Bei → fährt der Spieler noch nicht nach rechts');
    await setCodeMirrorContent(task, lessons[1].tasks[1].solution);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 30000 });
    // Beispiel (Aufgabe 1) zählt durch Spielen, Bonus (Aufgabe 3) wird übersprungen.
    await page.locator('.task-block').nth(0).locator('.btn-spielen').click();
    const bonus = page.locator('.task-block').nth(2);
    for (let i = 0; i < 2; i++) {
      await bonus.locator('.btn-check').click();
      await expect(bonus.locator('.feedback-error')).toBeVisible();
    }
    await bonus.locator('.btn-skip').click();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await page.locator('.lesson-complete-box .btn-next').click();
    await expect(page.locator('.spiel-lesson h1')).toHaveText(lessons[2].title);
  });

  test('Spielen: Pfeiltaste bewegt den Spieler auf der Bühne, Stopp hält an', async ({ page }) => {
    await openLesson(page, 2);
    const task = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(task, lessons[2].tasks[1].solution);
    await task.locator('.btn-spielen').click();
    await expect(task.locator('.btn-stopp')).toBeVisible();
    await page.locator('.spiel-canvas').scrollIntoViewIfNeeded();
    await expect.poll(() => spielerX(page)).toBe(180);
    await page.locator('.spiel-canvas').focus();
    await page.keyboard.down('ArrowRight');
    // Am rechten Rand (x = 360) bleibt er stehen.
    await expect.poll(() => spielerX(page), { timeout: 5000 }).toBe(360);
    await page.keyboard.up('ArrowRight');
    await task.locator('.btn-stopp').click();
    await expect(task.locator('.btn-spielen')).toBeVisible();
  });

  test('Eine Endlosschleife in jedes_bild hält das Spiel mit verständlicher Meldung an', async ({ page }) => {
    await openLesson(page, 1);
    const task = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(task, 'from spiel import *\n\nspieler = figur(180, 360, 40, 20, "blau")\n\ndef jedes_bild():\n    while True:\n        spieler.x += 1\n');
    await task.locator('.btn-spielen').click();
    await expect(task.locator('.output-content')).toContainText('Endlosschleife', { timeout: 15000 });
    await expect(task.locator('.btn-spielen')).toBeVisible();
    // Prüfen meldet es ebenfalls, statt den Tab einzufrieren.
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toContainText('Endlosschleife', { timeout: 30000 });
  });

  test('Blöcke: jede Lösung als Blöcke besteht das Prüfen (Rundweg Python → Blöcke → Python)', async ({ browser }) => {
    test.setTimeout(600000);
    for (const [idx, lesson] of lessons.entries()) {
      const blocks = zuBloecken(lesson.tasks.map((t) => t.solution || t.codeTemplate))
        .map((json) => JSON.stringify({ ...JSON.parse(json), gespeichert: true }));
      // Je Lektion ein frischer Kontext: addInitScript-Aufrufe wuerden sich sonst stapeln.
      const context = await browser.newContext();
      const page = await context.newPage();
      await openLesson(page, idx, { mode: 'bloecke', blocks });
      for (const [tIdx, task] of lesson.tasks.entries()) {
        const block = page.locator('.task-block').nth(tIdx);
        await expect(block.locator('.blocklySvg')).toBeVisible({ timeout: 30000 });
        await expect(block.locator('.spiel-python-ansehen pre')).toContainText('from spiel import *');
        if (task.example) {
          await block.locator('.btn-spielen').click();
        } else {
          await block.locator('.btn-check').click();
          await expect(block.locator('.feedback-success'), `${lesson.id} Aufgabe ${tIdx + 1}`).toBeVisible({ timeout: 30000 });
        }
      }
      await expect(page.locator('.lesson-complete-box'), lesson.id).toBeVisible();
      await context.close();
    }
  });

  test('Blöcke: unveränderte Vorlage fällt durch, ohne Änderung gibt es kein Zurücksetzen', async ({ page }) => {
    await openLesson(page, 1, { mode: 'bloecke' });
    const task = page.locator('.task-block').nth(1);
    await expect(task.locator('.blocklySvg')).toBeVisible({ timeout: 30000 });
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toContainText('Bei → fährt der Spieler noch nicht nach rechts');
    await expect(task.locator('.btn-reset')).toHaveCount(0);
  });

  test('Blöcke: gespeicherter Stand wird geladen, Zurücksetzen holt die Vorlage zurück', async ({ page }) => {
    const [loesung] = zuBloecken([lessons[1].tasks[1].solution]);
    const blocks = ['', JSON.stringify({ ...JSON.parse(loesung), gespeichert: true }), ''];
    await openLesson(page, 1, { mode: 'bloecke', blocks });
    const task = page.locator('.task-block').nth(1);
    await expect(task.locator('.spiel-python-ansehen pre')).toContainText('taste("rechts")', { timeout: 30000 });
    await task.locator('.btn-reset').click();
    await expect(task.locator('.spiel-python-ansehen pre')).not.toContainText('taste("rechts")');
    await expect(task.locator('.btn-reset')).toHaveCount(0);
    const saved = await page.evaluate((key) => JSON.parse(localStorage.getItem(key) || '{}'), BLOCKS_KEY);
    expect(saved[lessons[1].id]).toBeUndefined();
  });

  test('Python: Zurücksetzen holt nach einer Änderung die Vorlage zurück', async ({ page }) => {
    await openLesson(page, 1);
    const task = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(task, 'from spiel import *\n');
    await task.locator('.btn-reset').click();
    await expect(task.locator('.cm-content')).toContainText('taste("links")');
    await expect(task.locator('.btn-reset')).toHaveCount(0);
  });
});
