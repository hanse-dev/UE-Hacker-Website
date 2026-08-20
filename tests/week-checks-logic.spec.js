import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/weeks.json' with { type: 'json' };
import {
  isAnswerCorrect,
  scoreQuizAnswers,
  getCorrectIndices,
} from '../src/composables/useTaskValidation.js';

function shuffleList(items) {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

function shuffleQuestionOptions(q) {
  if (!q || !Array.isArray(q.options) || q.options.length < 2) return q;
  const indices = Array.isArray(q.correctIndices)
    ? q.correctIndices
    : [typeof q.correctIndex === 'number' ? q.correctIndex : 0];
  const correctTexts = indices.map((i) => q.options[i]);
  const options = shuffleList(q.options);
  const remapped = correctTexts.map((text) => options.indexOf(text)).filter((i) => i >= 0);
  if (q.type === 'multiple_select') return { ...q, options, correctIndices: remapped };
  return { ...q, options, correctIndex: remapped[0] ?? 0 };
}

test.describe('Checks: Logik & Content', () => {
  test('weeks.json: 12 Wochen, Placement-Pool, Multi-Select', () => {
    expect(Object.keys(checks.weeks)).toHaveLength(12);
    expect(checks.placementPerWeek).toBeGreaterThanOrEqual(2);
    expect(checks.projects).toHaveLength(3);

    for (const [num, week] of Object.entries(checks.weeks)) {
      expect(week.questions.length, `week ${num}`).toBeGreaterThanOrEqual(8);
      const placement = week.questions.filter((q) => q.inPlacement);
      expect(placement.length, `week ${num} placement pool`).toBeGreaterThanOrEqual(
        checks.placementPerWeek
      );
      expect(week.questions.some((q) => q.type === 'multiple_select')).toBeTruthy();
      for (const q of week.questions) {
        expect(q.type === 'true_false').toBeFalsy();
        expect(q.options?.length).toBeGreaterThanOrEqual(2);
        if (q.type === 'multiple_select') {
          expect(q.correctIndices.length).toBeGreaterThanOrEqual(2);
        } else {
          expect(typeof q.correctIndex).toBe('number');
        }
      }
    }
  });

  test('Scoring: single + multi-select', () => {
    const single = { type: 'multiple_choice', correctIndex: 1, options: ['a', 'b', 'c'] };
    const multi = { type: 'multiple_select', correctIndices: [0, 2], options: ['a', 'b', 'c', 'd'] };
    expect(isAnswerCorrect(single, 1)).toBeTruthy();
    expect(isAnswerCorrect(multi, [2, 0])).toBeTruthy();
    expect(isAnswerCorrect(multi, [0])).toBeFalsy();
    const scored = scoreQuizAnswers([single, multi], [1, [0, 2]]);
    expect(scored).toEqual({ score: 1, correct: 2, total: 2 });
  });

  test('Option-Shuffle behält richtige Antwort(en)', () => {
    const q = {
      type: 'multiple_select',
      options: ['richtig-a', 'falsch', 'richtig-b', 'auch-falsch'],
      correctIndices: [0, 2],
    };
    for (let i = 0; i < 20; i++) {
      const shuffled = shuffleQuestionOptions(q);
      const texts = getCorrectIndices(shuffled).map((idx) => shuffled.options[idx]).sort();
      expect(texts).toEqual(['richtig-a', 'richtig-b']);
    }
  });

  test('Jede Woche hat genug Placement-Fragen für placementPerWeek', () => {
    for (const [num, week] of Object.entries(checks.weeks)) {
      const pool = week.questions.filter((q) => q.inPlacement).length;
      expect(pool, `week ${num}`).toBeGreaterThanOrEqual(checks.placementPerWeek);
    }
  });
});
