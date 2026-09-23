import { test, expect } from '@playwright/test';
import { startKernel } from './helpers/kernel.js';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { openSolutionsNotebook } from './helpers/notebook.js';

const INTERACTIVE_URL = '/kurs/python-grundlagen-interaktiv';
const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const PLACEMENT_URL = '/kurs/python-einstufung';
const JS_GRUNDKURS_URL = '/kurs/js-grundkurs';

test.describe('Home & Navigation', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Home zeigt CTAs und Kern-Kurse', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#hero')).toBeVisible();
    await expect(page.locator('.cta-button')).toHaveCount(2);
    await expect(page.locator('a.cta-button[href="#kurse-uebersicht"]')).toBeVisible();
    await expect(page.locator('a.cta-button[href="/projekte"]')).toBeVisible();

    // Home filtert Kurse: 12-Wochen + Interaktiv + JS-Grundkurs immer sichtbar, andere nur mit
    // Termin. Projekt-Kurse (type: 'projekt') erscheinen hier nicht mehr — die haben eine eigene
    // Übersicht unter /projekte, verlinkt über den Projekte-Teaser.
    await expect(page.locator('#kurse-uebersicht .course-card')).toHaveCount(3);
    await expect(page.locator('a.course-card[href="/kurs/python-12-wochen-grundkurs"]')).toBeVisible();
    await expect(page.locator('a.course-card[href="/kurs/python-grundlagen-interaktiv"]')).toBeVisible();
    await expect(page.locator(`a.course-card[href="${JS_GRUNDKURS_URL}"]`)).toBeVisible();
    await expect(page.locator('.projekte-teaser-link')).toBeVisible();
    await expect(page.locator('a.placement-hint-link[href="/kurs/python-einstufung"]')).toBeVisible();

    // Kurskarten zeigen ein Format-Badge (Einstieg/Grundkurs, siehe VISION.md-Format-Modell)
    await expect(page.locator('.course-format-badge')).toHaveCount(3);
  });

  test('Hero-CTA "Kurse" springt zur Kursübersicht, "Projekte" öffnet die Projekte-Seite', async ({ page }) => {
    await page.goto('/');
    await page.locator('a.cta-button[href="#kurse-uebersicht"]').click();
    await expect(page).toHaveURL(/#kurse-uebersicht/);
    await expect(page.locator('#kurse-uebersicht')).toBeInViewport();

    await page.goto('/');
    await page.locator('a.cta-button[href="/projekte"]').click();
    await expect(page).toHaveURL(/\/projekte/);
    await expect(page.locator('.projekt-card').first()).toBeVisible({ timeout: 15000 });
  });

  test('Home-Kursliste öffnet den JS-Grundkurs mit korrektem Titel per Klick auf die ganze Karte', async ({ page }) => {
    await page.goto('/');
    // Die ganze Kurskarte ist klickbar, nicht nur der "Mehr erfahren"-Link
    await page.locator(`a.course-card[href="${JS_GRUNDKURS_URL}"] h3`).click();
    await expect(page).toHaveURL(/js-grundkurs/);
    await expect(page.locator('.course-detail > h1')).toHaveText('JavaScript-Grundkurs');
    await expect(page.locator('.week-tile')).toHaveCount(9, { timeout: 15000 });
  });

  test('Header-Nav verlinkt direkt zu den Projekten', async ({ page }) => {
    await page.goto('/');
    const link = page.locator('nav a', { hasText: 'Projekte' });
    await expect(link).toHaveAttribute('href', '/projekte');
    await link.click();
    await expect(page).toHaveURL(/\/projekte/);
    await expect(page.locator('.projekt-card').first()).toBeVisible({ timeout: 15000 });
  });

  test('Home-CTA Einstufung öffnet Placement-Kurs', async ({ page }) => {
    await page.goto('/');
    await page.locator('a.placement-hint-link[href="/kurs/python-einstufung"]').click();
    await expect(page).toHaveURL(/python-einstufung/);
    await expect(page.locator('.course-detail > h1')).toHaveText(/Einstufung|Placement/);
    await expect(page.locator('.placement-intro, .placement-results, .quiz-question').first()).toBeVisible({
      timeout: 15000,
    });
  });

  test('Sprachumschaltung DE → EN', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#hero h2')).toContainText(/Willkommen|Übergangshacker/i);
    await page.locator('.options-btn').click();
    await expect(page.locator('.settings-modal')).toBeVisible();
    await page.locator('.settings-modal .lang-switcher button', { hasText: 'EN' }).click();
    await page.locator('.settings-close').click();
    await expect(page.locator('a.placement-hint-link[href="/kurs/python-einstufung"]')).toContainText(/Placement/i);
    await expect(page.locator('#kurse-uebersicht h2')).toContainText(/Course/i);
    await expect(page.locator('#kurse-uebersicht .course-card').first()).toContainText(/Week|Interactive|Basics/i);
  });
});

test.describe('12-Wochen-Kurs UI', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Placement-Banner verlinkt zur Einstufung', async ({ page }) => {
    await page.goto(COURSE_URL);
    await expect(page.locator('.placement-banner')).toBeVisible({ timeout: 20000 });
    await page.locator('.placement-banner-link').click();
    await expect(page).toHaveURL(/python-einstufung/);
  });

  test('Kursstruktur erklärt den Ablauf inkl. Check', async ({ page }) => {
    await page.goto(COURSE_URL);
    await expect(page.locator('.course-structure')).toBeVisible({ timeout: 20000 });
    await expect(page.locator('.course-structure-tab')).toHaveCount(7);
    await expect(page.locator('.course-structure-tab', { hasText: 'Check' })).toBeVisible();
  });
});

test.describe('Interaktiver Kurs', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-variant');
    });
  });

  test('Variantwahl Kinder → Lektion wird geladen', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(INTERACTIVE_URL);
    await expect(page.locator('.variant-card').first()).toBeVisible({ timeout: 15000 });
    await page.locator('.variant-card').first().click();
    await expect(page.locator('.lessons-list .lesson-item').first()).toBeVisible({ timeout: 20000 });
    await expect(page.locator('.lesson-view, .lesson-content, .lesson-main').first()).toBeVisible();
    await expect(page.locator('.lesson-content, .code-editor, .editor-hint').first()).toBeVisible({
      timeout: 20000,
    });
  });

  test('Placement-Banner auch auf Interaktiv-Kurs', async ({ page }) => {
    await page.goto(INTERACTIVE_URL);
    await expect(page.locator('.placement-banner')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.placement-banner-link')).toHaveAttribute('href', '/kurs/python-einstufung');
  });

  test('Gestufter Hinweis: erster Fehlversuch verrät die Lösung nicht, ab dem zweiten schon', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(INTERACTIVE_URL);
    await page.locator('.variant-card').first().click();
    await page.waitForSelector('.task-block', { timeout: 20000 });
    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    const task = page.locator('.task-block').first();
    const editor = task.locator('.code-editor');

    await editor.fill('print("nope")');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback')).toBeVisible({ timeout: 10000 });
    await expect(task.locator('.feedback')).not.toContainText('Erwartet wurde etwas mit');

    await editor.fill('print("still nope")');
    await task.locator('.btn-check').click();
    await expect(task.locator('.feedback')).toContainText('Erwartet wurde etwas mit', { timeout: 10000 });
  });
});

test.describe('Cäsar-Chiffre-Projekt', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-progress-caesar-chiffre');
    });
  });

  test('Kurs lädt, Lektion 1 lösen schaltet Lektion 2 frei', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-caesar-chiffre');
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(5, { timeout: 15000 });
    await expect(page.locator('.course-description')).toContainText('Cäsar-Chiffre');

    await startKernel(page);
    await expect(page.locator('.btn-check').first()).toBeEnabled({ timeout: 40000 });

    const task1 = page.locator('.task-block').nth(0);
    await task1.locator('.code-editor').fill("print(ord('a'))");
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(1);
    await task2.locator('.code-editor').fill("print(chr(100))");
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);
  });

  test('Lösung wird erst nach Klick auf "Lösung anzeigen" sichtbar', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto('/kurs/projekt-caesar-chiffre');
    await page.waitForSelector('.task-block', { timeout: 15000 });

    const task = page.locator('.task-block').first();
    await expect(task.locator('.solution-code')).toHaveCount(0);
    await expect(task.locator('.btn-solution')).toBeVisible();

    await task.locator('.btn-solution').click();
    await expect(task.locator('.solution-code')).toContainText("print(ord('a'))");
    await expect(task.locator('.btn-solution')).toHaveCount(0);
  });
});

test.describe('Weitere Kursseiten', () => {
  test('Ferienkurs-Seite lädt ohne Fehler', async ({ page }) => {
    await page.goto('/kurs/ferienkurse');
    await expect(page.locator('.course-detail > h1, .course-loading')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.course-error')).toHaveCount(0);
  });
});

test.describe('Debug-Notebook-Sicherheit', () => {
  test('Endlosschleife bricht nach ~5s ab statt den Tab einzufrieren', async ({ page }) => {
    test.setTimeout(60000);
    await openSolutionsNotebook(page, 'pferde');
    await expect(page.locator('.btn-run-cell').first()).toBeVisible({ timeout: 20000 });

    // Kernel initialisiert sich beim Mount bereits automatisch — nicht extra klicken
    // (der Button kann währenddessen schon deaktiviert/instabil sein).
    await expect(page.locator('.btn-run-cell').first()).toBeEnabled({ timeout: 40000 });

    const editor = page.locator('.cm-host').first();
    const runBtn = page.locator('.btn-run-cell').first();
    await setCodeMirrorContent(editor, 'while True:\n    pass\n');

    const start = Date.now();
    await runBtn.click();
    await expect(page.locator('.output-error').first()).toBeVisible({ timeout: 15000 });
    const elapsed = Date.now() - start;

    expect(elapsed).toBeGreaterThan(3000);
    expect(elapsed).toBeLessThan(12000);
    await expect(page.locator('.output-error').first()).toContainText(/Endlosschleife/);

    // Kernel muss danach weiter benutzbar sein — keine dauerhafte Blockade.
    await setCodeMirrorContent(editor, 'print("kernel lebt", 1 + 1)');
    await runBtn.click();
    await expect(page.locator('.output-stream').first()).toContainText('kernel lebt 2', { timeout: 10000 });
  });
});

test.describe('Turtle-Grafik im Browser (Pyodide-Shim)', () => {
  // Pyodide entfernt `turtle` aus der Standardbibliothek (basiert auf tkinter,
  // das im Browser keinen Anzeige-Server hat) — siehe HANDOFF.md. usePyodide.js
  // registriert stattdessen einen eigenen Shim, der auf <canvas> zeichnet.
  test('import turtle wirft keinen ModuleNotFoundError mehr und zeichnet sichtbar', async ({ page }) => {
    test.setTimeout(150000); // Pyodide-Start unter Last (Volllauf, 4 Worker) kann > 30 s dauern
    await openSolutionsNotebook(page, 'abenteuer', 1, 90000);
    const runBtn = page.locator('.btn-run-cell').first();
    await expect(runBtn).toBeEnabled({ timeout: 90000 });

    const editor = page.locator('.cm-host').first();
    await setCodeMirrorContent(
      editor,
      'import turtle\n' +
      'pen = turtle.Turtle()\n' +
      'pen.color("blue")\n' +
      'for _ in range(4):\n' +
      '    pen.forward(80)\n' +
      '    pen.left(90)\n' +
      'turtle.done()\n'
    );
    await runBtn.click();

    await expect(page.locator('.output-error')).toHaveCount(0, { timeout: 10000 });
    const canvas = page.locator('.turtle-canvas-container canvas').first();
    await expect(canvas).toBeVisible({ timeout: 10000 });

    const hasDrawing = await canvas.evaluate((el) => {
      const ctx = el.getContext('2d');
      const data = ctx.getImageData(0, 0, el.width, el.height).data;
      for (let i = 0; i < data.length; i += 4) {
        if (!(data[i] === 255 && data[i + 1] === 255 && data[i + 2] === 255)) return true;
      }
      return false;
    });
    expect(hasDrawing).toBe(true);
  });

  test('begin_fill()/end_fill() füllt eine Form sichtbar', async ({ page }) => {
    test.setTimeout(150000); // Pyodide-Start unter Last (Volllauf, 4 Worker) kann > 30 s dauern
    await openSolutionsNotebook(page, 'abenteuer', 1, 90000);
    const runBtn = page.locator('.btn-run-cell').first();
    await expect(runBtn).toBeEnabled({ timeout: 90000 });

    const editor = page.locator('.cm-host').first();
    await setCodeMirrorContent(
      editor,
      'import turtle\n' +
      'pen = turtle.Turtle()\n' +
      'pen.fillcolor("red")\n' +
      'pen.begin_fill()\n' +
      'for _ in range(4):\n' +
      '    pen.forward(60)\n' +
      '    pen.left(90)\n' +
      'pen.end_fill()\n' +
      'turtle.done()\n'
    );
    await runBtn.click();

    await expect(page.locator('.output-error')).toHaveCount(0, { timeout: 10000 });
    const canvas = page.locator('.turtle-canvas-container canvas').first();
    const hasRedFill = await canvas.evaluate((el) => {
      const ctx = el.getContext('2d');
      const data = ctx.getImageData(0, 0, el.width, el.height).data;
      for (let i = 0; i < data.length; i += 4) {
        if (data[i] > 200 && data[i + 1] < 60 && data[i + 2] < 60) return true;
      }
      return false;
    });
    expect(hasRedFill).toBe(true);
  });
});
