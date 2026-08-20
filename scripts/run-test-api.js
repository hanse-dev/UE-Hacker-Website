import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dataDir = path.join(__dirname, '..', 'api', 'data');
const dbPath = path.join(dataDir, 'test-e2e.sqlite');

fs.mkdirSync(dataDir, { recursive: true });
for (const suffix of ['', '-shm', '-wal']) {
  try {
    fs.unlinkSync(`${dbPath}${suffix}`);
  } catch {
    /* ignore */
  }
}

process.env.ADMIN_PASSWORD = process.env.TEST_ADMIN_PASSWORD || 'test-admin-password';
process.env.SESSION_SECRET = process.env.TEST_SESSION_SECRET || 'test-session-secret';
process.env.API_PORT = process.env.TEST_API_PORT || '3011';
process.env.DB_PATH = dbPath;
process.env.DATA_DIR = dataDir;

await import('../api/src/index.js');
