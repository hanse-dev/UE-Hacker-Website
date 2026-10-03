import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import fs from 'node:fs';
import os from 'node:os';
import { ensureTestPrereqs, findStaleCellDirs, zipsAreStale } from '../scripts/ensure-test-prereqs.mjs';

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

// scripts/ensure-test-prereqs.mjs laeuft als globalSetup vor jedem Playwright-Lauf und erzeugt
// die gitignorten Notebook-Dateien/ZIPs neu, wenn sie fehlen oder aelter als ihre Quellen sind
// (frischer Worktree/Clone, Branch-Wechsel). Ohne das liefen die Notebook-Tests in ihren Timeout.
test.describe('ensure-test-prereqs.mjs erkennt fehlende/veraltete generierte Dateien', () => {
  let root;
  let cellDir;
  const setMtime = (file, secondsAgo) => {
    const t = new Date(Date.now() - secondsAgo * 1000);
    fs.utimesSync(file, t, t);
  };
  const write = (file, secondsAgo) => {
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, 'x');
    setMtime(file, secondsAgo);
  };

  test.beforeEach(() => {
    root = fs.mkdtempSync(path.join(os.tmpdir(), 'ue-prereqs-'));
    fs.mkdirSync(path.join(root, '.git'));
    cellDir = path.join(root, 'content', 'python-12-wochen-grundkurs', 'woche-1', 'abenteuer', 'woche1_abenteuer_0_glossar');
    write(path.join(cellDir, '01_markdown.py'), 100);
    write(path.join(cellDir, '02_code.py'), 100);
    write(path.join(cellDir, '_generated', 'woche1_abenteuer_0_glossar.ipynb.json'), 50);
    write(path.join(cellDir, '_bundle', 'woche1_abenteuer_0_glossar.py'), 50);
    write(path.join(root, 'public', 'python-12-wochen-notebooks.zip'), 10);
    write(path.join(root, 'public', 'wochen-zips', 'woche-1-komplett.zip'), 10);
    write(path.join(root, 'public', 'projekt-zips', 'caesar-chiffre-einzeln.zip'), 10);
    fs.writeFileSync(
      path.join(root, 'public', 'offline-downloads.json'),
      JSON.stringify({ files: ['python-12-wochen-notebooks.zip', 'wochen-zips/woche-1-komplett.zip', 'projekt-zips/caesar-chiffre-einzeln.zip'] })
    );
  });
  test.afterEach(() => fs.rmSync(root, { recursive: true, force: true }));

  test('aktueller Stand: nichts zu tun', () => {
    expect(findStaleCellDirs(root)).toEqual([]);
    expect(zipsAreStale(root)).toBe(false);
    expect(() => ensureTestPrereqs(root)).not.toThrow();
  });

  test('fehlende _generated-Datei wird erkannt', () => {
    fs.rmSync(path.join(cellDir, '_generated'), { recursive: true });
    expect(findStaleCellDirs(root)).toEqual([cellDir]);
  });

  test('Zelle neuer als ihre generierte Datei wird erkannt', () => {
    setMtime(path.join(cellDir, '02_code.py'), 20);
    expect(findStaleCellDirs(root)).toEqual([cellDir]);
  });

  test('fehlendes oder veraltetes ZIP wird erkannt', () => {
    write(path.join(root, 'content', 'python-woche1-abenteuer', 'lessons.json'), 5);
    expect(zipsAreStale(root)).toBe(true);

    setMtime(path.join(root, 'content', 'python-woche1-abenteuer', 'lessons.json'), 100);
    expect(zipsAreStale(root)).toBe(false);

    // Projekt-Kurs-Ordner gelten als Quelle, weil ein ZIP von ihnen in der Liste steht.
    write(path.join(root, 'content', 'caesar-chiffre', 'lessons.json'), 5);
    expect(zipsAreStale(root)).toBe(true);
    setMtime(path.join(root, 'content', 'caesar-chiffre', 'lessons.json'), 100);

    write(path.join(root, 'content', 'ki-labor-woche1', 'lessons.json'), 5);
    expect(zipsAreStale(root)).toBe(true);
    setMtime(path.join(root, 'content', 'ki-labor-woche1', 'lessons.json'), 100);
    expect(zipsAreStale(root)).toBe(false);

    fs.rmSync(path.join(root, 'public', 'wochen-zips', 'woche-1-komplett.zip'));
    expect(zipsAreStale(root)).toBe(true);
  });

  test('fehlende ZIP-Liste (public/offline-downloads.json) gilt als veraltet', () => {
    fs.rmSync(path.join(root, 'public', 'offline-downloads.json'));
    expect(zipsAreStale(root)).toBe(true);
  });

  test('Git-Worktree ohne worktree.ports.json bricht mit Hinweis ab', () => {
    // In einem verlinkten Worktree ist .git eine Datei, kein Ordner.
    fs.rmSync(path.join(root, '.git'), { recursive: true });
    fs.writeFileSync(path.join(root, '.git'), 'gitdir: /irgendwo');
    expect(() => ensureTestPrereqs(root)).toThrow(/worktree\.ports\.json/);

    fs.writeFileSync(path.join(root, 'worktree.ports.json'), '{}');
    expect(() => ensureTestPrereqs(root)).not.toThrow();
  });
});
