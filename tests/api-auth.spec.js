import { test, expect } from '@playwright/test';

const API = 'http://127.0.0.1:3011';
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
