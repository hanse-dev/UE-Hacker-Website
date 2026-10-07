import { Router } from 'express';
import bcrypt from 'bcryptjs';
import db from '../db.js';
import { createUserToken, requireUser } from '../auth.js';

const router = Router();

function publicUser(row) {
  return {
    id: row.id,
    username: row.username,
    ageGroup: row.age_group,
    mustChangePassword: Boolean(row.must_change_password),
  };
}

router.post('/login', (req, res) => {
  const username = String(req.body?.username || '').trim();
  const password = String(req.body?.password || '');

  if (!username || !password) {
    return res.status(400).json({ error: 'Username und Passwort nötig.' });
  }

  const row = db.prepare(`
    SELECT id, username, password_hash, age_group, must_change_password
    FROM users WHERE username = ? COLLATE NOCASE
  `).get(username);

  if (!row || !bcrypt.compareSync(password, row.password_hash)) {
    return res.status(401).json({ error: 'Username oder Passwort falsch.' });
  }

  return res.json({ token: createUserToken(row), user: publicUser(row) });
});

router.get('/me', requireUser, (req, res) => {
  const row = db.prepare(`
    SELECT id, username, age_group, must_change_password FROM users WHERE id = ?
  `).get(req.user.userId);
  if (!row) return res.status(401).json({ error: 'Nutzer nicht gefunden.' });
  return res.json({ user: publicUser(row) });
});

// Eigenes Passwort ändern: nur mit Login und nur, wenn das aktuelle Passwort stimmt.
// Antwortet mit einem frischen Token — alle älteren Tokens werden ungültig (requireUser).
router.post('/password', requireUser, (req, res) => {
  const currentPassword = String(req.body?.currentPassword || '');
  const newPassword = String(req.body?.newPassword || '');

  if (!currentPassword || !newPassword) {
    return res.status(400).json({ error: 'Aktuelles und neues Passwort nötig.' });
  }
  if (newPassword.length < 4 || newPassword.length > 200) {
    return res.status(400).json({ error: 'Passwort: mindestens 4 Zeichen.' });
  }

  const row = db.prepare(`
    SELECT id, username, password_hash, age_group FROM users WHERE id = ?
  `).get(req.user.userId);
  if (!row) return res.status(401).json({ error: 'Nutzer nicht gefunden.' });

  // 403 statt 401: das Token ist gültig, die Sitzung soll im Frontend bestehen bleiben.
  if (!bcrypt.compareSync(currentPassword, row.password_hash)) {
    return res.status(403).json({ error: 'Aktuelles Passwort ist falsch.' });
  }
  // Sonst ließe sich ein Einmal-Passwort einfach behalten.
  if (newPassword === currentPassword) {
    return res.status(400).json({ error: 'Das neue Passwort muss sich vom aktuellen unterscheiden.' });
  }

  const now = new Date().toISOString();
  db.prepare(`
    UPDATE users
    SET password_hash = ?, must_change_password = 0, password_changed_at = ?, updated_at = ?
    WHERE id = ?
  `).run(bcrypt.hashSync(newPassword, 10), now, now, row.id);

  return res.json({
    token: createUserToken(row),
    user: publicUser({ ...row, must_change_password: 0 }),
  });
});

router.get('/progress', requireUser, (req, res) => {
  const row = db.prepare(`
    SELECT payload, updated_at FROM progress WHERE user_id = ?
  `).get(req.user.userId);

  let payload = {};
  if (row?.payload) {
    try {
      payload = JSON.parse(row.payload);
    } catch {
      payload = {};
    }
  }

  return res.json({
    payload: payload && typeof payload === 'object' ? payload : {},
    updatedAt: row?.updated_at || null,
  });
});

router.put('/progress', requireUser, (req, res) => {
  const payload = req.body?.payload;
  if (!payload || typeof payload !== 'object' || Array.isArray(payload)) {
    return res.status(400).json({ error: 'payload muss ein Objekt sein.' });
  }

  const now = new Date().toISOString();
  const json = JSON.stringify(payload);

  const existing = db.prepare('SELECT user_id FROM progress WHERE user_id = ?').get(req.user.userId);
  if (existing) {
    db.prepare(`
      UPDATE progress SET payload = ?, updated_at = ? WHERE user_id = ?
    `).run(json, now, req.user.userId);
  } else {
    db.prepare(`
      INSERT INTO progress (user_id, payload, updated_at) VALUES (?, ?, ?)
    `).run(req.user.userId, json, now);
  }

  return res.json({ payload, updatedAt: now });
});

export default router;
