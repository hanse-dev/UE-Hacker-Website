import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import path from 'node:path';

// scripts/build_lesson_bundle.py baut aus dem Lektions-Format + den Referenzlösungen je
// Woche/Variante/Sprache EINE lauffähige .py-Datei fürs den Offline-ZIP-Download (siehe
// scripts/pack_notebooks.py, INHALTE.md "Offline-ZIP-Download"). Die Aufgaben/Lösungen-Zuordnung
// selbst prüft schon python-lektionen-format.spec.js ("Lösungen passen zu den Aufgaben") - hier
// nur: der Generator läuft für alle 12 Wochen × 3 Varianten × 2 Sprachen durch und jede erzeugte
// Datei kompiliert fehlerfrei (build_lesson_bundle.py ruft compile() pro Datei selbst auf, siehe
// dort - ein Fehler dort bricht den Prozess mit non-zero exit ab, kein stilles Weiterlaufen).
test('build_lesson_bundle.py erzeugt für alle 12 Wochen × 3 Varianten × 2 Sprachen eine kompilierende Datei', () => {
  const cwd = path.join(process.cwd());
  const output = execFileSync('python3', ['scripts/build_lesson_bundle.py'], { cwd, encoding: 'utf8' });
  expect(output).toContain('72 Wochen-Pakete geprueft');
});
