import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import path from 'node:path';

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

test('pack_notebooks.py packt die Jupyter-Notebooks mit in den Wochen-ZIP-Download (DE + EN)', () => {
  const cwd = path.join(process.cwd());
  execFileSync('python3', ['scripts/pack_notebooks.py'], { cwd, encoding: 'utf8' });

  const listZip = (zipName) =>
    execFileSync('unzip', ['-l', path.join(cwd, 'public', 'wochen-zips', zipName)], { encoding: 'utf8' });

  const de = listZip('woche-4.zip');
  expect(de).toContain('woche4_abenteuer_komplett.py');
  expect(de).toContain('notebooks/woche4_abenteuer_aufgaben.ipynb');
  expect(de).toContain('notebooks/woche4_abenteuer_loesungen.ipynb');
  expect(de).toContain('notebooks/woche4_pferde_aufgaben.ipynb');
  expect(de).toContain('notebooks/woche4_scifi_aufgaben.ipynb');

  const en = listZip('woche-4-en.zip');
  expect(en).toContain('week4_adventure_complete.py');
  expect(en).toContain('notebooks/week4_adventure_tasks.ipynb');
  expect(en).toContain('notebooks/week4_adventure_solutions.ipynb');
});
