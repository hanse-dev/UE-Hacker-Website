import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/weeks.json' with { type: 'json' };

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

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

async function passWeek1Quiz(week) {
  const cards = week.locator('.quiz-question');
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
  await week.locator('.btn-check-quiz').click();
}

async function passWeek1CodingChallenge(week) {
  await expect(week.locator('.code-challenge .btn-check')).toBeEnabled({ timeout: 40000 });
  await week.locator('.code-challenge .code-editor').fill('print("Level 1 geschafft!")');
  await week.locator('.code-challenge .btn-check').click();
  await expect(week.locator('.code-challenge .feedback-success, .code-challenge .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
}

test.describe('Wochen-Zertifikate', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-fortschritt');
      localStorage.removeItem('ue-hacker-week-checks');
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Missionen allein reichen nicht — Zertifikat braucht auch den Wochen-Check', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-content')).toBeVisible({ timeout: 20000 });

    await week.locator('.missionen-panel-header').click();
    const missionItems = week.locator('.mission-item');
    await expect(missionItems.first()).toBeVisible({ timeout: 10000 });
    const missionCount = await missionItems.count();
    expect(missionCount).toBe(6);
    for (let i = 0; i < missionCount; i++) {
      await missionItems.nth(i).locator('.btn-claim').click();
    }

    await expect(week.locator('.certificate-earned')).toHaveCount(0);
  });

  test('Alle Missionen + Quiz + Coding-Aufgabe → Zertifikat wird verliehen', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-content')).toBeVisible({ timeout: 20000 });

    await week.locator('.missionen-panel-header').click();
    const missionItems = week.locator('.mission-item');
    await expect(missionItems.first()).toBeVisible({ timeout: 10000 });
    const missionCount = await missionItems.count();
    for (let i = 0; i < missionCount; i++) {
      await missionItems.nth(i).locator('.btn-claim').click();
    }

    await week.locator('.tab-btn:has-text("Check")').click();
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });
    await passWeek1Quiz(week);
    await passWeek1CodingChallenge(week);

    // Das Missionen-Panel ist eine eigene Zeile (kein Tab-Inhalt) und bleibt aufgeklappt.
    await expect(week.locator('.certificate-earned')).toBeVisible({ timeout: 5000 });
  });

  test('Coding-Aufgabe: falsche Ausgabe zeigt Fehler-Feedback, keine Bestanden-Markierung', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.code-challenge')).toBeVisible({ timeout: 20000 });
    await expect(week.locator('.code-challenge .btn-check')).toBeEnabled({ timeout: 40000 });

    await week.locator('.code-challenge .code-editor').fill('print("etwas ganz anderes")');
    await week.locator('.code-challenge .btn-check').click();
    await expect(week.locator('.code-challenge .feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(week.locator('.code-challenge .challenge-badge')).toHaveCount(0);
  });

  test('FortschrittWidget zeigt das Zertifikat im Wochen-Raster', async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-fortschritt', JSON.stringify({
        version: 3,
        courseId: 'python-12-wochen-grundkurs',
        variants: {
          abenteuer: { done: ['w1-m1', 'w1-m2', 'w1-m3', 'w1-boss1', 'w1-boss2', 'w1-boss3'] },
          pferde: { done: [] },
          scifi: { done: [] },
        },
      }));
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '1': { quizPassed: true, codingPassed: true, at: new Date().toISOString() } },
        placement: null,
      }));
    });

    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    await expect(page.locator('.week-content').first()).toBeVisible({ timeout: 20000 });

    await page.locator('.fortschritt-widget-header').click();
    await page.locator('.fortschritt-weekly-header').click();
    await page.locator('.weekly-tab-btn', { hasText: 'Abenteuer' }).click();

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    await expect(week1Card).toContainText('Verliehen');

    const week2Card = page.locator('.certificate-card').nth(1);
    await expect(week2Card).not.toHaveClass(/earned/);
  });
});
