import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Wird von vite.config.js/playwright*.config.js genutzt, damit jeder Git-Worktree (siehe
// scripts/new-worktree.mjs) eigene Ports fuer Dev-Server/Tests hat und sich nicht mit dem
// Haupt-Checkout oder anderen Worktrees in die Quere kommt. `worktree.ports.json` liegt nur in
// per new-worktree.mjs angelegten Worktrees (gitignored) - im Haupt-Checkout fehlt die Datei,
// dann gelten die bisherigen Standardports unveraendert.
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const portsFile = path.join(__dirname, '..', 'worktree.ports.json');

const DEFAULTS = { vite: 5173, test: 5174, api: 3001, testApi: 3011 };

let overrides = {};
try {
  overrides = JSON.parse(fs.readFileSync(portsFile, 'utf8'));
} catch {
  // Kein Worktree-Setup oder Datei (noch) nicht vorhanden - Standardports bleiben.
}

export const ports = { ...DEFAULTS, ...overrides };
