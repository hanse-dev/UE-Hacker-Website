import { test, expect } from '@playwright/test';

// Prueft die neue JS-Sandbox-Ausfuehrungsumgebung (useJsSandbox.js/JsSandboxFrame.vue) und
// JsLessonView.vue - unabhaengig von Pyodide, daher kein Kernel-Warmup noetig, laeuft schnell.
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
    await task1.locator('.code-editor').fill(
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'yellow';\nctx.fillRect(50, 50, 100, 80);"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });

    // Die Ausgabe soll auch ohne console.log einen Hinweis zeigen, dass das Spielfeld verändert
    // wurde - sonst wirkt "keine Ausgabe" faelschlich wie "nichts ist passiert".
    await expect(task1.locator('.output-content')).toContainText('Spielfeld');

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
    await task1.locator('.code-editor').fill(
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\n// nichts gezeichnet"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
  });

  test('Kill-Switch: "Neu starten" baut das iframe wirklich neu auf', async ({ page }) => {
    await page.goto('/kurs/projekt-js-spielewerkstatt');
    await expect(page.locator('iframe.js-sandbox')).toBeVisible({ timeout: 15000 });

    const task1 = page.locator('.task-block').nth(1);
    await task1.locator('.code-editor').fill(
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
    await task1.locator('.code-editor').fill(
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
    await task1.locator('.code-editor').fill('function bewegeSchlaeger(x, taste) {\n  return 140;\n}');
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await task1.locator('.code-editor').fill(
      "function bewegeSchlaeger(x, taste) {\n  let neueX = x;\n  if (taste === 'ArrowLeft') neueX -= 20;\n  if (taste === 'ArrowRight') neueX += 20;\n  if (neueX < 0) neueX = 0;\n  if (neueX > 320) neueX = 320;\n  return neueX;\n}"
    );
    await task1.locator('.btn-check').click();
    await expect(task1.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
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
    await task2.locator('.code-editor').fill(
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nlet ballY = 0;\n\nfunction frame() {\n  ctx.clearRect(0, 0, canvas.width, canvas.height);\n  ctx.fillStyle = 'orange';\n  ctx.beginPath();\n  ctx.arc(200, ballY, 10, 0, Math.PI * 2);\n  ctx.fill();\n\n  requestAnimationFrame(frame);\n}\n\nframe();"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await task2.locator('.code-editor').fill(
      "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nlet ballY = 0;\n\nfunction frame() {\n  ctx.clearRect(0, 0, canvas.width, canvas.height);\n  ctx.fillStyle = 'orange';\n  ctx.beginPath();\n  ctx.arc(200, ballY, 10, 0, Math.PI * 2);\n  ctx.fill();\n\n  ballY = ballY + 2;\n\n  requestAnimationFrame(frame);\n}\n\nframe();"
    );
    await task2.locator('.btn-check').click();
    await expect(task2.locator('.feedback-success')).toBeVisible({ timeout: 10000 });
  });
});
