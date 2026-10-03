import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';

// scripts/build_lesson_notebook.py baut aus dem Lektions-Format + den Referenzlösungen je
// Woche/Variante/Sprache ein Aufgaben- und ein Lösungs-Jupyter-Notebook (siehe
// scripts/pack_notebooks.py, INHALTE.md "Offline-ZIP-Download") - ergänzt die flache .py-Datei aus
// build_lesson_bundle.py (geprüft in lesson-bundle-generator.spec.js) um ein echtes Notebook-
// Format für Jupyter/VS Code. Hier nur: der Generator läuft für alle 12 Wochen × 3 Varianten × 2
// Sprachen durch (Aufgaben-/Lösungsanzahl passt, jede "garantiert gültige" Code-Zelle - Beispiele
// und Referenzlösungen, nicht die absichtlich kaputten Debug-Quest-Templates - kompiliert
// fehlerfrei, siehe dort).
test('build_lesson_notebook.py erzeugt für alle 12 Wochen × 3 Varianten × 2 Sprachen valide Aufgaben-/Lösungs-Notebooks', () => {
  const cwd = path.join(process.cwd());
  const output = execFileSync('python3', ['scripts/build_lesson_notebook.py', '--check'], { cwd, encoding: 'utf8' });
  expect(output).toContain('72 Wochen-Pakete geprueft');
});

test('build_offline_py.py baut für Projekt-Kurse und KI-Labor eine Python-Datei + Einzeldateien je Lektion, alles kompiliert', () => {
  const output = execFileSync('python3', ['scripts/build_offline_py.py', '--check'], { cwd: process.cwd(), encoding: 'utf8' });
  expect(output).toContain('5 Projekt-Kurse + 8 KI-Labor-Wochen geprueft');
});

// Die ZIPs selbst baut der globalSetup (scripts/ensure-test-prereqs.mjs) vor jedem Lauf - hier
// wird nur ihr Inhalt geprueft, nicht neu gepackt (paralleles Neuschreiben wuerde andere Tests
// stoeren, die dieselben Dateien gerade ueber den Dev-Server laden).
const listZip = (relPath) =>
  execFileSync('unzip', ['-Z1', path.join(process.cwd(), 'public', relPath)], { encoding: 'utf8' }).split('\n').filter(Boolean);

test('12-Wochen-Kurs: je Woche und Sprache drei ZIPs (Notebooks, eine Python-Datei je Thema, Einzeldateien je Lektion)', () => {
  const nb = listZip('wochen-zips/woche-4-notebooks.zip');
  expect(nb).toEqual(expect.arrayContaining([
    'woche4_abenteuer_aufgaben.ipynb', 'woche4_abenteuer_loesungen.ipynb',
    'woche4_pferde_aufgaben.ipynb', 'woche4_scifi_loesungen.ipynb',
  ]));
  expect(nb.some((f) => f.endsWith('.py'))).toBe(false);

  const komplett = listZip('wochen-zips/woche-4-komplett.zip');
  expect(komplett).toEqual(expect.arrayContaining(['woche4_abenteuer_komplett.py', 'woche4_pferde_komplett.py', 'woche4_scifi_komplett.py']));
  expect(komplett.some((f) => f.endsWith('.ipynb') && !f.includes('cheat_sheet'))).toBe(false);

  const einzeln = listZip('wochen-zips/woche-4-einzeln.zip');
  expect(einzeln).toEqual(expect.arrayContaining([
    'woche4_abenteuer/00_glossar.py', 'woche4_abenteuer/01_lektion-01.py', 'woche4_abenteuer/09_debug-01.py',
    'woche4_pferde/01_lektion-01.py', 'woche4_scifi/01_lektion-01.py',
  ]));

  const en = listZip('wochen-zips/woche-4-en-einzeln.zip');
  expect(en).toEqual(expect.arrayContaining(['week4_adventure/00_glossary.py', 'week4_adventure/01_lektion-01.py']));
  expect(listZip('wochen-zips/woche-4-en-komplett.zip')).toContain('week4_adventure_complete.py');
  expect(listZip('wochen-zips/woche-4-en-notebooks.zip')).toContain('week4_adventure_solutions.ipynb');
});

test('Projekt-Kurse und KI-Labor: je drei ZIPs; jedes Python-Projekt aus kurse.json ist dabei', () => {
  const kurse = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'public', 'kurse.json'), 'utf8'));
  const pythonProjects = kurse.filter((k) => k.type === 'projekt' && k.engine !== 'js-sandbox');
  expect(pythonProjects.length).toBeGreaterThan(0);
  // ProjectCourse.vue zeigt die Buttons fuer jedes Python-Projekt - ohne ZIP waeren das tote Links.
  for (const p of pythonProjects) {
    for (const format of ['notebooks', 'komplett', 'einzeln']) {
      expect(fs.existsSync(path.join(process.cwd(), 'public', 'projekt-zips', `${p.contentPath}-${format}.zip`)), `${p.contentPath}-${format}.zip`).toBe(true);
    }
  }
  expect(listZip('projekt-zips/morsecode-notebooks.zip')).toEqual(['morsecode_aufgaben.ipynb', 'morsecode_loesungen.ipynb']);
  expect(listZip('projekt-zips/morsecode-komplett.zip')).toEqual(['morsecode_komplett.py']);
  expect(listZip('projekt-zips/morsecode-einzeln.zip')).toContain('01_lektion-01.py');

  expect(listZip('ki-labor-zips/woche-3-notebooks.zip')).toEqual(['ki-labor-woche3_aufgaben.ipynb']);
  expect(listZip('ki-labor-zips/woche-3-komplett.zip')).toEqual(['ki-labor-woche3_komplett.py']);
  expect(listZip('ki-labor-zips/woche-3-einzeln.zip')).toEqual(expect.arrayContaining(['01_lektion-01.py', '06_debug-01.py']));
});
