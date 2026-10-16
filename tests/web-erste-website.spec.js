import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { readFileSync } from 'fs';
import checks from '../content/web-erste-website-checks/index.mjs';

const lessons = JSON.parse(readFileSync(new URL('../content/web-erste-website/lessons.json', import.meta.url), 'utf-8'));

const PROGRESS_KEY = 'ue-hacker-interactive-progress-web-erste-website';
const CHECK_KEY = 'ue-hacker-week-checks-web-erste-website';
const COURSE_URL = '/kurs/web-erste-website';

// Kurs A des Web-Tracks: Einstiegskurs (`"type": "lektionen"`) in der Lektionsliste von
// ProjectCourse.vue, Web-Sandbox (siehe tests/web-sandbox.spec.js), danach ein Abschluss-Check
// (`"finalCheck": true`, content/web-erste-website-checks/) mit Zertifikat.
const completeLessons = (page, ids) =>
  page.addInitScript(
    ({ key, ids: list }) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.setItem(key, JSON.stringify({
        version: 1, courseId: 'web-erste-website', variant: 'web-erste-website', completedLessonIds: list,
      }));
    },
    { key: PROGRESS_KEY, ids }
  );

const openCourse = async (page) => {
  // Stufe Einfach direkt waehlen (WebsiteCourse.vue), sonst kommt nach „Kurs starten“ die Stufenwahl.
  await page.goto(`${COURSE_URL}?stufe=einfach`);
  await page.locator('.btn-start-course').click();
  await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 15000 });
};

const preview = (page) => page.frameLocator('.js-workspace iframe.js-sandbox');

test.describe('Meine erste Website: Lektionen', () => {
  // Jede Lektion einzeln: Beispiele laufen durch, jede Pflichtaufgabe faellt mit der
  // unveraenderten Vorlage durch und besteht mit der Musterloesung.
  for (const [lessonIdx, lesson] of lessons.entries()) {
    test(`Lektion ${lessonIdx + 1} „${lesson.title}“: Vorlagen fallen durch, Musterloesungen bestehen`, async ({ page }) => {
      test.setTimeout(60000);
      await completeLessons(page, lessons.map((l) => l.id));
      await openCourse(page);
      await page.locator('.lesson-item').nth(lessonIdx).click();
      await expect(page.locator('.task-block')).toHaveCount(lesson.tasks.length);

      for (const [idx, task] of lesson.tasks.entries()) {
        const block = page.locator('.task-block').nth(idx);
        if (task.example) {
          await block.locator('.btn-run').click();
          await expect(block.locator('.task-done')).toBeVisible({ timeout: 10000 });
          continue;
        }
        expect(task.solution, `Lektion ${lessonIdx + 1}, Aufgabe ${idx + 1} braucht eine Musterloesung`).toBeTruthy();
        for (const check of task.validation.checks) {
          expect(check.hint, `Lektion ${lessonIdx + 1}, Aufgabe ${idx + 1}: jede Pruefung braucht einen Hinweis`).toBeTruthy();
        }
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
        await setCodeMirrorContent(block.locator('.cm-host'), task.solution);
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
      }
    });
  }

  test('Bilder aus /web-bilder/ erscheinen in der Vorschau', async ({ page }) => {
    await completeLessons(page, lessons.map((l) => l.id));
    await openCourse(page);
    await page.locator('.lesson-item').nth(2).click();
    await page.locator('.task-block').nth(0).locator('.btn-run').click();
    const img = preview(page).locator('img');
    await expect(img).toHaveAttribute('src', '/web-bilder/katze.svg', { timeout: 10000 });
    await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth), { timeout: 10000 }).toBeGreaterThan(0);
  });

  test('Bilderliste im Lektionstext passt zu den Dateien in public/web-bilder/', () => {
    const text = readFileSync(new URL('../content/web-erste-website/lektion-03.md', import.meta.url), 'utf-8');
    const line = text.split('\n').find((l) => l.startsWith('**Bilder zum Aussuchen:**'));
    const named = [...line.matchAll(/`([a-z]+)`/g)].map((m) => m[1]);
    expect(named.length).toBeGreaterThan(10);
    for (const name of named) {
      expect(() => readFileSync(new URL(`../public/web-bilder/${name}.svg`, import.meta.url)), name).not.toThrow();
    }
    // Jede Vorlage/Loesung nutzt nur Bilder, die es wirklich gibt.
    const used = JSON.stringify(lessons).match(/\/web-bilder\/[a-z]+\.svg/g) || [];
    for (const src of used) expect(named, src).toContain(src.replace('/web-bilder/', '').replace('.svg', ''));
  });
});

test.describe('Meine erste Website: Kurs und Abschluss-Check', () => {
  test('Startseite zeigt den Kurs als Einstieg, die Projekte-Uebersicht nicht', async ({ page }) => {
    await page.goto('/');
    const card = page.locator(`a.course-card[href="${COURSE_URL}"]`);
    await expect(card).toBeVisible({ timeout: 15000 });
    await expect(card.locator('.course-format-badge')).toHaveText('Einstieg');
    await page.goto('/projekte');
    await expect(page.locator('a.projekt-card').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator(`a.projekt-card[href="${COURSE_URL}"]`)).toHaveCount(0);
  });

  test('Abschluss-Check ist gesperrt, bis alle Lektionen erledigt sind', async ({ page }) => {
    await completeLessons(page, lessons.slice(0, -1).map((l) => l.id));
    await openCourse(page);
    const item = page.locator('.final-check-item');
    await expect(item).toHaveClass(/locked/);
    await item.click();
    await expect(page.locator('.week-check-panel')).toHaveCount(0);
  });

  test('Letzte Lektion fuehrt mit „Zum Abschluss-Check“ direkt zum Check', async ({ page }) => {
    test.setTimeout(60000);
    await completeLessons(page, lessons.slice(0, -1).map((l) => l.id));
    await openCourse(page);
    const last = lessons.length - 1;
    await page.locator('.lesson-item').nth(last).click();
    for (const [idx, task] of lessons[last].tasks.entries()) {
      const block = page.locator('.task-block').nth(idx);
      if (task.example) {
        await block.locator('.btn-run').click();
        await expect(block.locator('.task-done')).toBeVisible({ timeout: 10000 });
      } else {
        await setCodeMirrorContent(block.locator('.cm-host'), task.solution);
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
      }
    }
    await page.locator('.lesson-complete-box .btn-next').click();
    await expect(page.locator('.week-check-panel h3')).toHaveText('Abschluss-Check', { timeout: 15000 });
    await expect(page.locator('.final-check-item')).toHaveClass(/active/);
  });

  test('Quiz + beide Web-Aufgaben bestehen → Zertifikat, ohne Login nur mit Hinweis', async ({ page }) => {
    test.setTimeout(90000);
    await completeLessons(page, lessons.map((l) => l.id));
    await page.addInitScript((key) => localStorage.removeItem(key), CHECK_KEY);
    await openCourse(page);
    await page.locator('.final-check-item').click();
    await expect(page.locator('.week-check-panel')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.final-check-pending')).toBeVisible();

    const week = checks.weeks['1'];
    for (const [idx, challenge] of week.codingChallenges.entries()) {
      const box = page.locator(`.web-code-challenge[data-challenge-index="${idx}"]`);
      await box.locator('.btn-check').click();
      await expect(box.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
      await setCodeMirrorContent(box.locator('.cm-host'), challenge.solution);
      await box.locator('.btn-check').click();
      await expect(box.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
      await expect(box.locator('iframe.js-sandbox')).toBeVisible();
    }
    await expect(page.locator('.certificate-reveal')).toHaveCount(0);

    // Quiz: jede gezogene Frage ueber ihren Text im Check-Content finden und richtig beantworten.
    const cards = page.locator('.quiz-question');
    const count = await cards.count();
    expect(count).toBe(checks.weekCheckCount);
    for (let i = 0; i < count; i++) {
      const card = cards.nth(i);
      const squash = (str) => str.replace(/\s+/g, ' ').trim();
      const text = squash(await card.locator('.question-text').innerText());
      const q = week.questions.find((x) => text.includes(squash(x.question)));
      expect(q, text).toBeTruthy();
      await card.locator('.option-btn', { hasText: q.options[q.correctIndex] }).first().click();
    }
    await page.locator('.btn-check-quiz').click();

    await expect(page.locator('.certificate-reveal')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.certificate-reveal')).toContainText('Meine erste Website');
    await expect(page.locator('.certificate-login-hint')).toBeVisible();
    await expect(page.locator('.final-check-item')).toHaveClass(/completed/);
    const stored = await page.evaluate((key) => JSON.parse(localStorage.getItem(key)), CHECK_KEY);
    expect(stored.weeks['1']).toMatchObject({ quizPassed: true, codingPassed: { 0: true, 1: true } });
  });

  test('Profil-Link ?week=1 oeffnet den Abschluss-Check direkt', async ({ page }) => {
    await completeLessons(page, lessons.map((l) => l.id));
    await page.goto(`${COURSE_URL}?week=1`);
    await expect(page.locator('.week-check-panel h3')).toHaveText('Abschluss-Check', { timeout: 15000 });
  });

  test('Check-Content: jede Coding-Aufgabe hat Vorlage, Musterloesung und Hinweise; Lernziele fuers Zertifikat', () => {
    const week = checks.weeks['1'];
    expect(Object.keys(checks.weeks)).toEqual(['1']);
    expect(week.lernziele.length).toBeGreaterThan(2);
    expect(week.questions.length).toBeGreaterThanOrEqual(checks.weekCheckCount);
    expect(week.codingChallenges).toHaveLength(2);
    for (const c of week.codingChallenges) {
      expect(c.validation.type).toBe('web');
      expect(c.solution).toBeTruthy();
      for (const check of c.validation.checks) expect(check.hint).toBeTruthy();
    }
  });
});
