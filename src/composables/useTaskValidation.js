/**
 * Shared validation for code tasks and quizzes.
 */

/**
 * @param {string} output - stdout der ausgefuehrten Zelle
 * @param {object} validation - { type, expected, variables?, functionCalls? }.
 * @param {object} [variables] - tatsaechliche Werte aus dem Python-Namespace nach der Ausfuehrung
 *   (Variablenname → Wert), von der aufrufenden Komponente aus `pyodide.globals` ausgelesen.
 *   Verhindert, dass eine Aufgabe durch bloßes Ausgeben des erwarteten Texts umgangen wird, ohne
 *   die geforderten Variablen tatsaechlich anzulegen.
 * @param {Array<{expected: any, actual?: any, error?: boolean}>} [functionResults] - Ergebnisse
 *   eines erneuten Aufrufs der geforderten Funktion(en) mit einem in der Aufgabenstellung nie
 *   genannten Eingabewert (von der aufrufenden Komponente ermittelt). Deckt auf, wenn eine
 *   Funktion nur zufaellig fuer das eine vorgerechnete Beispiel das richtige Ergebnis liefert.
 */
export function validateOutput(output, validation, variables, functionResults, code) {
  if (!validation) return true;
  const { type, expected } = validation;
  const out = (output || '').trim();

  // Manche Aufgaben (z.B. Canvas-/Funktions-Checks in der JS-Spielewerkstatt) verlangen keine
  // bestimmte Ausgabe, nur echte Werte/Funktionsaufrufe oder einen Canvas-Zustand - dafuer laesst
  // `validation` das Feld `expected` bewusst weg. Kein bestehendes validation-Objekt im Repo laesst
  // `expected` weg, das ist also rueckwirkend kompatibel.
  let outputOk = true;
  if (expected !== undefined) {
    switch (type) {
      case 'output_contains':
        outputOk = out.includes(expected);
        break;
      case 'output_equals':
        outputOk = out === expected;
        break;
      default:
        outputOk = out.includes(expected);
    }
  }
  if (!outputOk) return false;

  // Struktur-Pruefung: nur wenn der Aufrufer den eingereichten Code mitgibt (LessonView).
  if (code !== undefined && missingCodeParts(code, validation).length > 0) return false;

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
 * `validation.codeContains`: Bausteine, die im Code der Lernenden vorkommen muessen (z.B. `def`, `class`,
 * `super()`, `try`), damit ein hart codiertes `print` nicht besteht. Kommentarzeilen zaehlen nicht;
 * Woerter werden ganz gematcht (`def` trifft nicht `undefined`). Texte in Anfuehrungszeichen werden
 * nicht ausgeklammert - bewusst einfach gehalten.
 * @returns {string[]} die fehlenden Bausteine (leer = alles da)
 */
export function missingCodeParts(code, validation) {
  const required = validation?.codeContains;
  if (!Array.isArray(required) || required.length === 0) return [];
  const source = String(code || '').split('\n').filter((line) => !line.trim().startsWith('#')).join('\n');
  return required.filter((token) => {
    const escaped = token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const pattern = (/^\w/.test(token) ? '\\b' : '') + escaped + (/\w$/.test(token) ? '\\b' : '');
    return !new RegExp(pattern).test(source);
  });
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
