import { test, expect } from '@playwright/test';

// Regression tests for the storytelling overhaul (see HANDOFF.md, section 3.4).
// These assert on rendered notebook TEXT so they run fast (no Pyodide/kernel
// needed) and catch the exact bugs that were found and fixed during that work.

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

async function openWeek(page, weekIndex) {
  const week = page.locator('.week-section').nth(weekIndex);
  if (weekIndex !== 0) await week.locator('.week-header').click();
  await week.locator('.cell').first().waitFor({ state: 'visible', timeout: 8000 });
  return week;
}

async function selectVariant(week, label) {
  await week.locator(`.variant-btn:has-text("${label}")`).click();
  await week.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
}

async function selectTab(week, label) {
  await week.locator(`.tab-btn:has-text("${label}")`).click();
  await week.locator('.cell').first().waitFor({ state: 'visible', timeout: 5000 });
}

test.describe('Storytelling-Überarbeitung: Pferde', () => {
  test('Woche 2: Hufschlag-Typen benannt, kein "Sonnentals"-Tippfehler', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week = await openWeek(page, 1); // Woche 2
    await selectVariant(week, 'Pferde');
    await selectTab(week, 'Lektion');

    const text = await week.locator('.notebook-cells').innerText();
    expect(text).toContain('Sonnental');
    expect(text).not.toContain('Sonnentals');
    for (const gait of ['Schritt', 'Trab', 'Galopp', 'Sprung']) {
      expect(text).toContain(gait);
    }
  });

  test('Woche 9: eigene Rahmengeschichte statt Woche-8-Duplikat, korrektes Belohnungsitem', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week8 = await openWeek(page, 7); // Woche 8
    await selectVariant(week8, 'Pferde');
    await selectTab(week8, 'Lektion');
    const week8Text = await week8.locator('.notebook-cells').innerText();

    const week9 = await openWeek(page, 8); // Woche 9
    await selectVariant(week9, 'Pferde');
    await selectTab(week9, 'Lektion');
    const week9Text = await week9.locator('.notebook-cells').innerText();

    expect(week9Text).toContain('Zuchtbücher von Sonnental');
    // The two weeks must not share their opening story paragraph anymore.
    const week8Intro = week8Text.split('\n').slice(0, 6).join('\n');
    expect(week9Text).not.toContain(week8Intro);
    expect(week9Text).not.toContain('Sonnentals');

    await selectTab(week9, 'Missionen');
    const missionsText = await week9.locator('.notebook-cells').innerText();
    expect(missionsText).toContain('Stammbaum-Urkunde');
    expect(missionsText).not.toContain('Daten-Chip');
  });

  test('Woche 12: Huf-Punkte statt XP', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week = await openWeek(page, 11); // Woche 12
    await selectVariant(week, 'Pferde');
    await selectTab(week, 'Boss-Quest');

    const text = await week.locator('.notebook-cells').innerText();
    expect(text).toContain('Huf-Punkte');
    expect(text).not.toMatch(/\bXP\b/);
  });
});

test.describe('Storytelling-Überarbeitung: Sci-Fi', () => {
  test('Woche 11: Lektion-Code ist syntaktisch korrekt (def/self vorhanden)', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week = await openWeek(page, 10); // Woche 11
    await selectVariant(week, 'Sci-Fi');
    await selectTab(week, 'Lektion');

    const text = await week.locator('.notebook-cells').innerText();
    expect(text).toContain('Raumstation Nebula-7');
    expect(text).not.toContain('Evolution-Station Alpha-7');

    const codeCells = week.locator('.cell-code .code-editor');
    const count = await codeCells.count();
    expect(count).toBeGreaterThan(0);
    for (let i = 0; i < count; i++) {
      const code = await codeCells.nth(i).inputValue();
      // The original bug: every method inside a class was missing "def" and/or
      // "self" (e.g. "aktivieren():" instead of "def aktivieren(self):", or
      // "def __init__(id, name):" instead of "def __init__(self, id, name):").
      // Any line indented >=4 that looks like a method signature must start
      // with "def" and take "self" as its first parameter.
      for (const line of code.split('\n')) {
        const indent = line.match(/^ */)[0].length;
        const trimmed = line.trim();
        if (indent < 4 || !/^[a-zA-Z_]\w*\(.*\):\s*$/.test(trimmed)) continue;
        expect(trimmed.startsWith('def ')).toBe(true);
        const params = trimmed.match(/^def\s+\w+\(([^)]*)\)/)[1];
        const firstParam = params.split(',')[0].trim();
        if (firstParam !== '') {
          expect(firstParam).toBe('self');
        }
      }
    }
  });

  test('Woche 6/8: Boss-Quest 2 ist nicht mehr der Woche-5-Klon', async ({ page }) => {
    await page.goto(COURSE_URL);

    const week5 = await openWeek(page, 4);
    await selectVariant(week5, 'Sci-Fi');
    await selectTab(week5, 'Boss-Quest');
    const week5Text = await week5.locator('.notebook-cells').innerText();
    expect(week5Text).toContain('Der Raumstation-Manager');

    const week6 = await openWeek(page, 5);
    await selectVariant(week6, 'Sci-Fi');
    await selectTab(week6, 'Boss-Quest');
    const week6Text = await week6.locator('.notebook-cells').innerText();
    expect(week6Text).toContain('Der Hangar-Verwalter');
    expect(week6Text).not.toContain('Der Raumstation-Manager');

    const week8 = await openWeek(page, 7);
    await selectVariant(week8, 'Sci-Fi');
    await selectTab(week8, 'Boss-Quest');
    const week8Text = await week8.locator('.notebook-cells').innerText();
    expect(week8Text).toContain('Die Sensor-Matrix');
    expect(week8Text).not.toContain('Der Raumstation-Manager');
  });

  test('Woche 12: Cyber Credits statt XP', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week = await openWeek(page, 11); // Woche 12
    await selectVariant(week, 'Sci-Fi');
    await selectTab(week, 'Boss-Quest');

    const text = await week.locator('.notebook-cells').innerText();
    expect(text).toContain('Cyber Credits');
    expect(text).not.toMatch(/\bXP\b/);
  });

  test('Woche 12: Debug-Bugs verraten die Lösung nicht im Kommentar', async ({ page }) => {
    await page.goto(COURSE_URL);
    const week = await openWeek(page, 11); // Woche 12
    await selectVariant(week, 'Sci-Fi');
    await selectTab(week, 'Debug');

    const codeCells = week.locator('.cell-code .code-editor');
    const count = await codeCells.count();
    for (let i = 0; i < count; i++) {
      const code = await codeCells.nth(i).inputValue();
      expect(code).not.toMatch(/#\s*Bug:/i);
    }
  });
});
