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
});
