import { defineConfig, devices } from '@playwright/test';
import { ports } from './scripts/worktree-ports.mjs';

export default defineConfig({
  testDir: './tests',
  testIgnore: /(?:api-auth|auth-ui|dev-skip-checks)\.spec\.js/,
  // Generierte Notebook-Dateien/ZIPs (gitignored) vor jedem Lauf sicherstellen.
  globalSetup: './scripts/ensure-test-prereqs.mjs',
  timeout: 30000,
  retries: 0,
  use: {
    baseURL: `http://localhost:${ports.test}`,
    headless: true,
  },
  webServer: {
    command: `npx vite --port ${ports.test}`,
    port: ports.test,
    // false: Ein zweiter Lauf im selben Checkout (z.B. Pre-push-Hook parallel zu einem manuellen
    // Lauf) bricht sofort mit "Port belegt" ab, statt sich den Server des ersten zu leihen - der
    // verschwindet, sobald der erste Lauf fertig ist, und alle weiteren Tests scheitern mit
    // ERR_CONNECTION_REFUSED.
    reuseExistingServer: false,
    timeout: 60000,
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
