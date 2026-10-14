import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { existsSync, readFileSync } from 'fs';

const CONTENT = new URL('../content/js-quiz/', import.meta.url);
const lessons = JSON.parse(readFileSync(new URL('lessons.json', CONTENT), 'utf-8'));
const STORAGE_KEY = 'ue-hacker-interactive-progress-js-quiz';

// Projekt-Kurs "Quiz-Generator" (projekt-js-quiz): erstes JS-Projekt auf der DOM-Uebungsflaeche
// statt auf dem Canvas (`"sandbox": "dom"` in kurse.json -> ProjectCourse.vue reicht `domMode` an
// JsLessonView.vue durch). Die Antwort-Knoepfe erzeugt der Code der Lernenden selbst
// (createElement, IDs antwort-0..2) - geprueft wird ueber `dom_text`/`dom_click_text`.
async function openCourse(page, completedLessonIds = []) {
  await page.addInitScript(
    ({ key, ids }) => {
      localStorage.removeItem('ue-hacker-lang');
      if (ids.length) {
        localStorage.setItem(
          key,
          JSON.stringify({ version: 1, courseId: 'projekt-js-quiz', variant: 'js-quiz', completedLessonIds: ids })
        );
      } else {
        localStorage.removeItem(key);
      }
    },
    { key: STORAGE_KEY, ids: completedLessonIds }
  );
  await page.goto('/kurs/projekt-js-quiz');
  await page.locator('.btn-start-course').click();
  await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
}

test.describe('Projekt: Quiz-Generator (JS, DOM-Sandbox)', () => {
  test('Inhalt: jede Aufgabe hat eine Prüfung, jede Pflichtaufgabe eine Musterlösung, jede Lektion ihren Text', () => {
    expect(lessons.length).toBe(7);
    for (const lesson of lessons) {
      expect(existsSync(new URL(lesson.file, CONTENT)), `${lesson.id}: ${lesson.file} fehlt`).toBe(true);
      expect(lesson.lessonSummary, lesson.id).toBeTruthy();
      // Die letzte Aufgabe jeder Lektion ist eine echte Pflichtaufgabe (kein reines Beispiel).
      expect(lesson.tasks.at(-1).example, `${lesson.id}: endet mit einem Beispiel`).toBeFalsy();
      for (const [idx, task] of lesson.tasks.entries()) {
        const where = `${lesson.id} Aufgabe ${idx}`;
        const v = task.validation;
        expect(v?.type, where).toBeTruthy();
        // dom_*-Typen pruefen ueber `text`, die Ausgabe-Typen ueber `expected`.
        if (v.type.startsWith('dom_')) {
          expect(v.target, where).toBeTruthy();
          expect(v.text, where).toBeTruthy();
          expect(v.expected, where).toBeUndefined();
        } else {
          expect(v.expected, where).toBeTruthy();
        }
        if (!task.example) {
          expect(task.solution, `${where}: keine Musterlösung`).toBeTruthy();
          expect(task.codeTemplate, where).toContain('Dein Code hier');
          expect(task.solution, where).not.toContain('Dein Code hier');
        }
      }
    }
  });

  test('Kurs steht in der Projekte-Übersicht und lädt mit der DOM-Übungsfläche statt Canvas', async ({ page }) => {
    await page.goto('/projekte');
    const card = page.locator('a.projekt-card[href="/kurs/projekt-js-quiz"]');
    await expect(card).toBeVisible({ timeout: 15000 });
    await expect(card).toContainText('Quiz-Generator');
    await expect(card).toContainText('JavaScript');

    await openCourse(page);
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(7);
    await expect(page.locator('.btn-kernel')).toHaveCount(0);

    // Letzte Aufgabe von Lektion 1 schreibt auf die Uebungsflaeche: im iframe ist die feste
    // DOM-Flaeche sichtbar, das Canvas der Spiele-Projekte dagegen nicht.
    const task = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task.locator('.cm-host'), lessons[0].tasks[2].solution);
    await task.locator('.btn-run').click();
    const frame = task.frameLocator('iframe.js-sandbox');
    await expect(frame.locator('#ueberschrift')).toHaveText('Mein Quiz');
    await expect(frame.locator('#text')).toHaveText('Wie viele Beine hat eine Spinne?');
    await expect(frame.locator('canvas')).toBeHidden();
  });

  test('Falsche Lösung fällt durch, Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(45000);
    await openCourse(page);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);

    const [example, addQuestions, showQuestion] = [0, 1, 2].map((i) => page.locator('.task-block').nth(i));
    await example.locator('.btn-run').click();
    await expect(example.locator('.task-done')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(addQuestions.locator('.cm-host'), lessons[0].tasks[1].solution);
    await addQuestions.locator('.btn-check').click();
    await expect(addQuestions.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    // Zweite statt erste Frage angezeigt -> dom_text muss das ablehnen.
    const wrong = lessons[0].tasks[2].solution.replace('fragen[0].frage', 'fragen[1].frage');
    expect(wrong).not.toBe(lessons[0].tasks[2].solution);
    await setCodeMirrorContent(showQuestion.locator('.cm-host'), wrong);
    await showQuestion.locator('.btn-check').click();
    await expect(showQuestion.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);

    await setCodeMirrorContent(showQuestion.locator('.cm-host'), lessons[0].tasks[2].solution);
    await showQuestion.locator('.btn-check').click();
    await expect(showQuestion.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Punkte zählen nur richtige Antworten: wer jede Antwort zählt, fällt durch', async ({ page }) => {
    await openCourse(page, lessons.map((l) => l.id));
    await page.locator('.lesson-item').nth(4).click();
    await expect(page.locator('.lesson-item.active')).toContainText(lessons[4].title);

    // Scheinloesung: zaehlt den Punkt hinter dem if/else, also auch bei falschen Antworten. Nach
    // drei Klicks auf die erste Antwort stuenden dann 3 statt 2 Punkte da.
    const solution = lessons[4].tasks[2].solution;
    const counting = "    punkte++;\n    stand.textContent = 'Punkte: ' + punkte;\n";
    expect(solution).toContain(counting);
    const cheat = solution.replace(counting, '').replace('  nummer++;', counting + '  nummer++;');
    const task = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task.locator('.cm-host'), cheat);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(task.frameLocator('iframe.js-sandbox').locator('#punkte')).toHaveText('Punkte: 3');
  });

  test('Kompletter Durchlauf: keine Vorlage besteht unverändert, jede Musterlösung besteht ihre Prüfung', async ({ page }) => {
    test.setTimeout(180000);
    await openCourse(page, lessons.map((l) => l.id));

    for (const [lessonIdx, lesson] of lessons.entries()) {
      await page.locator('.lesson-item').nth(lessonIdx).click();
      await expect(page.locator('.lesson-item.active')).toContainText(lesson.title);
      await expect(page.locator('.task-block')).toHaveCount(lesson.tasks.length);

      for (const [taskIdx, task] of lesson.tasks.entries()) {
        const where = `${lesson.id} Aufgabe ${taskIdx}`;
        const block = page.locator('.task-block').nth(taskIdx);

        if (task.example) {
          // Beispiele haben keinen Pruefen-Button; ihre validation muss trotzdem zum
          // unveraenderten Code passen. Dafuer wird sie hier ueber den Pflichtaufgaben-Weg
          // einer Kopie nicht nachgebaut, sondern direkt im iframe nachgeschaut.
          await block.locator('.btn-run').click();
          await expect(block.locator('.task-done'), where).toBeVisible({ timeout: 10000 });
          const v = task.validation;
          const frame = block.frameLocator('iframe.js-sandbox');
          if (v.type === 'dom_text') {
            await expect(frame.locator(`#${v.target}`), where).toHaveText(v.text);
          } else if (v.type === 'dom_click_text') {
            for (let n = 0; n < (v.clicks || 1); n++) {
              await frame.locator(`#${v.click}`).click();
            }
            await expect(frame.locator(`#${v.target}`), where).toHaveText(v.text);
          } else {
            await expect(block.locator('.output-content'), where).toContainText(v.expected);
          }
          continue;
        }

        // Die unveraenderte Vorlage darf die Aufgabe nicht schon loesen.
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-error'), `${where}: Vorlage besteht unverändert`).toBeVisible({ timeout: 10000 });

        await setCodeMirrorContent(block.locator('.cm-host'), task.solution);
        await block.locator('.btn-check').click();
        await expect(block.locator('.feedback-success'), where).toBeVisible({ timeout: 10000 });
      }
    }
  });

  test('Das fertige Quiz ist wirklich spielbar: Rückmeldung, Punkte, Auswertung, nochmal spielen', async ({ page }) => {
    test.setTimeout(45000);
    await openCourse(page, lessons.map((l) => l.id));
    await page.locator('.lesson-item').nth(6).click();
    await expect(page.locator('.lesson-item.active')).toContainText(lessons[6].title);

    // Musterloesung von "Nochmal spielen" ohne die drei automatischen Test-Antworten am Ende -
    // so spielt der Test das Quiz von der ersten Frage an selbst durch, wie ein Kind es tut.
    const solution = lessons[6].tasks[0].solution;
    const autoplay = solution.indexOf('// Test:');
    expect(autoplay).toBeGreaterThan(0);
    const task = page.locator('.task-block').nth(0);
    await setCodeMirrorContent(task.locator('.cm-host'), solution.slice(0, autoplay));
    await task.locator('.btn-run').click();

    const frame = task.frameLocator('iframe.js-sandbox');
    const answer = (i) => frame.locator(`#antwort-${i}`);
    await expect(frame.locator('#ueberschrift')).toHaveText('Mein Quiz');
    await expect(frame.locator('#text')).toHaveText('Wie viele Beine hat eine Spinne?');
    await expect(answer(0)).toHaveText('6');
    await expect(answer(1)).toHaveText('8');
    await expect(answer(2)).toHaveText('10');
    await expect(frame.locator('#knopf')).toBeHidden();
    await expect(frame.locator('#punkte')).toHaveText('Punkte: 0');

    await answer(1).click();
    await expect(frame.locator('#anzeige')).toHaveText('Richtig!');
    await expect(frame.locator('#punkte')).toHaveText('Punkte: 1');
    await expect(frame.locator('#text')).toHaveText('Welcher Planet ist der Sonne am nächsten?');
    await expect(answer(0)).toHaveText('Merkur');

    await answer(2).click();
    await expect(frame.locator('#anzeige')).toHaveText('Falsch! Richtig wäre: Merkur');
    await expect(frame.locator('#punkte')).toHaveText('Punkte: 1');
    await expect(frame.locator('#text')).toHaveText('Wie viele Minuten hat eine Stunde?');

    await answer(0).click();
    await expect(frame.locator('#ueberschrift')).toHaveText('Auswertung');
    await expect(frame.locator('#text')).toHaveText('Du hast 2 von 3 Punkten. Gut gemacht!');
    await expect(answer(0)).toBeHidden();
    await expect(answer(2)).toBeHidden();

    await frame.locator('#knopf', { hasText: 'Nochmal spielen' }).click();
    await expect(frame.locator('#ueberschrift')).toHaveText('Mein Quiz');
    await expect(frame.locator('#text')).toHaveText('Wie viele Beine hat eine Spinne?');
    await expect(frame.locator('#punkte')).toHaveText('Punkte: 0');
    await expect(frame.locator('#anzeige')).toHaveText('');
    await expect(answer(0)).toBeVisible();
    await expect(frame.locator('#knopf')).toBeHidden();
  });

  test('Eigenes Quiz: leeres Fragen-Array fällt durch, ein Quiz mit eigenen Fragen und Titel besteht', async ({ page }) => {
    await openCourse(page, lessons.map((l) => l.id));
    await page.locator('.lesson-item').nth(6).click();
    await expect(page.locator('.lesson-item.active')).toContainText(lessons[6].title);

    const task = page.locator('.task-block').nth(1);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    // Drei eigene Fragen (die Mindestzahl) statt der fuenf aus der Musterloesung - die Pruefung
    // haengt nicht an einer festen Fragenzahl.
    const template = lessons[6].tasks[1].codeTemplate;
    const own = template
      .replace(
        '  // Dein Code hier: deine eigenen Fragen\n',
        "  { frage: 'Welche Farbe hat eine reife Banane?', antworten: ['Gelb', 'Blau', 'Lila'], richtig: 0 },\n" +
          "  { frage: 'Wie viele Tage hat eine Woche?', antworten: ['5', '6', '7'], richtig: 2 },\n" +
          "  { frage: 'Was trinkt eine Kuh?', antworten: ['Milch', 'Wasser', 'Saft'], richtig: 1 },\n"
      )
      .replace("'Mein Quiz'", "'Kunterbunt-Quiz'");
    expect(own).toContain('Kunterbunt-Quiz');
    expect(own).toContain('Banane');
    await setCodeMirrorContent(task.locator('.cm-host'), own);
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
    await expect(task.frameLocator('iframe.js-sandbox').locator('#text')).toHaveText('Du hast 1 von 3 Punkten. Übe noch ein bisschen!');
  });
});
