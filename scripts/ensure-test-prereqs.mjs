#!/usr/bin/env node
// Stellt sicher, dass vor einem Playwright-Lauf alles da ist, was die Tests brauchen, aber nicht
// im Repo liegt (gitignored): die generierten Notebook-Dateien des 12-Wochen-Kurses
// (_generated/_bundle) und die Download-ZIPs unter public/. `npm run dev`/`npm run build` erzeugen
// sie selbst - der Playwright-Webserver startet aber nacktes `vite`. Fehlen sie (frischer
// Worktree, frischer Clone) oder sind sie aelter als ihre Quellen (Branch-Wechsel, Content-
// Aenderung ohne `npm run dev`), laufen die Notebook-Tests in ihren Timeout bzw. pruefen alten
// Stand.
//
// Laeuft als `globalSetup` in playwright.config.js/playwright.auth.config.js, also bei jedem
// Testlauf (test:checks, test:precommit, test:auth, npm test). Erzeugt nur bei Bedarf neu: ein
// unnoetiges Neuschreiben wuerde den Vite-Dev-Server (Polling) zu Seiten-Reloads mitten im
// Testlauf bringen.
//
// Manuell: node scripts/ensure-test-prereqs.mjs

import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DEFAULT_ROOT = path.join(__dirname, '..');

const CELL_COURSE_DIRS = ['python-12-wochen-grundkurs', 'python-12-wochen-grundkurs-en'];
const CELL_FILE = /^\d\d.*_(markdown|code)\.py$/;

function mtime(file) {
  return fs.statSync(file, { throwIfNoEntry: false })?.mtimeMs ?? null;
}

function walkDirs(dir, visit) {
  if (!fs.existsSync(dir)) return;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  visit(dir, entries);
  for (const e of entries) {
    if (e.isDirectory() && e.name !== '_generated' && e.name !== '_bundle') {
      walkDirs(path.join(dir, e.name), visit);
    }
  }
}

function newestMtime(dir, fileFilter) {
  let newest = 0;
  walkDirs(dir, (d, entries) => {
    for (const e of entries) {
      if (e.isFile() && fileFilter(e.name)) newest = Math.max(newest, mtime(path.join(d, e.name)) ?? 0);
    }
  });
  return newest;
}

// Zellen-Ordner, deren _generated/_bundle-Datei fehlt oder aelter ist als eine ihrer Zellen.
export function findStaleCellDirs(root = DEFAULT_ROOT) {
  const stale = [];
  for (const course of CELL_COURSE_DIRS) {
    walkDirs(path.join(root, 'content', course), (dir, entries) => {
      const cells = entries.filter((e) => e.isFile() && CELL_FILE.test(e.name));
      if (cells.length === 0) return;
      const name = path.basename(dir);
      const newestCell = Math.max(...cells.map((e) => mtime(path.join(dir, e.name))));
      const outputs = [path.join(dir, '_generated', `${name}.ipynb.json`), path.join(dir, '_bundle', `${name}.py`)];
      if (outputs.some((o) => mtime(o) === null || mtime(o) < newestCell)) stale.push(dir);
    });
  }
  return stale;
}

// Offline-Download-ZIPs fehlen oder sind aelter als ihre Quellen. Welche ZIPs es gibt, steht in
// public/offline-downloads.json (schreibt scripts/pack_notebooks.py) - fehlt die Liste, fehlt alles.
// Quellen: Lektions-Format/Referenzloesungen/Cheat-Sheets des 12-Wochen-Kurses, KI-Labor-Wochen,
// die Projekt-Kurs-Ordner (aus den ZIP-Namen abgeleitet) und die Generator-Skripte selbst.
export function zipsAreStale(root = DEFAULT_ROOT) {
  let files;
  try {
    files = JSON.parse(fs.readFileSync(path.join(root, 'public', 'offline-downloads.json'), 'utf8')).files;
  } catch {
    return true;
  }
  const zipTimes = files.map((f) => mtime(path.join(root, 'public', f)));
  if (zipTimes.length === 0 || zipTimes.includes(null)) return true;
  const oldestZip = Math.min(...zipTimes);

  const projectFolders = new Set(
    files.filter((f) => f.startsWith('projekt-zips/')).map((f) => path.basename(f).replace(/-(notebooks|komplett|einzeln)\.zip$/, ''))
  );
  const scriptsDir = path.join(root, 'scripts');
  let newestSource = 0;
  for (const f of fs.existsSync(scriptsDir) ? fs.readdirSync(scriptsDir) : []) {
    if (/^(build_.*|pack_notebooks|notebook_utils)\.py$/.test(f)) newestSource = Math.max(newestSource, mtime(path.join(scriptsDir, f)) ?? 0);
  }
  const contentDir = path.join(root, 'content');
  for (const entry of fs.existsSync(contentDir) ? fs.readdirSync(contentDir) : []) {
    if (
      entry.startsWith('python-woche') ||
      entry.startsWith('ki-labor-woche') ||
      CELL_COURSE_DIRS.includes(entry) ||
      projectFolders.has(entry)
    ) {
      newestSource = Math.max(newestSource, newestMtime(path.join(contentDir, entry), () => true));
    }
  }
  return oldestZip < newestSource;
}

function fail(message) {
  throw new Error(`\n\n✖  Test-Voraussetzung fehlt: ${message}\n`);
}

export function ensureTestPrereqs(root = DEFAULT_ROOT) {
  // Ein Git-Worktree ohne eigene Ports wuerde die Standardports nutzen. Laeuft dort schon der
  // Dev-/Test-Server des Haupt-Checkouts, testet Playwright (reuseExistingServer) stillschweigend
  // dessen Code statt den des Worktrees.
  const isLinkedWorktree = fs.statSync(path.join(root, '.git'), { throwIfNoEntry: false })?.isFile();
  if (isLinkedWorktree && !fs.existsSync(path.join(root, 'worktree.ports.json'))) {
    fail(
      'Dieser Git-Worktree hat keine worktree.ports.json (eigene Dev-/Test-Ports).\n' +
        '   Worktrees mit `npm run worktree:new -- <branch>` anlegen (siehe WORKFLOW.md), sonst\n' +
        '   testet Playwright womöglich den Server des Haupt-Checkouts.'
    );
  }

  const staleCells = findStaleCellDirs(root);
  const staleZips = zipsAreStale(root);
  if (staleCells.length === 0 && !staleZips) return;

  try {
    execFileSync('python3', ['--version'], { stdio: 'ignore' });
  } catch {
    fail('python3 nicht gefunden - wird für die generierten Notebook-Dateien gebraucht.');
  }

  if (staleCells.length > 0) {
    console.log(`▶  ${staleCells.length} Notebook-Ordner fehlen/veraltet - erzeuge _generated/_bundle neu …`);
    execFileSync('python3', ['scripts/build_cell_notebooks.py'], { cwd: root, stdio: 'inherit' });
  }
  if (staleCells.length > 0 || staleZips) {
    console.log('▶  Download-ZIPs fehlen/veraltet - packe neu …');
    execFileSync('python3', ['scripts/pack_notebooks.py'], { cwd: root, stdio: 'inherit' });
  }
}

// Playwright ruft globalSetup mit seinem Config-Objekt auf - deshalb ein eigener Wrapper ohne
// Parameter statt ensureTestPrereqs direkt als Default-Export.
export default function globalSetup() {
  ensureTestPrereqs();
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    ensureTestPrereqs();
    console.log('✔  Test-Voraussetzungen vorhanden.');
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
}
