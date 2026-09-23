import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

// Regression tests for the storytelling overhaul (see HANDOFF.md, section 3.4).
// These assert on rendered notebook TEXT so they run fast (no Pyodide/kernel
// needed) and catch the exact bugs that were found and fixed during that work.

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

// Woche 1 (alle Themen) ist im Lektions-Format: die Bugs stehen als Aufgaben in debug-01
// (python-woche1-lektionen.spec.js prueft das Format selbst) - hier nur die Inhalts-Regeln.
function debugGoalsTest(themeLabel, variant) {
  test(`Woche 1 ${themeLabel}: Debug-Bugs nennen ein Ziel, ohne den Fehler zu verraten`, async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.setItem(key, JSON.stringify({
        version: 1,
        completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
      }));
    }, `ue-hacker-interactive-progress-python-woche1-${variant}`);
    await page.goto(`${COURSE_URL}?week=1&variant=${variant}`);
    await page.locator('.js-course-tour .stepper-step').nth(5).click();
    await page.locator('.task-block').first().waitFor({ state: 'visible', timeout: 15000 });

    const text = await page.locator('.lesson-editor-section').innerText();
    const bugCount = (text.match(/Bug #\d/g) || []).length;
    const zielCount = (text.match(/Ziel:/g) || []).length;
    expect(bugCount).toBe(3);
    expect(zielCount).toBe(bugCount);
    expect(text).toContain('Das Programm soll den Text');

    // Ziel-Text darf den Fehler selbst nicht verraten (z.B. "fehlende Klammer", "Tippfehler").
    const spoilerWords = /fehlende[rs]?\s+(Klammer|Anführungszeichen|import)|Tippfehler|falsch geschrieben/i;
    expect(text).not.toMatch(spoilerWords);
  });
}

test.describe('Debug-Ziele Woche 1 (Lektions-Format)', () => {
  debugGoalsTest('Abenteuer', 'abenteuer');
  debugGoalsTest('Pferde', 'pferde');
  debugGoalsTest('Sci-Fi', 'scifi');
});

test.describe('Storytelling-Überarbeitung: Pferde', () => {
  test('Woche 2: Hufschlag-Typen benannt, kein "Sonnentals"-Tippfehler', async () => {
    // Woche 2 ist im Lektions-Format (content/python-woche2-pferde/)
    const dir = path.join(process.cwd(), 'content/python-woche2-pferde');
    const text = fs.readdirSync(dir).filter((f) => f.endsWith('.md'))
      .map((f) => fs.readFileSync(path.join(dir, f), 'utf8')).join('\n');
    expect(text).toContain('Sonnental');
    expect(text).not.toContain('Sonnentals');
    for (const gait of ['Schritt', 'Trab', 'Galopp', 'Sprung']) {
      expect(text).toContain(gait);
    }
  });

  test('Woche 9: eigene Rahmengeschichte statt Woche-8-Duplikat', async () => {
    // Woche 8 und 9 sind im Lektions-Format (content/python-woche{8,9}-pferde/lektion-01.md).
    const intro = (w) => fs.readFileSync(
      path.join(process.cwd(), `content/python-woche${w}-pferde/lektion-01.md`), 'utf-8');
    const week8Text = intro(8);
    const week9Text = intro(9);

    expect(week9Text).not.toContain('Sonnentals');
    // The two weeks must not share their opening story paragraph.
    const week8Intro = week8Text.split('\n').slice(0, 4).join('\n');
    expect(week9Text).not.toContain(week8Intro);
  });

});

test.describe('Storytelling-Überarbeitung: Abenteuer', () => {

});

test.describe('Storytelling-Überarbeitung: Sci-Fi', () => {
  test('Woche 11: Lektion-Code ist syntaktisch korrekt (def/self vorhanden)', async () => {
    // Woche 11 ist im Lektions-Format (content/python-woche11-scifi/).
    const dir = path.join(process.cwd(), 'content/python-woche11-scifi');
    const mdFiles = fs.readdirSync(dir).filter((f) => f.endsWith('.md'));
    const text = mdFiles.map((f) => fs.readFileSync(path.join(dir, f), 'utf-8')).join('\n');
    expect(text).toContain('Raumstation Nebula-7');
    expect(text).not.toContain('Evolution-Station Alpha-7');

    const lessons = JSON.parse(fs.readFileSync(path.join(dir, 'lessons.json'), 'utf-8'));
    const codeSnippets = [
      ...mdFiles.map((f) => fs.readFileSync(path.join(dir, f), 'utf-8')),
      ...lessons.flatMap((l) => l.tasks.map((t) => t.codeTemplate)),
    ];
    expect(codeSnippets.length).toBeGreaterThan(0);
    for (const code of codeSnippets) {
      // The original bug: every method inside a class was missing "def" and/or
      // "self" (e.g. "aktivieren():" instead of "def aktivieren(self):", or
      // "def __init__(id, name):" instead of "def __init__(self, id, name):").
      // Any line indented >=4 that looks like a method signature must start
      // with "def" and take "self" as its first parameter.
      for (const line of code.split('\n')) {
        const indent = line.match(/^ */)[0].length;
        const trimmed = line.trim();
        if (indent < 4 || !/^[a-zA-Z_]\w*\(.*\):\s*$/.test(trimmed)) continue;
        expect(trimmed.startsWith('def ')).toBe(true);
        const params = trimmed.match(/^def\s+\w+\(([^)]*)\)/)[1];
        const firstParam = params.split(',')[0].trim();
        if (firstParam !== '') {
          expect(firstParam).toBe('self');
        }
      }
    }
  });

  test('Woche 6/8: Boss-Quest 2 ist nicht mehr der Woche-5-Klon', async () => {
    // Woche 5, 6, 8 sind im Lektions-Format (content/python-woche{N}-scifi/boss-02.md) -
    // die zweite Extra-Herausforderung jeder Woche muss einen eigenen Titel haben.
    const bossTwoTitle = (w) => fs.readFileSync(
      path.join(process.cwd(), `content/python-woche${w}-scifi/boss-02.md`), 'utf-8',
    ).split('\n')[0];
    const week5Title = bossTwoTitle(5);
    const week6Title = bossTwoTitle(6);
    const week8Title = bossTwoTitle(8);

    expect(week6Title).not.toBe(week5Title);
    expect(week8Title).not.toBe(week5Title);
    expect(week8Title).not.toBe(week6Title);
  });

  test('Woche 12: Debug-Bugs verraten die Lösung nicht im Kommentar', async () => {
    // Woche 12 ist im Lektions-Format (content/python-woche12-scifi[-en]/lessons.json).
    const codes = [];
    for (const lang of ['', '-en']) {
      const lessons = JSON.parse(fs.readFileSync(path.join(process.cwd(), `content/python-woche12-scifi${lang}/lessons.json`), 'utf-8'));
      for (const t of lessons.find((l) => l.id === 'debug-01').tasks) codes.push(t.codeTemplate);
    }
    expect(codes.length).toBeGreaterThan(0);
    for (const code of codes) expect(code).not.toMatch(/#\s*Bug:/i);
  });

});

// Glossare (0_glossar) duerfen keine Begriffe aus spaeteren Wochen erklaeren (Vorgriffe):
// Woche 4 kennt noch keine Listen, try/except kommt erst in Woche 8.
test.describe('Glossare: keine Vorgriffe', () => {
  const bases = ['python-12-wochen-grundkurs', 'python-12-wochen-grundkurs-en'];
  const glossarText = (week) => bases.flatMap((base) => {
    const weekDir = path.join('content', base, `woche-${week}`);
    return fs.readdirSync(weekDir, { withFileTypes: true }).filter((e) => e.isDirectory()).map((e) => e.name).flatMap((variant) => {
      const dir = fs.readdirSync(path.join(weekDir, variant)).find((n) => n.endsWith('_0_glossar'));
      const gdir = path.join(weekDir, variant, dir);
      return fs.readdirSync(gdir).filter((f) => /^\d\d_.*\.py$/.test(f))
        .map((f) => ({ id: `${base}/${variant}/${f}`, text: fs.readFileSync(path.join(gdir, f), 'utf8') }));
    });
  });

  test('Woche 4: keine Listen (Liste/append/Index)', () => {
    for (const { id, text } of glossarText(4)) {
      expect(text, id).not.toMatch(/\.append\(|\*\*(Liste|List|Index)\*\*|\blist_\b|\bliste\b/);
    }
  });

  for (const week of [3, 4, 5, 6, 7]) {
    test(`Woche ${week}: kein try/except vor Woche 8`, () => {
      for (const { id, text } of glossarText(week)) {
        expect(text, id).not.toMatch(/\btry\b|\bexcept\b/);
      }
    });
  }

  test('Woche 6: Tabelle ohne kaputte Zeilen', () => {
    for (const { id, text } of glossarText(6)) {
      expect(text, id).not.toMatch(/\|"$/m);
    }
  });
});
