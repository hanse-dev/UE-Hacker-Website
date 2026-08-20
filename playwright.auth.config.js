import { defineConfig, devices } from '@playwright/test';

/**
 * Auth / API suite — starts a throwaway SQLite API on :3011
 * and Vite with proxy to that API.
 *
 * Run: npm run test:auth
 */
export default defineConfig({
  testDir: './tests',
  testMatch: /(?:progress-merge|api-auth|auth-ui)\.spec\.js/,
  timeout: 30000,
  retries: 0,
  use: {
    baseURL: 'http://localhost:5174',
    headless: true,
  },
  webServer: [
    {
      command: 'node scripts/run-test-api.js',
      url: 'http://127.0.0.1:3011/api/health',
      reuseExistingServer: false,
      timeout: 30000,
    },
    {
      command: 'VITE_API_PROXY=http://127.0.0.1:3011 npx vite --port 5174',
      url: 'http://localhost:5174',
      reuseExistingServer: true,
      timeout: 60000,
    },
  ],
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
