import { test, expect } from '@playwright/test';
import { spawnSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { devSkipPorts } from '../playwright.devskip.config.js';

// Dev-Modus "Admin-Login überspringen" (api/src/devAdminLogin.js, npm run dev:skip-checks).
// Laeuft in der Dev-Modus-Suite (playwright.devskip.config.js): der Dev-Server zeigt dort auf eine
// Wegwerf-API mit DEV_SKIP_ADMIN_LOGIN=1. Dass die Route ohne Schalter fehlt, prueft
// tests/api-auth.spec.js (dortige API laeuft ohne Schalter).
const BUILD = `http://localhost:${devSkipPorts.build}`;
const ROOT = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');

test.describe('Dev-Modus: Admin-Login ohne Passwort', () => {
  test('Admin-Seite meldet im Dev-Modus ohne Passwort an', async ({ page }) => {
    await page.goto('/admin');
    await expect(page.locator('.admin-tabs')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.admin-login-card')).toHaveCount(0);
  });

  test('Produktions-Build: Login-Formular bleibt, kein Dev-Login-Versuch', async ({ page }) => {
    const devLoginCalls = [];
    page.on('request', (req) => {
      if (req.url().includes('/api/admin/dev-login')) devLoginCalls.push(req.url());
    });
    await page.goto(`${BUILD}/admin`);
    await expect(page.locator('.admin-login-card')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.admin-tabs')).toHaveCount(0);
    expect(devLoginCalls).toEqual([]);
  });

  test('Server startet mit Schalter und NODE_ENV=production gar nicht', () => {
    const dataDir = path.join(ROOT, 'api', 'data');
    fs.mkdirSync(dataDir, { recursive: true });
    const result = spawnSync(process.execPath, ['api/src/index.js'], {
      cwd: ROOT,
      timeout: 15000,
      encoding: 'utf8',
      env: {
        ...process.env,
        NODE_ENV: 'production',
        DEV_SKIP_ADMIN_LOGIN: '1',
        ADMIN_PASSWORD: 'egal',
        API_PORT: String(devSkipPorts.api + 1),
        DB_PATH: path.join(dataDir, 'test-devskip-prod.sqlite'),
        STATIC_DIR: path.join(dataDir, 'gibt-es-nicht'),
      },
    });
    // status null = Timeout, d.h. der Server lief und lauschte - genau das darf nicht passieren.
    expect(result.status).toBe(1);
    expect(result.stderr).toContain('DEV_SKIP_ADMIN_LOGIN=1 ist mit NODE_ENV=production nicht erlaubt');
  });
});
