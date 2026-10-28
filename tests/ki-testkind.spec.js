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
    aendern: [{ stelle: 'Aufgabe 3', problem: 'Woher die 15 kommt, steht nirgends', haette_geholfen: 'Rechenweg nennen', gewicht: 'mittel' }],
  }));
  fs.writeFileSync(path.join(antworten, '2-lektion-02.json'), JSON.stringify({
    aufgaben: [{ nr: 2, verstanden: 'ja', was_ich_tun_soll: 'fragen', code: 'n = input("Name? ")\nprint(f"Hallo {n}")', unklar: '' }],
    schwere_woerter: ['Eingabe'], verwirrende_saetze: [], gesamteindruck: 'Leicht.', aendern: [],
  }));
  return { root, antworten };
}

const run = (args) => execFileSync('python3', ['scripts/ki_testkind.py', ...args], { cwd: process.cwd(), encoding: 'utf8' });

test('Bericht: nur lohnende Änderungen als Tabelle, Code geprüft wie auf der Website', () => {
  const { root, antworten } = miniKurs();
  const out = run(['--content', root, '--wochen', '2', '--antworten', antworten]);
  expect(out).toContain('2 Lektionen geprüft, 1 davon ohne Änderungsbedarf. 2 Stellen lohnen eine Änderung, 1 davon wichtig');
  expect(out).toContain('| Woche | Lektion | Stelle | Problem | Hätte geholfen | Gewicht |');
  // Aufgabe 2 nutzt gold aus dem Beispiel (gleicher Kernel) und ist geschafft - keine Zeile.
  // Aufgabe 3 ist nicht geschafft: immer eine wichtige Zeile, mit dem, was unklar war
  expect(out).toContain('| 2 | lektion-01 – Rechnen | Aufgabe 3 | nicht geschafft: Ausgabe `Gold: 5` statt `Gold: 15` – Woher kommt 15? |  | **hoch** |');
  expect(out).toContain('| Aufgabe 3 | Woher die 15 kommt, steht nirgends | Rechenweg nennen | mittel |');
  expect(out).not.toContain('Aufgabe 2 |');
  // Lektion 2 ist insgesamt klar (aendern leer, Aufgabe mit input() geschafft): taucht nicht auf,
  // auch nicht wegen eines einzelnen schweren Worts
  expect(out).not.toContain('lektion-02');
});

test('Liste in expected: geschafft, wenn jeder Eintrag in der Ausgabe vorkommt (wie auf der Website)', () => {
  const { root, antworten } = miniKurs();
  const datei = path.join(root, 'python-woche2-abenteuer', 'lessons.json');
  const lessons = JSON.parse(fs.readFileSync(datei, 'utf8'));
  lessons[0].tasks[1].validation.expected = ['Gold:', '10'];
  fs.writeFileSync(datei, JSON.stringify(lessons));
  const out = run(['--content', root, '--wochen', '2', '--antworten', antworten]);
  expect(out).toContain('Aufgabe 3 | nicht geschafft');
  expect(out).not.toContain('Aufgabe 2 |');
});

test('Fehler in einer früheren Aufgabe (SyntaxError) bricht spätere nicht ab – wie getrennte Zellen auf der Website', () => {
  const { root, antworten } = miniKurs();
  const datei = path.join(antworten, '2-lektion-01.json');
  const a = JSON.parse(fs.readFileSync(datei, 'utf8'));
  a.aufgaben[0].code = 'print("Gold: " gold)'; // SyntaxError
  a.aufgaben[1].code = 'print("Gold: 15")';
  fs.writeFileSync(datei, JSON.stringify(a));
  const out = run(['--content', root, '--wochen', '2', '--antworten', antworten]);
  expect(out).toContain('| Aufgabe 2 | nicht geschafft: Ausgabe `Fehler: SyntaxError: invalid syntax');
  expect(out).not.toContain('Aufgabe 3 | nicht geschafft');
});

test('Prompt enthält Glossar früherer Wochen und die Lektion, aber nie eine Musterlösung', () => {
  const { root } = miniKurs();
  const out = run(['--content', root, '--wochen', '2', '--trocken', '--alter', '10']);
  expect(out).toContain('Du spielst ein 10-jähriges Kind');
  expect(out).toContain('"aendern": Nur die Stellen, an denen ein echtes Kind');
  expect(out).toContain('| `print()` | Gibt Text aus |');
  expect(out).toContain('Mit `*` rechnest du mal.');
  expect(out).toContain('Bearbeite die Aufgaben 2, 3');
  expect(out).not.toContain('GEHEIME_MUSTERLOESUNG');
});

// Anleitungs-Kurse (micro:bit, --kurs): nichts wird ausgeführt, das Test-Kind sagt je Abhakpunkt,
// ob es ohne Hilfe ankäme. Es sieht nur die gewählte Variante und Bilder als Beschreibung.
function miniGuide() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'ki-guide-'));
  const kurs = path.join(root, 'microbit-test');
  fs.mkdirSync(kurs, { recursive: true });
  fs.writeFileSync(path.join(kurs, 'beschreibung.md'), '**Ihr braucht:** einen micro:bit und eine LED.\n');
  fs.writeFileSync(path.join(kurs, 'lessons.json'), JSON.stringify([{
    id: 'lektion-01', title: 'Erste LED', file: 'lektion-01.md', lessonSummary: '',
    tasks: [{ instruction: 'Die LED leuchtet.' }, { instruction: 'Die LED blinkt.', isBonus: true }],
  }]));
  fs.writeFileSync(path.join(kurs, 'lektion-01.md'), [
    '# Erste LED', '', '<img src="/x.svg" alt="Steckplan: LED an P13">', '',
    ':::bloecke', '', 'BLOCK-TEXT', '', ':::', '', ':::python', '', 'PYTHON-TEXT', '', ':::', '',
  ].join('\n'));
  const antworten = fs.mkdtempSync(path.join(os.tmpdir(), 'ki-guide-antw-'));
  fs.writeFileSync(path.join(antworten, 'microbit-test-lektion-01.json'), JSON.stringify({
    aufgaben: [
      { nr: 1, schaffe_ich: 'ja', was_ich_tue: 'stecken', unklar: '' },
      { nr: 2, schaffe_ich: 'nein', was_ich_tue: '', unklar: 'Wie blinkt man?' },
    ],
    schwere_woerter: [], verwirrende_saetze: [], gesamteindruck: 'Ok.', aendern: [],
  }));
  return { root, antworten };
}

test('Anleitungs-Kurs: Prompt nur mit der gewählten Variante, Bilder als Beschreibung', () => {
  const { root } = miniGuide();
  const out = run(['--content', root, '--kurs', 'microbit-test', '--variante', 'python', '--trocken']);
  expect(out).toContain('Ihr programmiert mit Python');
  expect(out).toContain('PYTHON-TEXT');
  expect(out).not.toContain('BLOCK-TEXT');
  expect(out).toContain('[Bild: Steckplan: LED an P13]');
  expect(out).toContain('2. Die LED blinkt. (Bonus, freiwillig)');
});

test('Anleitungs-Kurs: "ohne Hilfe nicht geschafft" landet als wichtige Zeile im Bericht', () => {
  const { root, antworten } = miniGuide();
  const out = run(['--content', root, '--kurs', 'microbit-test', '--antworten', antworten]);
  expect(out).toContain('| Kurs | Lektion | Stelle |');
  expect(out).toContain('| microbit-test (bloecke) | lektion-01 – Erste LED | Abhaken 2 | ohne Hilfe nicht geschafft – Wie blinkt man? |  | **hoch** |');
  expect(out).not.toContain('Abhaken 1');
});

// --geaendert: nur Lektionen, die seit der Abzweigung neu sind oder sich geändert haben – auch
// noch nicht committete. Geprüft an einem kleinen Git-Repo mit Python- und micro:bit-Lektionen.
test('--geaendert findet geänderte Lektionen (Text und lessons.json), unveränderte nicht', () => {
  const repo = fs.mkdtempSync(path.join(os.tmpdir(), 'ki-geaendert-'));
  const py = path.join(repo, 'content', 'python-woche1-abenteuer');
  const mb = path.join(repo, 'content', 'microbit-test');
  fs.mkdirSync(py, { recursive: true });
  fs.mkdirSync(mb, { recursive: true });
  const pyTask = { instruction: 'Gib Hallo aus.', codeTemplate: '', validation: { type: 'output_contains', expected: 'Hallo' } };
  fs.writeFileSync(path.join(py, 'lessons.json'), JSON.stringify([
    { id: 'lektion-01', section: 'lektion', title: 'Eins', file: 'lektion-01.md', lessonSummary: '', tasks: [pyTask] },
    { id: 'lektion-02', section: 'lektion', title: 'Zwei', file: 'lektion-02.md', lessonSummary: '', tasks: [pyTask] },
  ]));
  fs.writeFileSync(path.join(py, 'lektion-01.md'), '# Eins\n');
  fs.writeFileSync(path.join(py, 'lektion-02.md'), '# Zwei\n');
  const mbLessons = [{ id: 'lektion-01', title: 'LED', file: 'lektion-01.md', lessonSummary: '', tasks: [{ instruction: 'Die LED leuchtet.' }] }];
  fs.writeFileSync(path.join(mb, 'lessons.json'), JSON.stringify(mbLessons));
  fs.writeFileSync(path.join(mb, 'lektion-01.md'), '# LED\n');
  // Ohne GIT_DIR & Co.: Im Pre-commit-Hook zeigen sie auf das echte Repo. Ein `git init`/`commit`
  // im Mini-Repo landete sonst im Branch des Hooks (und setzte core.bare im Haupt-Repo).
  const env = Object.fromEntries(Object.entries(process.env).filter(([k]) => !k.startsWith('GIT_')));
  const git = (...a) => execFileSync('git', ['-C', repo, ...a], { encoding: 'utf8', env });
  git('init', '-q');
  git('add', '.');
  git('-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '-qm', 'basis');

  fs.writeFileSync(path.join(py, 'lektion-02.md'), '# Zwei\n\nNeuer Text.\n');
  mbLessons[0].tasks[0].instruction = 'Die rote LED leuchtet.';
  fs.writeFileSync(path.join(mb, 'lessons.json'), JSON.stringify(mbLessons));

  const out = execFileSync('python3', ['scripts/ki_testkind.py', '--content', path.join(repo, 'content'), '--geaendert', 'HEAD', '--trocken'],
    { cwd: process.cwd(), encoding: 'utf8', env });
  expect(out).toContain('Würde prüfen: 1 abenteuer lektion-02');
  expect(out).toContain('Würde prüfen: microbit-test lektion-01');
  expect(out).not.toContain('abenteuer lektion-01');
});
