import { test, expect } from '@playwright/test';
import { startKernel } from './helpers/kernel.js';
import { openSolutionsNotebook } from './helpers/notebook.js';
import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

// Woche 12 ist das Abschlussprojekt "Text-Adventure" (kein Turtle mehr). Im Lektions-Format laeuft die Lektion
// als Einzel-Aufgaben (Referenzloesungen per python3 geprueft); als echtes Notebook gibt es noch das Nachschlagewerk
// "Loesungen". Die Notebooks bestehen aus
// langen, zusammenhaengenden Code-Zellen (Startpaket, Klassen, Kampf mit random, JSON-Speichern) -
// nur ein echter Lauf in Pyodide zeigt, ob alles zusammen funktioniert.
const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const VARIANTS = [
  { key: 'abenteuer', de: 'abenteuer', en: 'adventure' },
  { key: 'pferde', de: 'pferde', en: 'horses' },
  { key: 'scifi', de: 'scifi', en: 'scifi' },
];

test.describe('Woche 12: Abschlussprojekt Text-Adventure', () => {
  for (const v of VARIANTS) {
    test(`${v.key}: Lösungs-Notebook (DE und EN) läuft fehlerfrei in Pyodide`, async ({ page }) => {
      test.setTimeout(150000);

      for (const lang of ['de', 'en']) {
        await page.addInitScript((l) => localStorage.setItem('ue-hacker-lang', l), lang);
        await openSolutionsNotebook(page, v.key);
        // Kernel kann durch den Wechsel des Nachschlagewerks schon bereit sein (dann ist der Button aus).
        await startKernel(page);
        await expect(page.locator('.btn-run-all').first()).toBeEnabled({ timeout: 120000 });
        await page.locator('.btn-run-all').first().click();
        // Das Finale endet mit dem Sieg- oder Game-Over-Text - beides ist ein gueltiger Lauf.
        await expect(page.locator('.cell-output').last()).toContainText(/🏆|💀/, { timeout: 30000 });
        await expect(page.locator('.output-error')).toHaveCount(0);
      }
    });
  }

  test('Kein Turtle mehr in den Woche-12-Notebooks und -Checks', async () => {
    const roots = [
      'content/python-12-wochen-grundkurs/woche-12',
      'content/python-12-wochen-grundkurs-en/woche-12',
    ];
    const hits = [];
    const walk = (dir) => {
      for (const entry of readdirSync(dir, { withFileTypes: true })) {
        if (entry.name === '_generated' || entry.name === '_bundle') continue;
        const p = join(dir, entry.name);
        if (entry.isDirectory()) walk(p);
        else if (/turtle/i.test(readFileSync(p, 'utf-8')) || /turtle/i.test(entry.name)) hits.push(p);
      }
    };
    for (const r of roots) if (existsSync(r)) walk(r);
    if (/turtle/i.test(readFileSync('content/python-checks/week-12.json', 'utf-8'))) hits.push('week-12.json');
    expect(hits).toEqual([]);
  });
});
