import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const CONTENT_DIR = path.join('content', 'microbit-auto');
const lessons = JSON.parse(fs.readFileSync(path.join(CONTENT_DIR, 'lessons.json'), 'utf8'));

test.describe('micro:bit-Kurs: Roboterauto (Anleitung zum Abhaken)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      // Nur beim ersten Laden leeren, damit der Reload-Test den gespeicherten Stand sieht.
      if (sessionStorage.getItem('microbit-test-init')) return;
      sessionStorage.setItem('microbit-test-init', '1');
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-guide-mode');
      localStorage.removeItem('ue-hacker-interactive-progress-microbit-auto');
    });
  });

  async function openCourse(page) {
    await page.goto('/kurs/projekt-microbit-auto');
    await expect(page.locator('.course-description')).toContainText('Roboterauto');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
  }

  test('Inhalt: jede Stufe hat Pflichtaufgaben, und jeder Abschnitt gibt es für Blöcke und Python', () => {
    for (const lesson of lessons) {
      expect(lesson.tasks.some((task) => !task.isBonus), lesson.id).toBe(true);
      const md = fs.readFileSync(path.join(CONTENT_DIR, lesson.file), 'utf8');
      // Jede Bonusaufgabe braucht im Text eine eigene Aufgabenstellung.
      if (lesson.tasks.some((task) => task.isBonus)) {
        expect(md, `${lesson.file}: Bonus-Abschnitt`).toMatch(/^## Bonus: /m);
      }
      const opened = md.match(/^:::(bloecke|python)$/gm) || [];
      const closed = md.match(/^:::$/gm) || [];
      expect(closed.length, `${lesson.file}: Abschnitte geschlossen`).toBe(opened.length);
      expect(opened.filter((m) => m === ':::bloecke').length, `${lesson.file}: Blöcke und Python gleich oft`)
        .toBe(opened.filter((m) => m === ':::python').length);
      // Ein Block-Listing ausserhalb eines :::bloecke-Abschnitts waere auch in der Python-Ansicht sichtbar.
      const outside = md.replace(/^:::(bloecke|python)$[\s\S]*?^:::$/gm, '');
      expect(outside, `${lesson.file}: Code nur innerhalb der Abschnitte`).not.toMatch(/```(bloecke|python)/);
    }
  });

  test('Umschalter zeigt Blöcke oder Python und merkt sich die Wahl', async ({ page }) => {
    await openCourse(page);
    const content = page.locator('.guide-lesson .lesson-content');

    await expect(content.locator('.mc-blocks').first()).toBeVisible();
    await expect(content.locator('.mc-block.mc-grundlagen').first()).toHaveText('beim Start');
    await expect(content.locator('pre code.language-python').first()).toBeHidden();
    await expect(content).not.toContainText(':::');

    await page.locator('.guide-mode-btn[data-mode="python"]').click();
    await expect(content.locator('pre code.language-python').first()).toBeVisible();
    await expect(content.locator('pre code.language-python').first()).toContainText('display.show(Image.HEART)');
    await expect(content.locator('.mc-blocks').first()).toBeHidden();

    // Nach dem Neuladen bleibt der Kurs geoeffnet (?started=1).
    await page.reload();
    await expect(page.locator('.guide-mode-btn[data-mode="python"]')).toHaveClass(/active/);
    await expect(page.locator('.guide-lesson .lesson-content pre code.language-python').first()).toBeVisible();
  });

  test('Pflichtaufgaben abhaken schließt die Stufe ab und schaltet die nächste frei, Bonus ist freiwillig', async ({ page }) => {
    await openCourse(page);
    // Kein Python-Kernel und kein Code-Editor: die Aufgaben werden am echten Auto ausprobiert.
    await expect(page.locator('.btn-kernel')).toHaveCount(0);
    // Offline-ZIPs gibt es nur fuer Pyodide-Projekte - hier waeren es tote Links.
    await expect(page.locator('.offline-downloads')).toHaveCount(0);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);

    const required = lessons[0].tasks.filter((task) => !task.isBonus).length;
    const tasks = page.locator('.guide-task');
    await expect(tasks).toHaveCount(lessons[0].tasks.length);
    await expect(tasks.locator('.task-bonus-badge')).toHaveCount(lessons[0].tasks.length - required);

    for (let i = 0; i < required - 1; i++) await tasks.nth(i).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toHaveCount(0);
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);

    await tasks.nth(required - 1).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);

    await page.locator('.btn-next').click();
    await expect(page.locator('.guide-lesson .lesson-content h1')).toContainText('Stufe 1');
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(0);

    // Abgeschlossene Stufe bleibt nach dem Neuladen abgehakt.
    await page.reload();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1, { timeout: 15000 });
    await page.locator('.lesson-item').first().click();
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(required);
  });

  test('Bonus: Aufgabenstellung ist sichtbar, die Tipps sind eingeklappt und zeigen nur die gewählte Ansicht', async ({ page }) => {
    await page.addInitScript(() => localStorage.setItem(
      'ue-hacker-interactive-progress-microbit-auto',
      JSON.stringify({ variant: 'microbit-auto', completedLessonIds: ['lektion-01'] }),
    ));
    await openCourse(page);
    await page.locator('.lesson-item').nth(1).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h2', { hasText: 'Bonus: Der Countdown' })).toBeVisible();

    const tips = content.locator('details');
    await expect(tips).toHaveCount(1);
    await expect(tips.locator('.mc-block', { hasText: 'zeige Zahl 3' })).toBeHidden();
    await tips.locator('summary').click();
    await expect(tips.locator('.mc-block', { hasText: 'zeige Zahl 3' })).toBeVisible();
    await expect(tips.locator('pre code.language-python')).toBeHidden();
    await expect(tips).not.toContainText(':::');
  });

  test('Haken zurücknehmen nimmt den Abschluss der Stufe zurück und sperrt die nächste wieder', async ({ page }) => {
    await openCourse(page);
    const tasks = page.locator('.guide-task');
    const required = lessons[0].tasks.filter((task) => !task.isBonus).length;
    for (let i = 0; i < required; i++) await tasks.nth(i).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);

    // Ein Bonus-Haken ändert nichts am Abschluss.
    await tasks.nth(required).locator('.guide-task-check').check();
    await tasks.nth(required).locator('.guide-task-check').uncheck();
    await expect(page.locator('.lesson-complete-box')).toBeVisible();

    await tasks.nth(0).locator('.guide-task-check').uncheck();
    await expect(tasks.nth(0).locator('.guide-task-check')).not.toBeChecked();
    await expect(page.locator('.lesson-complete-box')).toHaveCount(0);
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);
    await expect(page.locator('.lesson-item').nth(1)).toHaveClass(/locked/);

    // Auch nach dem Neuladen gilt die Stufe nicht mehr als abgeschlossen.
    await page.reload();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);
    // Die übrigen Haken sind gespeichert, nur der zurückgenommene fehlt.
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(required - 1);
    await expect(tasks.nth(0).locator('.guide-task-check')).not.toBeChecked();

    // Wieder abhaken schließt die Stufe erneut ab.
    for (let i = 0; i < required; i++) await tasks.nth(i).locator('.guide-task-check').check();
    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
  });

  test('Einzelne Haken bleiben nach dem Neuladen erhalten, ohne Account aber nur einen Tag', async ({ page }) => {
    const KEY = 'ue-hacker-interactive-progress-microbit-auto';
    await openCourse(page);
    const tasks = page.locator('.guide-task');
    await tasks.nth(1).locator('.guide-task-check').check();
    await tasks.nth(lessons[0].tasks.length - 1).locator('.guide-task-check').check(); // Bonus

    await page.reload();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(2);
    await expect(tasks.nth(1).locator('.guide-task-check')).toBeChecked();
    await expect(tasks.nth(0).locator('.guide-task-check')).not.toBeChecked();
    // Die Stufe ist damit nicht abgeschlossen.
    await expect(page.locator('.lesson-item.completed')).toHaveCount(0);
    await expect(page.locator('.lesson-complete-box')).toHaveCount(0);

    // 23 Stunden alt: noch da. 25 Stunden alt: zurückgesetzt.
    const age = (hours) => page.evaluate(([key, h]) => {
      const state = JSON.parse(localStorage.getItem(key));
      state.partialChecksAt = new Date(Date.now() - h * 3600 * 1000).toISOString();
      localStorage.setItem(key, JSON.stringify(state));
    }, [KEY, hours]);
    await age(23);
    await page.reload();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(2);

    await age(25);
    await page.reload();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.guide-task')).toHaveCount(lessons[0].tasks.length);
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(0);

    // Ein neuer Haken nach dem Verfall bringt die alten nicht zurück.
    await tasks.nth(0).locator('.guide-task-check').check();
    await page.reload();
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(lessons.length, { timeout: 15000 });
    await expect(page.locator('.guide-task-check:checked')).toHaveCount(1);
    await expect(tasks.nth(0).locator('.guide-task-check')).toBeChecked();
  });

  test('Stufe 9: Plan und Programm sind zum Selbermachen, fertiger Plan und Lösung sind eingeklappt', async ({ page }) => {
    await page.addInitScript(() => localStorage.setItem(
      'ue-hacker-interactive-progress-microbit-auto',
      JSON.stringify({
        variant: 'microbit-auto',
        completedLessonIds: Array.from({ length: 9 }, (_, i) => `lektion-${String(i + 1).padStart(2, '0')}`),
      }),
    ));
    await openCourse(page);
    await page.locator('.lesson-item').nth(9).click();
    const content = page.locator('.guide-lesson .lesson-content');
    await expect(content.locator('h1')).toContainText('Stufe 9');

    // Sichtbar ist nur der erste Fall, die drei anderen bauen die Teams selbst.
    await expect(content.locator('.mc-block:visible', { hasText: 'wenn linie = 3 dann' })).toHaveCount(1);
    await expect(content.locator('.mc-block:visible', { hasText: 'Backward' })).toHaveCount(0);
    await expect(content.getByText('nach links drehen, die Linie wandert nach links weg')).toBeHidden();

    const plan = content.locator('details', { has: page.locator('summary', { hasText: 'Plan anzeigen' }) });
    await plan.locator('summary').click();
    await expect(plan.getByText('nach links drehen, die Linie wandert nach links weg')).toBeVisible();

    const solution = content.locator('details', { has: page.locator('summary', { hasText: 'Lösung anzeigen' }) });
    await expect(solution.locator('.mc-block', { hasText: 'sonst wenn linie = 2 dann' })).toBeHidden();
    await solution.locator('summary').click();
    await expect(solution.locator('.mc-block', { hasText: 'sonst wenn linie = 2 dann' })).toBeVisible();
    await expect(solution.locator('pre code.language-python')).toBeHidden();
  });

  test('Kurs ist in der Projekte-Übersicht verlinkt, mit eigenen Filtern für micro:bit und Robotik', async ({ page }) => {
    await page.goto('/projekte');
    await expect(page.locator('a.projekt-card[href="/kurs/projekt-microbit-auto"]')).toBeVisible({ timeout: 15000 });

    await page.locator('.filter-chip', { hasText: 'Robotik' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(1);
    await page.locator('.filter-reset').click();
    await page.locator('.filter-chip', { hasText: 'micro:bit' }).click();
    await expect(page.locator('.projekt-card')).toHaveCount(1);

    await page.locator('a.projekt-card[href="/kurs/projekt-microbit-auto"]').click();
    await expect(page.locator('.course-description')).toContainText('Roboterauto');
    await expect(page.locator('.btn-start-course')).toBeVisible();
  });

  test('Ein Kurs mit "unlisted" fehlt in der Projekte-Übersicht, ist per direktem Link aber erreichbar', async ({ page }) => {
    await page.route('**/kurse.json', async (route) => {
      const response = await route.fetch();
      const kurse = await response.json();
      kurse.find((k) => k.id === 'projekt-microbit-auto').unlisted = true;
      await route.fulfill({ response, json: kurse });
    });
    await page.goto('/projekte');
    await expect(page.locator('.projekt-card').first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('a[href="/kurs/projekt-microbit-auto"]')).toHaveCount(0);
    await expect(page.locator('.filter-chip', { hasText: 'micro:bit' })).toHaveCount(0);
    await expect(page.locator('.filter-chip', { hasText: 'Robotik' })).toHaveCount(0);

    await page.goto('/kurs/projekt-microbit-auto');
    await expect(page.locator('.course-description')).toContainText('Roboterauto');
    await expect(page.locator('.btn-start-course')).toBeVisible();
  });

  test('Bibliothek für Python wird zum Download ausgeliefert', async ({ page }) => {
    const res = await page.request.get('/microbit/keyes_MiniCar.py');
    expect(res.status()).toBe(200);
    expect(await res.text()).toContain('class MiniCar');
  });
});
