#!/usr/bin/env node
// Legt einen neuen Git-Worktree fuer einen Branch an, mit eigenen Dev-/Test-Ports (siehe
// scripts/worktree-ports.mjs) und symlinked node_modules (kein zweites `npm install` noetig).
// Damit kann an mehreren Branches parallel gearbeitet werden, ohne dass Dev-Server/Playwright
// sich gegenseitig Ports wegnehmen oder das Haupt-Checkout beim Branch-Wechsel gestoert wird.
//
// Nutzung: node scripts/new-worktree.mjs <branch-name> [--from <basis-branch>]
// Fuer einen bereits existierenden lokalen Branch wird kein neuer angelegt, sondern nur
// ausgecheckt.

import { execFileSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.join(__dirname, '..');

const args = process.argv.slice(2);
const branch = args[0];
if (!branch || branch.startsWith('--')) {
  console.error('Nutzung: node scripts/new-worktree.mjs <branch-name> [--from <basis-branch>]');
  process.exit(1);
}
const fromIdx = args.indexOf('--from');
const fromBranch = fromIdx !== -1 ? args[fromIdx + 1] : 'main';

function git(cmdArgs, opts = {}) {
  return execFileSync('git', cmdArgs, { cwd: repoRoot, encoding: 'utf8', ...opts });
}

function branchExists(name) {
  try {
    git(['rev-parse', '--verify', '--quiet', `refs/heads/${name}`]);
    return true;
  } catch {
    return false;
  }
}

// Slot-Nummer: monoton steigender Zaehler (nie wiederverwendet, auch wenn Worktrees geloescht
// wurden) - garantiert kollisionsfreie Ports ueber die Lebensdauer des Repos hinweg.
const slotFile = path.join(repoRoot, '.worktree-next-slot');
let slot = 1;
try {
  slot = parseInt(fs.readFileSync(slotFile, 'utf8').trim(), 10) || 1;
} catch {
  /* erster Aufruf */
}
fs.writeFileSync(slotFile, String(slot + 1));

const offset = slot * 10;
const worktreePorts = {
  vite: 5173 + offset,
  test: 5174 + offset,
  api: 3001 + offset,
  testApi: 3011 + offset,
};

const repoName = path.basename(repoRoot);
const worktreesRoot = path.join(repoRoot, '..', `${repoName}-worktrees`);
fs.mkdirSync(worktreesRoot, { recursive: true });
const worktreePath = path.join(worktreesRoot, branch);

if (fs.existsSync(worktreePath)) {
  console.error(`Verzeichnis existiert schon: ${worktreePath}`);
  process.exit(1);
}

console.log(`▶  Lege Worktree an: ${worktreePath} (Branch "${branch}", Slot ${slot})`);
if (branchExists(branch)) {
  git(['worktree', 'add', worktreePath, branch]);
} else {
  git(['worktree', 'add', worktreePath, '-b', branch, fromBranch]);
}

// node_modules symlinken statt neu installieren - beide Worktrees teilen sich dieselben
// Pakete (gleiches OS/Architektur, da lokal auf derselben Maschine).
for (const rel of ['node_modules', path.join('api', 'node_modules')]) {
  const src = path.join(repoRoot, rel);
  const dest = path.join(worktreePath, rel);
  if (fs.existsSync(src) && !fs.existsSync(dest)) {
    fs.symlinkSync(src, dest, 'dir');
    console.log(`▶  ${rel} symlinked`);
  }
}

// .env uebernehmen (falls vorhanden), API_PORT auf den Worktree-Slot umbiegen.
const envSrc = fs.existsSync(path.join(repoRoot, '.env'))
  ? path.join(repoRoot, '.env')
  : fs.existsSync(path.join(repoRoot, '.env.example'))
    ? path.join(repoRoot, '.env.example')
    : null;
if (envSrc) {
  let envContent = fs.readFileSync(envSrc, 'utf8');
  if (/^API_PORT=/m.test(envContent)) {
    envContent = envContent.replace(/^API_PORT=.*/m, `API_PORT=${worktreePorts.api}`);
  } else {
    envContent += `\nAPI_PORT=${worktreePorts.api}\n`;
  }
  fs.writeFileSync(path.join(worktreePath, '.env'), envContent);
  console.log('▶  .env angelegt (API_PORT angepasst)');
}

fs.writeFileSync(
  path.join(worktreePath, 'worktree.ports.json'),
  JSON.stringify(worktreePorts, null, 2) + '\n'
);

console.log(`
✅ Worktree bereit: ${worktreePath}

  Web-Dev:    http://localhost:${worktreePorts.vite}
  API:        http://localhost:${worktreePorts.api}
  Tests:      http://localhost:${worktreePorts.test} (npm run test:checks / test:precommit)
  Auth-Tests: API auf :${worktreePorts.testApi}

  cd ${path.relative(process.cwd(), worktreePath)}
  npm run start:all   # startet Web+API automatisch auf den Worktree-Ports
`);
