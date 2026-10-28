/**
 * Shared validation for code tasks and quizzes.
 */
import { DEV_SKIP_CHECKS } from './devSkipChecks.js';

/**
 * @param {string} output - stdout der ausgefuehrten Zelle
 * @param {object} validation - { type, expected }. `expected` darf bei `output_contains` auch eine
 *   Liste sein: dann muss jeder Eintrag in der Ausgabe vorkommen (Aufgaben mit mehreren geforderten
 *   Zeilen, z.B. Ueberschrift + Ergebnis).
 *
 * Prueft bewusst nur die Ausgabe - nicht, wie sie zustande kam. Fuer den Wochen-Check
 * (`CodeChallenge.vue`, zertifikatsrelevant) gibt es dafuer zusaetzlich `structuralChecksOk()`.
 */
export function validateOutput(output, validation) {
  if (DEV_SKIP_CHECKS) return true;
  if (!validation) return true;
  const { type, expected } = validation;
  const out = (output || '').trim();

  // Manche Aufgaben (z.B. Canvas-/Funktions-Checks in der JS-Spielewerkstatt) verlangen keine
  // bestimmte Ausgabe, nur echte Werte/Funktionsaufrufe oder einen Canvas-Zustand - dafuer laesst
  // `validation` das Feld `expected` bewusst weg. Kein bestehendes validation-Objekt im Repo laesst
  // `expected` weg, das ist also rueckwirkend kompatibel.
  if (expected === undefined) return true;

  if (Array.isArray(expected) && type !== 'output_equals') return missingExpected(out, validation).length === 0;

  switch (type) {
    case 'output_contains':
      // Bewusst tolerant: Groß-/Kleinschreibung, mehrfache/rand-staendige Leerzeichen und
      // Satzzeichen am Ende sind fuer den Lerninhalt nicht relevant und sollen eine sonst
      // richtige Loesung nicht durchfallen lassen. `output_equals` bleibt exakt (prueft
      // teils bewusst auch auf ungewollte Extra-Ausgabe).
      return normalizeForComparison(out).includes(normalizeForComparison(expected));
    case 'output_equals':
      return out === expected;
    default:
      return normalizeForComparison(out).includes(normalizeForComparison(expected));
  }
}

/**
 * Die Eintraege von `validation.expected`, die in der Ausgabe fehlen (tolerant wie
 * `output_contains`) - fuer den Hinweis ab dem zweiten Fehlversuch: gezeigt wird der erste
 * fehlende statt der ganzen Liste.
 */
export function missingExpected(output, validation) {
  const expected = validation?.expected;
  if (expected === undefined) return [];
  const out = normalizeForComparison((output || '').trim());
  return (Array.isArray(expected) ? expected : [expected])
    .filter((e) => !out.includes(normalizeForComparison(e)));
}

/**
 * `validation.varies` (Zufalls-Aufgaben, Woche 7): Die Aufgabe wird mehrmals ausgefuehrt und muss
 * dabei mindestens einmal eine andere Ausgabe liefern. So faellt auf, wenn die Zufallswerte gar
 * nicht aus `random` kommen, ohne dass der Code selbst geprueft wird. Die Aufgabe muss dafuer den
 * gezogenen Wert mit ausgeben.
 */
export const VARIES_MAX_RUNS = 6;

export function outputsVary(outputs) {
  if (DEV_SKIP_CHECKS) return true;
  return new Set(outputs.map((o) => (o || '').trim())).size > 1;
}

/**
 * Web-Kurse (`validation.type: 'web'`): Bei HTML/CSS ist die gerenderte Seite die "Ausgabe".
 * `validation.checks` ist eine Liste, jede Pruefung muss passen:
 *   { selector, min = 1, max?, text?, notEmpty?, property?, value?, notValue?, hint? }
 * Ein Element zaehlt nur, wenn es alle eigenen Bedingungen erfuellt (Text enthaelt `text`, ist
 * nicht leer, berechneter CSS-Wert von `property` gleich `value` bzw. ungleich `notValue`); davon
 * muss es mindestens `min` geben. `max` begrenzt die Gesamtzahl der Treffer des Selektors.
 * Attribute prueft der Selektor selbst, z.B. `img[alt]:not([alt=""])`.
 *
 * @param {object} validation
 * @param {Array|null} facts - je Pruefung { count, elements: [{ text, actual }], expected?,
 *   notExpected? } aus der Sandbox (useJsSandbox.js, checkWeb) - CSS-Werte schon vom Browser
 *   normalisiert, hier wird nur verglichen.
 * @returns {{ ok: boolean, failedIndex: number }} failedIndex = erste nicht erfuellte Pruefung
 *   (fuer ihren `hint`), sonst -1.
 */
export function validateWebChecks(validation, facts) {
  if (DEV_SKIP_CHECKS) return { ok: true, failedIndex: -1 };
  const checks = validation?.checks || [];
  for (let i = 0; i < checks.length; i++) {
    if (!webCheckOk(checks[i], facts?.[i])) return { ok: false, failedIndex: i };
  }
  return { ok: true, failedIndex: -1 };
}

function webCheckOk(check, fact) {
  if (!fact || fact.error) return false;
  if (check.max !== undefined && fact.count > check.max) return false;
  const matching = (fact.elements || []).filter((el) => {
    if (check.text !== undefined && !normalizeForComparison(el.text).includes(normalizeForComparison(check.text))) return false;
    if (check.notEmpty && !el.text) return false;
    if (check.property) {
      if (check.value !== undefined && el.actual !== fact.expected) return false;
      if (check.notValue !== undefined && el.actual === fact.notExpected) return false;
    }
    return true;
  });
  return matching.length >= (check.min ?? 1);
}

/**
 * Zusaetzlich zu `validateOutput()`: prueft, ob die geforderten Variablen/Funktionsergebnisse
 * wirklich vorliegen - verhindert, dass der Wochen-Check (Zertifikat) durch bloßes Ausgeben des
 * erwarteten Texts umgangen wird, ohne die Variablen/Funktionen tatsaechlich anzulegen. Bewusst
 * nur fuer `CodeChallenge.vue` (Wochen-Check) genutzt, nicht fuer normale Lektionsaufgaben
 * (`LessonView.vue`/`JsLessonView.vue`) - dort zaehlt nur die Ausgabe.
 * @param {object} [variables] - tatsaechliche Werte aus dem Namespace nach der Ausfuehrung.
 * @param {Array<{expected: any, actual?: any, error?: boolean}>} [functionResults] - Ergebnisse
 *   eines erneuten Aufrufs der geforderten Funktion(en) mit einem in der Aufgabenstellung nie
 *   genannten Eingabewert. Deckt auf, wenn eine Funktion nur zufaellig fuer das eine
 *   vorgerechnete Beispiel das richtige Ergebnis liefert.
 */
export function structuralChecksOk(validation, variables, functionResults) {
  if (DEV_SKIP_CHECKS) return true;
  if (!validation) return true;

  if (validation.variables) {
    const ok = Object.entries(validation.variables).every(([name, expectedValue]) => {
      if (!variables || !(name in variables)) return false;
      return valuesMatch(variables[name], expectedValue);
    });
    if (!ok) return false;
  }

  if (validation.functionCalls) {
    if (!functionResults) return false;
    const ok = functionResults.every((r) => !r.error && valuesMatch(r.actual, r.expected));
    if (!ok) return false;
  }

  return true;
}

/**
 * Normalisiert einen Ausgabe-String fuer den (tolerannten) `output_contains`-Vergleich:
 * Groß-/Kleinschreibung ignorieren, mehrfache/fuehrende/folgende Leerzeichen zusammenfassen,
 * Satzzeichen am Ende weglassen (z.B. "Fläche 40." vs. "Fläche 40").
 */
function normalizeForComparison(str) {
  return String(str || '')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim()
    .replace(/[.,!?:;]+$/, '');
}

/**
 * Vergleicht einen aus Python gelesenen Wert mit einem erwarteten Wert. Skalare (Zahl, String,
 * Bool) werden direkt verglichen. Ist der erwartete Wert ein Objekt (z.B. bei einer Aufgabe, die
 * ein Dictionary verlangt), wird rekursiv Schluessel fuer Schluessel verglichen - der aufrufenden
 * Komponente reicht es, die geforderte Variable per `pyodide.globals.get(name).toJs(...)` als
 * einfaches JS-Objekt zu uebergeben.
 */
function valuesMatch(actual, expected) {
  if (expected !== null && typeof expected === 'object' && !Array.isArray(expected)) {
    if (actual === null || typeof actual !== 'object') return false;
    return Object.entries(expected).every(([key, val]) => valuesMatch(actual[key], val));
  }
  return actual === expected;
}

export function scoreQuizAnswers(questions, answers) {
  if (!questions?.length) return { score: 1, correct: 0, total: 0 };
  let correct = 0;
  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const answer = answers[i];
    if (isAnswerCorrect(q, answer)) correct++;
  }
  return { score: correct / questions.length, correct, total: questions.length };
}

/** Normalize correct option indices for single- and multi-select. */
export function getCorrectIndices(q) {
  if (!q) return [];
  if (q.type === 'multiple_select' && Array.isArray(q.correctIndices)) {
    return [...q.correctIndices].map(Number).sort((a, b) => a - b);
  }
  if (typeof q.correctIndex === 'number') return [q.correctIndex];
  // legacy true_false → treat as unused
  return [];
}

export function isAnswerCorrect(q, answer) {
  if (DEV_SKIP_CHECKS) return true;
  if (q?.type === 'true_false') {
    return answer === q.correct;
  }
  if (q?.type === 'multiple_select') {
    const expected = getCorrectIndices(q);
    const got = Array.isArray(answer)
      ? [...answer].map(Number).sort((a, b) => a - b)
      : [];
    if (expected.length !== got.length) return false;
    return expected.every((v, i) => v === got[i]);
  }
  // multiple_choice (default)
  return answer === q.correctIndex;
}

export function isQuizPassed(score, threshold = 0.8) {
  return score >= threshold;
}

/**
 * Explanation text for a given (possibly wrong) answer. Prefers a per-option
 * explanation (personalized to the specific wrong option picked) over the
 * question's shared explanation. Only single-choice answers (a number) can
 * have a per-option explanation — multi-select answers always fall back to
 * the shared explanation, since several options may be wrong at once.
 */
export function explanationForAnswer(q, answer, lang = 'de') {
  if (typeof answer === 'number') {
    const perOption = lang === 'en' && Array.isArray(q?.optionExplanations_en)
      ? q.optionExplanations_en
      : q?.optionExplanations;
    if (Array.isArray(perOption) && perOption[answer]) return perOption[answer];
  }
  return lang === 'en' && q?.explanation_en ? q.explanation_en : q?.explanation;
}
