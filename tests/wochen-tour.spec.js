import { test, expect } from '@playwright/test';
import { startKernel } from './helpers/kernel.js';
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
    await startKernel(challenge);
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

    // Woche 12 ist (wie alle Wochen) im Lektions-Format: die eingebettete Lektions-Tour
    // (JsCourseTour.vue, Klasse .js-course-tour) ersetzt die alten Notebook-Schritte.
    await page.locator('.week-tile[data-week="12"]').click();
    await expect(page.locator('.week-tile')).toHaveCount(0); // Wochen-Seite verlassen
    await expect(page.locator('.variant-tile')).toHaveCount(3);

    await page.locator('.variant-tile').nth(1).click();
    await expect(page.locator('.variant-tile')).toHaveCount(0); // Themen-Seite verlassen
    await expect(page.locator('.js-course-tour .stepper-step').first()).toHaveClass(/current/);
    await expect(page.locator('.js-course-tour .breadcrumb-lesson')).toContainText('1');
    await expect(page.locator('.task-block').first()).toBeVisible();
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

  test('Auf der ersten Lektion gibt es keinen "Weiter zu Check"-Sprung, der die Lektionen überspringt', async ({ page }) => {
    await page.goto(`${TOUR_URL}?week=1&variant=pferde`);
    await expect(page.locator('.js-course-tour .stepper-step').first()).toHaveClass(/current/);
    // Die äußere Wochen-Tour (WeekTourStepper.vue) darf hier keinen eigenen "Weiter"-Button
    // anbieten, der auf den Check-Schritt springt - die eingebettete Lektions-Tour navigiert
    // sich selbst und meldet "open-check" erst nach der letzten Lektion/Extra-Herausforderung.
    await expect(page.locator('.tour-next-btn')).toHaveCount(0);
  });

  // Die Wahl-Seite nach den Missionen (Extra-Herausforderung oder Check) gehört seit dem
  // Lektions-Format zur eingebetteten Lektions-Tour (JsCourseTour.vue) und wird dort - mit
  // echten geloesten Aufgaben statt nur Navigation - bereits geprueft, siehe
  // python-woche1-lektionen.spec.js ("mission-03 lösen -> Wahl-Seite statt direkt Extra-Herausforderung").

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
    // Unterabschnitte (Seitenmenü "Abschnitte") gibt es nur innerhalb eines Notebooks - im
    // Lektions-Format also nur in den Nachschlagewerken (Glossar/Lösungen), nicht in den Lektionen
    // selbst (siehe WeekTourStepper.vue: `headings` kommt aus dem aktuell offenen Notebook).
    await page.goto(`${TOUR_URL}?week=12&variant=pferde`);
    await page.locator('[data-reference-key="6_loesungen"]').click();
    const heading = page.locator('.side-menu-heading').first();
    await expect(heading).toBeVisible();
    const headingText = await heading.textContent();
    await heading.click();

    const targetCell = page.locator('.cell-markdown', { hasText: headingText.trim() }).first();
    await expect(targetCell).toBeInViewport();
  });

  test('Seitenmenü: Glossar öffnen und zurück zur Tour behält den Fortschritt', async ({ page }) => {
    // "Fortschritt" ist seit dem Lektions-Format die erste noch offene Lektion in der
    // eingebetteten Lektions-Tour (JsCourseTour.vue). Die Komponente wird beim Umschalten auf ein
    // Nachschlagewerk (v-if-Zweig in WeekTourStepper.vue) neu gemountet - ohne die Fixierung in
    // JsCourseTour.vue (siehe dort) würde das immer auf Lektion 1 zurückspringen.
    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-interactive-progress-python-woche12-pferde', JSON.stringify({
        version: 1, courseId: 'python-12-wochen-grundkurs', variant: 'python-woche12-pferde',
        completedLessonIds: ['lektion-01'],
      }));
    });
    await page.goto(`${TOUR_URL}?week=12&variant=pferde`);
    await expect(page.locator('.js-course-tour .breadcrumb-lesson')).toContainText('2');

    await page.locator('[data-reference-key="0_glossar"]').click();
    await expect(page.locator('.tour-reference-banner')).toBeVisible();
    await expect(page.locator('.js-course-tour')).toHaveCount(0);

    await page.locator('.tour-back-btn').click();
    await expect(page.locator('.js-course-tour .breadcrumb-lesson')).toContainText('2');
  });
});
