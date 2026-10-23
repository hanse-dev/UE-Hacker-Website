import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

// scripts/check_verstaendlichkeit.py sucht Stellen, an denen Teilnehmende hängen bleiben (vor
// allem: Musterlösung braucht etwas, das nie gezeigt wurde). Geprüft an einem Mini-Kurs mit einer
// Woche, damit die Erwartungen nicht vom echten Content abhängen.
function miniKurs({ lektionstext, loesung, aufgabe = 'Gib den Namen groß aus.' }) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'verstaendlichkeit-'));
  const lessonsDir = path.join(root, 'python-woche1-abenteuer');
  const solDir = path.join(root, 'python-12-wochen-grundkurs', 'woche-1', 'abenteuer', 'woche1_abenteuer_6_loesungen');
  fs.mkdirSync(lessonsDir, { recursive: true });
  fs.mkdirSync(solDir, { recursive: true });
  fs.writeFileSync(path.join(lessonsDir, 'lessons.json'), JSON.stringify([{
    id: 'lektion-01', section: 'lektion', title: 'Texte', file: 'lektion-01.md', lessonSummary: '',
    tasks: [
      { instruction: 'Beispiel', example: true, codeTemplate: 'name = "Mira"\nprint(name)\n', validation: { type: 'output_contains', expected: 'Mira' } },
      { instruction: aufgabe, codeTemplate: 'name = "Mira"\n', validation: { type: 'output_contains', expected: 'MIRA' } },
    ],
  }]));
  fs.writeFileSync(path.join(lessonsDir, 'lektion-01.md'), `# Texte\n\n${lektionstext}\n`);
  fs.writeFileSync(path.join(solDir, '01_markdown.py'), '"""### Aufgabe"""\n');
  fs.writeFileSync(path.join(solDir, '02_code.py'), loesung);
  return root;
}

const bericht = (content) => execFileSync('python3', [
  'scripts/check_verstaendlichkeit.py', '--content', content, '--wochen', '1', '--themen', 'abenteuer',
], { cwd: process.cwd(), encoding: 'utf8' });

test('meldet einen Baustein, den die Musterlösung braucht, der aber nie gezeigt wurde', () => {
  const out = bericht(miniKurs({ lektionstext: 'Mit print() gibst du Text aus.', loesung: 'name = "Mira"\nprint(name.upper())\n' }));
  expect(out).toContain('[nie-gezeigt] Aufgabe 2: `.upper()` – vorher nirgends gezeigt');
});

test('meldet nichts, wenn der Lektionstext den Baustein erklärt (auch ohne Punkt davor)', () => {
  const out = bericht(miniKurs({ lektionstext: 'Mit `upper()` wird ein Text groß.', loesung: 'name = "Mira"\nprint(name.upper())\n' }));
  expect(out).not.toContain('[nie-gezeigt]');
});

test('unterscheidet "nur im Aufgabentext genannt" von "nirgends gezeigt"', () => {
  const out = bericht(miniKurs({
    lektionstext: 'Mit print() gibst du Text aus.', aufgabe: 'Gib den Namen mit upper() groß aus.',
    loesung: 'name = "Mira"\nprint(name.upper())\n',
  }));
  expect(out).toContain('`.upper()` – vorher nur im Aufgabentext gezeigt');
});

test('Fachwörter: meldet "Integer", aber keinen Variablennamen wie "klasse = 1"', () => {
  const out = bericht(miniKurs({
    lektionstext: 'Eine ganze Zahl heißt Integer. Schreibe klasse = 1 in den Editor.',
    loesung: 'name = "Mira"\nprint(name)\n',
  }));
  expect(out).toContain('erstes „Integer“');
  expect(out).not.toMatch(/erstes „[Kk]lasse“/);
});

test('läuft über den echten 12-Wochen-Kurs (alle Themen) ohne Fehler durch', () => {
  const out = execFileSync('python3', ['scripts/check_verstaendlichkeit.py'], { cwd: process.cwd(), encoding: 'utf8' });
  expect(out).toContain('# Verständlichkeits-Bericht Python-Kurs');
  expect(out).toContain('## Woche 12');
});
