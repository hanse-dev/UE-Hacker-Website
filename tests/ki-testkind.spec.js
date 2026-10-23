import { test, expect } from '@playwright/test';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

// scripts/ki_testkind.py: Claude spielt ein Kind, das nur das bisherige Kursmaterial kennt. Hier
// ohne KI geprüft - mit vorbereiteten Antworten (--antworten) an einem Mini-Kurs: Was bekommt das
// Test-Kind zu sehen, und wird sein Code wie auf der Website gegen `expected` geprüft?
function miniKurs() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'ki-testkind-'));
  const w1 = path.join(root, 'python-woche1-abenteuer');
  const w2 = path.join(root, 'python-woche2-abenteuer');
  const glossar = path.join(root, 'python-12-wochen-grundkurs', 'woche-1', 'abenteuer', 'woche1_abenteuer_0_glossar');
  for (const d of [w1, w2, glossar]) fs.mkdirSync(d, { recursive: true });
  fs.writeFileSync(path.join(glossar, '01_markdown.py'), '"""| `print()` | Gibt Text aus |"""\n');
  fs.writeFileSync(path.join(w1, 'lessons.json'), '[]');
  fs.writeFileSync(path.join(w2, 'lessons.json'), JSON.stringify([{
    id: 'lektion-01', section: 'lektion', title: 'Rechnen', file: 'lektion-01.md', lessonSummary: '',
    tasks: [
      { instruction: 'Beispiel', example: true, codeTemplate: 'gold = 5\nprint(gold)\n', validation: { type: 'output_contains', expected: '5' } },
      { instruction: 'Verdopple gold und gib Gold: 10 aus.', codeTemplate: '', validation: { type: 'output_contains', expected: 'Gold: 10' } },
      { instruction: 'Gib Gold: 15 aus.', codeTemplate: '', validation: { type: 'output_contains', expected: 'Gold: 15' } },
    ],
  }]));
  fs.writeFileSync(path.join(w2, 'lektion-01.md'), '# Rechnen\n\nMit `*` rechnest du mal.\n');
  // Lektion 2: Das Beispiel ruft selbst input() auf - es darf die Prüf-Eingabe der Aufgabe nicht wegessen
  const lessons = JSON.parse(fs.readFileSync(path.join(w2, 'lessons.json'), 'utf8'));
  lessons.push({
    id: 'lektion-02', section: 'lektion', title: 'Fragen', file: 'lektion-02.md', lessonSummary: '',
    tasks: [
      { instruction: 'Beispiel', example: true, codeTemplate: 'x = input("Wie geht es? ")\n', validation: { type: 'output_contains', expected: '' } },
      { instruction: 'Frage nach dem Namen.', codeTemplate: '', validation: { type: 'output_contains', expected: 'Hallo Blitz', stdin: ['Blitz'] } },
    ],
  });
  fs.writeFileSync(path.join(w2, 'lessons.json'), JSON.stringify(lessons));
  fs.writeFileSync(path.join(w2, 'lektion-02.md'), '# Fragen\n');
  // Musterlösung liegt im Lösungsordner - die darf das Test-Kind nie sehen
  const sol = path.join(root, 'python-12-wochen-grundkurs', 'woche-2', 'abenteuer', 'woche2_abenteuer_6_loesungen');
  fs.mkdirSync(sol, { recursive: true });
  fs.writeFileSync(path.join(sol, '02_code.py'), 'GEHEIME_MUSTERLOESUNG = 1\n');

  const antworten = fs.mkdtempSync(path.join(os.tmpdir(), 'ki-antworten-'));
  fs.writeFileSync(path.join(antworten, '2-lektion-01.json'), JSON.stringify({
    aufgaben: [
      // baut auf gold aus dem Beispiel auf (gleicher Kernel wie auf der Website)
      { nr: 2, verstanden: 'ja', was_ich_tun_soll: 'gold mal 2', code: 'print(f"Gold: {gold * 2}")', unklar: '' },
      { nr: 3, verstanden: 'nein', was_ich_tun_soll: 'weiß nicht', code: 'print("Gold: 5")', unklar: 'Woher kommt 15?' },
    ],
    schwere_woerter: ['f-String'],
    verwirrende_saetze: [],
    gesamteindruck: 'Ging so.',
  }));
  fs.writeFileSync(path.join(antworten, '2-lektion-02.json'), JSON.stringify({
    aufgaben: [{ nr: 2, verstanden: 'ja', was_ich_tun_soll: 'fragen', code: 'n = input("Name? ")\nprint(f"Hallo {n}")', unklar: '' }],
    schwere_woerter: [], verwirrende_saetze: [], gesamteindruck: 'Leicht.',
  }));
  return { root, antworten };
}

const run = (args) => execFileSync('python3', ['scripts/ki_testkind.py', ...args], { cwd: process.cwd(), encoding: 'utf8' });

test('prüft den Code des Test-Kinds wie die Website (inkl. Variablen aus dem Beispiel)', () => {
  const { root, antworten } = miniKurs();
  const out = run(['--content', root, '--wochen', '2', '--antworten', antworten]);
  expect(out).toContain('- **Aufgaben nicht geschafft:** 1');
  expect(out).toContain('✅ **Aufgabe 2** (ja verstanden)');
  expect(out).toContain('❌ **Aufgabe 3** (nein verstanden)');
  expect(out).toContain('Unklar: Woher kommt 15?');
  expect(out).toContain('Ausgabe: `Gold: 5` – erwartet: `Gold: 15`');
  expect(out).toContain('Schwere Wörter: „f-String“');
  // input(): die automatische Eingabe kommt bei der geprüften Aufgabe an, nicht beim Beispiel davor
  expect(out).toMatch(/lektion-02 – Fragen[\s\S]*✅ \*\*Aufgabe 2\*\*/);
});

test('Prompt enthält Glossar früherer Wochen und die Lektion, aber nie eine Musterlösung', () => {
  const { root } = miniKurs();
  const out = run(['--content', root, '--wochen', '2', '--trocken', '--alter', '10']);
  expect(out).toContain('Du spielst ein 10-jähriges Kind');
  expect(out).toContain('| `print()` | Gibt Text aus |');
  expect(out).toContain('Mit `*` rechnest du mal.');
  expect(out).toContain('Bearbeite die Aufgaben 2, 3');
  expect(out).not.toContain('GEHEIME_MUSTERLOESUNG');
});
