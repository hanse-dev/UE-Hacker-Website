/**
 * Lokaler Zwischenspeicher fuer den selbst geschriebenen Code in Lektionen (LessonView.vue).
 *
 * Bewusst NUR im Browser (localStorage) und NICHT mit dem Account synchronisiert - der Key liegt
 * ausserhalb des Sync-Praefixes `ue-hacker-interactive-progress-`. Wer den Code mitnehmen will,
 * nutzt den Fortschritts-Export. Eintraege verfallen nach 5 Tagen ohne Aenderung: danach steht
 * wieder die Vorlage im Editor.
 */
export const SAVED_CODE_TTL_MS = 5 * 24 * 60 * 60 * 1000;

const storageKey = (contentPath) => `ue-hacker-lesson-code-${contentPath}`;

/** Liest alle noch gueltigen Eintraege { lessonId: { savedAt, codes } }; abgelaufene werden verworfen. */
export function loadSavedCode(contentPath, now = Date.now()) {
  try {
    const raw = localStorage.getItem(storageKey(contentPath));
    if (!raw) return {};
    const all = JSON.parse(raw);
    const valid = {};
    for (const [lessonId, entry] of Object.entries(all || {})) {
      if (entry && Array.isArray(entry.codes) && now - entry.savedAt < SAVED_CODE_TTL_MS) {
        valid[lessonId] = entry;
      }
    }
    if (Object.keys(valid).length !== Object.keys(all || {}).length) writeAll(contentPath, valid);
    return valid;
  } catch {
    return {};
  }
}

function writeAll(contentPath, all) {
  try {
    if (Object.keys(all).length) localStorage.setItem(storageKey(contentPath), JSON.stringify(all));
    else localStorage.removeItem(storageKey(contentPath));
  } catch (e) {
    console.error('Code konnte nicht zwischengespeichert werden:', e);
  }
}

/** Speichert den Code einer Lektion; entspricht er den Vorlagen, wird der Eintrag entfernt. */
export function saveLessonCode(contentPath, lessonId, codes, templates, now = Date.now()) {
  const all = loadSavedCode(contentPath, now);
  const untouched = codes.every((c, i) => c === (templates[i] ?? ''));
  if (untouched) delete all[lessonId];
  else all[lessonId] = { savedAt: now, codes: [...codes] };
  writeAll(contentPath, all);
}

/** Fuer den Export: alle gueltigen Eintraege. */
export const exportSavedCode = (contentPath) => loadSavedCode(contentPath);

/** Fuer den Import: uebernimmt Eintraege (Zeitstempel wird auf jetzt gesetzt) ohne vorhandenen neueren Code zu ueberschreiben. */
export function importSavedCode(contentPath, incoming, now = Date.now()) {
  if (!incoming || typeof incoming !== 'object') return;
  const all = loadSavedCode(contentPath, now);
  for (const [lessonId, entry] of Object.entries(incoming)) {
    if (!all[lessonId] && entry && Array.isArray(entry.codes)) all[lessonId] = { savedAt: now, codes: entry.codes };
  }
  writeAll(contentPath, all);
}

/**
 * „Meine Seite“ (Web-Kurse): die eigene Website, die über alle Lektionen eines Kurses mitwächst.
 * Aufgaben mit `"meineSeite": true` in lessons.json starten mit diesem Stand statt mit ihrer
 * Vorlage und speichern jede Änderung zurück. Anders als der Lektions-Zwischenspeicher oben verfällt
 * sie NICHT - es ist ein Projekt über Wochen. Ebenfalls nur lokal (kein Sync-Präfix); mitnehmen
 * lässt sie sich über „Seite herunterladen“.
 */
const meineSeiteKey = (contentPath) => `ue-hacker-meine-seite-${contentPath}`;

export function loadMeineSeite(contentPath) {
  try {
    const raw = localStorage.getItem(meineSeiteKey(contentPath));
    if (!raw) return null;
    const entry = JSON.parse(raw);
    return typeof entry?.code === 'string' && entry.code.trim() ? entry.code : null;
  } catch {
    return null;
  }
}

export function saveMeineSeite(contentPath, code, now = Date.now()) {
  try {
    localStorage.setItem(meineSeiteKey(contentPath), JSON.stringify({ savedAt: now, code }));
  } catch (e) {
    console.error('Meine Seite konnte nicht gespeichert werden:', e);
  }
}
