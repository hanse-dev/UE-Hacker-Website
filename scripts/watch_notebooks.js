#!/usr/bin/env node
/**
 * Überwacht den content/ Ordner und erstellt automatisch das Notebook-Paket,
 * sobald eine .ipynb-Datei geändert wurde.
 * Start: npm run watch:notebooks
 */

import { readdirSync, statSync } from "fs";
import { spawn } from "child_process";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, "..");
const CONTENT_DIR = join(ROOT, "content", "python-12-wochen-grundkurs");
const INTERVAL_MS = 5000;

function findLatestMtime(dir) {
  let latest = 0;
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = join(dir, entry.name);
    const stat = statSync(full);
    if (entry.isDirectory()) {
      latest = Math.max(latest, findLatestMtime(full));
    } else if (entry.name.endsWith(".ipynb")) {
      latest = Math.max(latest, stat.mtimeMs);
    }
  }
  return latest;
}

function runPack() {
  const child = spawn("npm", ["run", "pack:notebooks"], {
    cwd: ROOT,
    stdio: "inherit",
    shell: true,
  });
  child.on("close", (code) => {
    if (code !== 0) console.error("Pack fehlgeschlagen.");
  });
}

let lastMtime = 0;

console.log("👀 Überwache Notebooks in", CONTENT_DIR);
console.log("   Prüfe alle " + INTERVAL_MS / 1000 + " Sekunden auf Änderungen.\n");

// Einmal beim Start
runPack();

setInterval(() => {
  try {
    const latest = findLatestMtime(CONTENT_DIR);
    if (latest > lastMtime && lastMtime > 0) {
      console.log(`   [${new Date().toLocaleTimeString()}] Änderung erkannt → Paket wird aktualisiert...`);
      runPack();
    }
    lastMtime = latest;
  } catch (e) {
    console.error("Fehler:", e.message);
  }
}, INTERVAL_MS);
