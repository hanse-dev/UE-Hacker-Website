import { defineConfig, devices } from '@playwright/test';
import { ports } from './scripts/worktree-ports.mjs';

export default defineConfig({
  testDir: './tests',
  testIgnore: /(?:api-auth|auth-ui)\.spec\.js/,
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
    reuseExistingServer: true,
    timeout: 60000,
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
