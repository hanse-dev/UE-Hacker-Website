import { test, expect } from '@playwright/test';
import { setCodeMirrorContent, hoverOverCodeMirrorText } from './helpers/codemirror.js';

// Prueft die neue JS-Sandbox-Ausfuehrungsumgebung (useJsSandbox.js/JsSandboxFrame.vue) und
// JsLessonView.vue - unabhaengig von Pyodide, daher kein Kernel-Warmup noetig, laeuft schnell.
// Der Code-Editor ist CodeMirror (JsCodeCell.vue), keine <textarea> - .fill() funktioniert nicht,
// siehe tests/helpers/codemirror.js.
//
// Jede Aufgabe hat ihre eigene Sandbox-Instanz (eigenes iframe.js-sandbox) statt einer geteilten
// pro Lektion - `page.locator('iframe.js-sandbox')` matcht deshalb i.d.R. mehrere Elemente.
// `.first()` fuer reine "ist der Kurs ueberhaupt geladen"-Checks, sonst innerhalb der jeweiligen
// `.task-block`-Locator (`taskN.frameLocator(...)`) scopen.
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

    // Das Sandbox-iframe wird erst beim ersten Ausführen einer Aufgabe gemountet (lazy, siehe
    // JsLessonView.vue) - vorher gibt es keines zu sehen, erst ein Klick auf "Ausführen".
    const task0 = page.locator('.task-block').nth(0);
    await task0.locator('.btn-run').click();
    await expect(task0.locator('iframe.js-sandbox')).toBeVisible();
  });

  test('Canvas-Aufgabe: echtes Zeichnen wird per Pixel-Check erkannt', async ({ page }) => {
    test.setTimeout(30000);
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    // Task 0+1 sind bereits fertige Beispiele zum Ausführen - die eigentliche Schreibaufgabe (mit
    // "Pruefen"-Button) ist die letzte Aufgabe der Lektion, Task 2.
    const task1 = page.locator('.task-block').nth(2);
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

    const hasDrawing = await task1
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
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\n// nichts gezeichnet"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
  });

  test('Kill-Switch: "Neu starten" baut das iframe wirklich neu auf', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(
      task1.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'red';\nctx.fillRect(0, 0, 50, 50);"
    );
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.output-display')).toBeVisible({ timeout: 10000 });

    const readNotBlank = () =>
      task1
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

    await task1.locator('.btn-restart-sandbox').click();
    await expect(task1.locator('.sandbox-status')).toHaveText(/bereit/i, { timeout: 10000 });
    expect(await readNotBlank()).toBe(false);
  });

  test('Beispiel- und Pflicht-Aufgaben einer Lektion sind klar unterschieden und schalten zusammen die naechste Lektion frei', async ({ page }) => {
    test.setTimeout(30000);
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    // Lektion 1 hat 3 Aufgaben: zwei Beispiele zuerst (nur Ausfuehren, kein Pruefen-Button) - erst
    // Rechteck ansehen, dann andere Farbe ansehen - dann als letzte Aufgabe "Deine Aufgabe" (selbst
    // zeichnen, Ausfuehren + Pruefen). "Pruefen" ist immer die letzte Aufgabe einer Lektion.
    const task0 = page.locator('.task-block').nth(0);
    await expect(task0.locator('.btn-selfcheck')).toHaveCount(0);
    await expect(task0).toHaveClass(/task-example/);
    await expect(task0.locator('.badge-example')).toBeVisible();
    await expect(task0.locator('.btn-check')).toHaveCount(0);
    await task0.locator('.btn-run').click();
    await expect(task0.locator('.task-done')).toBeVisible({ timeout: 10000 });

    const task1 = page.locator('.task-block').nth(1);
    await expect(task1).toHaveClass(/task-example/);
    await expect(task1.locator('.btn-check')).toHaveCount(0);
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.task-done')).toBeVisible({ timeout: 10000 });

    const task2 = page.locator('.task-block').nth(2);
    await expect(task2).toHaveClass(/task-required/);
    await expect(task2.locator('.badge-required')).toBeVisible();
    await setCodeMirrorContent(
      task2.locator('.cm-host'),
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'yellow';\nctx.fillRect(50, 50, 100, 80);"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

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
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
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
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
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
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    const content = task1.locator('.cm-content');
    await content.click();
    await content.press('ControlOrMeta+a');
    await content.press('Backspace');
    // Zeichenweise tippen (statt insertText), damit CodeMirror die Vervollstaendigung live
    // nachverfolgt, wie es beim echten Tippen im Browser auch passiert. Eindeutiger Praefix
    // (statt z.B. "docum", das sowohl "document" als auch die Klasse "Document" trifft und je
    // nach interner Sortierung mal das eine, mal das andere zuerst zeigt).
    await page.keyboard.type('requestAnimationFra');

    const suggestion = page.locator('.cm-tooltip-autocomplete .cm-completionLabel').first();
    await expect(suggestion).toBeVisible({ timeout: 5000 });
    await expect(suggestion).toContainText('requestAnimationFrame');

    await page.keyboard.press('Tab');
    await expect(content).toHaveText('requestAnimationFrame');
  });

  test('CodeMirror-Editor: Autovervollständigung kennt ctx-Canvas-Methoden (fillRect, arc, ...)', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    const content = task1.locator('.cm-content');
    await content.click();
    await content.press('ControlOrMeta+a');
    await content.press('Backspace');
    // `ctx` ist nur eine lokale Variable - ohne eigenes Scope-Objekt in JsCodeCell.vue koennte
    // CodeMirror nicht wissen, dass sie ein CanvasRenderingContext2D ist, und "ctx." haette keine
    // Vorschlaege.
    await page.keyboard.type('ctx.fill');

    const items = page.locator('.cm-tooltip-autocomplete .cm-completionLabel');
    await expect(items.first()).toBeVisible({ timeout: 5000 });
    const labels = await items.allInnerTexts();
    expect(labels).toContain('fillRect');
    expect(labels).toContain('fillStyle');
  });

  test('CodeMirror-Editor: Hover über ctx-Methode zeigt Signatur-Tooltip', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    const content = task1.locator('.cm-content');
    await setCodeMirrorContent(task1.locator('.cm-host'), 'ctx.fillRect(0, 0, 10, 10);');

    await hoverOverCodeMirrorText(content, 'fillRect');
    const tooltip = page.locator('.cm-api-hover');
    await expect(tooltip).toBeVisible({ timeout: 3000 });
    await expect(tooltip).toContainText('fillRect(x, y, breite, hoehe)');
  });

  test('CodeMirror-Editor: Tab rückt ein, wenn keine Vervollständigung offen ist', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

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
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });

    // Task 0 = fertige Loesung zum Anschauen (Beispiel, nur Ausfuehren), Task 1 = naechstePosition
    // (Pflichtaufgabe), Task 2 = die Schleife selbst nachbauen (Pflichtaufgabe, canvas_changed).
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
