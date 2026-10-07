import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { ports } from '../scripts/worktree-ports.mjs';

// Port der Auth-Test-API: im Haupt-Checkout 3011, im Worktree ein eigener (worktree.ports.json).
const API = `http://127.0.0.1:${ports.testApi}`;
const ADMIN_PASSWORD = 'test-admin-password';

async function adminToken(request) {
  const res = await request.post(`${API}/api/admin/login`, {
    data: { password: ADMIN_PASSWORD },
  });
  expect(res.ok()).toBeTruthy();
  const body = await res.json();
  expect(body.token).toBeTruthy();
  return body.token;
}

test.describe('API: Admin + Auth + Progress', () => {
  test('health', async ({ request }) => {
    const res = await request.get(`${API}/api/health`);
    expect(res.ok()).toBeTruthy();
    await expect(res.json()).resolves.toMatchObject({ ok: true });
  });

  test('Admin-Login: falsch → 401, richtig → Token', async ({ request }) => {
    const bad = await request.post(`${API}/api/admin/login`, {
      data: { password: 'wrong' },
    });
    expect(bad.status()).toBe(401);

    const good = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    expect(good.ok()).toBeTruthy();
    const body = await good.json();
    expect(body.token).toMatch(/\./);
  });

  test('User CRUD + Learner-Login + Progress Sync', async ({ request }) => {
    const token = await adminToken(request);
    const username = `kid_${Date.now()}`;

    const created = await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });
    expect(created.status()).toBe(201);
    const { user } = await created.json();
    expect(user.username).toBe(username);
    expect(user.ageGroup).toBe('kinder');

    const listed = await request.get(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const listBody = await listed.json();
    expect(listBody.users.some((u) => u.id === user.id)).toBeTruthy();

    const patched = await request.patch(`${API}/api/admin/users/${user.id}`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { ageGroup: 'jugendliche' },
    });
    expect(patched.ok()).toBeTruthy();
    expect((await patched.json()).user.ageGroup).toBe('jugendliche');

    const loginBad = await request.post(`${API}/api/login`, {
      data: { username, password: 'wrong' },
    });
    expect(loginBad.status()).toBe(401);

    const login = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(login.ok()).toBeTruthy();
    const session = await login.json();
    expect(session.token).toBeTruthy();
    expect(session.user.username).toBe(username);

    const payload = {
      'ue-hacker-week-checks': {
        value: { version: 1, weeks: { 1: { passed: true } }, placement: null },
        updatedAt: '2026-02-01T12:00:00.000Z',
      },
      'ue-hacker-notebook-state-/demo.ipynb': {
        value: { sources: ['print(1)'], outputs: {} },
        updatedAt: '2026-02-01T12:00:00.000Z',
      },
    };

    const put = await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${session.token}` },
      data: { payload },
    });
    expect(put.ok()).toBeTruthy();

    const got = await request.get(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${session.token}` },
    });
    expect(got.ok()).toBeTruthy();
    const progress = await got.json();
    expect(progress.payload['ue-hacker-week-checks'].value.weeks['1'].passed).toBe(true);
    expect(progress.payload['ue-hacker-notebook-state-/demo.ipynb'].value.sources).toEqual(['print(1)']);

    const del = await request.delete(`${API}/api/admin/users/${user.id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    expect(del.status()).toBe(204);

    const loginGone = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(loginGone.status()).toBe(401);
  });

  test('Passwort ändern: nur mit Login und richtigem aktuellen Passwort', async ({ request }) => {
    const token = await adminToken(request);
    const username = `pw_${Date.now()}`;
    const created = await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });
    expect(created.status()).toBe(201);

    const login = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const session = await login.json();
    const auth = { Authorization: `Bearer ${session.token}` };

    const noToken = await request.post(`${API}/api/password`, {
      data: { currentPassword: 'pass1234', newPassword: 'neu12345' },
    });
    expect(noToken.status()).toBe(401);

    const wrongCurrent = await request.post(`${API}/api/password`, {
      headers: auth,
      data: { currentPassword: 'falsch', newPassword: 'neu12345' },
    });
    expect(wrongCurrent.status()).toBe(403);

    const tooShort = await request.post(`${API}/api/password`, {
      headers: auth,
      data: { currentPassword: 'pass1234', newPassword: 'abc' },
    });
    expect(tooShort.status()).toBe(400);

    // Nach den abgelehnten Versuchen gilt weiter das alte Passwort.
    const stillOld = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(stillOld.ok()).toBeTruthy();

    const changed = await request.post(`${API}/api/password`, {
      headers: auth,
      data: { currentPassword: 'pass1234', newPassword: 'neu12345' },
    });
    expect(changed.status()).toBe(200);
    const changedBody = await changed.json();
    expect(changedBody.user.mustChangePassword).toBe(false);

    const oldLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(oldLogin.status()).toBe(401);

    const newLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'neu12345' },
    });
    expect(newLogin.ok()).toBeTruthy();

    // Andere Geräte werden abgemeldet: das alte Token gilt nicht mehr, das frisch ausgestellte schon.
    const oldToken = await request.get(`${API}/api/me`, { headers: auth });
    expect(oldToken.status()).toBe(401);
    const freshToken = await request.get(`${API}/api/me`, {
      headers: { Authorization: `Bearer ${changedBody.token}` },
    });
    expect(freshToken.ok()).toBeTruthy();
  });

  test('Admin setzt Passwort zurück: Einmal-Passwort, Zwangswechsel, alte Sitzung endet', async ({ request }) => {
    const token = await adminToken(request);
    const admin = { Authorization: `Bearer ${token}` };
    const username = `reset_${Date.now()}`;
    const created = await request.post(`${API}/api/admin/users`, {
      headers: admin,
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });
    const { user } = await created.json();
    expect(user.mustChangePassword).toBe(false);

    const before = await (await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    })).json();
    expect(before.user.mustChangePassword).toBe(false);

    const noAdmin = await request.post(`${API}/api/admin/users/${user.id}/reset-password`);
    expect(noAdmin.status()).toBe(401);
    const unknown = await request.post(`${API}/api/admin/users/gibt-es-nicht/reset-password`, { headers: admin });
    expect(unknown.status()).toBe(404);

    const reset = await request.post(`${API}/api/admin/users/${user.id}/reset-password`, { headers: admin });
    expect(reset.ok()).toBeTruthy();
    const resetBody = await reset.json();
    const temp = resetBody.temporaryPassword;
    expect(temp).toMatch(/^[A-Z][a-z]+-[A-Z][a-z]+-\d{2}$/);
    expect(resetBody.user.mustChangePassword).toBe(true);

    // Altes Passwort und alte Sitzung sind weg.
    const oldLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(oldLogin.status()).toBe(401);
    const oldSession = await request.get(`${API}/api/me`, {
      headers: { Authorization: `Bearer ${before.token}` },
    });
    expect(oldSession.status()).toBe(401);

    const tempLogin = await request.post(`${API}/api/login`, {
      data: { username, password: temp },
    });
    expect(tempLogin.ok()).toBeTruthy();
    const session = await tempLogin.json();
    expect(session.user.mustChangePassword).toBe(true);
    const auth = { Authorization: `Bearer ${session.token}` };
    expect((await (await request.get(`${API}/api/me`, { headers: auth })).json()).user.mustChangePassword).toBe(true);

    // Das Einmal-Passwort einfach behalten geht nicht.
    const same = await request.post(`${API}/api/password`, {
      headers: auth,
      data: { currentPassword: temp, newPassword: temp },
    });
    expect(same.status()).toBe(400);

    const changed = await request.post(`${API}/api/password`, {
      headers: auth,
      data: { currentPassword: temp, newPassword: 'meins1234' },
    });
    expect(changed.ok()).toBeTruthy();
    const fresh = await changed.json();
    const me = await request.get(`${API}/api/me`, {
      headers: { Authorization: `Bearer ${fresh.token}` },
    });
    expect((await me.json()).user.mustChangePassword).toBe(false);
  });

  test('DB-Migration: bestehende users-Tabelle bekommt die neuen Passwort-Spalten, Daten bleiben', () => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ue-hacker-migration-'));
    const dbPath = path.join(dir, 'alt.sqlite');
    const script = `
      import { DatabaseSync } from 'node:sqlite';
      const old = new DatabaseSync(process.env.DB_PATH);
      old.exec(\`CREATE TABLE users (
        id TEXT PRIMARY KEY,
        username TEXT NOT NULL UNIQUE COLLATE NOCASE,
        password_hash TEXT NOT NULL,
        age_group TEXT NOT NULL CHECK (age_group IN ('kinder', 'jugendliche')),
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
      )\`);
      old.exec("INSERT INTO users VALUES ('u1', 'alt', 'hash', 'kinder', 'x', 'x')");
      old.close();
      const { default: db } = await import('./api/src/db.js');
      console.log(JSON.stringify(db.prepare('SELECT * FROM users').all()));
    `;
    try {
      const out = execFileSync('node', ['--input-type=module', '-e', script], {
        env: { ...process.env, DB_PATH: dbPath, NODE_NO_WARNINGS: '1' },
        encoding: 'utf8',
      });
      expect(JSON.parse(out.trim().split('\n').pop())).toEqual([{
        id: 'u1',
        username: 'alt',
        password_hash: 'hash',
        age_group: 'kinder',
        created_at: 'x',
        updated_at: 'x',
        must_change_password: 0,
        password_changed_at: null,
      }]);
    } finally {
      fs.rmSync(dir, { recursive: true, force: true });
    }
  });

  test('ohne Token kein Admin/Progress', async ({ request }) => {
    const users = await request.get(`${API}/api/admin/users`);
    expect(users.status()).toBe(401);

    const progress = await request.get(`${API}/api/progress`);
    expect(progress.status()).toBe(401);
  });

  test('Termine: Admin-CRUD + öffentliche Liste ohne Login', async ({ request }) => {
    const token = await adminToken(request);
    const topic = `Testthema ${Date.now()}`;

    const noAuth = await request.get(`${API}/api/admin/termine`);
    expect(noAuth.status()).toBe(401);

    const created = await request.post(`${API}/api/admin/termine`, {
      headers: { Authorization: `Bearer ${token}` },
      data: {
        date: 'Dienstag, 14.10.26',
        time: '17:30 - 18:30 Uhr',
        location: 'Übergangshaus, Königstraße 54, 23564 Lübeck',
        topic,
        link: '/kurs/python-12-wochen-grundkurs#woche-6',
      },
    });
    expect(created.status()).toBe(201);
    const { termin } = await created.json();
    expect(termin.topic).toBe(topic);
    expect(termin.cancelled).toBe(false);

    // Ein Termin ohne Login sichtbar (öffentliche Liste, wie zuvor die statische termine.json)
    const publicList = await request.get(`${API}/api/termine`);
    expect(publicList.ok()).toBeTruthy();
    const publicTermine = await publicList.json();
    expect(publicTermine.some((t) => t.id === termin.id)).toBeTruthy();

    const patched = await request.patch(`${API}/api/admin/termine/${termin.id}`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { cancelled: true },
    });
    expect(patched.ok()).toBeTruthy();
    expect((await patched.json()).termin.cancelled).toBe(true);

    const deleted = await request.delete(`${API}/api/admin/termine/${termin.id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    expect(deleted.status()).toBe(204);

    const publicAfterDelete = await request.get(`${API}/api/termine`);
    const afterDelete = await publicAfterDelete.json();
    expect(afterDelete.some((t) => t.id === termin.id)).toBeFalsy();
  });

  test('Termine: Validierung lehnt fehlende Pflichtfelder und ungültige Links ab', async ({ request }) => {
    const token = await adminToken(request);

    const missingTopic = await request.post(`${API}/api/admin/termine`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { date: 'Montag, 01.01.27', time: '10:00 Uhr', location: 'Online', topic: '', link: '/kurs/x' },
    });
    expect(missingTopic.status()).toBe(400);

    const badLink = await request.post(`${API}/api/admin/termine`, {
      headers: { Authorization: `Bearer ${token}` },
      data: { date: 'Montag, 01.01.27', time: '10:00 Uhr', location: 'Online', topic: 'Test', link: 'kurs/x' },
    });
    expect(badLink.status()).toBe(400);

    const recurringWithoutValidFrom = await request.post(`${API}/api/admin/termine`, {
      headers: { Authorization: `Bearer ${token}` },
      data: {
        date: 'Jeden Montag', time: '10:00 Uhr', location: 'Online', topic: 'Test',
        link: '/kurs/x', recurring: true,
      },
    });
    expect(recurringWithoutValidFrom.status()).toBe(400);
  });
});
