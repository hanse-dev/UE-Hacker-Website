import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';

// Geteilte Ansicht der JS-Lektionen (JsLessonView.vue): eine gemeinsame Arbeitsflaeche
// (`.js-workspace`) pro Lektion. Breit steht sie als mitlaufende Spalte rechts neben Text und
// Aufgaben, schmal erscheint sie direkt unter der zuletzt ausgefuehrten Aufgabe.
const DRAW = "const canvas = document.getElementById('spielfeld');\nconst ctx = canvas.getContext('2d');\nctx.fillStyle = 'red';\nctx.fillRect(0, 0, 50, 50);";

const openSpielewerkstatt = async (page) => {
  await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
  await page.goto('/kurs/projekt-js-spielewerkstatt');
  await page.locator('.btn-start-course').click();
  await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
};

test.describe('JS-Lektionen: geteilte Ansicht mit Arbeitsfläche', () => {
  test('breit: Arbeitsfläche steht rechts neben den Aufgaben und läuft beim Scrollen mit', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await openSpielewerkstatt(page);

    const workspace = page.locator('.js-workspace');
    const task0 = page.locator('.task-block').nth(0);
    // Schon vor dem ersten Lauf sichtbar, mit Hinweis statt leerem Kasten.
    await expect(workspace).toBeVisible();
    await expect(workspace.locator('.js-workspace-hint')).toContainText('Ausführen');
    await expect(workspace.locator('iframe.js-sandbox')).toHaveCount(0);

    const taskBox = await task0.boundingBox();
    const wsBox = await workspace.locator('.js-workspace-inner').boundingBox();
    expect(wsBox.x).toBeGreaterThanOrEqual(taskBox.x + taskBox.width);

    await task0.locator('.btn-run').click();
    await expect(workspace.locator('.js-workspace-title')).toContainText('Aufgabe 1');
    await expect(workspace.locator('iframe.js-sandbox')).toBeVisible();

    // Weiter unten eine andere Aufgabe ausfuehren: dieselbe (einzige) Arbeitsflaeche zeigt jetzt
    // deren Ergebnis und steht weiterhin im sichtbaren Bereich.
    const task2 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task2.locator('.cm-host'), DRAW);
    await task2.locator('.btn-run').click();
    await expect(page.locator('.js-workspace .output-display')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('iframe.js-sandbox')).toHaveCount(1);
    await expect(workspace.locator('.js-workspace-title')).toContainText('Aufgabe 3');

    await page.evaluate(() => window.scrollBy(0, 400));
    const inner = await workspace.locator('.js-workspace-inner').boundingBox();
    expect(inner.y).toBeGreaterThanOrEqual(0);
    expect(inner.y + inner.height).toBeLessThanOrEqual(900);
    const t2 = await task2.boundingBox();
    expect(inner.x).toBeGreaterThanOrEqual(t2.x + t2.width);
  });

  test('schmal: Arbeitsfläche erscheint erst nach dem Lauf, direkt unter der ausgeführten Aufgabe', async ({ page }) => {
    await page.setViewportSize({ width: 800, height: 1000 });
    await openSpielewerkstatt(page);

    const workspace = page.locator('.js-workspace');
    await expect(workspace).toBeHidden();

    const task1 = page.locator('.task-block').nth(1);
    const task2 = page.locator('.task-block').nth(2);
    await setCodeMirrorContent(task1.locator('.cm-host'), DRAW);
    await task1.locator('.btn-run').click();
    await expect(task1.locator('.output-display')).toBeVisible({ timeout: 10000 });
    await expect(workspace).toBeVisible();
    await expect(workspace.locator('.js-workspace-title')).toContainText('Aufgabe 2');

    const t1 = await task1.boundingBox();
    const ws = await workspace.boundingBox();
    const t2 = await task2.boundingBox();
    expect(ws.y).toBeGreaterThanOrEqual(t1.y + t1.height - 1);
    expect(t2.y).toBeGreaterThanOrEqual(ws.y + ws.height - 1);
  });

  // Aufgaben ohne Zeichenflaeche (nur console.log, `"showCanvas": false`) - Quiz Lektion 1, Aufgabe 1.
  const openQuiz = async (page) => {
    await page.addInitScript(() => localStorage.removeItem('ue-hacker-lang'));
    await page.goto('/kurs/projekt-js-quiz');
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
  };

  test('breit: auch eine Aufgabe ohne Zeichenfläche zeigt ihr Ergebnis rechts auf der Arbeitsfläche', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await openQuiz(page);

    const task0 = page.locator('.task-block').nth(0);
    const workspace = page.locator('.js-workspace');
    await task0.locator('.btn-run').click();
    await expect(workspace.locator('.output-content')).toContainText('Wie viele Beine hat eine Spinne?', { timeout: 10000 });
    await expect(workspace.locator('.js-workspace-title')).toContainText('Aufgabe 1');
    // Keine zweite Kopie der Ausgabe unter dem Code.
    await expect(task0.locator('.output-display')).toBeHidden();
    // Der Editor nutzt die linke Spalte aus, statt bei 500px abzuschneiden.
    const editor = await task0.locator('.code-editor-wrapper').boundingBox();
    expect(editor.width).toBeGreaterThan(600);
  });

  test('schmal: Aufgabe ohne Zeichenfläche zeigt die Ausgabe unter dem Code, keine leere Arbeitsfläche', async ({ page }) => {
    await page.setViewportSize({ width: 800, height: 1000 });
    await openQuiz(page);

    const task0 = page.locator('.task-block').nth(0);
    await task0.locator('.btn-run').click();
    await expect(task0.locator('.output-content')).toContainText('Wie viele Beine hat eine Spinne?', { timeout: 10000 });
    await expect(page.locator('.js-workspace')).toBeHidden();
  });
});
