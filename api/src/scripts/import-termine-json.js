import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/**
 * Einmaliger Umzug der bisherigen public/termine.json (jetzt als Seed unter
 * termine-seed.json abgelegt) in die termine-Tabelle — seit der Admin-Termine-Verwaltung
 * ist termine.json/die Tabelle die einzige Datenquelle, nicht mehr die statische Datei.
 * Idempotent: überspringt Einträge, deren Kombination aus date+time+topic schon existiert.
 */
export function importTermine(db, entries) {
  const now = new Date().toISOString();

  const exists = db.prepare(`
    SELECT id FROM termine WHERE date = ? AND time = ? AND topic = ?
  `);
  const insert = db.prepare(`
    INSERT INTO termine (date, time, location, topic, link, cancelled, recurring, valid_from, valid_until, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);

  let imported = 0;
  let skipped = 0;
  for (const t of entries) {
    if (exists.get(t.date, t.time, t.topic)) {
      skipped += 1;
      continue;
    }
    insert.run(
      t.date, t.time, t.location, t.topic, t.link,
      t.cancelled ? 1 : 0, t.recurring ? 1 : 0,
      t.validFrom ?? null, t.validUntil ?? null,
      now, now,
    );
    imported += 1;
  }
  return { imported, skipped };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const jsonPath = process.argv[2] || path.join(__dirname, 'termine-seed.json');
  const entries = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  const { default: db } = await import('../db.js');
  const result = importTermine(db, entries);
  console.log(`Termine importiert: ${result.imported}, übersprungen (schon vorhanden): ${result.skipped}`);
}
