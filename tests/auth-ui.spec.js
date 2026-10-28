import { test, expect } from '@playwright/test';
import { ports } from '../scripts/worktree-ports.mjs';

// Port der Auth-Test-API: im Haupt-Checkout 3011, im Worktree ein eigener (worktree.ports.json).
const API = `http://127.0.0.1:${ports.testApi}`;
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

    // Nav-Link "Admin" erscheint nach Admin-Login und bleibt beim Navigieren sichtbar
    const adminNavLink = page.locator('nav a[href="/admin"]');
    await expect(adminNavLink).toBeVisible();
    await page.goto('/');
    await expect(adminNavLink).toBeVisible();
    await adminNavLink.click();
    await expect(page).toHaveURL(/\/admin$/);

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

    // Nav-Link verschwindet nach Admin-Logout wieder
    await page.locator('.admin-toolbar .btn-secondary').click();
    await expect(adminNavLink).toHaveCount(0);
  });

  test('Admin: Reiter Kurse listet nicht verlinkte Kurse zuerst, mit Beta-Kennzeichnung und Link', async ({ page }) => {
    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    await page.locator('.admin-tab', { hasText: /Kurse|Courses/ }).click();

    const rows = page.locator('.admin-kurse tbody tr');
    // Nicht verlinkt ist nur die micro:bit-Einführung (erreichbar über den Kasten in jedem micro:bit-Kurs).
    await expect(rows.first()).toHaveAttribute('data-kurs', 'projekt-microbit-einfuehrung');
    await expect(rows.first().locator('.badge-unlisted')).toBeVisible();
    await expect(rows.first().locator('.beta-badge')).toBeVisible();
    await expect(rows.first().locator('a')).toHaveAttribute('href', '/kurs/projekt-microbit-einfuehrung');
    await expect(page.locator('.admin-kurse .badge-unlisted')).toHaveCount(1);

    const auto = page.locator('.admin-kurse tr[data-kurs="projekt-microbit-auto"]');
    await expect(auto.locator('.badge-unlisted')).toHaveCount(0);
    await expect(auto.locator('.beta-badge')).toHaveCount(0);
    await expect(page.locator('.admin-kurse tr[data-kurs="ki-labor"] .beta-badge')).toBeVisible();
  });

  test('Admin: Termin über die Termine-Verwaltung anlegen, bearbeiten und löschen', async ({ page, request }) => {
    const topic = `UI-Testtermin ${Date.now()}`;

    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    await expect(page.locator('.admin-tabs')).toBeVisible();

    await page.locator('.admin-tab', { hasText: /Termine|Appointments/ }).click();
    await page.locator('.admin-termine .btn-primary').click();

    await expect(page.locator('.modal-card')).toBeVisible();
    await page.locator('.modal-card .termin-auswahl').selectOption('python-12-wochen-grundkurs');
    await page.locator('.modal-card .termin-woche').selectOption('8');
    await expect(page.locator('.modal-card .termin-topic')).toHaveValue('Woche 8: Dictionaries & Tupel');
    await page.locator('.modal-card .termin-topic').fill(topic);
    await page.locator('.modal-card .termin-datum').fill('2027-02-03');
    await page.locator('.modal-card .termin-ort').selectOption('__neu');
    const ort = `Testort ${Date.now()}`;
    await page.locator('.modal-card .termin-neuer-ort').fill(ort);
    await expect(page.locator('.modal-card .termin-preview')).toHaveText(`Mittwoch, 03.02.27 · 17:00 - 18:00 Uhr · ${ort}`);
    await page.locator('.modal-card .btn-primary').click();

    await expect(page.locator('.admin-termine .admin-table')).toContainText(topic);

    // Der neue Termin ist auch öffentlich sichtbar, ganz ohne Admin-Login.
    const publicList = await request.get(`${API}/api/termine`);
    const publicTermine = await publicList.json();
    const saved = publicTermine.find((t) => t.topic === topic);
    expect(saved).toMatchObject({
      date: 'Mittwoch, 03.02.27',
      time: '17:00 - 18:00 Uhr',
      location: ort,
      link: '/kurs/python-12-wochen-grundkurs#woche-8',
    });

    // Bearbeiten: Thema, Woche und Ort bleiben stehen; als abgesagt markieren
    const row = page.locator('.admin-termine .admin-table tr', { hasText: topic });
    await row.locator('.btn-link').first().click();
    await expect(page.locator('.modal-card')).toBeVisible();
    await expect(page.locator('.modal-card .termin-topic')).toHaveValue(topic);
    await expect(page.locator('.modal-card .termin-woche')).toHaveValue('8');
    await expect(page.locator('.modal-card .termin-ort')).toHaveValue(ort);
    await page.locator('.modal-card .termin-cancelled').check();
    await page.locator('.modal-card .btn-primary').click();
    await expect(row.locator('.badge-cancelled')).toBeVisible();

    // Neuer Termin: Vorgaben Mittwoch 17–18 Uhr, der neue Ort steht zur Auswahl und lässt sich entfernen
    await page.locator('.admin-termine .btn-primary').click();
    await expect(page.locator('.modal-card .termin-start')).toHaveValue('17:00');
    await expect(page.locator('.modal-card .termin-end')).toHaveValue('18:00');
    const datum = await page.locator('.modal-card .termin-datum').inputValue();
    expect(new Date(`${datum}T12:00:00`).getDay()).toBe(3);
    await page.locator('.modal-card .termin-ort').selectOption(ort);
    page.once('dialog', (dialog) => dialog.accept());
    await page.locator('.modal-card .termin-ort-entfernen').click();
    await expect(page.locator('.modal-card .termin-ort option', { hasText: ort })).toHaveCount(0);
    await page.locator('.modal-card .btn-secondary').click();

    // Löschen
    page.once('dialog', (dialog) => dialog.accept());
    await row.locator('.btn-link.danger').click();
    await expect(page.locator('.admin-termine')).not.toContainText(topic);
  });

  test('Admin: Neuer Termin schlägt die nächste Kurswoche vor, sonst eine offene Werkstatt', async ({ page }) => {
    const ort = 'Übergangshaus, Königstraße 54, 23564 Lübeck';
    let liste = [
      { id: 1, date: 'Mittwoch, 07.10.26', time: '17:00 - 18:00 Uhr', location: 'Online', topic: 'Alt', link: '/kurs/python-12-wochen-grundkurs#woche-2', cancelled: false, recurring: false },
      { id: 2, date: 'Mittwoch, 14.10.26', time: '17:00 - 18:00 Uhr', location: ort, topic: 'Neu', link: '/kurs/python-12-wochen-grundkurs#woche-8', cancelled: false, recurring: false },
    ];
    await page.route('**/api/admin/termine', (route) => (route.request().method() === 'GET'
      ? route.fulfill({ json: { termine: liste } })
      : route.fallback()));

    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    await page.locator('.admin-tab', { hasText: /Termine|Appointments/ }).click();

    await page.locator('.admin-termine .btn-primary').click();
    await expect(page.locator('.modal-card .termin-auswahl')).toHaveValue('python-12-wochen-grundkurs');
    await expect(page.locator('.modal-card .termin-woche')).toHaveValue('9');
    await expect(page.locator('.modal-card .termin-topic')).toHaveValue('Woche 9: Dateien & I/O');
    await expect(page.locator('.modal-card .termin-vorschlag')).toBeVisible();
    // Zuletzt genutzter Ort ist vorausgewählt (oder als neuer Ort vorausgefüllt, falls nicht gespeichert)
    const ortWert = await page.locator('.modal-card .termin-ort').inputValue();
    if (ortWert === '__neu') await expect(page.locator('.modal-card .termin-neuer-ort')).toHaveValue(ort);
    else expect(ortWert).toBe(ort);
    await page.locator('.modal-card .btn-secondary').click();

    // Ohne laufenden Kurs: offene Werkstatt
    liste = [{ ...liste[0], id: 3, link: '/kurs/ferienkurse', topic: 'Ferien' }];
    await page.reload();
    await page.locator('.admin-tab', { hasText: /Termine|Appointments/ }).click();
    await page.locator('.admin-termine .btn-primary').click();
    await expect(page.locator('.modal-card .termin-auswahl')).toHaveValue('__werkstatt');
    await expect(page.locator('.modal-card .termin-topic')).toHaveValue(/Offene Werkstatt/);
    await expect(page.locator('.modal-card .termin-woche')).toHaveCount(0);
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

  test('Optionen: eingeloggt das eigene Passwort ändern', async ({ page, request }) => {
    const username = `pwui_${Date.now()}`;
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
    const modal = page.locator('.settings-modal');

    // Ohne Login gibt es die Funktion nicht.
    await expect(modal.locator('.change-password-btn')).toHaveCount(0);

    await modal.locator('.auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await modal.locator('input').nth(0).fill(username);
    await modal.locator('input[type="password"]').fill('pass1234');
    await modal.locator('.auth-btn.primary').click();
    await expect(modal).toContainText(username);

    await modal.locator('.change-password-btn').click();
    const form = modal.locator('.password-form');
    await expect(form).toBeVisible();

    // Wiederholung stimmt nicht → Hinweis, nichts wird geändert.
    await form.locator('input[name="current-password"]').fill('pass1234');
    await form.locator('input[name="new-password"]').fill('neu12345');
    await form.locator('input[name="new-password-repeat"]').fill('neu99999');
    await form.locator('.auth-btn.primary').click();
    await expect(form.locator('.login-error')).toContainText(/stimmen nicht überein|do not match/);

    // Falsches aktuelles Passwort → Fehler vom Server, Sitzung bleibt bestehen.
    await form.locator('input[name="current-password"]').fill('falsch');
    await form.locator('input[name="new-password-repeat"]').fill('neu12345');
    await form.locator('.auth-btn.primary').click();
    await expect(form.locator('.login-error')).toContainText('Aktuelles Passwort ist falsch');

    await form.locator('input[name="current-password"]').fill('pass1234');
    await form.locator('.auth-btn.primary').click();
    await expect(form).toHaveCount(0);
    await expect(modal.locator('.login-success')).toContainText(/Passwort geändert|Password changed/);
    await expect(modal).toContainText(username);

    const oldLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    expect(oldLogin.status()).toBe(401);
    const newLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'neu12345' },
    });
    expect(newLogin.ok()).toBeTruthy();
  });

  test('Admin setzt Passwort zurück → Login mit Einmal-Passwort erzwingt ein neues Passwort', async ({ page, request }) => {
    const username = `resetui_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });

    // Admin-Panel: zurücksetzen, Einmal-Passwort wird angezeigt.
    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    const row = page.locator('.admin-table tr', { hasText: username });
    await expect(row).toBeVisible();
    page.once('dialog', (dialog) => dialog.accept());
    await row.locator('.reset-password-btn').click();
    const tempLocator = page.locator('.reset-result .temp-password');
    await expect(tempLocator).toHaveText(/^[A-Z][a-z]+-[A-Z][a-z]+-\d{2}$/);
    const temp = (await tempLocator.textContent()).trim();
    await expect(row.locator('.must-change-badge')).toBeVisible();
    await page.locator('.admin-toolbar .btn-secondary').click();

    // Login mit dem Einmal-Passwort: das Formular erscheint von selbst und lässt sich nicht schließen.
    await page.goto('/');
    await page.locator('.options-btn').click();
    const modal = page.locator('.settings-modal');
    await modal.locator('.auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await modal.locator('input').nth(0).fill(username);
    await modal.locator('input[type="password"]').fill(temp);
    await modal.locator('.auth-btn.primary').click();

    const form = modal.locator('.password-form');
    await expect(form).toBeVisible();
    await expect(form).toContainText(/Einmal-Passwort|one-time password/);
    // Gerade eben eingegeben → wird nicht nochmal abgefragt.
    await expect(form.locator('input[name="current-password"]')).toHaveCount(0);
    await expect(modal.locator('.settings-close')).toHaveCount(0);
    await page.locator('.login-backdrop').click({ position: { x: 5, y: 5 } });
    await expect(form).toBeVisible();

    // Auch ein Seiten-Reload führt nicht daran vorbei; dann wird das aktuelle Passwort abgefragt.
    await page.reload();
    await expect(form).toBeVisible();
    await expect(modal.locator('.settings-close')).toHaveCount(0);
    await form.locator('input[name="current-password"]').fill(temp);
    await form.locator('input[name="new-password"]').fill('meins1234');
    await form.locator('input[name="new-password-repeat"]').fill('meins1234');
    await form.locator('.auth-btn.primary').click();

    await expect(form).toHaveCount(0);
    await expect(modal.locator('.login-success')).toBeVisible();
    await modal.locator('.settings-close').click();
    await expect(modal).toHaveCount(0);

    // Sitzung läuft mit dem neuen Token weiter, Reload erzwingt nichts mehr.
    await page.reload();
    await expect(page.locator('.options-btn')).toBeVisible();
    await expect(modal).toHaveCount(0);
    await page.locator('.options-btn').click();
    await expect(modal).toContainText(username);

    const tempLogin = await request.post(`${API}/api/login`, {
      data: { username, password: temp },
    });
    expect(tempLogin.status()).toBe(401);
    const newLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'meins1234' },
    });
    expect(newLogin.ok()).toBeTruthy();
    expect((await newLogin.json()).user.mustChangePassword).toBe(false);
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

    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.certificates-link')).toBeVisible({ timeout: 20000 });
    await page.locator('.certificates-link').click();

    await page.locator('#certificate-name-input').fill('Max Mustermann');

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    await expect(week1Card.locator('.certificate-login-hint')).toHaveCount(0);
    const downloadBtn = week1Card.locator('.btn-certificate-pdf');
    await expect(downloadBtn).toBeVisible();

    const downloadPromise = page.waitForEvent('download');
    await downloadBtn.click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toMatch(/^Zertifikat_Woche_1_Max_Mustermann\.pdf$/);
  });

  test('Zertifikat-PDF für einen Kurs mit Abschluss-Check: „Abschluss“ statt „Woche 1“, Dateiname mit Kursname', async ({ page, request }) => {
    test.setTimeout(60000);
    const username = `certweb_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });

    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-week-checks-web-erste-website', JSON.stringify({
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

    // Profil: eigener Block für den Kurs, Kachel heißt „Abschluss“.
    await page.goto('/profil');
    const block = page.locator('.cert-course-block').filter({ has: page.locator('.cert-course-title', { hasText: /^Meine erste Website \d/ }) });
    await expect(block).toBeVisible({ timeout: 20000 });
    const card = block.locator('.badge-card');
    await expect(card).toHaveClass(/earned/);
    await expect(card.locator('.badge-title')).toHaveText('Abschluss');

    // Kursseite: Zertifikat-Box nach dem Check mit Download.
    await page.goto('/kurs/web-erste-website?week=1');
    const reveal = page.locator('.certificate-reveal');
    await expect(reveal).toBeVisible({ timeout: 20000 });
    await reveal.locator('input').fill('Max Mustermann');
    const downloadPromise = page.waitForEvent('download');
    await reveal.locator('.btn-certificate-pdf').click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toBe('Zertifikat_Meine_erste_Website_Max_Mustermann.pdf');
  });

  test('Zertifikat-PDF: eine andere Woche als Woche 1 lädt auch ihre eigenen Daten', async ({ page, request }) => {
    test.setTimeout(60000);
    const username = `certpdf5_${Date.now()}`;
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
        weeks: {
          '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() },
          '5': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() },
        },
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

    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.certificates-link')).toBeVisible({ timeout: 20000 });
    await page.locator('.certificates-link').click();

    const week5Card = page.locator('.certificate-card').nth(4);
    await expect(week5Card).toHaveClass(/earned/);
    const downloadPromise = page.waitForEvent('download');
    await week5Card.locator('.btn-certificate-pdf').click();
    const download = await downloadPromise;
    // Guards against an off-by-one in FortschrittWidget's week→content lookup: this must be
    // week 5's certificate, not week 1's (the first earned week) reused for every button.
    expect(download.suggestedFilename()).toMatch(/^Zertifikat_Woche_5_/);
  });

  test('Zertifikat-PDF: funktioniert auch auf Englisch (Titel/Lernziele enthalten Emoji, das die PDF-Schrift nicht kennt)', async ({ page, request }) => {
    test.setTimeout(60000);
    const username = `certpdfen_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-lang', 'en');
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() } },
        placement: null,
      }));
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);

    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.certificates-link')).toBeVisible({ timeout: 20000 });
    await page.locator('.certificates-link').click();

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    const downloadPromise = page.waitForEvent('download');
    await week1Card.locator('.btn-certificate-pdf').click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toMatch(/^Certificate_Week_1_/);
  });

  test('Mein Profil: Abschluss-Abzeichen erscheint nach vollständigem Projekt-Kurs', async ({ page, request }) => {
    // Nicht verlinkt ist nur die micro:bit-Einfuehrung - fuer die Pruefung am Ende das Roboterauto so markieren.
    await page.route('**/kurse.json', async (route) => {
      const response = await route.fetch();
      const kurse = await response.json();
      kurse.find((k) => k.id === 'projekt-microbit-auto').unlisted = true;
      await route.fulfill({ response, json: kurse });
    });
    // Der Account-Fortschritt kommt erst an, wenn das Profil schon offen ist - die Abzeichen
    // muessen dann nachziehen statt auf dem Stand vom Laden der Seite zu bleiben.
    await page.route('**/api/progress', async (route) => {
      if (route.request().method() === 'GET') await new Promise((resolve) => setTimeout(resolve, 1500));
      await route.continue();
    });
    const username = `profil_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    // Fortschritt liegt bereits auf dem Account (Server), nicht nur lokal vor dem Login — seit
    // dem Login-Reset (Account-Stand ersetzt lokale Vor-Login-Daten statt sie zu mergen) würde
    // rein lokaler Vor-Login-Fortschritt beim Login sonst verworfen statt übernommen.
    const userLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const { token: userToken } = await userLogin.json();
    await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${userToken}` },
      data: {
        payload: {
          'ue-hacker-interactive-progress-caesar-chiffre': {
            value: {
              version: 1,
              courseId: 'projekt-caesar-chiffre',
              variant: 'caesar-chiffre',
              completedLessonIds: ['lektion-01', 'lektion-02', 'lektion-03', 'lektion-04', 'lektion-05'],
            },
            updatedAt: new Date().toISOString(),
          },
        },
      },
    });

    await page.goto('/');
    // Ohne Login gibt es weder den Nav-Link noch Zugriff auf die Seite.
    await expect(page.locator('nav a', { hasText: 'Mein Profil' })).toHaveCount(0);
    await page.goto('/profil');
    await expect(page.locator('.profil-login-required')).toBeVisible();

    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);
    await page.locator('.settings-close').click();

    await expect(page.locator('nav a', { hasText: 'Mein Profil' })).toBeVisible();
    await page.locator('nav a', { hasText: 'Mein Profil' }).click();
    await expect(page).toHaveURL(/\/profil/);

    await expect(page.locator('.badge-card').first()).toBeVisible({ timeout: 10000 });
    const caesarBadge = page.locator('.badge-card', { hasText: 'Cäsar' });
    await expect(caesarBadge).toHaveClass(/earned/);
    await expect(caesarBadge.locator('.badge-icon')).toHaveText('🏅');

    // Ein anderes Projekt, das noch nicht bearbeitet wurde, bleibt gesperrt.
    const morseBadge = page.locator('.badge-card', { hasText: 'Morsecode' });
    await expect(morseBadge).not.toHaveClass(/earned/);
    await expect(morseBadge.locator('.badge-icon')).toHaveText('🔒');
    await expect(morseBadge.locator('.badge-status')).toContainText('0/5');

    // Ein nicht verlinkter Kurs (`unlisted` in kurse.json) zeigt kein Abzeichen, solange er nicht begonnen wurde.
    await expect(page.locator('.badge-card', { hasText: 'Roboterauto' })).toHaveCount(0);
  });

  test('Anleitung zum Abhaken: mit Account bleiben einzelne Haken auch nach mehr als einem Tag erhalten', async ({ page, request }) => {
    const username = `haken_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, { data: { password: ADMIN_PASSWORD } });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });
    const userLogin = await request.post(`${API}/api/login`, { data: { username, password: 'pass1234' } });
    const { token: userToken } = await userLogin.json();
    // Drei Tage alte Haken auf dem Account - ohne Account wären sie nach einem Tag verfallen
    // (tests/microbit-auto.spec.js prüft das).
    await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${userToken}` },
      data: {
        payload: {
          'ue-hacker-interactive-progress-microbit-auto': {
            value: {
              version: 1,
              courseId: 'projekt-microbit-auto',
              variant: 'microbit-auto',
              completedLessonIds: [],
              partialChecks: { 'lektion-01': [0, 2] },
              partialChecksAt: new Date(Date.now() - 3 * 24 * 3600 * 1000).toISOString(),
            },
            updatedAt: new Date().toISOString(),
          },
        },
      },
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);
    await page.locator('.settings-close').click();

    await page.goto('/kurs/projekt-microbit-auto');
    await page.locator('.btn-start-course').click();
    const tasks = page.locator('.guide-task');
    await expect(tasks.nth(0).locator('.guide-task-check')).toBeChecked({ timeout: 15000 });
    await expect(tasks.nth(2).locator('.guide-task-check')).toBeChecked();
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(2);
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);
  });

  test('Mein Profil: Zertifikate aus mehreren Kursen (Python + KI-Labor) erscheinen im eigenen Abschnitt', async ({ page, request }) => {
    // Wie beim Abzeichen-Test: Der Account-Fortschritt kommt erst an, wenn das Profil schon offen ist.
    await page.route('**/api/progress', async (route) => {
      if (route.request().method() === 'GET') await new Promise((resolve) => setTimeout(resolve, 1500));
      await route.continue();
    });
    const username = `profilcert_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    // Fortschritt liegt bereits auf dem Account (Server), nicht nur lokal vor dem Login — seit
    // dem Login-Reset (Account-Stand ersetzt lokale Vor-Login-Daten statt sie zu mergen) würde
    // rein lokaler Vor-Login-Fortschritt beim Login sonst verworfen statt übernommen.
    const userLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const { token: userToken } = await userLogin.json();
    await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${userToken}` },
      data: {
        payload: {
          // Python-Woche 1 bestanden, KI-Labor-Woche 1 noch nicht - jeder Kurs hat einen eigenen
          // Storage-Key (siehe useWeekChecks.js storageKeyFor), damit sich beide "Woche 1" nicht
          // gegenseitig überschreiben.
          'ue-hacker-week-checks': {
            value: {
              version: 1,
              weeks: { '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() } },
              placement: null,
            },
            updatedAt: new Date().toISOString(),
          },
        },
      },
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);
    await page.locator('.settings-close').click();

    await page.goto('/profil');
    // Python, KI-Labor und „Meine erste Website“ in beiden Stufen (Einfach: Abschluss-Check,
    // Intensiv: Wochen-Checks) - die beiden letzten hier noch nicht bestanden.
    await expect(page.locator('.cert-course-block')).toHaveCount(4, { timeout: 10000 });
    const einfachBlock = page.locator('.cert-course-block').filter({ has: page.locator('.cert-course-title', { hasText: /^Meine erste Website \d/ }) });
    await expect(einfachBlock.locator('.cert-course-count')).toContainText('0/1');
    const intensivBlock = page.locator('.cert-course-block', { hasText: 'Meine erste Website – Intensiv' });
    await expect(intensivBlock.locator('.badge-card-link').first()).toHaveAttribute('href', '/kurs/web-erste-website?stufe=intensiv&week=1');

    const pythonBlock = page.locator('.cert-course-block', { hasText: 'Python 12-Wochen-Grundkurs' });
    await expect(pythonBlock.locator('.cert-course-count')).toContainText('1/12');
    const pythonWeek1 = pythonBlock.locator('.badge-card').first();
    await expect(pythonWeek1).toHaveClass(/earned/);
    await expect(pythonWeek1.locator('.badge-icon')).toHaveText('🎓');
    const pythonWeek2 = pythonBlock.locator('.badge-card').nth(1);
    await expect(pythonWeek2).not.toHaveClass(/earned/);
    await expect(pythonWeek2.locator('.badge-icon')).toHaveText('🔒');

    const kiLaborBlock = page.locator('.cert-course-block', { hasText: 'KI-Labor' });
    await expect(kiLaborBlock.locator('.cert-course-count')).toContainText('0/8');
    await expect(kiLaborBlock.locator('.badge-card')).toHaveCount(8);
    await expect(kiLaborBlock.locator('.badge-card').first()).not.toHaveClass(/earned/);

    // Nur verliehene Zertifikate haben einen Download-Button.
    await expect(pythonWeek1.locator('.btn-certificate-pdf')).toBeVisible();
    await expect(pythonWeek2.locator('.btn-certificate-pdf')).toHaveCount(0);

    await page.locator('#profil-certificate-name').fill('Max Mustermann');
    const downloadPromise = page.waitForEvent('download');
    await pythonWeek1.locator('.btn-certificate-pdf').click();
    const download = await downloadPromise;
    expect(download.suggestedFilename()).toMatch(/^Zertifikat_Woche_1_Max_Mustermann\.pdf$/);

    // Ein Klick auf ein verliehenes Zertifikat führt direkt in die Wochen-Tour dieses Kurses.
    await pythonWeek1.locator('.badge-card-link').click();
    await expect(page).toHaveURL(/\/kurs\/python-12-wochen-grundkurs\?week=1/);
    await expect(page.locator('.course-structure')).toHaveCount(0);
  });

  test('Mein Profil: Projekt-Fortschritt wird über den Account synchronisiert', async ({ page, request }) => {
    const username = `profilsync_${Date.now()}`;
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
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);
    await page.locator('.settings-close').click();

    // Simuliert das Abschließen einer Lektion (touchSyncKey passiert normalerweise automatisch
    // über useInteractiveProgress.js beim echten Lösen einer Aufgabe).
    await page.evaluate(() => {
      const key = 'ue-hacker-interactive-progress-caesar-chiffre';
      const value = {
        version: 1,
        courseId: 'projekt-caesar-chiffre',
        variant: 'caesar-chiffre',
        completedLessonIds: ['lektion-01'],
      };
      localStorage.setItem(key, JSON.stringify(value));
      const meta = JSON.parse(localStorage.getItem('ue-hacker-sync-meta') || '{}');
      meta[key] = new Date().toISOString();
      localStorage.setItem('ue-hacker-sync-meta', JSON.stringify(meta));
    });
    // Reload läuft restoreSession()/syncNow() erneut an, ohne auf den 1.5s-Debounce warten zu müssen.
    await page.reload();
    await page.waitForTimeout(2500);

    const userLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const session = await userLogin.json();
    const progress = await request.get(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${session.token}` },
    });
    const body = await progress.json();
    expect(body.payload['ue-hacker-interactive-progress-caesar-chiffre'].value.completedLessonIds).toContain('lektion-01');
  });

  test('Login: Account-Stand ersetzt lokale Gast-Daten statt sie zu mergen (geteilter Rechner)', async ({ page, request }) => {
    const username = `resetlogin_${Date.now()}`;
    const adminLogin = await request.post(`${API}/api/admin/login`, {
      data: { password: ADMIN_PASSWORD },
    });
    const { token: adminToken } = await adminLogin.json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'jugendliche' },
    });

    // Der Account hat bereits eigenen, vom Server geladenen Fortschritt (z.B. von einem anderen Gerät).
    const userLogin = await request.post(`${API}/api/login`, {
      data: { username, password: 'pass1234' },
    });
    const { token: userToken } = await userLogin.json();
    await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${userToken}` },
      data: {
        payload: {
          'ue-hacker-week-checks': {
            value: { version: 1, weeks: { 3: { passed: true, score: 1 } }, placement: null },
            updatedAt: new Date().toISOString(),
          },
        },
      },
    });

    await page.goto('/');
    // Lokale Gast-Daten, die vor dem Login auf diesem Rechner entstanden sind (anderes Kind, kein Account).
    await page.evaluate(() => {
      const key = 'ue-hacker-week-checks';
      const value = { version: 1, weeks: { 2: { passed: true, score: 1 } }, placement: null };
      localStorage.setItem(key, JSON.stringify(value));
      const meta = JSON.parse(localStorage.getItem('ue-hacker-sync-meta') || '{}');
      meta[key] = new Date().toISOString();
      localStorage.setItem('ue-hacker-sync-meta', JSON.stringify(meta));

      const projectKey = 'ue-hacker-interactive-progress-caesar-chiffre';
      localStorage.setItem(projectKey, JSON.stringify({
        version: 1,
        courseId: 'projekt-caesar-chiffre',
        variant: 'caesar-chiffre',
        completedLessonIds: ['lektion-01'],
      }));
      meta[projectKey] = new Date().toISOString();
      localStorage.setItem('ue-hacker-sync-meta', JSON.stringify(meta));
    });

    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);

    const localState = await page.evaluate(() => ({
      weekChecks: JSON.parse(localStorage.getItem('ue-hacker-week-checks') || 'null'),
      projectProgress: localStorage.getItem('ue-hacker-interactive-progress-caesar-chiffre'),
    }));
    // Account-Stand (Woche 3) hat lokale Gast-Daten (Woche 2) ersetzt, nicht gemergt.
    expect(localState.weekChecks.weeks['3']).toBeTruthy();
    expect(localState.weekChecks.weeks['2']).toBeFalsy();
    // Ein Key, den der Account nicht hat, wird beim Login komplett entfernt statt lokal stehenzubleiben.
    expect(localState.projectProgress).toBeNull();

    // Die verworfenen Gast-Daten dürfen nicht auf den Account übertragen worden sein.
    const progress = await request.get(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${userToken}` },
    });
    const body = await progress.json();
    expect(body.payload['ue-hacker-interactive-progress-caesar-chiffre']).toBeUndefined();
  });

  test('Partnerarbeit: zweite Person eintragen, der Stand des Kurses landet in beiden Accounts', async ({ page, request }) => {
    const KEY = 'ue-hacker-interactive-progress-microbit-auto';
    const stamp = Date.now();
    const nameA = `pilot_${stamp}`;
    const nameB = `navi_${stamp}`;
    const { token: adminToken } = await (await request.post(`${API}/api/admin/login`, { data: { password: ADMIN_PASSWORD } })).json();
    const tokens = {};
    for (const username of [nameA, nameB]) {
      await request.post(`${API}/api/admin/users`, {
        headers: { Authorization: `Bearer ${adminToken}` },
        data: { username, password: 'pass1234', ageGroup: 'kinder' },
      });
      tokens[username] = (await (await request.post(`${API}/api/login`, { data: { username, password: 'pass1234' } })).json()).token;
    }
    const courseState = async (username) => {
      const res = await request.get(`${API}/api/progress`, { headers: { Authorization: `Bearer ${tokens[username]}` } });
      return (await res.json()).payload;
    };
    // Die zweite Person hat schon etwas: einen Haken in Stufe 1 (lektion-02) und ein anderes Projekt.
    await request.put(`${API}/api/progress`, {
      headers: { Authorization: `Bearer ${tokens[nameB]}` },
      data: {
        payload: {
          [KEY]: {
            value: { version: 1, courseId: 'projekt-microbit-auto', variant: 'microbit-auto', completedLessonIds: [], partialChecks: { 'lektion-02': [0] }, partialChecksAt: new Date().toISOString() },
            updatedAt: new Date().toISOString(),
          },
          'ue-hacker-interactive-progress-morsecode': { value: { completedLessonIds: ['lektion-01'] }, updatedAt: new Date().toISOString() },
        },
      },
    });

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(nameA);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(nameA);
    await page.locator('.settings-close').click();

    await page.goto('/kurs/projekt-microbit-auto');
    await page.locator('.btn-start-course').click();
    const box = page.locator('.partner-box');
    await box.locator('.partner-open').click();

    // Sich selbst oder ein falsches Passwort eintragen geht nicht.
    await box.locator('.partner-username').fill(nameA);
    await box.locator('.partner-password').fill('pass1234');
    await box.locator('.partner-submit').click();
    await expect(box.locator('.partner-error')).toContainText('Das bist du selbst');
    await box.locator('.partner-username').fill(nameB);
    await box.locator('.partner-password').fill('falsch');
    await box.locator('.partner-submit').click();
    await expect(box.locator('.partner-error')).toContainText('stimmt nicht');

    await box.locator('.partner-password').fill('pass1234');
    await box.locator('.partner-submit').click();
    await expect(box.locator('.partner-names')).toHaveText(`${nameA} + ${nameB}`);

    // Zusammengeführt: Der Haken der zweiten Person ist jetzt auch im Account der ersten.
    await expect.poll(async () => (await courseState(nameA))[KEY]?.value.partialChecks?.['lektion-02']).toEqual([0]);

    // Stufe abschließen und in der nächsten einen Haken setzen: beide Accounts haben denselben Stand.
    const tasks = page.locator('.guide-task');
    const required = 3;
    for (let i = 0; i < required; i++) await tasks.nth(i).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    for (const username of [nameA, nameB]) {
      await expect.poll(async () => (await courseState(username))[KEY]?.value.completedLessonIds, { message: username }).toEqual(['lektion-01']);
    }
    const stateB = await courseState(nameB);
    expect(stateB[KEY].value.partialChecks['lektion-02']).toEqual([0]);
    expect(stateB[KEY].value.partialChecks['lektion-01']).toEqual([0, 1, 2]);
    // Andere Kurse der zweiten Person bleiben unberührt.
    expect(stateB['ue-hacker-interactive-progress-morsecode'].value.completedLessonIds).toEqual(['lektion-01']);

    // Ein zurückgenommener Haken nimmt den Abschluss bei beiden zurück.
    await tasks.nth(0).locator('.guide-task-check').uncheck();
    for (const username of [nameA, nameB]) {
      await expect.poll(async () => (await courseState(username))[KEY]?.value.completedLessonIds, { message: username }).toEqual([]);
    }

    // Die Verbindung übersteht ein Neuladen und endet beim Trennen.
    await page.reload();
    await expect(page.locator('.partner-names')).toHaveText(`${nameA} + ${nameB}`, { timeout: 15000 });
    await page.locator('.partner-unlink').click();
    await expect(page.locator('.partner-open')).toBeVisible();
    await tasks.nth(0).locator('.guide-task-check').check();
    await expect.poll(async () => (await courseState(nameA))[KEY]?.value.completedLessonIds).toEqual(['lektion-01']);
    expect((await courseState(nameB))[KEY].value.completedLessonIds).toEqual([]);
  });

  test('Admin schreibt ein Projekt gut: Abzeichen erscheint im Profil des Accounts', async ({ page, request }) => {
    const username = `gutschrift_${Date.now()}`;
    const { token: adminToken } = await (await request.post(`${API}/api/admin/login`, { data: { password: ADMIN_PASSWORD } })).json();
    await request.post(`${API}/api/admin/users`, {
      headers: { Authorization: `Bearer ${adminToken}` },
      data: { username, password: 'pass1234', ageGroup: 'kinder' },
    });

    await page.goto('/admin');
    await page.locator('.admin-login-card input[type="password"]').fill(ADMIN_PASSWORD);
    await page.locator('.admin-login-card .btn-primary').click();
    const row = page.locator('.admin-table tr', { hasText: username });
    await row.locator('.grant-project-btn').click();
    await expect(page.locator('.grant-modal h2')).toContainText(username);
    await page.locator('.grant-course').selectOption({ label: 'micro:bit: Das Roboterauto' });
    await page.locator('.grant-submit').click();
    await expect(page.locator('.grant-result')).toContainText('micro:bit: Das Roboterauto');
    await expect(page.locator('.grant-result')).toContainText(username);
    await page.locator('.admin-toolbar .btn-secondary').click();

    await page.goto('/');
    await page.locator('.options-btn').click();
    await page.locator('.settings-modal .auth-btn.primary', { hasText: /Anmelden|Log in/ }).click();
    await page.locator('.settings-modal input').nth(0).fill(username);
    await page.locator('.settings-modal input[type="password"]').fill('pass1234');
    await page.locator('.settings-modal .auth-btn.primary').click();
    await expect(page.locator('.settings-modal')).toContainText(username);
    await page.locator('.settings-close').click();

    await page.locator('nav a', { hasText: 'Mein Profil' }).click();
    const badge = page.locator('.badge-card', { hasText: 'Roboterauto' });
    await expect(badge).toHaveClass(/earned/, { timeout: 10000 });
    // Ein nicht gutgeschriebenes Projekt bleibt gesperrt.
    await expect(page.locator('.badge-card', { hasText: 'Morsecode' })).not.toHaveClass(/earned/);
  });
});
