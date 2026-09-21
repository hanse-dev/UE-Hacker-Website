// Seit alle Wochen im Lektions-Format sind, gibt es in der Wochen-Tour kein Notebook mehr als
// Kurs-Schritt. Ein echtes Notebook (Code-Zellen, "Alle ausfuehren", Kernel) liefert nur noch das
// Nachschlagewerk "Loesungen". Standard ist Woche 1 (43 Zellen): die Loesungen der spaeteren Wochen haben
// bis zu ~100 CodeMirror-Zellen und brauchen unter Last (mehrere Sessions auf dem Rechner) laenger als 30 s.
export async function openSolutionsNotebook(page, variant = 'abenteuer', week = 1, timeout = 30000) {
  await page.goto(`/kurs/python-12-wochen-grundkurs?week=${week}&variant=${variant}`);
  await page.locator('[data-reference-key="6_loesungen"]').click();
  await page.locator('.notebook-cells .cell').first().waitFor({ state: 'visible', timeout });
}
