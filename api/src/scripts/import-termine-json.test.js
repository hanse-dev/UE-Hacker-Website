import test from 'node:test';
import assert from 'node:assert/strict';
import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { importTermine } from './import-termine-json.js';

function makeTempDb() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'import-termine-test-'));
  const db = new DatabaseSync(path.join(dir, 'test.sqlite'));
  db.exec(`
    CREATE TABLE termine (
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
    )
  `);
  return { dir, db };
}

const sample = [
  {
    date: 'Dienstag, 14.10.25', time: '17:30 - 18:30 Uhr', location: 'Übergangshaus',
    topic: 'Listen', link: '/kurs/python-12-wochen-grundkurs#woche-6', cancelled: true,
  },
  {
    date: 'Jeden Mittwoch', time: '17:00 - 18:00 Uhr', location: 'Online',
    topic: '12-Wochen-Kurs Python', link: '/kurs/python-12-wochen-grundkurs',
    recurring: true, validFrom: '2025-01-07', validUntil: null,
  },
];

test('importTermine übernimmt alle Felder inkl. cancelled/recurring', () => {
  const { dir, db } = makeTempDb();

  const result = importTermine(db, sample);
  assert.deepEqual(result, { imported: 2, skipped: 0 });

  const rows = db.prepare('SELECT * FROM termine ORDER BY id').all();
  assert.equal(rows.length, 2);
  assert.equal(rows[0].cancelled, 1);
  assert.equal(rows[1].recurring, 1);
  assert.equal(rows[1].valid_from, '2025-01-07');
  assert.equal(rows[1].valid_until, null);

  db.close();
  fs.rmSync(dir, { recursive: true, force: true });
});

test('importTermine ist idempotent (überspringt schon vorhandene date+time+topic)', () => {
  const { dir, db } = makeTempDb();

  importTermine(db, sample);
  const second = importTermine(db, sample);
  assert.deepEqual(second, { imported: 0, skipped: 2 });

  const rows = db.prepare('SELECT * FROM termine').all();
  assert.equal(rows.length, 2);

  db.close();
  fs.rmSync(dir, { recursive: true, force: true });
});
