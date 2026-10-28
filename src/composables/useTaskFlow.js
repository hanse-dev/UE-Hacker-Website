/**
 * Weiter-Flow in Lektionen (LessonView.vue, JsLessonView.vue): Nach einer geloesten Aufgabe fuehrt
 * ein Knopf zur naechsten offenen Aufgabe, statt dass Kinder sie selbst suchen muessen.
 */

/**
 * Index der naechsten offenen Pflicht-Aufgabe nach `fromIdx` (danach von vorne), sonst -1.
 * @param {Array<{example?: boolean}>} tasks
 * @param {(idx: number) => boolean} isDone - erledigt oder uebersprungen
 */
export function nextOpenTask(tasks, isDone, fromIdx) {
  const n = tasks.length;
  for (let step = 1; step < n; step++) {
    const idx = (fromIdx + step) % n;
    if (!tasks[idx]?.example && !isDone(idx)) return idx;
  }
  return -1;
}

/** Scrollt zur Aufgabe `idx` (n-tes `.task-block` in `root`) und setzt den Cursor in ihren Editor. */
export function focusTask(root, idx) {
  const block = root?.querySelectorAll('.task-block')[idx];
  if (!block) return;
  block.scrollIntoView({ behavior: 'smooth', block: 'start' });
  block.querySelector('textarea, .cm-content')?.focus({ preventScroll: true });
}
