#!/usr/bin/env node
// Entfernt einen mit scripts/new-worktree.mjs angelegten Worktree wieder (z.B. nach dem Merge
// des Branches nach main). Loescht nur den Worktree, nicht den Branch selbst - dafuer weiterhin
// das normale `git branch -d <branch>` nutzen.
//
// Nutzung: node scripts/remove-worktree.mjs <branch-name>

import { execFileSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.join(__dirname, '..');

const branch = process.argv[2];
if (!branch) {
  console.error('Nutzung: node scripts/remove-worktree.mjs <branch-name>');
  process.exit(1);
}

const repoName = path.basename(repoRoot);
const worktreePath = path.join(repoRoot, '..', `${repoName}-worktrees`, branch);

// Die von new-worktree.mjs angelegten node_modules-Symlinks gelten fuer git als "untracked"
// (das .gitignore-Muster `node_modules/` trifft nur Ordner, keine Symlinks) - ohne sie vorher zu
// loesen, verweigert `git worktree remove` immer. Nur der Link wird entfernt, nie das Ziel.
for (const rel of ['node_modules', path.join('api', 'node_modules')]) {
  const link = path.join(worktreePath, rel);
  if (fs.lstatSync(link, { throwIfNoEntry: false })?.isSymbolicLink()) fs.unlinkSync(link);
}

execFileSync('git', ['worktree', 'remove', worktreePath], { cwd: repoRoot, stdio: 'inherit' });
console.log(`✅ Worktree entfernt: ${worktreePath}`);
