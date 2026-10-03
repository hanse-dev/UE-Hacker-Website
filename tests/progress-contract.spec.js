import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import { collect, dbSchema, diffContract, FIXTURE } from '../scripts/progress-contract.mjs';

// Schutz fuer gespeicherten Fortschritt (Account-Datenbank + localStorage): Was Lernende schon
// erreicht haben, haengt an Lektions-IDs, Content-Ordnernamen, Quizfragen-IDs, der Position der
// Coding-Aufgaben, Storage-Keys/-Versionen und dem DB-Schema. Der Stand ist in
// tests/fixtures/progress-contract.json eingefroren. Dazukommen darf alles, wegfallen nichts.
//
// Schlaegt der Test an: Aenderung zuruecknehmen ODER eine Migration fuer bestehende Daten bauen
// und den Stand danach bewusst neu einfrieren: npm run contract:update
const HINWEIS = '\nGespeicherter Fortschritt würde brechen. Entweder die Änderung zurücknehmen oder eine Migration '
  + 'für bestehende Daten bauen und danach "npm run contract:update" ausführen (siehe WORKFLOW.md).';

test.describe('Fortschritts-Vertrag: ein Deploy darf gespeicherten Fortschritt nicht brechen', () => {
  const frozen = JSON.parse(fs.readFileSync(FIXTURE, 'utf8'));

  test('aktueller Stand entfernt oder verändert nichts, woran gespeicherter Fortschritt hängt', () => {
    const problems = diffContract(frozen, collect(), dbSchema().migrated);
    expect(problems, problems.join('\n') + HINWEIS).toEqual([]);
  });

  test('der Vergleich erkennt entfernte Lektionen, Fragen, Aufgaben, Keys, Versionen und Spalten', () => {
    const kaputt = JSON.parse(JSON.stringify(frozen));
    const ordner = Object.keys(kaputt.lessons)[0];
    const entfernteLektion = kaputt.lessons[ordner].pop();
    const check = Object.keys(kaputt.checks)[0];
    const entfernteFrage = kaputt.checks[check]['week-1'].questions.pop();
    kaputt.checks[check]['week-1'].coding -= 1;
    kaputt.courses.pop();
    kaputt.storage.keys.pop();
    kaputt.storage.versions[Object.keys(kaputt.storage.versions)[0]] += 1;
    kaputt.db.users.pop();
    kaputt.db.progress.push('neue_spalte');

    const problems = diffContract(frozen, kaputt).join('\n');
    expect(problems).toContain(`Lektion "${entfernteLektion}" fehlt`);
    expect(problems).toContain(`Quizfrage "${entfernteFrage}" fehlt`);
    expect(problems).toContain('Coding-Aufgaben');
    expect(problems).toContain('Kurs-ID');
    expect(problems).toContain('Storage-Key');
    expect(problems).toContain('Daten-Version');
    expect(problems).toContain('DB-Spalte users.');
    expect(problems).toContain('Neue DB-Spalte progress.neue_spalte ohne');
  });

  test('neue Kurse, Lektionen, Fragen und migrierte Spalten sind erlaubt', () => {
    const erweitert = JSON.parse(JSON.stringify(frozen));
    erweitert.lessons['neuer-kurs'] = ['lektion-01'];
    erweitert.lessons[Object.keys(frozen.lessons)[0]].push('lektion-99');
    erweitert.courses.push('neuer-kurs');
    erweitert.db.users.push('email');
    expect(diffContract(frozen, erweitert, ['users.email'])).toEqual([]);
  });
});
