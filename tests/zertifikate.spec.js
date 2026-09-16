import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/index.mjs';

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

async function passCodingChallenge(week, challengeIndex, code) {
  const challenge = week.locator(`.code-challenge[data-challenge-index="${challengeIndex}"]`);
  await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });
  await challenge.locator('.code-editor').fill(code);
  await challenge.locator('.btn-check').click();
  await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
}

async function passWeek1CodingChallenges(week) {
  await passCodingChallenge(week, 0, 'print("Level 1 geschafft!")');
  await passCodingChallenge(week, 1, 'name = "Nova"\nlevel = 3\nprint(name + " hat Level " + str(level) + " erreicht!")');
}

test.describe('Wochen-Zertifikate', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.removeItem('ue-hacker-fortschritt');
      localStorage.removeItem('ue-hacker-week-checks');
      localStorage.removeItem('ue-hacker-lang');
    });
  });

  test('Missionen allein reichen nicht — Zertifikat braucht den Wochen-Check', async ({ page }) => {
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

  test('Nur Quiz ohne beide Coding-Aufgaben reicht nicht', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });
    await passWeek1Quiz(week);
    await passCodingChallenge(week, 0, 'print("Level 1 geschafft!")');

    await expect(week.locator('.certificate-earned')).toHaveCount(0);
  });

  test('Quiz + beide Coding-Aufgaben (ohne Missionen) → Zertifikat wird verliehen', async ({ page }) => {
    test.setTimeout(90000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    await expect(week.locator('.week-check-panel')).toBeVisible({ timeout: 20000 });
    await passWeek1Quiz(week);
    await passWeek1CodingChallenges(week);

    await week.locator('.missionen-panel-header').click();
    await expect(week.locator('.certificate-earned')).toBeVisible({ timeout: 5000 });
  });

  test('Coding-Aufgabe: falsche Ausgabe zeigt Fehler-Feedback, keine Bestanden-Markierung', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    const challenge = week.locator('.code-challenge[data-challenge-index="0"]');
    await expect(challenge).toBeVisible({ timeout: 20000 });
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });

    await challenge.locator('.code-editor').fill('print("etwas ganz anderes")');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(challenge.locator('.challenge-badge')).toHaveCount(0);
  });

  test('Coding-Aufgabe: erwartete Variablen fehlen trotz passender Textausgabe → nicht bestanden', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=1&tab=check#woche-1`);
    const week = page.locator('#woche-1');
    const challenge = week.locator('.code-challenge[data-challenge-index="1"]');
    await expect(challenge).toBeVisible({ timeout: 20000 });
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });

    // Den erwarteten Text hart kodieren, ohne die geforderten Variablen anzulegen - die
    // Ausgabe allein passt exakt, die Aufgabe verlangt aber echte name/level-Variablen.
    await challenge.locator('.code-editor').fill('print("Nova hat Level 3 erreicht!")');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(challenge.locator('.challenge-badge')).toHaveCount(0);

    // Mit echten Variablen muss dieselbe Aufgabe weiterhin bestehen (kein Overblocking).
    await challenge.locator('.code-editor').fill(
      'name = "Nova"\nlevel = 3\nprint(name + " hat Level " + str(level) + " erreicht!")'
    );
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Coding-Aufgabe: verlangtes Dictionary fehlt trotz passender Textausgabe → nicht bestanden', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=8&tab=check#woche-8`);
    const week = page.locator('#woche-8');
    const challenge = week.locator('.code-challenge[data-challenge-index="0"]');
    await expect(challenge).toBeVisible({ timeout: 20000 });
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });

    // Hart kodiert, ohne das verlangte "person"-Dictionary anzulegen.
    await challenge.locator('.code-editor').fill('print("Alex")');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(challenge.locator('.challenge-badge')).toHaveCount(0);

    // Mit echtem Dictionary muss dieselbe Aufgabe weiterhin bestehen (kein Overblocking).
    await challenge.locator('.code-editor').fill('person = {"name": "Alex"}\nprint(person["name"])');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Coding-Aufgabe: Funktion, die nur zufällig für das Beispiel stimmt → nicht bestanden', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=5&tab=check#woche-5`);
    const week = page.locator('#woche-5');
    const challenge = week.locator('.code-challenge[data-challenge-index="0"]');
    await expect(challenge).toBeVisible({ timeout: 20000 });
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });

    // Gar keine Funktion, nur hart kodiert.
    await challenge.locator('.code-editor').fill('print(12)');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(challenge.locator('.challenge-badge')).toHaveCount(0);

    // "verdopple(6)" stimmt zufaellig auch mit +6 statt *2 (ergibt ebenfalls 12) - der Re-Test
    // mit einem zweiten, nie genannten Wert (verdopple(10)) muss das aufdecken: 10+6=16 != 20.
    await challenge.locator('.code-editor').fill('def verdopple(zahl):\n    return zahl + 6\nprint(verdopple(6))');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });
    await expect(challenge.locator('.challenge-badge')).toHaveCount(0);

    // Echte, korrekte Funktion muss weiterhin bestehen (kein Overblocking).
    await challenge.locator('.code-editor').fill('def verdopple(zahl):\n    return zahl * 2\nprint(verdopple(6))');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('Coding-Aufgabe: zweite Funktionsaufgabe (addiere) besteht mit echter Lösung', async ({ page }) => {
    test.setTimeout(60000);
    await page.goto(`${COURSE_URL}?week=5&tab=check#woche-5`);
    const week = page.locator('#woche-5');
    const challenge = week.locator('.code-challenge[data-challenge-index="1"]');
    await expect(challenge).toBeVisible({ timeout: 20000 });
    await expect(challenge.locator('.btn-check')).toBeEnabled({ timeout: 40000 });

    await challenge.locator('.code-editor').fill('print(17)');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-error')).toBeVisible({ timeout: 10000 });

    await challenge.locator('.code-editor').fill('def addiere(a, b):\n    return a + b\nprint(addiere(9, 8))');
    await challenge.locator('.btn-check').click();
    await expect(challenge.locator('.feedback-success, .challenge-feedback.feedback-success')).toBeVisible({ timeout: 10000 });
  });

  test('FortschrittWidget zeigt das Zertifikat im Wochen-Raster', async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() } },
        placement: null,
      }));
    });

    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    await expect(page.locator('.week-content').first()).toBeVisible({ timeout: 20000 });

    await page.locator('.fortschritt-widget-header').click();
    await page.locator('.fortschritt-weekly-header').click();

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    await expect(week1Card).toContainText('Verliehen');

    const week2Card = page.locator('.certificate-card').nth(1);
    await expect(week2Card).not.toHaveClass(/earned/);
  });

  test('PDF-Download braucht einen Account — ohne Login nur Hinweistext', async ({ page }) => {
    await page.addInitScript(() => {
      localStorage.setItem('ue-hacker-week-checks', JSON.stringify({
        version: 1,
        weeks: { '1': { quizPassed: true, codingPassed: { 0: true, 1: true }, at: new Date().toISOString() } },
        placement: null,
      }));
    });

    await page.goto(`${COURSE_URL}?week=1&tab=lektion#woche-1`);
    await expect(page.locator('.week-content').first()).toBeVisible({ timeout: 20000 });

    await page.locator('.fortschritt-widget-header').click();
    await page.locator('.fortschritt-weekly-header').click();

    const week1Card = page.locator('.certificate-card').first();
    await expect(week1Card).toHaveClass(/earned/);
    await expect(week1Card.locator('.btn-certificate-pdf')).toHaveCount(0);
    await expect(week1Card.locator('.certificate-login-hint')).toBeVisible();
  });
});
