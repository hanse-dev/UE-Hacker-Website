// Erfasst alles, woran gespeicherter Fortschritt haengt ("Fortschritts-Vertrag"): Lektions-IDs,
// Wochen-Check-Fragen/-Aufgaben, Kurs-IDs, localStorage-Keys samt Versionen und das DB-Schema.
// tests/progress-contract.spec.js vergleicht den aktuellen Stand mit dem eingefrorenen Stand in
// tests/fixtures/progress-contract.json: Dazukommen ist erlaubt, Wegfallen/Umbenennen nicht.
//
//   node scripts/progress-contract.mjs --write   # Stand bewusst neu einfrieren (npm run contract:update)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');
export const FIXTURE = path.join(ROOT, 'tests', 'fixtures', 'progress-contract.json');
const read = (p) => fs.readFileSync(path.join(ROOT, p), 'utf8');
const readJson = (p) => JSON.parse(read(p));

// localStorage-Keys, unter denen Fortschritt liegt (und mit dem Account synchronisiert wird).
// Jeder Eintrag: Datei, in der der Key definiert ist, und der Key-Text, der dort stehen muss.
const STORAGE_KEYS = [
  ['src/composables/useFortschritt.js', 'ue-hacker-fortschritt'],
  ['src/composables/useWeekChecks.js', 'ue-hacker-week-checks'],
  ['src/composables/useInteractiveProgress.js', 'ue-hacker-interactive-progress-'],
  ['src/components/JupyterNotebook.vue', 'ue-hacker-notebook-state-'],
  ['src/composables/useProgressSync.js', 'ue-hacker-sync-meta'],
];
// Versionsnummern in gespeicherten Daten: ein Hochzaehlen verwirft den alten Stand.
const STORAGE_VERSIONS = [
  ['src/composables/useFortschritt.js', /version:\s*(\d+)/],
  ['src/composables/useInteractiveProgress.js', /version:\s*(\d+)/],
];

function lessons() {
  const out = {};
  for (const dir of fs.readdirSync(path.join(ROOT, 'content')).sort()) {
    const file = path.join('content', dir, 'lessons.json');
    if (!fs.existsSync(path.join(ROOT, file))) continue;
    const data = readJson(file);
    out[dir] = (Array.isArray(data) ? data : data.lessons).map((l) => l.id);
  }
  return out;
}

function checks() {
  const out = {};
  for (const dir of fs.readdirSync(path.join(ROOT, 'content')).filter((d) => d.endsWith('-checks')).sort()) {
    out[dir] = {};
    for (const file of fs.readdirSync(path.join(ROOT, 'content', dir)).filter((f) => /^week-\d+\.json$/.test(f)).sort()) {
      const data = readJson(path.join('content', dir, file));
      out[dir][file.replace('.json', '')] = {
        questions: (data.questions || []).map((q) => q.id).filter(Boolean),
        coding: (data.codingChallenges || []).length,
      };
    }
  }
  return out;
}

function courses() {
  const data = readJson('public/kurse.json');
  const list = Array.isArray(data) ? data : data.kurse || Object.values(data);
  return list.map((k) => k.id).filter(Boolean).sort();
}

function storage() {
  const keys = STORAGE_KEYS.filter(([file, key]) => read(file).includes(key)).map(([file, key]) => `${file}: ${key}`);
  const versions = {};
  for (const [file, re] of STORAGE_VERSIONS) {
    const m = read(file).match(re);
    if (m) versions[file] = Number(m[1]);
  }
  return { keys, versions };
}

// Spalten je Tabelle aus den CREATE-TABLE-Bloecken in api/src/db.js, plus ALTER-TABLE-Migrationen.
export function dbSchema(source = read('api/src/db.js')) {
  const tables = {};
  for (const m of source.matchAll(/CREATE TABLE IF NOT EXISTS (\w+)\s*\(([\s\S]*?)\n\s*\);/g)) {
    tables[m[1]] = m[2].split('\n').map((l) => l.trim().split(/\s+/)[0]).filter((w) => /^[a-z_]+$/.test(w));
  }
  const migrated = [...source.matchAll(/ALTER TABLE (\w+) ADD COLUMN (\w+)/g)].map((m) => `${m[1]}.${m[2]}`);
  return { tables, migrated };
}

export function collect() {
  return { lessons: lessons(), checks: checks(), courses: courses(), storage: storage(), db: dbSchema().tables };
}

// Vergleicht eingefrorenen und aktuellen Stand. Liefert eine Liste von Verstoessen (leer = alles gut).
// Erlaubt: neue Kurse/Lektionen/Fragen/Tabellen. Nicht erlaubt: etwas Bestehendes entfernen oder
// umbenennen, Coding-Aufgaben eines Checks streichen, Storage-Keys/-Versionen aendern, Spalten ohne
// ALTER-TABLE-Migration ergaenzen (CREATE TABLE IF NOT EXISTS aendert eine bestehende Tabelle nicht).
export function diffContract(frozen, current, migrated = []) {
  const problems = [];
  for (const [dir, ids] of Object.entries(frozen.lessons)) {
    if (!current.lessons[dir]) { problems.push(`Content-Ordner "${dir}" fehlt (Fortschritt liegt unter diesem Namen)`); continue; }
    for (const id of ids) if (!current.lessons[dir].includes(id)) problems.push(`Lektion "${id}" fehlt in ${dir}/lessons.json`);
  }
  for (const [dir, weeks] of Object.entries(frozen.checks)) {
    for (const [week, w] of Object.entries(weeks)) {
      const cur = current.checks[dir]?.[week];
      if (!cur) { problems.push(`Wochen-Check ${dir}/${week}.json fehlt`); continue; }
      for (const id of w.questions) if (!cur.questions.includes(id)) problems.push(`Quizfrage "${id}" fehlt in ${dir}/${week}.json`);
      if (cur.coding < w.coding) problems.push(`${dir}/${week}.json hat nur noch ${cur.coding} statt ${w.coding} Coding-Aufgaben (bestanden wird je Position gespeichert)`);
    }
  }
  for (const id of frozen.courses) if (!current.courses.includes(id)) problems.push(`Kurs-ID "${id}" fehlt in public/kurse.json (URLs, Abzeichen)`);
  for (const key of frozen.storage.keys) if (!current.storage.keys.includes(key)) problems.push(`Storage-Key geändert oder entfernt: ${key}`);
  for (const [file, v] of Object.entries(frozen.storage.versions)) {
    if (current.storage.versions[file] !== v) problems.push(`Daten-Version in ${file} ist ${current.storage.versions[file]} statt ${v} – alter Fortschritt würde verworfen`);
  }
  for (const [table, cols] of Object.entries(frozen.db)) {
    const cur = current.db[table];
    if (!cur) { problems.push(`DB-Tabelle "${table}" fehlt in api/src/db.js`); continue; }
    for (const c of cols) if (!cur.includes(c)) problems.push(`DB-Spalte ${table}.${c} fehlt`);
    for (const c of cur) {
      if (!cols.includes(c) && !migrated.includes(`${table}.${c}`)) {
        problems.push(`Neue DB-Spalte ${table}.${c} ohne "ALTER TABLE ${table} ADD COLUMN ${c}" – auf dem Server existiert die Tabelle schon, CREATE TABLE IF NOT EXISTS ergänzt sie nicht`);
      }
    }
  }
  return problems;
}

if (process.argv.includes('--write')) {
  fs.mkdirSync(path.dirname(FIXTURE), { recursive: true });
  fs.writeFileSync(FIXTURE, `${JSON.stringify(collect(), null, 2)}\n`);
  console.log(`✓ Fortschritts-Vertrag eingefroren: ${path.relative(ROOT, FIXTURE)}`);
}
