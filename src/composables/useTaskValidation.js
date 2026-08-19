/**
 * Shared validation for code tasks (interactive course + learning path).
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
    if (q.type === 'true_false') {
      if (answer === q.correct) correct++;
    } else if (q.type === 'multiple_choice') {
      if (answer === q.correctIndex) correct++;
    }
  }
  return { score: correct / questions.length, correct, total: questions.length };
}

export function isQuizPassed(score, threshold = 0.8) {
  return score >= threshold;
}
