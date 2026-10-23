import { DEV_SKIP_CHECKS } from './devSkipChecks';

/**
 * Stolperstellen-Zähler: meldet anonym, wo Teilnehmende hängen bleiben (api/src/routes/taskStats.js,
 * Admin-Reiter "Stolperstellen"). Es geht kein Name und kein Account mit, nur Kurs-Ordner,
 * Lektions-ID, Aufgaben-Nummer und das Ereignis.
 *
 * Ereignisse: open (Lektion geöffnet, task -1), fail (Prüfen ohne Erfolg), solved, skip, solution
 * (Musterlösung aufgeklappt). Pro Browser zählt jedes Ereignis einmal, Fehlversuche höchstens
 * MAX_FAILS-mal - sonst würde ein Kind, das 30-mal auf "Prüfen" klickt, eine Aufgabe allein
 * schwer aussehen lassen.
 *
 * Gesendet wird nicht im Dev-Modus "Prüfungen überspringen" und nicht aus automatisierten Browsern
 * (Playwright: `navigator.webdriver`), damit Testläufe keine Zahlen erzeugen. Ein Test schaltet es
 * mit `window.__ueTaskStatsInTests = true` gezielt ein.
 */
const SENT_KEY = 'ue-hacker-task-stats-sent';
const MAX_FAILS = 10;

function enabled() {
  if (DEV_SKIP_CHECKS || typeof window === 'undefined') return false;
  return !navigator.webdriver || window.__ueTaskStatsInTests === true;
}

function loadSent() {
  try {
    return JSON.parse(localStorage.getItem(SENT_KEY) || '{}') || {};
  } catch {
    return {};
  }
}

function saveSent(sent) {
  try {
    localStorage.setItem(SENT_KEY, JSON.stringify(sent));
  } catch {
    // Privater Modus / voller Speicher: dann wird eben öfter gezählt
  }
}

export function reportTaskEvent(course, lesson, task, event) {
  if (!enabled() || !course || !lesson) return;
  const key = `${course}|${lesson}|${task}|${event}`;
  const sent = loadSent();
  const limit = event === 'fail' ? MAX_FAILS : 1;
  if ((sent[key] || 0) >= limit) return;
  sent[key] = (sent[key] || 0) + 1;
  saveSent(sent);
  fetch('/api/stats/task', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ course, lesson, task, event }),
    keepalive: true,
  }).catch(() => {});
}

/** Eine Lektion mit mindestens einer echten (nicht Beispiel-)Aufgabe wurde geöffnet. */
export function reportLessonOpen(course, lesson) {
  if (!lesson?.id || !(lesson.tasks || []).some((task) => !task.example)) return;
  reportTaskEvent(course, lesson.id, -1, 'open');
}
