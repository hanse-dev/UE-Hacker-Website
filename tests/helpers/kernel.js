// Startet den Python-Kernel, falls er nicht schon laeuft. Der Button ist nach dem Start
// deaktiviert ("Python bereit"); "erst isEnabled() pruefen, dann click()" ist ein Race:
// wird der Kernel dazwischen bereit, wartet click() bis zum Test-Timeout auf einen toten Button.
export async function startKernel(scope) {
  await scope.locator('.btn-kernel').first().click({ timeout: 3000 }).catch(() => {});
}
