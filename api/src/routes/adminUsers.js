import { Router } from 'express';
import bcrypt from 'bcryptjs';
import crypto from 'crypto';
import db from '../db.js';
import { requireAdmin } from '../auth.js';

const router = Router();
const AGE_GROUPS = new Set(['kinder', 'jugendliche']);

function publicUser(row) {
  return {
    id: row.id,
    username: row.username,
    ageGroup: row.age_group,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
}

function validateUsername(username) {
  const u = String(username || '').trim();
  if (u.length < 2 || u.length > 40) return null;
  if (!/^[a-zA-Z0-9._-]+$/.test(u)) return null;
  return u;
}

function validatePassword(password) {
  const p = String(password || '');
  if (p.length < 4 || p.length > 200) return null;
  return p;
}

router.use(requireAdmin);

router.get('/users', (_req, res) => {
  const rows = db.prepare(`
    SELECT id, username, age_group, created_at, updated_at
    FROM users
    ORDER BY username COLLATE NOCASE
  `).all();
  res.json({ users: rows.map(publicUser) });
});

router.post('/users', (req, res) => {
  const username = validateUsername(req.body?.username);
  const password = validatePassword(req.body?.password);
  const ageGroup = String(req.body?.ageGroup || '');

  if (!username) {
    return res.status(400).json({ error: 'Username: 2–40 Zeichen, nur Buchstaben/Zahlen/._-' });
  }
  if (!password) {
    return res.status(400).json({ error: 'Passwort: mindestens 4 Zeichen.' });
  }
  if (!AGE_GROUPS.has(ageGroup)) {
    return res.status(400).json({ error: 'ageGroup muss kinder oder jugendliche sein.' });
  }

  const existing = db.prepare('SELECT id FROM users WHERE username = ? COLLATE NOCASE').get(username);
  if (existing) {
    return res.status(409).json({ error: 'Username ist schon vergeben.' });
  }

  const now = new Date().toISOString();
  const id = crypto.randomUUID();
  const passwordHash = bcrypt.hashSync(password, 10);

  db.prepare(`
    INSERT INTO users (id, username, password_hash, age_group, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?)
  `).run(id, username, passwordHash, ageGroup, now, now);

  db.prepare(`
    INSERT INTO progress (user_id, payload, updated_at) VALUES (?, '{}', ?)
  `).run(id, now);

  const row = db.prepare(`
    SELECT id, username, age_group, created_at, updated_at FROM users WHERE id = ?
  `).get(id);

  return res.status(201).json({ user: publicUser(row) });
});

router.patch('/users/:id', (req, res) => {
  const row = db.prepare('SELECT * FROM users WHERE id = ?').get(req.params.id);
  if (!row) return res.status(404).json({ error: 'Nutzer nicht gefunden.' });

  let username = row.username;
  let ageGroup = row.age_group;
  let passwordHash = row.password_hash;

  if (req.body?.username != null) {
    const next = validateUsername(req.body.username);
    if (!next) {
      return res.status(400).json({ error: 'Username: 2–40 Zeichen, nur Buchstaben/Zahlen/._-' });
    }
    const clash = db.prepare(`
      SELECT id FROM users WHERE username = ? COLLATE NOCASE AND id != ?
    `).get(next, row.id);
    if (clash) return res.status(409).json({ error: 'Username ist schon vergeben.' });
    username = next;
  }

  if (req.body?.ageGroup != null) {
    const next = String(req.body.ageGroup);
    if (!AGE_GROUPS.has(next)) {
      return res.status(400).json({ error: 'ageGroup muss kinder oder jugendliche sein.' });
    }
    ageGroup = next;
  }

  if (req.body?.password != null && req.body.password !== '') {
    const next = validatePassword(req.body.password);
    if (!next) {
      return res.status(400).json({ error: 'Passwort: mindestens 4 Zeichen.' });
    }
    passwordHash = bcrypt.hashSync(next, 10);
  }

  const now = new Date().toISOString();
  db.prepare(`
    UPDATE users
    SET username = ?, password_hash = ?, age_group = ?, updated_at = ?
    WHERE id = ?
  `).run(username, passwordHash, ageGroup, now, row.id);

  const updated = db.prepare(`
    SELECT id, username, age_group, created_at, updated_at FROM users WHERE id = ?
  `).get(row.id);

  return res.json({ user: publicUser(updated) });
});

router.delete('/users/:id', (req, res) => {
  const info = db.prepare('DELETE FROM users WHERE id = ?').run(req.params.id);
  if (info.changes === 0) {
    return res.status(404).json({ error: 'Nutzer nicht gefunden.' });
  }
  return res.status(204).send();
});

export default router;
