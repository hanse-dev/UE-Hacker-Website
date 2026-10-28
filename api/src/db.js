import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dataDir = process.env.DATA_DIR || path.join(__dirname, '..', 'data');
const dbPath = process.env.DB_PATH || path.join(dataDir, 'ue-hacker.sqlite');

fs.mkdirSync(path.dirname(dbPath), { recursive: true });

const db = new DatabaseSync(dbPath);
db.exec('PRAGMA journal_mode = WAL');
db.exec('PRAGMA foreign_keys = ON');

const hadTerminOrte = !!db.prepare("SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'termin_orte'").get();

db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    age_group TEXT NOT NULL CHECK (age_group IN ('kinder', 'jugendliche')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    must_change_password INTEGER NOT NULL DEFAULT 0,
    password_changed_at TEXT
  );

  CREATE TABLE IF NOT EXISTS progress (
    user_id TEXT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    payload TEXT NOT NULL DEFAULT '{}',
    updated_at TEXT NOT NULL
  );

  CREATE TABLE IF NOT EXISTS termine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    location TEXT NOT NULL,
    topic TEXT NOT NULL,
    link TEXT NOT NULL,
    cancelled INTEGER NOT NULL DEFAULT 0,
    recurring INTEGER NOT NULL DEFAULT 0,
    valid_from TEXT,
    valid_until TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
  );

  -- Orte zur Auswahl im Termin-Formular (routes/adminTermine.js)
  CREATE TABLE IF NOT EXISTS termin_orte (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
  );

  -- Stolperstellen: anonyme Zähler je Aufgabe (routes/taskStats.js); task -1 = Lektion geöffnet
  CREATE TABLE IF NOT EXISTS task_stats (
    course TEXT NOT NULL,
    lesson TEXT NOT NULL,
    task INTEGER NOT NULL,
    opens INTEGER NOT NULL DEFAULT 0,
    fails INTEGER NOT NULL DEFAULT 0,
    solved INTEGER NOT NULL DEFAULT 0,
    skipped INTEGER NOT NULL DEFAULT 0,
    solutions INTEGER NOT NULL DEFAULT 0,
    updated_at TEXT NOT NULL,
    PRIMARY KEY (course, lesson, task)
  );
`);

// Migrationen für Datenbanken, die vor der jeweiligen Spalte angelegt wurden
// (CREATE TABLE IF NOT EXISTS ergänzt bestehende Tabellen nicht).
const userColumns = new Set(db.prepare('PRAGMA table_info(users)').all().map((c) => c.name));
if (!userColumns.has('must_change_password')) {
  db.exec('ALTER TABLE users ADD COLUMN must_change_password INTEGER NOT NULL DEFAULT 0');
}
if (!userColumns.has('password_changed_at')) {
  db.exec('ALTER TABLE users ADD COLUMN password_changed_at TEXT');
}
// Nur beim Anlegen füllen: Ein später gelöschter Ort soll nicht beim nächsten Start zurückkommen.
if (!hadTerminOrte) {
  db.prepare(`
    INSERT OR IGNORE INTO termin_orte (name, created_at)
    SELECT DISTINCT location, ? FROM termine
  `).run(new Date().toISOString());
}

export default db;
