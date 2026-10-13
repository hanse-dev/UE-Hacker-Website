import { expect } from '@playwright/test';

// Startet den Python-Kernel, falls er nicht schon laeuft. Der Button ist nach dem Start
// deaktiviert ("Python bereit"); "erst isEnabled() pruefen, dann click()" ist ein Race:
// wird der Kernel dazwischen bereit, wartet click() bis zum Test-Timeout auf einen toten Button.
// dispatchEvent statt click: die smooth-scroll-Animation beim Lektionswechsel verschiebt den Button,
// ein Maus-Klick (auch mit force) scheitert dann sporadisch mit "Element is outside of the viewport".
// Ein deaktivierter Button ignoriert das Ereignis, es gibt also nichts abzuwarten.
export async function startKernel(scope) {
  await scope.locator('.btn-kernel').first().dispatchEvent('click', {}, { timeout: 3000 }).catch(() => {});
}

// Vor dem Loesen einer Lektion aufrufen: Nach "Weiter" zeigt die Seite kurz noch die alte, schon
// abgeschlossene Lektion. Wer sofort tippt, fuellt deren Editor - die Eingabe ist nach dem Wechsel weg.
export async function waitForFreshLesson(page) {
  await expect(page.locator('.lesson-complete-box')).toHaveCount(0);
}
