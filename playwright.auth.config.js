import { defineConfig, devices } from '@playwright/test';
import { ports } from './scripts/worktree-ports.mjs';

/**
 * Auth / API suite — starts a throwaway SQLite API (Standard :3011, in einem Worktree ein
 * eigener Port, siehe scripts/worktree-ports.mjs) and Vite with proxy to that API.
 *
 * Run: npm run test:auth
 */
export default defineConfig({
  testDir: './tests',
  testMatch: /(?:progress-merge|api-auth|auth-ui)\.spec\.js/,
  timeout: 30000,
  retries: 0,
  use: {
    baseURL: `http://localhost:${ports.test}`,
    headless: true,
  },
  webServer: [
    {
      command: 'node scripts/run-test-api.js',
      url: `http://127.0.0.1:${ports.testApi}/api/health`,
      reuseExistingServer: false,
      timeout: 30000,
      env: { TEST_API_PORT: String(ports.testApi) },
    },
    {
      command: `npx vite --port ${ports.test}`,
      url: `http://localhost:${ports.test}`,
      reuseExistingServer: true,
      timeout: 60000,
      env: { VITE_API_PROXY: `http://127.0.0.1:${ports.testApi}` },
    },
  ],
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
