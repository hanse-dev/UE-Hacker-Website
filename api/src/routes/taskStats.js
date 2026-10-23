import { Router } from 'express';
import db from '../db.js';
import { requireAdmin } from '../auth.js';

// Stolperstellen: anonyme Summen je Aufgabe (wie oft geöffnet, falsch geprüft, gelöst,
// übersprungen, Lösung angesehen). Kein Account, keine IP, kein Zeitstempel je Ereignis -
// gespeichert wird nur der Zähler. Das Frontend schickt jedes Ereignis pro Browser höchstens
// einmal (Fehlversuche höchstens 10-mal), siehe src/composables/useTaskStats.js.

export const EVENTS = { open: 'opens', fail: 'fails', solved: 'solved', skip: 'skipped', solution: 'solutions' };
const ID_RE = /^[a-z0-9][a-z0-9_-]{0,79}$/i;
// Obergrenze gegen Müll-Einträge (der Endpunkt ist öffentlich): so viele Aufgaben hat kein Kurs.
const MAX_ROWS = 20000;
// Einfache Bremse je IP im Speicher (nicht gespeichert). Großzügig, weil hinter einem Proxy oder
// im Schulnetz eine ganze Gruppe dieselbe IP hat: 3000 Ereignisse pro 10 Minuten.
const WINDOW_MS = 10 * 60 * 1000;
const MAX_PER_WINDOW = 3000;
const recent = new Map();

function tooMany(ip) {
  const now = Date.now();
  const entry = recent.get(ip);
  if (!entry || now - entry.start > WINDOW_MS) {
    recent.set(ip, { start: now, count: 1 });
    if (recent.size > 5000) {
      for (const [key, value] of recent) if (now - value.start > WINDOW_MS) recent.delete(key);
    }
    return false;
  }
  entry.count += 1;
  return entry.count > MAX_PER_WINDOW;
}

const publicRouter = Router();

publicRouter.post('/stats/task', (req, res) => {
  const { course, lesson, task, event } = req.body || {};
  const column = EVENTS[event];
  const taskIndex = Number(task);
  if (!column || !ID_RE.test(String(course ?? '')) || !ID_RE.test(String(lesson ?? ''))
    || !Number.isInteger(taskIndex) || taskIndex < -1 || taskIndex > 199) {
    return res.status(400).json({ error: 'Ungültiges Ereignis.' });
  }
  // Öffnen gilt für die Lektion (task -1), alles andere für eine Aufgabe.
  if ((event === 'open') !== (taskIndex === -1)) {
    return res.status(400).json({ error: 'Ungültiges Ereignis.' });
  }
  if (tooMany(req.ip)) return res.status(429).json({ error: 'Zu viele Ereignisse.' });

  const exists = db.prepare('SELECT 1 FROM task_stats WHERE course = ? AND lesson = ? AND task = ?')
    .get(course, lesson, taskIndex);
  if (!exists && db.prepare('SELECT COUNT(*) AS n FROM task_stats').get().n >= MAX_ROWS) {
    return res.status(204).end();
  }
  db.prepare(`
    INSERT INTO task_stats (course, lesson, task, ${column}, updated_at) VALUES (?, ?, ?, 1, ?)
    ON CONFLICT (course, lesson, task) DO UPDATE SET ${column} = ${column} + 1, updated_at = excluded.updated_at
  `).run(course, lesson, taskIndex, new Date().toISOString());
  return res.status(204).end();
});

const adminRouter = Router();
adminRouter.use(requireAdmin);

// Je Aufgabe eine Zeile; `opens` kommt aus der Lektions-Zeile (task -1).
adminRouter.get('/stats/tasks', (_req, res) => {
  const rows = db.prepare(`
    SELECT t.course, t.lesson, t.task, t.fails, t.solved, t.skipped, t.solutions, t.updated_at AS updatedAt,
           COALESCE(l.opens, 0) AS opens
    FROM task_stats t
    LEFT JOIN task_stats l ON l.course = t.course AND l.lesson = t.lesson AND l.task = -1
    WHERE t.task >= 0
  `).all();
  res.json({ rows });
});

// Nach einer Überarbeitung neu messen: einzelne Aufgabe oder ganze Lektion (ohne task) zurücksetzen.
adminRouter.delete('/stats/tasks', (req, res) => {
  const { course, lesson, task } = req.query;
  if (!ID_RE.test(String(course ?? '')) || !ID_RE.test(String(lesson ?? ''))) {
    return res.status(400).json({ error: 'Kurs und Lektion angeben.' });
  }
  if (task === undefined) {
    db.prepare('DELETE FROM task_stats WHERE course = ? AND lesson = ?').run(course, lesson);
  } else {
    db.prepare('DELETE FROM task_stats WHERE course = ? AND lesson = ? AND task = ?').run(course, lesson, Number(task));
  }
  return res.status(204).end();
});

export { publicRouter as taskStatsPublicRouter, adminRouter as taskStatsAdminRouter };
