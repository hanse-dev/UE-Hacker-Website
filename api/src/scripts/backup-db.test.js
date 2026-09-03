import test from 'node:test';
import assert from 'node:assert/strict';
import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { runBackup, pruneOldBackups } from './backup-db.js';

function makeTempDb() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'backup-db-test-'));
  const dbPath = path.join(dir, 'ue-hacker.sqlite');
  const db = new DatabaseSync(dbPath);
  db.exec('PRAGMA journal_mode = WAL');
  db.exec('CREATE TABLE users (id TEXT PRIMARY KEY, username TEXT NOT NULL)');
  db.prepare('INSERT INTO users (id, username) VALUES (?, ?)').run('u1', 'alice');
  db.close();
  return { dir, dbPath };
}

test('runBackup erstellt eine lesbare, inhaltsgleiche Kopie', () => {
  const { dir, dbPath } = makeTempDb();
  const backupDir = path.join(dir, 'backups');

  const backupPath = runBackup({ dbPath, backupDir });

  assert.ok(fs.existsSync(backupPath), 'Backup-Datei sollte existieren');

  const backupDb = new DatabaseSync(backupPath, { readOnly: true });
  const rows = backupDb.prepare('SELECT * FROM users').all();
  backupDb.close();

  assert.equal(rows.length, 1);
  assert.equal(rows[0].username, 'alice');

  fs.rmSync(dir, { recursive: true, force: true });
});

test('runBackup wirft einen Fehler, wenn die Quelldatenbank fehlt', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'backup-db-test-'));
  assert.throws(() => runBackup({
    dbPath: path.join(dir, 'does-not-exist.sqlite'),
    backupDir: path.join(dir, 'backups'),
  }));
  fs.rmSync(dir, { recursive: true, force: true });
});

test('pruneOldBackups behält nur die N neuesten Dateien', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'backup-db-test-'));
  const backupDir = path.join(dir, 'backups');
  fs.mkdirSync(backupDir);

  const names = [
    'ue-hacker-2026-01-01T00-00-00-000Z.sqlite',
    'ue-hacker-2026-01-02T00-00-00-000Z.sqlite',
    'ue-hacker-2026-01-03T00-00-00-000Z.sqlite',
    'ue-hacker-2026-01-04T00-00-00-000Z.sqlite',
  ];
  for (const name of names) {
    fs.writeFileSync(path.join(backupDir, name), 'dummy');
  }

  const deleted = pruneOldBackups(backupDir, 2);

  assert.deepEqual(deleted.sort(), names.slice(0, 2).sort());
  const remaining = fs.readdirSync(backupDir).sort();
  assert.deepEqual(remaining, names.slice(2).sort());

  fs.rmSync(dir, { recursive: true, force: true });
});

test('pruneOldBackups ignoriert fremde Dateien im Backup-Ordner', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'backup-db-test-'));
  const backupDir = path.join(dir, 'backups');
  fs.mkdirSync(backupDir);
  fs.writeFileSync(path.join(backupDir, 'ue-hacker-2026-01-01T00-00-00-000Z.sqlite'), 'dummy');
  fs.writeFileSync(path.join(backupDir, '.gitkeep'), '');
  fs.writeFileSync(path.join(backupDir, 'readme.txt'), 'hinweis');

  const deleted = pruneOldBackups(backupDir, 0);

  assert.deepEqual(deleted, ['ue-hacker-2026-01-01T00-00-00-000Z.sqlite']);
  const remaining = fs.readdirSync(backupDir).sort();
  assert.deepEqual(remaining, ['.gitkeep', 'readme.txt']);

  fs.rmSync(dir, { recursive: true, force: true });
});
