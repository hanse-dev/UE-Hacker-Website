import { test, expect } from '@playwright/test';

const API = 'http://127.0.0.1:3011';
const ADMIN_PASSWORD = 'test-admin-password';
const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

test.describe('UI: Admin + Header-Login', () => {
  test('Admin: Login, User anlegen, in Liste sehen', async ({ page, request }) => {
    const username = `ui_${Date.now()}`;

    await page.goto('/admin');
    await expect(page.locator('.admin-page h1')).toContainText(/Admin/i);

    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();

    await expect(page.locator('.admin-toolbar')).toBeVisible();
    await page.locator('.admin-toolbar .btn-primary').click();

    await expect(page.locator('.modal-card')).toBeVisible();
    await page.locator('.modal-card input').nth(0).fill(username);
    await page.locator('.modal-card select').selectOption('kinder');
    await page.locator('.modal-card input[type="password"]').fill('pass1234');
    await page.locator('.modal-card .btn-primary').click();

    await expect(page.locator('.admin-table')).toContainText(username);

    const login = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token } = await login.json();
    const listed = await request.get(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const body = await listed.json();
    expect(body.users.some((u) => u.username === username)).toBeTruthy();
  });

  test('Optionen: Anmelden, Sync, Abmelden', async ({ page, request }) => {
    const username = `learner_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await expect(page.locator('.settings-modal')).toBeVisible();
    await expect(page.locator('.settings-modal')).toContainText(/Einstellungen|Settings/);

    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();

    await expect(page.locator('.settings-modal')).toContainText(username);

    await page.evaluate(async () => {
      const key = 'ue-hacker-week-checks';
      const value = {
        version: 1,
        weeks: { 2: { passed: true, score: 1 } },
        placement: null,
      };
      localStorage.setItem(key, JSON.stringify(value));
      const meta = JSON.parse(localStorage.getItem('ue-hacker-sync-meta') || '{}');
      meta[key] = new Date().toISOString();
      localStorage.setItem('ue-hacker-sync-meta', JSON.stringify(meta));

      const token = localStorage.getItem('ue-hacker-user-token');
      const res = await fetch('/api/progress', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          payload: {
            [key]: { value, updatedAt: new Date().toISOString() },
          },
        }),
      });
      if (!res.ok) throw new Error(`put failed ${res.status}`);
    });

    const userLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const session = await userLogin.json();
    const progress = await request.get(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${session.token}` },
    });
    const body = await progress.json();
    expect(body.payload['ue-hacker-week-checks'].value.weeks['2'].passed).toBe(true);

    await page.locator('.settings-modal .auth-btn', { hasText: /Abmelden|Log out/ }).click();
    await expect(page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ })).toBeVisible();
  });

  test('Zertifikat-PDF: Download-Button erscheint erst nach Login und liefert eine PDF-Datei', async ({ page, request }) => {
    test.setTimeout(60000);
    const username = `certpdf_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() } },
        placement: null,
      }));
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);

    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    await expect(page.locator('.week-content').first()).toBeVisible({ timeout: 20000 });

    await page.locator('.fortschritt-widget-header').click();
    await page.locator('.fortschritt-weekly-header').click();

    await page.locator('#certificate-name-input').fill('Max Mustermann');

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    await expect(week1Card.locator('.certificate-login-hint')).toHaveCount(0);
    const downloadBtn = week1Card.locator('.btn-certificate-pdf');
    await expect(downloadBtn).toBeVisible();

    const downloadPromise = page.waitForEvent('download');
    await downloadBtn.click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toMatch(/^Zertifikat_Woche_1_.*\.pdf$/);
  });
});
