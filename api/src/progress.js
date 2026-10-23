import db from './db.js';

// Der Fortschritt eines Accounts ist ein JSON-Objekt { storageKey: { value, updatedAt } } in der
// Tabelle `progress` (dieselben Keys wie im localStorage des Browsers, siehe useProgressSync.js).

export function readProgressPayload(userId) {
  const row = db.prepare('SELECT payload FROM progress WHERE user_id = ?').get(userId);
  if (!row?.payload) return {};
  try {
    const payload = JSON.parse(row.payload);
    return payload && typeof payload === 'object' && !Array.isArray(payload) ? payload : {};
  } catch {
    return {};
  }
}

// Schreibt einzelne Einträge in den Fortschritt, alle anderen Keys bleiben unberührt. PUT
// /api/progress ersetzt dagegen den ganzen Stand - für "nur diesen einen Kurs bei einem zweiten
// Account mitschreiben" (Partnerarbeit, Admin-Gutschrift) wäre das ein Rennen gegen dessen Geräte.
export function mergeProgressEntries(userId, entries) {
  // Lesen und Schreiben laufen synchron hintereinander (node:sqlite) - dazwischen kommt in diesem
  // Prozess keine andere Anfrage zum Zug.
  const now = new Date().toISOString();
  const payload = readProgressPayload(userId);
  for (const [key, entry] of Object.entries(entries)) {
    payload[key] = { value: entry.value, updatedAt: entry.updatedAt || now };
  }
  const json = JSON.stringify(payload);
  const existing = db.prepare('SELECT user_id FROM progress WHERE user_id = ?').get(userId);
  if (existing) {
    db.prepare('UPDATE progress SET payload = ?, updated_at = ? WHERE user_id = ?').run(json, now, userId);
  } else {
    db.prepare('INSERT INTO progress (user_id, payload, updated_at) VALUES (?, ?, ?)').run(userId, json, now);
  }
  return { payload, updatedAt: now };
}
