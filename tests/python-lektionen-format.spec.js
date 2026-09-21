import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

// Woche 1–4 und weitere (alle Themen, DE + EN) sind im Lektions-Format: content/python-woche{N}-{thema}[-en]/
// (Format wie der JS-Grundkurs). Diese Datei prueft (a) die Content-Integritaet aller dieser Ordner
// ohne Browser und (b) dass jede Kombination in der Wochen-Tour als Lektions-Leiste erscheint.
// Woche-1-Details (Beispiel/Pruefen, Rahmen, Check-Wahl usw.) stehen in python-woche1-lektionen.spec.js.
const CONTENT = path.join(process.cwd(), 'content');
// alle vorhandenen Wochen automatisch (jede neu umgestellte Woche wird sofort mitgeprüft)
const WEEKS = [...new Set(
  fs.readdirSync(CONTENT).map((d) => d.match(/^python-woche(\d+)-/)?.[1]).filter(Boolean).map(Number)
)].sort((a, b) => a - b);
const THEMES = ['abenteuer', 'pferde', 'scifi'];
const LANGS = ['de', 'en'];
const folder = (week, theme, lang) => `python-woche${week}-${theme}${lang === 'en' ? '-en' : ''}`;
const readLessons = (f) => JSON.parse(fs.readFileSync(path.join(CONTENT, f, 'lessons.json'), 'utf8'));

test.describe('Lektions-Format: Content-Integrität', () => {
  for (const week of WEEKS) for (const theme of THEMES) for (const lang of LANGS) {
    const f = folder(week, theme, lang);
    test(`${f}: ids eindeutig, Dateien vorhanden, Sections geordnet, Aufgaben vollständig`, () => {
      const lessons = readLessons(f);
      const ids = lessons.map((l) => l.id);
      expect(new Set(ids).size).toBe(ids.length);

      const order = { lektion: 0, debug: 1, mission: 2, boss: 3 };
      let last = 0;
      for (const l of lessons) {
        expect(fs.existsSync(path.join(CONTENT, f, l.file)), `${f}/${l.file}`).toBe(true);
        expect(order[l.section], `${l.id} section`).toBeDefined();
        expect(order[l.section]).toBeGreaterThanOrEqual(last);
        last = order[l.section];
        expect(l.tasks.length).toBeGreaterThan(0);
        // Beispiele stehen vor den eigenen Aufgaben einer Lektion
        const firstOwn = l.tasks.findIndex((t) => !t.example);
        if (firstOwn >= 0) expect(l.tasks.slice(firstOwn).some((t) => t.example), `${l.id} Beispiel nach Pflichtaufgabe`).toBe(false);
        for (const t of l.tasks) {
          expect(t.instruction).toBeTruthy();
          expect(typeof t.codeTemplate).toBe('string');
          expect(t.validation?.expected ?? t.validation?.variables).toBeTruthy();
          // Struktur-Pflichtbausteine duerfen nicht schon im vorgegebenen Code stehen (sonst sinnlos), nie bei Beispielen
          if (t.validation.codeContains) {
            expect(t.example, `${l.id}: codeContains bei Beispiel`).toBeFalsy();
            const given = t.codeTemplate.split('\n').filter((x) => !x.trim().startsWith('#')).join('\n');
            for (const tok of t.validation.codeContains) {
              const re = new RegExp((/^\w/.test(tok) ? '\\b' : '') + tok.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + (/\w$/.test(tok) ? '\\b' : ''));
              expect(re.test(given), `${l.id}: ${tok} steht schon im vorgegebenen Code`).toBe(false);
            }
          }
          // vorgegebene Eingaben fuer input(): Liste von Texten, nur wenn der Code input() nutzt (Beispiele ausgenommen)
          if (t.validation.stdin) {
            expect(Array.isArray(t.validation.stdin) && t.validation.stdin.every((x) => typeof x === 'string')).toBe(true);
          }
        }
      }
      const sections = new Set(lessons.map((l) => l.section));
      expect([...sections].sort()).toEqual(['boss', 'debug', 'lektion', 'mission']);
    });
  }
});

test.describe('Lektions-Format: Wochen-Tour', () => {
  for (const week of WEEKS) for (const theme of THEMES) for (const lang of LANGS) {
    const f = folder(week, theme, lang);
    test(`${f}: Leiste mit allen Lektionen + Check, frei anklickbar`, async ({ page }) => {
      await page.addInitScript((l) => localStorage.setItem('ue-hacker-lang', l), lang);
      await page.goto(`/kurs/python-12-wochen-grundkurs?week=${week}&variant=${theme}`);
      const n = readLessons(f).length;
      const dots = page.locator('.js-course-tour .stepper-step');
      await expect(dots).toHaveCount(n + 1); // + Check
      await expect(dots.nth(n - 1)).toBeEnabled();
      await expect(page.locator('.js-course-tour [data-open-check]')).toBeVisible();
      await expect(page.locator('.tour-stepper > .progress-stepper')).toHaveCount(0);
      // Beispiel-Aufgabe hat kein "Prüfen"
      await expect(page.locator('.task-block').first().locator('.btn-check')).toHaveCount(0);

      // Nachschlagewerk "Lösungen" gehört zur gleichen Sprache und ist nicht leer
      await page.locator('[data-reference-key="6_loesungen"]').click();
      await expect(page.locator('.notebook-cells .cell').first()).toBeVisible({ timeout: 15000 });
      await expect(page.locator('.error')).toHaveCount(0);
    });
  }
});

// Wochen mit passenden Lösungen (SOLUTION_WEEKS wächst, sobald eine Woche fertig ist): das Nachschlagewerk "Loesungen" ist aus den Referenzloesungen der Aufgaben erzeugt (eine Zelle je
// Aufgabe) - jede Aufgabenstellung muss dort stehen, sonst passen Loesungen und Aufgaben nicht mehr zusammen.
const SOLUTION_WEEKS = [1, 2, 3, 4, 10, 11, 12];
test.describe('Lektions-Format: Lösungen passen zu den Aufgaben', () => {
  const EN_THEME = { abenteuer: 'adventure', pferde: 'horses', scifi: 'scifi' };
  for (const week of SOLUTION_WEEKS) for (const theme of THEMES) for (const lang of LANGS) {
    test(`Woche ${week} ${theme} ${lang}: jede Aufgabe hat ihre Lösung`, () => {
      const dir = lang === 'en'
        ? path.join(CONTENT, 'python-12-wochen-grundkurs-en', `woche-${week}`, EN_THEME[theme], `week${week}_${EN_THEME[theme]}_6_loesungen`)
        : path.join(CONTENT, 'python-12-wochen-grundkurs', `woche-${week}`, theme, `woche${week}_${theme}_6_loesungen`);
      const files = fs.readdirSync(dir).filter((f) => /^\d+_(markdown|code)\.py$/.test(f)).sort();
      const md = files.filter((f) => f.endsWith('_markdown.py')).map((f) => fs.readFileSync(path.join(dir, f), 'utf8')).join('\n').replace(/\\"/g, '"').replace(/\\\\/g, '\\');
      const own = readLessons(folder(week, theme, lang)).flatMap((l) => l.tasks.filter((t) => !t.example));
      for (const t of own) expect(md, t.instruction.slice(0, 60)).toContain(t.instruction);
      expect(files.filter((f) => f.endsWith('_code.py')).length).toBe(own.length);
    });
  }
});
