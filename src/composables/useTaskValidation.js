/**
 * Shared validation for code tasks and quizzes.
 */

export function validateOutput(output, validation) {
  if (!validation) return true;
  const { type, expected } = validation;
  const out = (output || '').trim();
  switch (type) {
    case 'output_contains':
      return out.includes(expected);
    case 'output_equals':
      return out === expected;
    default:
      return out.includes(expected);
  }
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
