import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = path.dirname(fileURLToPath(import.meta.url));

function readJson(file) {
  return JSON.parse(readFileSync(path.join(dir, file), 'utf-8'));
}

const config = readJson('config.json');
const weeks = {};
for (const file of readdirSync(dir)) {
  const match = file.match(/^week-(\d+)\.json$/);
  if (match) weeks[match[1]] = readJson(file);
}

export default { ...config, weeks };
