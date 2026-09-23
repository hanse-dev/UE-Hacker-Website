import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

// Regression tests for the storytelling overhaul (see HANDOFF.md, section 3.4).
// These assert on rendered notebook TEXT so they run fast (no Pyodide/kernel
// needed) and catch the exact bugs that were found and fixed during that work.

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

const VARIANT_KEY = { Pferde: 'pferde', Abenteuer: 'abenteuer', 'Sci-Fi': 'scifi' };
const STEP_KEY = {
  Lektion: '1_lektion', Debug: '2_debug', Missionen: '3_missionen',
  'Boss-Quest': '5_boss', Check: '4_check', Lösungen: '6_loesungen', Glossar: '0_glossar',
};

// Direkter Deep-Link statt Akkordeon-Klick (Woche/Thema/Schritt in einem goto()) - die neue
// Wochen-Tour zeigt ohnehin immer nur eine Woche gleichzeitig, kein Scoping mehr nötig.
async function openWeekVariantTab(page, weekNumber, variantLabel, tabLabel) {
  const variant = VARIANT_KEY[variantLabel];
  const step = STEP_KEY[tabLabel];
  await page.goto(`${COURSE_URL}?week=${weekNumber}&variant=${variant}&step=${step}`);
  await page.locator('.cell').first().waitFor({ state: 'visible', timeout: 15000 });
  return page;
}

// Notebook-Code-Zellen nutzen seit der Zellen-Format-Umstellung CodeMirror statt einer
// <textarea class="code-editor"> - .inputValue() funktioniert dort nicht mehr.
async function getCodeCellText(cmHost) {
  return cmHost.locator('.cm-content').innerText();
}

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
    // Woche 8 und 9 sind im Lektions-Format (kein `.cell` in der Tour) - Original-Einleitung aus der Quelldatei lesen.
    const intro = (w) => fs.readFileSync(
      path.join(process.cwd(), `content/python-12-wochen-grundkurs/woche-${w}/pferde/woche${w}_pferde_1_lektion/01_markdown.py`), 'utf-8');
    const week8Text = intro(8);
    const week9Text = intro(9);

    expect(week9Text).toContain('Zuchtbücher von Sonnental');
    // The two weeks must not share their opening story paragraph anymore.
    const week8Intro = week8Text.split('\n').slice(0, 6).join('\n');
    expect(week9Text).not.toContain(week8Intro);
    expect(week9Text).not.toContain('Sonnentals');
  });

});

test.describe('Storytelling-Überarbeitung: Abenteuer', () => {

});

test.describe('Storytelling-Überarbeitung: Sci-Fi', () => {
  test('Woche 11: Lektion-Code ist syntaktisch korrekt (def/self vorhanden)', async () => {
    // Woche 11 ist im Lektions-Format (kein `.cell` in der Tour) - Original-Lektion aus den Quelldateien lesen.
    const dir = path.join(process.cwd(), 'content/python-12-wochen-grundkurs/woche-11/scifi/woche11_scifi_1_lektion');
    const files = fs.readdirSync(dir).filter((f) => /^\d+_(markdown|code)\.py$/.test(f)).sort();
    const text = files.map((f) => fs.readFileSync(path.join(dir, f), 'utf-8')).join('\n');
    expect(text).toContain('Raumstation Nebula-7');
    expect(text).not.toContain('Evolution-Station Alpha-7');

    const codeFiles = files.filter((f) => f.endsWith('_code.py'));
    expect(codeFiles.length).toBeGreaterThan(0);
    for (const f of codeFiles) {
      const code = fs.readFileSync(path.join(dir, f), 'utf-8');
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
    // Woche 5 ist seit dem Lektions-Format kein Notebook mehr im Kurs (kein `.cell` in der Tour) -
    // die Original-Boss-Quest liegt weiter als Nachschlagewerk-Quelle im Repo, daher aus der Datei lesen.
    const week5Text = fs.readFileSync(
      path.join(process.cwd(), 'content/python-12-wochen-grundkurs/woche-5/scifi/woche5_scifi_5_boss/04_markdown.py'),
      'utf-8',
    );
    expect(week5Text).toContain('Der Raumstation-Manager');

    // Woche 6 ist ebenfalls im Lektions-Format (siehe oben) - Original-Boss-Quest aus der Quelldatei lesen.
    const week6Text = fs.readFileSync(
      path.join(process.cwd(), 'content/python-12-wochen-grundkurs/woche-6/scifi/woche6_scifi_5_boss/04_markdown.py'),
      'utf-8',
    );
    expect(week6Text).toContain('Der Hangar-Verwalter');
    expect(week6Text).not.toContain('Der Raumstation-Manager');

    // Woche 8 ist ebenfalls im Lektions-Format - Original-Boss-Quest aus der Quelldatei lesen.
    const week8Text = fs.readFileSync(
      path.join(process.cwd(), 'content/python-12-wochen-grundkurs/woche-8/scifi/woche8_scifi_5_boss/04_markdown.py'),
      'utf-8',
    );
    expect(week8Text).toContain('Die Sensor-Matrix');
    expect(week8Text).not.toContain('Der Raumstation-Manager');
  });

  test('Woche 12: Debug-Bugs verraten die Lösung nicht im Kommentar', async () => {
    // Woche 12 ist im Lektions-Format - Original-Debug-Notebook aus den Quelldateien, dazu die neuen Debug-Aufgaben.
    const dir = path.join(process.cwd(), 'content/python-12-wochen-grundkurs/woche-12/scifi/woche12_scifi_2_debug');
    const codes = fs.readdirSync(dir).filter((f) => f.endsWith('_code.py')).map((f) => fs.readFileSync(path.join(dir, f), 'utf-8'));
    expect(codes.length).toBeGreaterThan(0);
    for (const lang of ['', '-en']) {
      const lessons = JSON.parse(fs.readFileSync(path.join(process.cwd(), `content/python-woche12-scifi${lang}/lessons.json`), 'utf-8'));
      for (const t of lessons.find((l) => l.id === 'debug-01').tasks) codes.push(t.codeTemplate);
    }
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
