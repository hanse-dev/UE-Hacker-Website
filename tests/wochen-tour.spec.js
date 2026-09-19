import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/index.mjs';

const TOUR_URL = '/kurs/python-12-wochen-grundkurs';

function findQuestion(text) {
  const normalized = text.replace(/^\d+\.\s*/, '').trim();
  for (const week of Object.values(checks.weeks)) {
    for (const q of week.questions) {
      if (q.question === normalized || q.question_en === normalized) return q;
    }
  }
  return null;
}

function correctOptionTexts(q) {
  if (q.type === 'multiple_select') return q.correctIndices.map((i) => q.options[i]);
  return [q.options[q.correctIndex]];
}

async function clickOptionByExactText(card, opt) {
  const buttons = card.locator('.option-btn');
  const count = await buttons.count();
  for (let i = 0; i < count; i++) {
    const text = (await buttons.nth(i).innerText()).replace(/^[☐☑]\s*/, '').trim();
    if (text === opt) {
      await buttons.nth(i).click();
      return;
    }
  }
  throw new Error(`Option not found: ${opt}`);
}

async function passWeek1CheckForReal(page) {
  const cards = page.locator('.quiz-question');
  await expect(cards.first()).toBeVisible({ timeout: 20000 });
  const count = await cards.count();
  for (let i = 0; i < count; i++) {
    const card = cards.nth(i);
    const raw = await card.locator('.question-text').innerText();
    const q = findQuestion(raw);
    expect(q, `Unbekannte Frage: ${raw}`).toBeTruthy();
    for (const opt of correctOptionTexts(q)) {
      await clickOptionByExactText(card, opt);
    }
  }
  await page.locator('.btn-check-quiz').click();

  async function passCoding(index, code) {
    const challenge = page.locator(`.code-challenge[data-challenge-index="${index}"]`);
    const kernelBtn = challenge.locator('.btn-kernel');
    if (await kernelBtn.isEnabled()) await kernelBtn.click();
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });
    await challenge.locator('.code-editor').fill(code);
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
  }
  await passCoding(0, 'print("Level 1 geschafft!")');
  await passCoding(1, 'name = "Nova"\nlevel = 3\nprint(name + " hat Level " + str(level) + " erreicht!")');
}

test.describe('12-Wochen-Kurs: Wochen-Tour', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-lang');
      localStorage.removeItem('ue-hacker-fortschritt');
      localStorage.removeItem('ue-hacker-week-checks');
    });
  });

  test('Kachel-Flow: Woche wählen -> Thema wählen -> Tour startet auf Lektion', async ({ page }) => {
    await page.goto(TOUR_URL);
    await expect(page.locator('.week-tile')).toHaveCount(12);

    // Woche 12: frühe Wochen sind im Lektions-Format (python-woche1-lektionen.spec.js)
    await page.locator('.week-tile[data-week="12"]').click();
    await expect(page.locator('.week-tile')).toHaveCount(0); // Wochen-Seite verlassen
    await expect(page.locator('.variant-tile')).toHaveCount(3);

    await page.locator('.variant-tile').nth(1).click();
    await expect(page.locator('.variant-tile')).toHaveCount(0); // Themen-Seite verlassen
    await expect(page.locator('.stepper-step.current')).toContainText('Lektion');
    await expect(page.locator('.tour-content .cell-markdown').first()).toBeVisible();
  });

  test('Wochen-Pfad: Schlangen-Anordnung platziert den Zeilenumbruch senkrecht statt quer über das Raster', async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(TOUR_URL);
    // Spaltenzahl kommt aus dem tatsächlich gerenderten Grid (auto-fill, abhängig vom Seiten-
    // Layout drumherum) - die letzte Woche der ersten Zeile hat die Wochennummer == Spaltenzahl.
    const cols = await page.locator('.week-tile-grid').evaluate(
      (el) => getComputedStyle(el).gridTemplateColumns.split(' ').filter(Boolean).length
    );
    expect(cols).toBeGreaterThan(1);
    const lastOfRow1 = await page.locator(`.week-tile[data-week="${cols}"]`).boundingBox();
    const firstOfRow2 = await page.locator(`.week-tile[data-week="${cols + 1}"]`).boundingBox();
    expect(lastOfRow1).toBeTruthy();
    expect(firstOfRow2).toBeTruthy();
    // Bei echter Schlangen-Anordnung (Zeile 2 läuft rückwärts) liegt die erste Woche der
    // zweiten Zeile direkt unter der letzten Woche der ersten Zeile in derselben Spalte -
    // ohne Umkehrung läge sie stattdessen ganz links.
    expect(Math.abs(lastOfRow1.x - firstOfRow2.x)).toBeLessThan(30);
    expect(firstOfRow2.y).toBeGreaterThan(lastOfRow1.y);
  });

  test('Breadcrumb springt zurück zur Wochen- bzw. Themen-Seite', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=2&variant=abenteuer`);
    await expect(page.locator('.tour-breadcrumb')).toBeVisible();

    await page.locator('.tour-breadcrumb .breadcrumb-link').nth(1).click(); // Thema wechseln
    await expect(page.locator('.variant-tile')).toHaveCount(3);

    await page.locator('.breadcrumb-back').click(); // zurück zur Wochen-Seite
    await expect(page.locator('.week-tile')).toHaveCount(12);
  });

  test('Nach den Missionen führt eine Wahl-Seite zu Extra-Herausforderung oder Check', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=12&variant=pferde&step=3_missionen`);
    await expect(page.locator('.stepper-step.current')).toContainText('Missionen');
    await page.locator('.tour-next-btn').click();

    await expect(page.locator('.branch-choice-page')).toBeVisible();
    await expect(page.locator('[data-branch="5_boss"]')).toContainText('Extra-Herausforderung');
    await expect(page.locator('[data-branch="4_check"]')).toContainText('Check');
    // Während der Wahl ist kein Tour-Schritt als "aktuell" markiert
    await expect(page.locator('.stepper-step.current')).toHaveCount(0);

    await page.locator('[data-branch="5_boss"]').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Extra-Herausforderung');
    await expect(page.locator('.stepper-step[data-step-key="5_boss"].done')).toHaveCount(1);

    await page.locator('.tour-next-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Check');
    await expect(page.locator('.week-check-panel')).toBeVisible();
  });

  test('Check direkt wählen überspringt die Extra-Herausforderung (bleibt unbesucht)', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=12&variant=pferde&step=3_missionen`);
    await expect(page.locator('.stepper-step.current')).toContainText('Missionen');
    await page.locator('.tour-next-btn').click();
    await page.locator('[data-branch="4_check"]').click();

    await expect(page.locator('.stepper-step.current')).toContainText('Check');
    await expect(page.locator('.stepper-step[data-step-key="5_boss"].done')).toHaveCount(0);
  });

  test('Bestandener Check zeigt das Zertifikat und führt zur nächsten Woche', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${TOUR_URL}?week=1&variant=pferde&step=4_check`);
    await passWeek1CheckForReal(page);

    await expect(page.locator('.certificate-reveal')).toBeVisible();
    await expect(page.locator('.certificate-reveal')).toContainText('Woche 1');
    await expect(page.locator('[data-after-check="overview"]')).toBeVisible();
    await expect(page.locator('[data-after-check="next-week"]')).toBeVisible();

    // Ganz unten beim Check-Schritt - nach "Nächste Woche" muss die neue Lektion oben beginnen,
    // nicht irgendwo mittendrin auf der alten Scroll-Position.
    await page.mouse.wheel(0, 2000);
    await expect.poll(() => page.evaluate(() => window.scrollY)).toBeGreaterThan(200);

    await page.locator('[data-after-check="next-week"]').click();
    await expect(page).toHaveURL(/week=2&variant=pferde/);
    await expect(page.locator('.tour-breadcrumb')).toContainText('Woche 2');
    await expect(page.locator('.tour-breadcrumb')).toContainText('Pferde');
    // Woche 2 ist im Lektions-Format: die eingebettete Lektions-Tour startet auf Lektion 1
    await expect(page.locator('.js-course-tour .stepper-step.current')).toContainText('1');
    // Scrollt zum Anfang der Lektion selbst (.tour-stepper), nicht zum obersten Seitenrand
    // (Kursbeschreibung/Banner stehen ja weiterhin darüber).
    await expect(page.locator('.tour-stepper')).toBeInViewport({ timeout: 2000 });
  });

  test('Zertifikat erscheint als Abzeichen in der Übersicht und auf der Zertifikate-Seite', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${TOUR_URL}?week=1&variant=pferde&step=4_check`);
    await passWeek1CheckForReal(page);
    await expect(page.locator('.certificate-reveal')).toBeVisible();

    await page.locator('.tour-breadcrumb .breadcrumb-link').first().click(); // zurück zur Wochenübersicht
    await expect(page.locator('.week-tile[data-week="1"] .week-tile-badge')).toBeVisible();
    await expect(page.locator('.certificates-link')).toContainText('1/12');

    await page.locator('.certificates-link').click();
    await expect(page.locator('.certificate-card.earned')).toHaveCount(1);
    await expect(page.locator('.certificate-card.earned')).toContainText('Woche 1');
  });

  test('"Nächste Woche" gibt es bei Woche 12 nicht mehr, nur noch "Zur Übersicht"', async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '12': { quizPassed: true, codingPassed: { 0: true, 1: true } } },
        placement: null,
      }));
    });
    await page.goto(`${TOUR_URL}?week=12&variant=abenteuer&step=4_check`);
    await expect(page.locator('.certificate-reveal')).toBeVisible();
    await expect(page.locator('[data-after-check="overview"]')).toBeVisible();
    await expect(page.locator('[data-after-check="next-week"]')).toHaveCount(0);
  });

  test('"Zur Übersicht"/"Nächste Woche" sind auch ohne bestandenen Check verfügbar', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=2&variant=abenteuer&step=4_check`);
    await expect(page.locator('.tour-check-pending')).toBeVisible();
    await expect(page.locator('.certificate-reveal')).toHaveCount(0);
    await expect(page.locator('[data-after-check="overview"]')).toBeVisible();
    await expect(page.locator('[data-after-check="next-week"]')).toBeVisible();

    await page.locator('[data-after-check="next-week"]').click();
    await expect(page).toHaveURL(/week=3&variant=abenteuer/);
    // Woche 3 ist im Lektions-Format: eingebettete Lektions-Tour statt Notebook-Schritte
    await expect(page.locator('.js-course-tour')).toBeVisible();
  });

  test('Seitenmenü lässt sich ein- und ausklappen', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=12&variant=pferde`);
    await expect(page.locator('.tour-side-menu')).toBeVisible();

    await page.locator('.side-menu-toggle').click();
    await expect(page.locator('.tour-side-menu')).toHaveCount(0);

    await page.locator('.side-menu-toggle').click();
    await expect(page.locator('.tour-side-menu')).toBeVisible();
  });

  test('Seitenmenü: Sprung zu einem Unterabschnitt scrollt zur passenden Zelle', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=12&variant=pferde`);
    const heading = page.locator('.side-menu-heading').first();
    await expect(heading).toBeVisible();
    const headingText = await heading.textContent();
    await heading.click();

    const targetCell = page.locator('.cell-markdown', { hasText: headingText.trim() }).first();
    await expect(targetCell).toBeInViewport();
  });

  test('Seitenmenü: Glossar öffnen und zurück zur Tour behält den Fortschritt', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=12&variant=pferde`);
    await page.locator('.tour-next-btn').click(); // -> Debug
    await expect(page.locator('.stepper-step.current')).toContainText('Debug');

    await page.locator('[data-reference-key="0_glossar"]').click();
    await expect(page.locator('.tour-reference-banner')).toBeVisible();
    await expect(page.locator('.stepper-step.current')).toHaveCount(0);

    await page.locator('.tour-back-btn').click();
    await expect(page.locator('.stepper-step.current')).toContainText('Debug');
  });
});
