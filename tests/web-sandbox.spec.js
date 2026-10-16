import { test, expect } from '@playwright/test';
import { setCodeMirrorContent } from './helpers/codemirror.js';
import { readFileSync } from 'fs';

const lessons = JSON.parse(readFileSync(new URL('../content/web-erste-website/lessons.json', import.meta.url), 'utf-8'));

const STORAGE_KEY = 'ue-hacker-interactive-progress-web-erste-website';
const COURSE_URL = '/kurs/web-erste-website';

// Web-Modus der JS-Sandbox (`"sandboxMode": "web"` in kurse.json): Das HTML des Kindes ist selbst
// die Seite im iframe der Arbeitsflaeche, Pruefungen laufen ueber `validation.type: 'web'`
// (useTaskValidation.js validateWebChecks, Fakten aus useJsSandbox.js checkWeb).
test.describe('Web-Sandbox (Meine erste Website)', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem(key);
    }, STORAGE_KEY);
    await page.goto(COURSE_URL);
    await page.locator('.btn-start-course').click();
    await expect(page.locator('.task-block').first()).toBeVisible({ timeout: 15000 });
  });

  const preview = (page) => page.frameLocator('.js-workspace iframe.js-sandbox');
  const task = (page, idx) => page.locator('.task-block').nth(idx);

  const check = async (page, idx, code) => {
    const t = task(page, idx);
    await setCodeMirrorContent(t.locator('.cm-host'), code);
    await t.locator('.btn-check').click();
    await expect(t.locator('.feedback')).toBeVisible({ timeout: 10000 });
    return t;
  };

  test('Beispiel zeigt die Seite des Kindes als Vorschau, ohne Canvas und ohne leere Ausgabe-Box', async ({ page }) => {
    const t0 = task(page, 0);
    await expect(t0.locator('.cm-host .cm-content')).toContainText('<h1>Hallo Welt!</h1>');
    await t0.locator('.btn-run').click();
    await expect(t0.locator('.task-done')).toBeVisible({ timeout: 10000 });
    await expect(preview(page).locator('h1')).toHaveText('Hallo Welt!');
    await expect(preview(page).locator('p')).toHaveText('Das ist meine allererste Website.');
    await expect(preview(page).locator('canvas, #dom-uebung')).toHaveCount(0);
    await expect(page.locator('.output-display')).toHaveCount(0);
  });

  test('Jede Pflichtaufgabe: unveraenderte Vorlage faellt durch, Musterloesung besteht', async ({ page }) => {
    test.setTimeout(60000);
    for (const [idx, data] of lessons[0].tasks.entries()) {
      if (data.example) continue;
      const t = await check(page, idx, data.codeTemplate);
      await expect(t.locator('.feedback-error')).toBeVisible();
      await check(page, idx, data.solution);
      await expect(t.locator('.feedback-success')).toBeVisible();
    }
  });

  test('Mehrere Pruefungen: alle muessen passen, beim zweiten Fehlversuch kommt der Hinweis der ersten offenen', async ({ page }) => {
    const [h1Check, pCheck] = lessons[0].tasks[1].validation.checks;
    const onlyOneP = '<h1>Mein Hund</h1>\n<p>Er heißt Bello.</p>';
    let t = await check(page, 1, onlyOneP);
    await expect(t.locator('.feedback-error')).toBeVisible();
    t = await check(page, 1, onlyOneP);
    await expect(t.locator('.feedback-error')).toHaveText(pCheck.hint);

    // Leerer Absatz zaehlt nicht (notEmpty), fehlende Ueberschrift meldet den h1-Hinweis.
    t = await check(page, 1, '<h1></h1>\n<p>Eins</p>\n<p></p>');
    await expect(t.locator('.feedback-error')).toHaveText(h1Check.hint);

    t = await check(page, 1, '<h1>Mein Hund</h1>\n<p>Er heißt Bello.</p>\n<p>Er mag Bälle.</p>');
    await expect(t.locator('.feedback-success')).toBeVisible();
  });

  test('CSS-Werte werden vom Browser normalisiert: #000 gilt als black, #ff0000 als Farbe', async ({ page }) => {
    const page3 = (color) => `<h1 style="color: ${color}">Titel</h1>`;
    let t = await check(page, 2, page3('#000'));
    await expect(t.locator('.feedback-error')).toBeVisible();
    t = await check(page, 2, page3('rgb(0, 0, 0)'));
    await expect(t.locator('.feedback-error')).toBeVisible();
    t = await check(page, 2, page3('#ff0000'));
    await expect(t.locator('.feedback-success')).toBeVisible();
    await expect(preview(page).locator('h1')).toHaveCSS('color', 'rgb(255, 0, 0)');
  });

  test('Vorschau bleibt stehen: Sprungmarken scrollen, Formulare werden nicht abgeschickt, console.log landet in der Ausgabe', async ({ page }) => {
    const t1 = task(page, 1);
    const code = [
      '<!DOCTYPE html>',
      '<html><head><style>#unten { margin-top: 2000px; }</style></head><body>',
      '<h1 id="oben">Oben</h1>',
      '<a id="sprung" href="#unten">Nach unten</a>',
      '<a id="weg" href="/projekte">Zur Kursseite</a>',
      '<form><button id="senden">Senden</button></form>',
      '<p id="unten">Unten</p>',
      '<script>console.log("Hallo aus dem Skript");</script>',
      '</body></html>',
    ].join('\n');
    await setCodeMirrorContent(t1.locator('.cm-host'), code);
    await t1.locator('.btn-run').click();
    const frame = preview(page);
    await expect(frame.locator('#oben')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.js-workspace .js-workspace-output')).toContainText('Hallo aus dem Skript');

    await frame.locator('#sprung').click();
    await expect(frame.locator('#unten')).toBeInViewport();
    await frame.locator('#weg').click();
    await frame.locator('#senden').click();
    // Die Seite im iframe ist noch dieselbe (kein Wegnavigieren auf die Kursseite, kein Neuladen).
    await expect(frame.locator('#oben')).toHaveText('Oben');
    await expect(frame.locator('#sprung')).toBeVisible();
  });

  test('Sicherheitsregeln gelten auch fuer die Seite des Kindes: Bilder von fremden Servern sind gesperrt', async ({ page }) => {
    const t1 = task(page, 1);
    const code = [
      '<p id="csp">frei</p>',
      '<script>document.addEventListener("securitypolicyviolation", (e) => {',
      '  document.getElementById("csp").textContent = e.effectiveDirective + " " + e.blockedURI;',
      '});</script>',
      '<img src="https://example.com/bild.png" alt="fremd">',
    ].join('\n');
    await setCodeMirrorContent(t1.locator('.cm-host'), code);
    await t1.locator('.btn-run').click();
    await expect(preview(page).locator('#csp')).toHaveText('img-src https://example.com/bild.png', { timeout: 10000 });
  });

  test('Schmale Ansicht: der zusaetzliche Download-Knopf bricht um statt aus der Aufgabe zu ragen', async ({ page }) => {
    await page.setViewportSize({ width: 420, height: 900 });
    const t1 = task(page, 1);
    const block = await t1.boundingBox();
    const button = await t1.locator('.btn-download').boundingBox();
    expect(button.x + button.width).toBeLessThanOrEqual(block.x + block.width);
  });

  test('Seite herunterladen liefert genau den eigenen Code, Bildpfade zeigen auf die volle Adresse', async ({ page }) => {
    const t1 = task(page, 1);
    const code = '<h1>Mein Hund</h1>\n<img src="/web-bilder/hund.png" alt="Hund">';
    await setCodeMirrorContent(t1.locator('.cm-host'), code);
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      t1.locator('.btn-download').click(),
    ]);
    expect(download.suggestedFilename()).toBe('meine-website.html');
    const content = readFileSync(await download.path(), 'utf-8');
    const origin = new URL(page.url()).origin;
    expect(content).toBe(`<h1>Mein Hund</h1>\n<img src="${origin}/web-bilder/hund.png" alt="Hund">`);
  });
});
