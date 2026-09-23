import { test, expect } from '@playwright/test';

const COURSE_URL = '/kurs/python-12-wochen-grundkurs';

// Seit Woche 1-12 komplett im Lektions-Format sind (siehe HANDOFF.md 3.47-3.54), gibt es in der
// Wochen-Tour keinen Notebook-Schritt mehr - die frühere Sweep-Pruefung ueber alle Tour-Schritte
// (Lektion/Debug/Missionen/Boss/Check) ist jetzt python-lektionen-format.spec.js ("Leiste mit
// allen Lektionen + Check") und python-woche1-lektionen.spec.js. Hier bleibt nur die Pruefung,
// dass die Nachschlagewerke (Glossar + Lösungen) im Seitenmenü auftauchen - das prüft sonst
// nichts anderes.
test('Nachschlagewerke (Glossar + Lösungen) stehen im Seitenmenü jeder Woche/Variante', async ({ page }) => {
  await page.goto(`${COURSE_URL}?week=12&variant=scifi`);
  await expect(page.locator('.js-course-tour')).toBeVisible();
  const refs = await page.locator('.side-menu-reference').evaluateAll(
    (els) => els.map((el) => el.dataset.referenceKey)
  );
  expect(refs).toEqual(expect.arrayContaining(['0_glossar', '6_loesungen']));
});
