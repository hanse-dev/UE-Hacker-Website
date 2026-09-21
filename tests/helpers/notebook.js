// Seit Woche 1-12 alle im Lektions-Format sind, gibt es in der Wochen-Tour kein Notebook mehr als
// Kurs-Schritt. Ein echtes Notebook (Code-Zellen, "Alle ausfuehren", Kernel) liefert nur noch das
// Nachschlagewerk "Loesungen" - dafuer der gemeinsame Einstieg.
export async function openSolutionsNotebook(page, variant = 'abenteuer', week = 12) {
  await page.goto(`/kurs/python-12-wochen-grundkurs?week=${week}&variant=${variant}`);
  await page.locator('[data-reference-key="6_loesungen"]').click();
  await page.locator('.notebook-cells .cell').first().waitFor({ state: 'visible', timeout: 30000 });
}
