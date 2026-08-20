import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { checkAdminPassword, createAdminToken } from './auth.js';
import adminUsersRouter from './routes/adminUsers.js';
import authRouter from './routes/auth.js';
import './db.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.join(__dirname, '..', '..', '.env') });
dotenv.config({ path: path.join(__dirname, '..', '.env') });

const app = express();
const PORT = Number(process.env.API_PORT || process.env.PORT || 3001);
const staticDir = path.resolve(
  process.env.STATIC_DIR || path.join(__dirname, '..', '..', 'dist')
);

app.use(cors({ origin: true, credentials: true }));
app.use(express.json({ limit: '8mb' }));

app.get('/api/health', (_req, res) => {
  res.json({ ok: true, service: 'ue-hacker-api' });
});

app.post('/api/admin/login', (req, res) => {
  try {
    if (!process.env.ADMIN_PASSWORD) {
      return res.status(500).json({ error: 'ADMIN_PASSWORD ist nicht gesetzt.' });
    }
    if (!checkAdminPassword(req.body?.password)) {
      return res.status(401).json({ error: 'Falsches Admin-Passwort.' });
    }
    return res.json({ token: createAdminToken() });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: 'Login fehlgeschlagen.' });
  }
});

app.use('/api/admin', adminUsersRouter);
app.use('/api', authRouter);

const serveStatic = fs.existsSync(staticDir);
if (serveStatic) {
  app.use(express.static(staticDir, { index: false }));
  app.get(/^(?!\/api(?:\/|$)).*/, (_req, res) => {
    res.sendFile(path.join(staticDir, 'index.html'));
  });
}

app.use((err, _req, res, _next) => {
  console.error(err);
  res.status(500).json({ error: 'Interner Serverfehler.' });
});

app.listen(PORT, () => {
  console.log(`UE Hacker listening on http://localhost:${PORT}`);
  if (serveStatic) {
    console.log(`  static: ${staticDir}`);
  } else {
    console.log(`  static: (none — set STATIC_DIR or run npm run build)`);
  }
  if (!process.env.ADMIN_PASSWORD) {
    console.warn('⚠  ADMIN_PASSWORD is not set — admin login will fail until configured.');
  }
});
