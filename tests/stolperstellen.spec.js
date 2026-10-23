import { test, expect } from '@playwright/test';
import { ports } from '../scripts/worktree-ports.mjs';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// Stolperstellen-Zähler (api/src/routes/taskStats.js, src/composables/useTaskStats.js,
// Admin-Reiter "Stolperstellen"): anonyme Summen je Aufgabe. Läuft in test:auth (Test-API).
const API = `http://127.0.0.1:${ports.testApi}`;
const ADMIN_PASSWORD = 'test-admin-password';

async function adminHeaders(request) {
  const res = await request.post(`${API}/api/admin/login`, { data: { password: ADMIN_PASSWORD } });
  return { Authorization: `Bearer ${(await res.json()).token}` };
}

async function statsRow(request, headers, course, lesson, task) {
  const res = await request.get(`${API}/api/admin/stats/tasks`, { headers });
  expect(res.ok()).toBeTruthy();
  return (await res.json()).rows.find((r) => r.course === course && r.lesson === lesson && r.task === task);
}

const send = (request, data) => request.post(`${API}/api/stats/task`, { data });

test.describe('Stolperstellen: API', () => {
  test('zählt Ereignisse je Aufgabe, Öffnen je Lektion; Zurücksetzen löscht', async ({ request }) => {
    const headers = await adminHeaders(request);
    const course = `testkurs-${Date.now()}`;
    for (const data of [
      { lesson: 'lektion-01', task: -1, event: 'open' },
      { lesson: 'lektion-01', task: 2, event: 'fail' },
      { lesson: 'lektion-01', task: 2, event: 'fail' },
      { lesson: 'lektion-01', task: 2, event: 'solved' },
      { lesson: 'lektion-01', task: 2, event: 'skip' },
      { lesson: 'lektion-01', task: 2, event: 'solution' },
    ]) {
      expect((await send(request, { course, ...data })).status()).toBe(204);
    }
    expect(await statsRow(request, headers, course, 'lektion-01', 2)).toMatchObject({
      opens: 1, fails: 2, solved: 1, skipped: 1, solutions: 1,
    });
    // Die Lektions-Zeile (task -1) taucht nicht als eigene Aufgabe auf
    expect(await statsRow(request, headers, course, 'lektion-01', -1)).toBeUndefined();

    const del = await request.delete(`${API}/api/admin/stats/tasks?course=${course}&lesson=lektion-01&task=2`, { headers });
    expect(del.status()).toBe(204);
    expect(await statsRow(request, headers, course, 'lektion-01', 2)).toBeUndefined();
  });

  test('lehnt unbekannte Ereignisse und kaputte IDs ab; Auswertung nur für Admins', async ({ request }) => {
    for (const data of [
      { course: 'kurs', lesson: 'l1', task: 0, event: 'hack' },
      { course: '../etc', lesson: 'l1', task: 0, event: 'fail' },
      { course: 'kurs', lesson: 'l1', task: 'x', event: 'fail' },
      { course: 'kurs', lesson: 'l1', task: 0, event: 'open' },
      { course: 'kurs', lesson: 'l1', task: -1, event: 'fail' },
    ]) {
      expect((await send(request, data)).status()).toBe(400);
    }
    expect((await request.get(`${API}/api/admin/stats/tasks`)).status()).toBe(401);
  });
});

test.describe('Stolperstellen: Lektionen melden', () => {
  const COURSE = 'js-grundkurs-woche1';

  test('JS-Lektion: Öffnen, Fehlversuch und Lösen kommen anonym an, jedes nur einmal je Browser', async ({ page, request }) => {
    const headers = await adminHeaders(request);
    await request.delete(`${API}/api/admin/stats/tasks?course=${COURSE}&lesson=lektion-01`, { headers });
    await page.addInitScript(() => {
      window.__ueTaskStatsInTests = true;
      localStorage.removeItem('ue-hacker-interactive-progress-js-grundkurs-woche1');
    });
    const bodies = [];
    page.on('request', (req) => {
      if (req.url().includes('/api/stats/task')) bodies.push(req.postDataJSON());
    });

    await page.goto('/kurs/js-grundkurs?week=1');
    const task = page.locator('.task-block').nth(2);
    await expect(task).toBeVisible({ timeout: 15000 });
    await setCodeMirrorContent(task.locator('.cm-host'), 'console.log("falsch");');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await task.locator('.btn-check').click();
    await setCodeMirrorContent(task.locator('.cm-host'), 'console.log("Ich lerne JavaScript");');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect.poll(() => statsRow(request, headers, COURSE, 'lektion-01', 2)).toMatchObject({
      opens: 1, fails: 2, solved: 1, skipped: 0,
    });
    // Nur Kurs, Lektion, Aufgabe und Ereignis - kein Name, kein Code
    expect(Object.keys(bodies[0]).sort()).toEqual(['course', 'event', 'lesson', 'task']);

    // Neu laden und noch einmal lösen: Öffnen und Lösen zählen nicht doppelt
    await page.reload();
    await expect(page.locator('.task-block').nth(2)).toBeVisible({ timeout: 15000 });
    await expect.poll(() => statsRow(request, headers, COURSE, 'lektion-01', 2)).toMatchObject({ opens: 1, solved: 1 });
  });

  test('ohne Freischaltung sendet ein Testbrowser nichts (Testläufe verfälschen keine Zahlen)', async ({ page }) => {
    let sent = 0;
    page.on('request', (req) => { if (req.url().includes('/api/stats/task')) sent += 1; });
    await page.goto('/kurs/js-grundkurs?week=1');
    const task = page.locator('.task-block').nth(2);
    await expect(task).toBeVisible({ timeout: 15000 });
    await setCodeMirrorContent(task.locator('.cm-host'), 'console.log("falsch");');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    expect(sent).toBe(0);
  });

  test('Python-Lektion (Pyodide) meldet Fehlversuche ebenfalls', async ({ page, request }) => {
    const course = 'python-woche1-abenteuer';
    const headers = await adminHeaders(request);
    await request.delete(`${API}/api/admin/stats/tasks?course=${course}&lesson=lektion-01`, { headers });
    await page.addInitScript(() => { window.__ueTaskStatsInTests = true; });
    await page.goto('/kurs/python-12-wochen-grundkurs?week=1&variant=abenteuer');
    await page.locator('.btn-kernel').dispatchEvent('click');
    await expect(page.locator('.btn-kernel')).toBeDisabled({ timeout: 60000 });
    const task = page.locator('.task-block').nth(1);
    await task.locator('.code-editor').fill('print("nichts")');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 15000 });
    await expect.poll(() => statsRow(request, headers, course, 'lektion-01', 1)).toMatchObject({ opens: 1, fails: 1 });
  });
});

test.describe('Stolperstellen: Admin-Reiter', () => {
  test('zeigt die Aufgabe mit Text, die schwierigste zuerst', async ({ page, request }) => {
    const headers = await adminHeaders(request);
    const course = 'js-grundkurs-woche2';
    await request.delete(`${API}/api/admin/stats/tasks?course=${course}&lesson=lektion-01`, { headers });
    // Aufgabe 0 leicht (1 Kind, sofort gelöst), Aufgabe 1 schwer (1 Kind, 4 Fehlversuche, übersprungen)
    for (const data of [
      { task: 0, event: 'solved' },
      ...Array(4).fill({ task: 1, event: 'fail' }),
      { task: 1, event: 'skip' },
    ]) await send(request, { course, lesson: 'lektion-01', ...data });

    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    await page.locator('.admin-tab', { hasText: 'Stolperstellen' }).click();
    await page.locator('.stats-filter').fill(course);
    const rows = page.locator('[data-stats-row]');
    await expect(rows).toHaveCount(2);
    await expect(rows.first()).toHaveAttribute('data-stats-row', `${course}|lektion-01|1`);
    await expect(rows.first().locator('[data-col="fails"]')).toHaveText('4.0');
    await expect(rows.first()).toContainText('Aufgabe 2:');
  });
});
