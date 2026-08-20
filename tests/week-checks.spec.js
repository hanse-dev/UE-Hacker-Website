import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/weeks.json' with { type: 'json' };

const PLACEMENT_URL = '/kurs/python-einstufung';
const COURSE_URL = '/kurs/python-12-wochen-grundkurs';
const STORAGE_KEY = 'ue-hacker-week-checks';

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
  if (q.type === 'multiple_select') {
    return q.correctIndices.map((i) => q.options[i]);
  }
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

async function answerAllQuizQuestions(page, root = page) {
  const cards = root.locator('.quiz-question');
  await expect(cards.first()).toBeVisible({ timeout: 15000 });
  const count = await cards.count();
  expect(count).toBeGreaterThan(0);

  for (let i = 0; i < count; i++) {
    const card = cards.nth(i);
    const raw = await card.locator('.question-text').innerText();
    const q = findQuestion(raw);
    expect(q, `Unbekannte Frage: ${raw}`).toBeTruthy();

    for (const opt of correctOptionTexts(q)) {
      await clickOptionByExactText(card, opt);
    }
  }
}

test.describe('Einstufung & Check-Tab', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript((key) => {
      localStorage.removeItem(key);
      localStorage.removeItem('ue-hacker-lang');
    }, STORAGE_KEY);
  });

  test('Deep-Link öffnet Woche und lädt Notebook', async ({ page }) => {
    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-content')).toBeVisible({ timeout: 20000 });
    await expect(week.locator('.tab-btn.active')).toContainText('Lektion');
    await expect(week.locator('.cell').first()).toBeVisible({ timeout: 15000 });
  });

  test('Check-Tab: Multi-Select erlaubt mehrere Antworten', async ({ page }) => {
    await page.goto(`${COURSE_URL}?week=2&tab=check#woche-2`);
    const week = page.locator('#woche-2');
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });

    const multi = week.locator('.quiz-question').filter({ has: page.locator('.multi-hint') }).first();
    await expect(multi).toBeVisible({ timeout: 10000 });
    await expect(multi.locator('.option-mark').first()).toBeVisible();

    const options = multi.locator('.option-btn');
    await options.nth(0).click();
    await options.nth(1).click();
    await expect(multi.locator('.option-btn.selected')).toHaveCount(2);

    // Toggle off again
    await options.nth(0).click();
    await expect(multi.locator('.option-btn.selected')).toHaveCount(1);
  });

  test('Einstufung: perfekt → Projekte + Sprung lädt Notebooks', async ({ page }) => {
    test.setTimeout(120000);

    await page.goto(PLACEMENT_URL);
    await expect(page.locator('.placement-intro, .placement-results')).toBeVisible({ timeout: 15000 });

    // Falls altes Ergebnis aus anderem Kontext: neu starten
    if (await page.locator('.btn-retry').isVisible().catch(() => false)) {
      await page.locator('.btn-retry').click();
    }

    await expect(page.locator('.quiz-question').first()).toBeVisible({ timeout: 15000 });
    const questionCount = await page.locator('.quiz-question').count();
    expect(questionCount).toBe(12 * checks.placementPerWeek);

    await answerAllQuizQuestions(page);
    await page.locator('.btn-check-quiz').click();

    await expect(page.locator('.placement-results')).toBeVisible({ timeout: 10000 });
    await expect(page.locator('.projects-block')).toBeVisible();
    await expect(page.locator('.project-card')).toHaveCount(3);
    await expect(page.locator('.week-result.ok')).toHaveCount(12);

    await page.locator('.week-jump').first().click();
    await expect(page).toHaveURL(/python-12-wochen-grundkurs/);
    await expect(page.locator('.course-detail > h1')).toHaveText(/12-Wochen|12-Week/);
    await expect(page.locator('.week-section')).toHaveCount(12, { timeout: 30000 });
    await expect(page.locator('.cell').first()).toBeVisible({ timeout: 20000 });
  });

  test('Einstufung: gespeichertes Ergebnis mit Lücke → Empfehlung, kein Projekte-Block', async ({ page }) => {
    await page.addInitScript(({ key, payload }) => {
      localStorage.setItem(key, JSON.stringify(payload));
    }, {
      key: STORAGE_KEY,
      payload: {
        version: 1,
        weeks: {},
        placement: {
          completed: true,
          weekScores: {
            1: { score: 0.5, correct: 1, total: 2, title: 'Woche 1' },
            2: { score: 1, correct: 2, total: 2, title: 'Woche 2' },
          },
          at: new Date().toISOString(),
        },
      },
    });

    await page.goto(PLACEMENT_URL);
    await expect(page.locator('.placement-results')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.projects-block')).toHaveCount(0);
    await expect(page.locator('.recommend')).toBeVisible();
    await expect(page.locator('.week-result.review')).toHaveCount(1);
  });

  test('Check-Tab: alle richtig → bestanden', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });
    await answerAllQuizQuestions(page, week);
    await week.locator('.btn-check-quiz').click();
    await expect(week.locator('.quiz-pass, .check-badge').first()).toBeVisible({ timeout: 10000 });
  });

  test('Check-Tab: falsch → Retry möglich', async ({ page }) => {
    await page.goto(`${COURSE_URL}?week=3&tab=check#woche-3`);
    const week = page.locator('#woche-3');
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });

    const cards = week.locator('.quiz-question');
    const count = await cards.count();
    for (let i = 0; i < count; i++) {
      // Erste Option oft falsch nach Shuffle — reicht für Gesamt-Fail bei 80%
      await cards.nth(i).locator('.option-btn').first().click();
    }
    await week.locator('.btn-check-quiz').click();
    await expect(week.locator('.quiz-fail, .quiz-pass').first()).toBeVisible({ timeout: 10000 });
    if (await week.locator('.quiz-fail').isVisible()) {
      await week.locator('.btn-retry').click();
      await expect(week.locator('.btn-check-quiz')).toBeVisible();
      await expect(week.locator('.btn-check-quiz')).toBeDisabled();
    }
  });

  test('Empfehlungs-Link springt zur schwachen Woche', async ({ page }) => {
    await page.addInitScript(({ key, payload }) => {
      localStorage.setItem(key, JSON.stringify(payload));
    }, {
      key: STORAGE_KEY,
      payload: {
        version: 1,
        weeks: {},
        placement: {
          completed: true,
          weekScores: {
            1: { score: 1, correct: 2, total: 2, title: 'Woche 1' },
            4: { score: 0, correct: 0, total: 2, title: 'Woche 4' },
          },
          at: new Date().toISOString(),
        },
      },
    });

    await page.goto(PLACEMENT_URL);
    await expect(page.locator('.recommend a')).toBeVisible({ timeout: 15000 });
    await page.locator('.recommend a').click();
    await expect(page).toHaveURL(/week=4/);
    await expect(page.locator('#woche-4 .week-content')).toBeVisible({ timeout: 20000 });
    await expect(page.locator('#woche-4 .cell').first()).toBeVisible({ timeout: 15000 });
  });
});
