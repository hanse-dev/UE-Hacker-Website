/**
 * Shared validation for code tasks and quizzes.
 */

/**
 * @param {string} output - stdout der ausgefuehrten Zelle
 * @param {object} validation - { type, expected }.
 *
 * Prueft bewusst nur die Ausgabe - nicht, wie sie zustande kam. Fuer den Wochen-Check
 * (`CodeChallenge.vue`, zertifikatsrelevant) gibt es dafuer zusaetzlich `structuralChecksOk()`.
 */
export function validateOutput(output, validation) {
  if (!validation) return true;
  const { type, expected } = validation;
  const out = (output || '').trim();

  // Manche Aufgaben (z.B. Canvas-/Funktions-Checks in der JS-Spielewerkstatt) verlangen keine
  // bestimmte Ausgabe, nur echte Werte/Funktionsaufrufe oder einen Canvas-Zustand - dafuer laesst
  // `validation` das Feld `expected` bewusst weg. Kein bestehendes validation-Objekt im Repo laesst
  // `expected` weg, das ist also rueckwirkend kompatibel.
  if (expected === undefined) return true;

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
