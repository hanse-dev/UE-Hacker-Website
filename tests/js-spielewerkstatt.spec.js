import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// Prueft die neue JS-Sandbox-Ausfuehrungsumgebung (useJsSandbox.js/JsSandboxFrame.vue) und
// JsLessonView.vue - unabhaengig von Pyodide, daher kein Kernel-Warmup noetig, laeuft schnell.
// Der Code-Editor ist CodeMirror (JsCodeCell.vue), keine <textarea> - .fill() funktioniert nicht,
// siehe tests/helpers/codemirror.js.
test.describe('JS-Spielewerkstatt (Sandbox-Engine)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-interactive-progress-js-spielewerkstatt');
    });
  });

  test('Kurs laedt mit der JS-Sandbox-Engine, nicht mit Pyodide', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.lessons-list .lesson-item')).toHaveCount(6, { timeout: 15000 });
    await expect(page.locator('.course-description')).toContainText('JavaScript');

    // Beweis, dass JsLessonView (nicht LessonView/Pyodide) gerendert wird: kein Kernel-Init-Button.
    await expect(page.locator('.btn-kernel')).toHaveCount(0);
    await expect(page.locator('iframe.js-sandbox')).toBeVisible();
  });

  test('Canvas-Aufgabe: echtes Zeichnen wird per Pixel-Check erkannt', async ({ page }) => {
    test.setTimeout(30000);
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    // Task 0 ist ein bereits fertiges Beispiel zum Ausführen - die eigentliche Schreibaufgabe ist
    // Task 1 (erst danach kommt man "ins kalte Wasser").
    const task1 = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'yellow';\nctx.fillRect(50, 50, 100, 80);"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    // Die Ausgabe soll auch ohne console.log einen Hinweis zeigen, dass das Spielfeld verändert
    // wurde - sonst wirkt "keine Ausgabe" faelschlich wie "nichts ist passiert".
    await expect(task1.locator('.output-content')).toContainText('Spielfeld');

    // Ein oranger Rahmen um den Editor zeigt, dass dieser Code schon ausgeführt wurde.
    await expect(task1.locator('.code-editor-wrapper')).toHaveClass(/code-editor-ran/);
    await expect(task1.locator('.code-ran-note')).toBeVisible();

    const hasDrawing = await page
      .frameLocator('iframe.js-sandbox')
      .locator('canvas')
      .evaluate((el) => {
        const ctx = el.getContext('2d');
        const data = ctx.getImageData(0, 0, el.width, el.height).data;
        for (let i = 3; i < data.length; i += 4) {
          if (data[i] !== 0) return true;
        }
        return false;
      });
    expect(hasDrawing).toBe(true);
  });

  test('Falsche Loesung (leeres Canvas) besteht die Canvas-Aufgabe nicht', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\n// nichts gezeichnet"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
  });

  test('Kill-Switch: "Neu starten" baut das iframe wirklich neu auf', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'red';\nctx.fillRect(0, 0, 50, 50);"
    );
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.output-display')).toBeVisible({ timeout: 10000 });

    const readNotBlank = () =>
      page
        .frameLocator('iframe.js-sandbox')
        .locator('canvas')
        .evaluate((el) => {
          const ctx = el.getContext('2d');
          const data = ctx.getImageData(0, 0, el.width, el.height).data;
          for (let i = 3; i < data.length; i += 4) {
            if (data[i] !== 0) return true;
          }
          return false;
        });

    expect(await readNotBlank()).toBe(true);

    await page.locator('.btn-restart-sandbox').click();
    await expect(page.locator('.sandbox-status')).toHaveText(/bereit/i, { timeout: 10000 });
    expect(await readNotBlank()).toBe(false);
  });

  test('Self-Check-Aufgaben zaehlen zum Fortschritt und schalten die naechste Lektion frei', async ({ page }) => {
    test.setTimeout(30000);
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    // Lektion 1 hat 3 Aufgaben: Beispiel ansehen (self) → selbst zeichnen (auto) → Farbe
    // ausprobieren (self). Erst wenn alle drei erledigt sind, gilt die Lektion als abgeschlossen.
    const task0 = page.locator('.task-block').nth(0);
    await expect(task0.locator('.btn-selfcheck')).toBeVisible();
    await task0.locator('.btn-selfcheck').click();
    await expect(task0.locator('.task-status-label').last()).toHaveText(/ausprobiert/i);

    const task1 = page.locator('.task-block').nth(1);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'yellow';\nctx.fillRect(50, 50, 100, 80);"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(2);
    await expect(task2.locator('.btn-selfcheck')).toBeVisible();
    await task2.locator('.btn-selfcheck').click();
    await expect(task2.locator('.task-status-label').last()).toHaveText(/ausprobiert/i);

    await expect(page.locator('.lesson-item.completed')).toHaveCount(1);
    await expect(page.locator('.lesson-item').nth(1)).not.toHaveClass(/locked/);

    // Klick auf "Weiter zur nächsten Lektion" soll oben bei Lektion 2 landen, nicht an der
    // Scroll-Position stehen bleiben, an der man die letzte Aufgabe von Lektion 1 abgeschlossen hat.
    await expect(page.locator('.btn-next')).toBeVisible();
    const scrollBefore = await page.evaluate(() => window.scrollY);
    const mainTop = await page.locator('.lesson-main').evaluate((el) => el.getBoundingClientRect().top + window.scrollY);
    expect(scrollBefore).toBeGreaterThan(mainTop + 200);

    await page.locator('.btn-next').click();
    await expect(page.locator('.lesson-item.active')).toContainText('Der Schläger');
    await expect
      .poll(() => page.evaluate(() => window.scrollY), { timeout: 3000 })
      .toBeLessThan(scrollBefore - 200);
  });

  test('Lösung ist hinter einem Banner versteckt, nicht direkt im Editor vorausgefüllt', async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-js-spielewerkstatt',
        JSON.stringify({ version: 1, courseId: 'projekt-js-spielewerkstatt', variant: 'js-spielewerkstatt', completedLessonIds: ['lektion-01'] })
      );
    });
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });
    await page.locator('.lesson-item', { hasText: 'Der Schläger hört auf die Tastatur' }).click();

    // Task 2 ("probiere deine Funktion aus") duerfte die fertige Loesung von Task 1 nicht direkt
    // im Editor vorausfuellen - sonst kann man sie einfach zurueckkopieren, ohne selbst zu loesen.
    const task2 = page.locator('.task-block').nth(2);
    const editorText = await task2.locator('.cm-content').innerText();
    expect(editorText).not.toContain("neueX -= 20");

    const solution = task2.locator('.solution-reveal');
    await expect(solution).toBeVisible();
    await expect(solution.locator('.solution-code')).toBeHidden();

    await solution.locator('summary').click();
    await expect(solution.locator('.solution-code')).toContainText('bewegeSchlaeger');
  });

  test('Funktionsaufgabe mit versteckten Testfaellen: nur echte Loesung besteht', async ({ page }) => {
    test.setTimeout(30000);
    // Lektion 2 ist erst frei, wenn Lektion 1 abgeschlossen ist - Fortschritt vorab setzen statt
    // ihn hier erst manuell durchzuklicken (das ist bereits durch einen anderen Test abgedeckt).
    await page.addInitScript(() => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-js-spielewerkstatt',
        JSON.stringify({ version: 1, courseId: 'projekt-js-spielewerkstatt', variant: 'js-spielewerkstatt', completedLessonIds: ['lektion-01'] })
      );
    });
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });
    await page.locator('.lesson-item', { hasText: 'Der Schläger hört auf die Tastatur' }).click();

    // Task 0 ist wieder das lauffähige Beispiel (verdopple) - die Schreibaufgabe ist Task 1.
    const task1 = page.locator('.task-block').nth(1);

    // Funktioniert nur fuer den einen vorgerechneten Fall, nicht fuer die Randfaelle -
    // muss an den versteckten Testfaellen scheitern (beweist: keine Scheinloesung besteht).
    await setCodeMirrorContent(task1.locator('.cm-host'), 'function bewegeSchlaeger(x, taste) {\n  return 140;\n}');
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "function bewegeSchlaeger(x, taste) {\n  let neueX = x;\n  if (taste === 'ArrowLeft') neueX -= 20;\n  if (taste === 'ArrowRight') neueX += 20;\n  if (neueX < 0) neueX = 0;\n  if (neueX > 320) neueX = 320;\n  return neueX;\n}"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('CodeMirror-Editor: Autovervollständigung schlägt Browser-Globals vor', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    const content = task1.locator('.cm-content');
    await content.click();
    await content.press('ControlOrMeta+a');
    await content.press('Backspace');
    // Zeichenweise tippen (statt insertText), damit CodeMirror die Vervollstaendigung live
    // nachverfolgt, wie es beim echten Tippen im Browser auch passiert.
    await page.keyboard.type('docum');

    const suggestion = page.locator('.cm-tooltip-autocomplete .cm-completionLabel').first();
    await expect(suggestion).toBeVisible({ timeout: 5000 });
    await expect(suggestion).toContainText('document');

    await page.keyboard.press('Tab');
    await expect(content).toHaveText('document');
  });

  test('CodeMirror-Editor: Tab rückt ein, wenn keine Vervollständigung offen ist', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    const content = task1.locator('.cm-content');
    await content.click();
    await content.press('ControlOrMeta+a');
    await content.press('Backspace');
    await page.keyboard.type('function foo() {');
    await page.keyboard.press('Enter');
    await page.keyboard.press('Tab');
    await page.keyboard.type('return 1;');

    const text = await content.innerText();
    expect(text).toMatch(/function foo\(\) \{\n\s+return 1;/);
  });

  test('Animationsschleife: canvas_changed erkennt eine wirklich laufende rAF-Schleife', async ({ page }) => {
    test.setTimeout(30000);
    await page.addInitScript(() => {
      localStorage.setItem(
        'ue-hacker-interactive-progress-js-spielewerkstatt',
        JSON.stringify({ version: 1, courseId: 'projekt-js-spielewerkstatt', variant: 'js-spielewerkstatt', completedLessonIds: ['lektion-01', 'lektion-02'] })
      );
    });
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await page.locator('.lesson-item', { hasText: 'Alles bewegt sich' }).click();
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    // Task 0 = naechstePosition (auto), Task 1 = fertige Loesung zum Anschauen (self),
    // Task 2 = die Schleife selbst nachbauen (auto, canvas_changed).
    const task2 = page.locator('.task-block').nth(2);
    // Ball bewegt sich nicht (ballY bleibt 0) - clearRect+identischer Neuzeichnen ergibt
    // unveraenderte Pixel, canvas_changed muss das erkennen und die Aufgabe ablehnen.
    await setCodeMirrorContent(
      task2.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nlet ballY = 0;\n\nfunction frame() {\n  ctx.clearRect(0, 0, canvas.width, canvas.height);\n  ctx.fillStyle = 'orange';\n  ctx.beginPath();\n  ctx.arc(200, ballY, 10, 0, Math.PI * 2);\n  ctx.fill();\n\n  requestAnimationFrame(frame);\n}\n\nframe();"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await setCodeMirrorContent(
      task2.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nlet ballY = 0;\n\nfunction frame() {\n  ctx.clearRect(0, 0, canvas.width, canvas.height);\n  ctx.fillStyle = 'orange';\n  ctx.beginPath();\n  ctx.arc(200, ballY, 10, 0, Math.PI * 2);\n  ctx.fill();\n\n  ballY = ballY + 2;\n\n  requestAnimationFrame(frame);\n}\n\nframe();"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });
});
