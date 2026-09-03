import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/**
 * Erstellt eine konsistente Kopie der SQLite-Datenbank via `VACUUM INTO`.
 * Funktioniert sicher auch im laufenden Betrieb (WAL-Modus) — anders als ein
 * simples `cp` liest `VACUUM INTO` die Datenbank über eine echte SQLite-Verbindung
 * und kann daher nicht mitten in einem Schreibvorgang eine inkonsistente Kopie ziehen.
 */
export function runBackup({ dbPath, backupDir }) {
  if (!fs.existsSync(dbPath)) {
    throw new Error(`Datenbank nicht gefunden: ${dbPath}`);
  }
  fs.mkdirSync(backupDir, { recursive: true });

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const backupPath = path.join(backupDir, `ue-hacker-${timestamp}.sqlite`);

  const db = new DatabaseSync(dbPath);
  try {
    db.exec(`VACUUM INTO '${backupPath.replace(/'/g, "''")}'`);
  } finally {
    db.close();
  }

  return backupPath;
}

/** Behält nur die `keep` neuesten Backups (nach Dateiname sortiert, der ist ISO-zeitsortierbar). */
export function pruneOldBackups(backupDir, keep) {
  if (!fs.existsSync(backupDir)) return [];
  const files = fs.readdirSync(backupDir)
    .filter((f) => f.startsWith('ue-hacker-') && f.endsWith('.sqlite'))
    .sort();

  const toDelete = files.slice(0, Math.max(0, files.length - keep));
  for (const f of toDelete) {
    fs.unlinkSync(path.join(backupDir, f));
  }
  return toDelete;
}

function isMainModule() {
  return import.meta.url === `file://${process.argv[1]}`;
}

if (isMainModule()) {
  const dataDir = process.env.DATA_DIR || path.join(__dirname, '..', '..', 'data');
  const dbPath = process.env.DB_PATH || path.join(dataDir, 'ue-hacker.sqlite');
  const backupDir = process.env.BACKUP_DIR || path.join(dataDir, 'backups');
  const keep = Number(process.env.BACKUP_KEEP) || 14;

  try {
    const backupPath = runBackup({ dbPath, backupDir });
    const deleted = pruneOldBackups(backupDir, keep);
    console.log(`Backup erstellt: ${backupPath}`);
    if (deleted.length) {
      console.log(`Alte Backups entfernt (behalte die neuesten ${keep}): ${deleted.join(', ')}`);
    }
  } catch (e) {
    console.error('Backup fehlgeschlagen:', e.message);
    process.exit(1);
  }
}
