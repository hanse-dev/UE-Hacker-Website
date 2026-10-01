import { Router } from 'express';
import db from '../db.js';
import { requireAdmin } from '../auth.js';
import { publicTermin } from './termine.js';

const router = Router();

function validateText(value, { min = 1, max = 300 } = {}) {
  const v = String(value ?? '').trim();
  if (v.length < min || v.length > max) return null;
  return v;
}

function validateLink(value) {
  const v = String(value ?? '').trim();
  if (!v.startsWith('/') || v.length > 300) return null;
  return v;
}

function validateIsoDateOrNull(value) {
  if (value == null || value === '') return null;
  const v = String(value);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return undefined;
  return v;
}

function parseTerminInput(body, existing) {
  const date = validateText(body.date ?? existing?.date);
  const time = validateText(body.time ?? existing?.time);
  const location = validateText(body.location ?? existing?.location, { max: 300 });
  const topic = validateText(body.topic ?? existing?.topic, { max: 300 });
  const link = validateLink(body.link ?? existing?.link);
  const cancelled = Boolean(body.cancelled ?? existing?.cancelled ?? false);
  const recurring = Boolean(body.recurring ?? existing?.recurring ?? false);

  const rawValidFrom = body.validFrom !== undefined ? body.validFrom : existing?.valid_from;
  const rawValidUntil = body.validUntil !== undefined ? body.validUntil : existing?.valid_until;
  const validFrom = validateIsoDateOrNull(rawValidFrom);
  const validUntil = validateIsoDateOrNull(rawValidUntil);

  if (!date) return { error: 'Datum: 1–300 Zeichen.' };
  if (!time) return { error: 'Uhrzeit: 1–300 Zeichen.' };
  if (!location) return { error: 'Ort: 1–300 Zeichen.' };
  if (!topic) return { error: 'Thema: 1–300 Zeichen.' };
  if (!link) return { error: 'Link muss mit "/" beginnen (max. 300 Zeichen).' };
  if (validFrom === undefined) return { error: 'Gültig ab: Format JJJJ-MM-TT.' };
  if (validUntil === undefined) return { error: 'Gültig bis: Format JJJJ-MM-TT.' };
  if (recurring && !validFrom) return { error: 'Wiederkehrende Termine brauchen ein Startdatum ("Gültig ab").' };

  return {
    value: {
      date, time, location, topic, link, cancelled, recurring,
      validFrom: recurring ? validFrom : null,
      validUntil: recurring ? validUntil : null,
    },
  };
}

router.use(requireAdmin);

router.get('/termine', (_req, res) => {
  const rows = db.prepare('SELECT * FROM termine ORDER BY id').all();
  res.json({ termine: rows.map(publicTermin) });
});

router.post('/termine', (req, res) => {
  const { value, error } = parseTerminInput(req.body || {});
  if (error) return res.status(400).json({ error });

  const now = new Date().toISOString();
  const info = db.prepare(`
    INSERT INTO termine (date, time, location, topic, link, cancelled, recurring, valid_from, valid_until, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).run(
    value.date, value.time, value.location, value.topic, value.link,
    value.cancelled ? 1 : 0, value.recurring ? 1 : 0, value.validFrom, value.validUntil, now, now,
  );

  const row = db.prepare('SELECT * FROM termine WHERE id = ?').get(info.lastInsertRowid);
  return res.status(201).json({ termin: publicTermin(row) });
});

router.patch('/termine/:id', (req, res) => {
  const existing = db.prepare('SELECT * FROM termine WHERE id = ?').get(req.params.id);
  if (!existing) return res.status(404).json({ error: 'Termin nicht gefunden.' });

  const { value, error } = parseTerminInput(req.body || {}, existing);
  if (error) return res.status(400).json({ error });

  const now = new Date().toISOString();
  db.prepare(`
    UPDATE termine
    SET date = ?, time = ?, location = ?, topic = ?, link = ?, cancelled = ?, recurring = ?, valid_from = ?, valid_until = ?, updated_at = ?
    WHERE id = ?
  `).run(
    value.date, value.time, value.location, value.topic, value.link,
    value.cancelled ? 1 : 0, value.recurring ? 1 : 0, value.validFrom, value.validUntil, now, existing.id,
  );

  const row = db.prepare('SELECT * FROM termine WHERE id = ?').get(existing.id);
  return res.json({ termin: publicTermin(row) });
});

router.delete('/termine/:id', (req, res) => {
  const info = db.prepare('DELETE FROM termine WHERE id = ?').run(req.params.id);
  if (info.changes === 0) {
    return res.status(404).json({ error: 'Termin nicht gefunden.' });
  }
  return res.status(204).send();
});

export default router;
