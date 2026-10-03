/**
 * Dev-Modus "Prüfungen überspringen" - nur zum schnellen Durchklicken eines Kurses beim
 * Entwickeln/Review, nie im Live-Betrieb.
 *
 * Aktiv nur mit `npm run dev:skip-checks` (setzt VITE_DEV_SKIP_CHECKS=1) UND im Vite-Dev-Server
 * (`import.meta.env.DEV`). Im Produktions-Build ist DEV immer false - auch eine gesetzte Variable
 * schaltet dort nichts frei (geprüft in tests/dev-skip-checks.spec.js).
 *
 * Wirkt zentral, damit jeder Kurs - auch künftige - automatisch mitmacht:
 * - useTaskValidation.js: validateOutput(), structuralChecksOk(), isAnswerCorrect() melden immer
 *   "bestanden" (Lektionsaufgaben, Wochen-Check-Coding, Quiz)
 * - useInteractiveProgress.js: alle Lektionen sind freigeschaltet
 * - LessonView/JsLessonView/CodeChallenge: "Prüfen" führt keinen Code aus (kein Warten auf den
 *   Python-Kernel), App.vue zeigt ein Hinweis-Banner.
 * Neue Prüf-Logik deshalb immer über useTaskValidation.js laufen lassen, nicht lokal nachbauen.
 */
// In Node (Tests, die useTaskValidation.js direkt importieren) gibt es kein import.meta.env.
const env = import.meta.env || {};

export const DEV_SKIP_CHECKS = Boolean(env.DEV) && env.VITE_DEV_SKIP_CHECKS === '1';
