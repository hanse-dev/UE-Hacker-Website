import { defineConfig, devices } from '@playwright/test';
import { ports } from './scripts/worktree-ports.mjs';

/**
 * Prueft den Dev-Modus "Pruefungen ueberspringen" (src/composables/devSkipChecks.js). Braucht zwei
 * eigene, frisch gestartete Server mit gesetzter Variable VITE_DEV_SKIP_CHECKS=1
 * (reuseExistingServer: false - ein schon laufender Server ohne die Variable darf nicht
 * wiederverwendet werden):
 *  - Dev-Server: dort muss der Modus wirken.
 *  - Produktions-Build (vite build + preview): dort darf er trotz gesetzter Variable NICHT wirken.
 * Eigene Ports neben dem normalen Test-Server (ports.test), damit beides parallel laufen kann.
 *
 * Run: npm run test:devskip (laeuft auch im Pre-push-Hook)
 */
export const devSkipPorts = { dev: ports.test + 2, build: ports.test + 3 };

export default defineConfig({
  testDir: './tests',
  testMatch: /dev-skip-checks\.spec\.js/,
  globalSetup: './scripts/ensure-test-prereqs.mjs',
  timeout: 30000,
  retries: 0,
  use: {
    baseURL: `http://localhost:${devSkipPorts.dev}`,
    headless: true,
  },
  webServer: [
    {
      command: `npx vite --port ${devSkipPorts.dev} --strictPort`,
      url: `http://localhost:${devSkipPorts.dev}`,
      reuseExistingServer: false,
      timeout: 60000,
      env: { VITE_DEV_SKIP_CHECKS: '1' },
    },
    {
      command: `npx vite build --outDir dist-devskip --emptyOutDir --logLevel warn && npx vite preview --outDir dist-devskip --port ${devSkipPorts.build} --strictPort`,
      url: `http://localhost:${devSkipPorts.build}`,
      reuseExistingServer: false,
      timeout: 120000,
      env: { VITE_DEV_SKIP_CHECKS: '1' },
    },
  ],
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
});
