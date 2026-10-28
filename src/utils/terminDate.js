// Termine speichern Datum und Uhrzeit als Anzeige-Text („Mittwoch, 04.11.26“, „17:00 - 18:00 Uhr“).
// Ältere Einträge wurden frei getippt, darum liest parseTerminDate auch „04.11.2026“, „4.11.“
// und ISO-Daten.

export const WEEKDAYS_DE = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];

const pad = (n) => String(n).padStart(2, '0');

export function toIso(date) {
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
}

export function parseIsoLocal(iso) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || '').trim());
  return m ? new Date(Number(m[1]), Number(m[2]) - 1, Number(m[3])) : null;
}

export function parseTerminDate(text, today = new Date()) {
  const s = String(text || '').trim();
  const iso = /(\d{4})-(\d{2})-(\d{2})/.exec(s);
  if (iso) return parseIsoLocal(iso[0]);
  const m = /(\d{1,2})\.\s*(\d{1,2})\.(?:\s*(\d{2,4}))?/.exec(s);
  if (!m) return null;
  let year = m[3] ? Number(m[3]) : today.getFullYear();
  if (year < 100) year += 2000;
  const date = new Date(year, Number(m[2]) - 1, Number(m[1]));
  return date.getDate() === Number(m[1]) ? date : null;
}

export function formatTerminDate(iso) {
  const date = parseIsoLocal(iso);
  if (!date) return '';
  return `${WEEKDAYS_DE[date.getDay()]}, ${pad(date.getDate())}.${pad(date.getMonth() + 1)}.${String(date.getFullYear()).slice(2)}`;
}

export function recurringLabel(iso) {
  const date = parseIsoLocal(iso);
  return date ? `Jeden ${WEEKDAYS_DE[date.getDay()]}` : '';
}

export function formatTerminTime(start, end) {
  return end ? `${start} - ${end} Uhr` : `${start} Uhr`;
}

export function parseTerminTime(text) {
  const m = /(\d{1,2})[:.](\d{2})(?:\s*[-–]\s*(\d{1,2})[:.](\d{2}))?/.exec(String(text || ''));
  if (!m) return null;
  return {
    start: `${pad(m[1])}:${m[2]}`,
    end: m[3] ? `${pad(m[3])}:${m[4]}` : '',
  };
}

// Nächster Mittwoch ab heute; heute selbst nur, solange 17 Uhr noch nicht vorbei ist.
export function nextWednesdayIso(now = new Date()) {
  const date = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  let diff = (3 - date.getDay() + 7) % 7;
  if (diff === 0 && now.getHours() >= 17) diff = 7;
  date.setDate(date.getDate() + diff);
  return toIso(date);
}

function startOfToday(now) {
  return new Date(now.getFullYear(), now.getMonth(), now.getDate());
}

function isRecurringActive(termin, today) {
  const from = parseIsoLocal(termin.validFrom);
  if (!from || today < from) return false;
  if (!termin.validUntil) return true;
  const until = parseIsoLocal(termin.validUntil);
  return !!until && today <= until;
}

export function terminSortDate(termin, today) {
  if (termin.recurring) return parseIsoLocal(termin.validFrom) || today;
  return parseTerminDate(termin.date, today) || today;
}

// Kommende, nicht abgesagte Termine: wiederkehrende zuerst, dann nach Datum.
export function upcomingTermine(termine, now = new Date()) {
  const today = startOfToday(now);
  return termine
    .filter((termin) => {
      if (termin.cancelled) return false;
      if (termin.recurring) return isRecurringActive(termin, today);
      const date = parseTerminDate(termin.date, today);
      return !!date && date >= today;
    })
    .sort((a, b) => {
      const aRec = a.recurring ? 0 : 1;
      const bRec = b.recurring ? 0 : 1;
      if (aRec !== bRec) return aRec - bRec;
      return terminSortDate(a, today) - terminSortDate(b, today);
    });
}
