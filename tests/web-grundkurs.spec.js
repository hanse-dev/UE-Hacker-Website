import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { readFileSync, existsSync } from 'fs';
import checks from '../content/web-grundkurs-checks/index.mjs';
import { WEB_GRUNDKURS_WEEKS } from '../src/data/webGrundkursWeeks.js';

// „Meine erste Website“, Stufe Intensiv (WebsiteCourse.vue → WeeklyCourseTour.vue): 9 Wochen
// HTML/CSS in der Web-Sandbox, je Woche Wochen-Check (content/web-grundkurs-checks/) mit Zertifikat.
// Die Inhaltstests laufen automatisch fuer jede Woche, deren Ordner existiert.
const COURSE_URL = '/kurs/web-erste-website';
const CHECK_KEY = 'ue-hacker-week-checks-web-grundkurs';
const weekDir = (n) => new URL(`../content/web-grundkurs-woche${n}/`, import.meta.url);
const WEEKS = WEB_GRUNDKURS_WEEKS.map((w) => w.number).filter((n) => existsSync(new URL('lessons.json', weekDir(n))));
const lessonsOf = (n) => JSON.parse(readFileSync(new URL('lessons.json', weekDir(n)), 'utf-8'));

const progressKey = (n) => `ue-hacker-interactive-progress-web-grundkurs-woche${n}`;

const completeWeek = (page, n, ids) =>
  page.addInitScript(
    ({ key, list, course }) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.setItem(key, JSON.stringify({ version: 1, courseId: course, variant: course, completedLessonIds: list }));
    },
    { key: progressKey(n), list: ids, course: `web-grundkurs-woche${n}` }
  );

const openWeek = async (page, n) => {
  await page.goto(`${COURSE_URL}?stufe=intensiv&week=${n}`);
  await expect(page.locator('.stepper-step').first()).toBeVisible({ timeout: 15000 });
};

test.describe('Meine erste Website: Stufenwahl', () => {
  test.beforeEach(async ({ page }) => {
    // Nur beim allerersten Laden zuruecksetzen - der Test laedt spaeter neu, um das Merken zu pruefen.
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      if (!sessionStorage.getItem('stufe-reset')) {
        localStorage.removeItem('ue-hacker-website-stufe');
        sessionStorage.setItem('stufe-reset', '1');
      }
    });
  });

  test('Nach „Kurs starten“ wählt man Einfach oder Intensiv, die Wahl bleibt gemerkt und lässt sich wechseln', async ({ page }) => {
    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.stufe-card')).toHaveCount(2);

    await page.locator('.stufe-card[data-stufe="intensiv"]').click();
    await expect(page.locator('.week-tile')).toHaveCount(WEB_GRUNDKURS_WEEKS.length);
    await expect(page.locator('.week-tile').first()).toContainText(WEB_GRUNDKURS_WEEKS[0].title);
    await expect(page).toHaveURL(/stufe=intensiv/);

    // Neu laden ohne ?stufe=: die Wahl ist gemerkt.
    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.week-tile').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.stufe-current')).toContainText('Intensiv');

    await page.locator('.btn-change-stufe').click();
    await page.locator('.stufe-card[data-stufe="einfach"]').click();
    await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.final-check-item')).toBeVisible();
  });

  test('Alter Profil-Link ?week=1 ohne Stufe führt weiter zum Abschluss-Check von Einfach', async ({ page }) => {
    await page.goto(`${COURSE_URL}?week=1`);
    await expect(page.locator('.stufe-current')).toContainText('Einfach', { timeout: 15000 });
  });

  test('Wochen ohne Inhalt sind gesperrt', async ({ page }) => {
    await page.goto(`${COURSE_URL}?stufe=intensiv&started=1`);
    await expect(page.locator('.week-tile')).toHaveCount(WEB_GRUNDKURS_WEEKS.length, { timeout: 15000 });
    await expect(page.locator('.week-tile:not(.locked)')).toHaveCount(WEEKS.length);
  });
});

test.describe('Meine erste Website, Intensiv: Wochen', () => {
  for (const n of WEEKS) {
    const lessons = lessonsOf(n);

    for (const [lessonIdx, lesson] of lessons.entries()) {
      test(`Woche ${n}, ${lesson.title}: Vorlagen fallen durch, Musterlösungen bestehen`, async ({ page }) => {
        test.setTimeout(60000);
        await completeWeek(page, n, lessons.map((l) => l.id));
        await openWeek(page, n);
        await page.locator('.stepper-step').nth(lessonIdx).click();
        await expect(page.locator('.task-block')).toHaveCount(lesson.tasks.length);

        for (const [idx, task] of lesson.tasks.entries()) {
          const block = page.locator('.task-block').nth(idx);
          if (task.example) {
            await block.locator('.btn-run').click();
            await expect(block.locator('.task-done')).toBeVisible({ timeout: 10000 });
            continue;
          }
          await block.locator('.btn-check').click();
          await expect(block.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
          await setCodeMirrorContent(block.locator('.cm-host'), task.solution);
          await block.locator('.btn-check').click();
          await expect(block.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
        }
      });
    }

    test(`Woche ${n}: Wochen-Check mit Web-Aufgaben verleiht das Zertifikat`, async ({ page }) => {
      test.setTimeout(90000);
      await completeWeek(page, n, lessons.map((l) => l.id));
      await page.addInitScript((key) => localStorage.removeItem(key), CHECK_KEY);
      await openWeek(page, n);
      await page.locator('[data-open-check]').click();
      await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });

      const week = checks.weeks[String(n)];
      for (const [idx, challenge] of week.codingChallenges.entries()) {
        const box = page.locator(`.web-code-challenge[data-challenge-index="${idx}"]`);
        await box.locator('.btn-check').click();
        await expect(box.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
        await setCodeMirrorContent(box.locator('.cm-host'), challenge.solution);
        await box.locator('.btn-check').click();
        await expect(box.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
      }

      const squash = (str) => str.replace(/\s+/g, ' ').trim();
      const cards = page.locator('.quiz-question');
      const count = await cards.count();
      expect(count).toBe(checks.weekCheckCount);
      for (let i = 0; i < count; i++) {
        const card = cards.nth(i);
        const text = squash(await card.locator('.question-text').innerText());
        const q = week.questions.find((x) => text.includes(squash(x.question)));
        expect(q, text).toBeTruthy();
        const buttons = card.locator('.option-btn');
        const total = await buttons.count();
        for (let b = 0; b < total; b++) {
          if (squash(await buttons.nth(b).innerText()) === squash(q.options[q.correctIndex])) {
            await buttons.nth(b).click();
            break;
          }
        }
      }
      await page.locator('.btn-check-quiz').click();
      await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
      await expect(page.locator('.certificate-login-hint')).toBeVisible();
    });
  }

  test('Content-Regeln: jede Woche hat Lektionen, Debug und Mission; jede Pflichtaufgabe Lösung und Hinweise; jeder Check 2 Web-Aufgaben', () => {
    expect(WEEKS.length).toBeGreaterThan(0);
    for (const n of WEEKS) {
      const lessons = lessonsOf(n);
      expect(lessons.map((l) => l.section), `Woche ${n}`).toEqual(expect.arrayContaining(['lektion', 'debug', 'mission']));
      for (const lesson of lessons) {
        for (const task of lesson.tasks) {
          expect(task.validation.type, `Woche ${n} ${lesson.id}`).toBe('web');
          if (task.example) continue;
          expect(task.solution, `Woche ${n} ${lesson.id}`).toBeTruthy();
          for (const c of task.validation.checks) expect(c.hint, `Woche ${n} ${lesson.id}`).toBeTruthy();
        }
      }
      // Jedes verwendete Bild gibt es wirklich unter public/web-bilder/.
      const used = JSON.stringify([lessons, checks.weeks[String(n)]]).match(/\/web-bilder\/[a-z]+\.svg/g) || [];
      for (const src of new Set(used)) {
        expect(existsSync(new URL(`../public${src}`, import.meta.url)), `Woche ${n}: ${src}`).toBe(true);
      }
      const week = checks.weeks[String(n)];
      expect(week, `Check für Woche ${n}`).toBeTruthy();
      expect(week.questions.length).toBeGreaterThanOrEqual(checks.weekCheckCount);
      expect(week.codingChallenges).toHaveLength(2);
      for (const c of week.codingChallenges) {
        expect(c.validation.type).toBe('web');
        expect(c.solution).toBeTruthy();
      }
    }
  });
});
