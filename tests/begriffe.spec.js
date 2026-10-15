import { test, expect } from '@playwright/test';
import { readFileSync, existsSync } from 'fs';

const readJson = (rel) => JSON.parse(readFileSync(new URL(`../${rel}`, import.meta.url), 'utf-8'));
const KURSE = readJson('public/kurse.json');
const BEGRIFFE = readJson('content/begriffe.json');

// Kurse mit Begriffs-Links, die nicht automatisch über `type: "projekt"` + `language` laufen:
// Die Tour reicht conceptLanguage/conceptCourse/conceptWeek selbst durch (HANDOFF 3.110).
const LINKED_COURSES = ['js-grundkurs', 'python-12-wochen-grundkurs', 'ki-labor'];

// Bewusst ohne Begriffs-Links - jeder Eintrag mit Grund. Ein neuer Kurs muss entweder Links
// bekommen oder hier mit Begründung stehen (siehe INHALTE.md §6).
const WITHOUT_LINKS = {
  'python-einstufung': 'Einstufungstest, kein Lernstoff zum Nachschlagen',
  'python-grundlagen-interaktiv': 'hat eigene Glossar-Tooltips (glossary.json), beides würde doppelt markieren',
  ferienkurse: 'Info- und Terminseite, keine Lektionen',
  'projekt-microbit-auto': 'micro:bit (MakeCode/MicroPython, eigene Anleitungs-Ansicht), keine Begriffsliste',
  'projekt-microbit-ampel': 'micro:bit (MakeCode/MicroPython, eigene Anleitungs-Ansicht), keine Begriffsliste',
};

// Zielordner einer Grundkurs-Woche (für die Prüfung, dass `lektion` dort wirklich vorkommt).
const WEEK_FOLDER = {
  'js-grundkurs': (w) => `content/js-grundkurs-woche${w}`,
  'python-12-wochen-grundkurs': (w) => `content/python-woche${w}-abenteuer`,
};

// Begriffe verlinken auf die Grundkurs-Woche, in der sie erklärt werden (useConcepts.js,
// content/begriffe.json): im Lektionstext beim ersten Vorkommen als Link, am Ende der Lektion als
// Kasten "Neu oder unklar? Hier lernst du mehr darüber". In Projekten auf jede Woche, in den
// Grundkursen selbst nur auf frühere Wochen; das KI-Labor verweist auf den Python-Grundkurs.
const openProject = async (page, courseId) => {
  await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
  await page.goto(`/kurs/${courseId}`);
  await page.locator('.btn-start-course').click();
  await expect(page.locator('.lesson-content h1').first()).toBeVisible({ timeout: 15000 });
};

test.describe('Begriffe verlinken auf die Grundkurse (Projekte und Kurse)', () => {
  test('JS-Projekt: "Array" verlinkt auf JS-Grundkurs Woche 5, Kasten am Lektionsende', async ({ page }) => {
    await openProject(page, 'projekt-js-quiz');
    const content = page.locator('.lesson-content');

    const arrayLinks = content.locator('a.concept-link[href="/kurs/js-grundkurs?week=5"]');
    // Nur das erste Vorkommen ist ein Link, auch wenn "Array" öfter im Text steht.
    await expect(arrayLinks).toHaveCount(1);
    await expect(arrayLinks).toHaveText(/^Arrays?$/);
    await expect(arrayLinks).toHaveAttribute('target', '_blank');
    await expect(arrayLinks).toHaveAttribute('title', /Woche 5/);
    // Nie in Code-Blöcken oder Überschriften.
    await expect(content.locator('pre a.concept-link, code a.concept-link, h1 a.concept-link')).toHaveCount(0);

    const box = content.locator('.concept-box');
    await expect(box).toContainText('Neu oder unklar?');
    // Jeder Begriff nur einmal im Kasten, auch wenn er in Text und Aufgaben vorkommt.
    const items = box.locator('.concept-box-item');
    const names = await items.locator('strong').allTextContents();
    expect(names.length).toBeGreaterThan(1);
    expect(new Set(names).size).toBe(names.length);
    const item = box.locator('.concept-box-item', { hasText: 'Array' }).first();
    await expect(item.locator('a.concept-box-link')).toHaveAttribute('href', '/kurs/js-grundkurs?week=5');
    await expect(item).toContainText('JavaScript-Grundkurs, Woche 5');
  });

  test('Python-Projekt: "Dictionary" verlinkt auf den Python-Grundkurs Woche 8', async ({ page }) => {
    await openProject(page, 'projekt-morsecode');
    const content = page.locator('.lesson-content');
    await expect(content.locator('a.concept-link[href="/kurs/python-12-wochen-grundkurs?week=8"]')).toHaveCount(1);
    await expect(content.locator('.concept-box')).toContainText('Python-Grundkurs (12 Wochen), Woche 8');
  });

  test('der Link landet in der richtigen Grundkurs-Woche', async ({ page }) => {
    await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
    await page.goto('/kurs/js-grundkurs?week=5');
    await expect(page.getByText('Arrays: mehrere Werte in einer Variable').first()).toBeVisible({ timeout: 15000 });
  });

  test('jeder Kurs hat Begriffs-Links oder steht mit Grund auf der Ausnahmeliste', () => {
    const missing = [];
    for (const kurs of KURSE) {
      const automatic = kurs.type === 'projekt' && Array.isArray(BEGRIFFE[kurs.language]);
      if (automatic || LINKED_COURSES.includes(kurs.id) || WITHOUT_LINKS[kurs.id]) continue;
      missing.push(kurs.id);
    }
    expect(
      missing,
      'Neue Kurse ohne Entscheidung zu Begriffs-Links. Projekt: `language` (javascript/python) in '
        + 'kurse.json setzen; Kurs mit eigener Tour: conceptLanguage/conceptCourse/conceptWeek '
        + 'durchreichen und in LINKED_COURSES eintragen; sonst mit Grund in WITHOUT_LINKS.',
    ).toEqual([]);
    // Ausnahmeliste und Link-Liste nur mit Kursen, die es wirklich gibt.
    const ids = KURSE.map((k) => k.id);
    for (const id of [...LINKED_COURSES, ...Object.keys(WITHOUT_LINKS)]) expect(ids, id).toContain(id);
  });

  test('jeder Begriff zeigt auf eine existierende Woche mit passender Lektion', () => {
    const ids = KURSE.map((k) => k.id);
    for (const [lang, list] of Object.entries(BEGRIFFE)) {
      if (!Array.isArray(list)) continue;
      for (const c of list) {
        const where = `${lang}: ${c.begriff}`;
        expect(ids, where).toContain(c.kurs);
        expect(Object.keys(BEGRIFFE.kurse), where).toContain(c.kurs);
        expect(c.formen.length, where).toBeGreaterThan(0);
        const folder = WEEK_FOLDER[c.kurs]?.(c.woche);
        expect(folder, `${where}: unbekannter Zielkurs`).toBeTruthy();
        expect(existsSync(new URL(`../${folder}/lessons.json`, import.meta.url)), `${where}: Woche ${c.woche} fehlt`).toBe(true);
        const raw = readJson(`${folder}/lessons.json`);
        const titles = (Array.isArray(raw) ? raw : raw.lessons).map((l) => l.title);
        expect(titles.some((t) => t.includes(c.lektion)), `${where}: Lektion „${c.lektion}“ nicht in Woche ${c.woche}`).toBe(true);
      }
    }
  });

  const openWeek = async (page, url, lang = 'de') => {
    await page.addInitScript((l) => localStorage.setItem('ue-hacker-lang', l), lang);
    await page.goto(url);
    await expect(page.locator('.lesson-content h1').first()).toBeVisible({ timeout: 20000 });
  };

  const linkedWeeks = async (page, course) => page.locator(`a.concept-link[href^="/kurs/${course}?"]`)
    .evaluateAll((as) => as.map((a) => Number(new URL(a.href).searchParams.get('week'))));

  test('JS-Grundkurs: verlinkt nur auf frühere Wochen (Woche 6: Array → Woche 5, Objekt nicht)', async ({ page }) => {
    await openWeek(page, '/kurs/js-grundkurs?week=6');
    const content = page.locator('.lesson-content');
    await expect(content.locator('a.concept-link[href="/kurs/js-grundkurs?week=5"]')).toHaveCount(1);
    // Die aktuelle Woche erklärt Objekte gerade selbst - kein Verweis darauf.
    await expect(content).toContainText('Objekt');
    expect((await linkedWeeks(page, 'js-grundkurs')).every((w) => w < 6)).toBe(true);
    await expect(content.locator('.concept-box')).toContainText('Array');
  });

  test('JS-Grundkurs Woche 3: "Schleife" verweist nicht auf die eigene Woche', async ({ page }) => {
    await openWeek(page, '/kurs/js-grundkurs?week=3');
    await expect(page.locator('.lesson-content')).toContainText('Schleife');
    await expect(page.locator('a.concept-link[href="/kurs/js-grundkurs?week=3"]')).toHaveCount(0);
    expect((await linkedWeeks(page, 'js-grundkurs')).every((w) => w < 3)).toBe(true);
  });

  test('Python-Grundkurs Woche 6: nur Verweise auf Woche 1–5', async ({ page }) => {
    await openWeek(page, '/kurs/python-12-wochen-grundkurs?week=6&variant=abenteuer');
    const weeks = await linkedWeeks(page, 'python-12-wochen-grundkurs');
    expect(weeks.length).toBeGreaterThan(0);
    expect(weeks.every((w) => w < 6)).toBe(true);
  });

  test('KI-Labor: Python-Begriffe verlinken auf den Python-Grundkurs', async ({ page }) => {
    await openWeek(page, '/kurs/ki-labor?week=3');
    await expect(page.locator('.lesson-content a.concept-link[href="/kurs/python-12-wochen-grundkurs?week=5"]')).toHaveCount(1);
  });

  test('auf Englisch keine Begriffs-Links (die Erklärungen sind deutsch)', async ({ page }) => {
    await openWeek(page, '/kurs/js-grundkurs?week=6', 'en');
    await expect(page.locator('a.concept-link')).toHaveCount(0);
    await expect(page.locator('.concept-box')).toHaveCount(0);
  });
});
