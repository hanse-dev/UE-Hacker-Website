import { createAdminToken } from './auth.js';

/**
 * Dev-Modus "Admin-Login überspringen" - Gegenstück zu src/composables/devSkipChecks.js.
 *
 * Aktiv nur mit DEV_SKIP_ADMIN_LOGIN=1, gesetzt ausschließlich vom Skript
 * `npm run dev:skip-checks` (nie in .env eintragen). Sicherungen:
 * - Zusammen mit NODE_ENV=production (setzt das Docker-Image) startet der Server gar nicht -
 *   ein versehentlich gesetzter Schalter fällt so beim Deploy auf, statt den Admin-Bereich zu öffnen.
 * - Die Route /api/admin/dev-login gibt es nur, wenn der Schalter aktiv ist, und sie antwortet nur
 *   auf Anfragen von localhost (Zusatz, kein Ersatz: hinter einem Proxy auf demselben Rechner
 *   kommt jede Anfrage von localhost).
 * Geprüft in tests/dev-admin-login.spec.js.
 */
export function devSkipAdminLoginEnabled() {
  return process.env.DEV_SKIP_ADMIN_LOGIN === '1';
}

// Wirft, wenn der Schalter in Produktion gesetzt ist; index.js beendet den Prozess dann.
export function assertDevSkipAdminLoginAllowed() {
  if (devSkipAdminLoginEnabled() && process.env.NODE_ENV === 'production') {
    throw new Error(
      'DEV_SKIP_ADMIN_LOGIN=1 ist mit NODE_ENV=production nicht erlaubt - Schalter aus .env/Umgebung entfernen.'
    );
  }
}

const LOOPBACK = new Set(['127.0.0.1', '::1', '::ffff:127.0.0.1']);

export function registerDevAdminLogin(app) {
  if (!devSkipAdminLoginEnabled()) return false;
  app.post('/api/admin/dev-login', (req, res) => {
    if (!LOOPBACK.has(req.socket.remoteAddress)) {
      return res.status(403).json({ error: 'Dev-Login nur von localhost.' });
    }
    return res.json({ token: createAdminToken() });
  });
  return true;
}
