import { test, expect } from '@playwright/test';
import checks from '../content/python-checks/weeks.json' with { type: 'json' };
import {
  isAnswerCorrect,
  scoreQuizAnswers,
  getCorrectIndices,
  explanationForAnswer,
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
  const hasExplanations = Array.isArray(q.optionExplanations)
    && q.optionExplanations.length === q.options.length;
  const pairs = shuffleList(
    q.options.map((opt, i) => [opt, hasExplanations ? q.optionExplanations[i] : undefined])
  );
  const options = pairs.map(([opt]) => opt);
  const optionExplanations = hasExplanations ? pairs.map(([, expl]) => expl) : q.optionExplanations;
  const remapped = correctTexts.map((text) => options.indexOf(text)).filter((i) => i >= 0);
  if (q.type === 'multiple_select') return { ...q, options, optionExplanations, correctIndices: remapped };
  return { ...q, options, optionExplanations, correctIndex: remapped[0] ?? 0 };
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

  test('Personalisierte Falsch-Antworten: vorhanden, ausgerichtet, echt übersetzt', () => {
    for (const [num, week] of Object.entries(checks.weeks)) {
      for (const q of week.questions) {
        if (q.type === 'multiple_select') {
          expect(q.optionExplanations, `week ${num} ${q.id} multi-select sollte keine optionExplanations haben`).toBeUndefined();
          continue;
        }
        expect(q.optionExplanations, `week ${num} ${q.id} optionExplanations fehlt`).toBeDefined();
        expect(q.optionExplanations_en, `week ${num} ${q.id} optionExplanations_en fehlt`).toBeDefined();
        expect(q.optionExplanations.length, `week ${num} ${q.id}`).toBe(q.options.length);
        expect(q.optionExplanations_en.length, `week ${num} ${q.id}`).toBe(q.options.length);
        q.options.forEach((_, i) => {
          if (i === q.correctIndex) {
            expect(q.optionExplanations[i], `week ${num} ${q.id} correctIndex(${i}) sollte leer sein`).toBeFalsy();
            expect(q.optionExplanations_en[i], `week ${num} ${q.id} correctIndex(${i}) EN sollte leer sein`).toBeFalsy();
          } else {
            expect(q.optionExplanations[i], `week ${num} ${q.id} Option ${i} ohne Erklärung`).toBeTruthy();
            expect(q.optionExplanations_en[i], `week ${num} ${q.id} Option ${i} EN ohne Erklärung`).toBeTruthy();
            expect(q.optionExplanations[i], `week ${num} ${q.id} Option ${i}: DE=EN, wohl unübersetzt`).not.toBe(q.optionExplanations_en[i]);
          }
        });
      }
    }
  });

  test('explanation_en ist echtes Englisch, nicht die deutsche Dopplung', () => {
    for (const [num, week] of Object.entries(checks.weeks)) {
      for (const q of week.questions) {
        expect(q.explanation, `week ${num} ${q.id} explanation fehlt`).toBeTruthy();
        expect(q.explanation_en, `week ${num} ${q.id} explanation_en fehlt`).toBeTruthy();
        expect(q.explanation, `week ${num} ${q.id}: explanation === explanation_en, wohl unübersetzt`).not.toBe(q.explanation_en);
      }
    }
  });

  test('explanationForAnswer: personalisiert bei Treffer, sonst geteilte Erklärung', () => {
    const q = {
      type: 'multiple_choice',
      correctIndex: 0,
      options: ['richtig', 'Print(...)', 'print[...]'],
      explanation: 'Geteilte Erklärung.',
      explanation_en: 'Shared explanation.',
      optionExplanations: [null, 'Großschreibung ist falsch.', 'Eckige statt runde Klammern.'],
      optionExplanations_en: [null, 'Capitalisation is wrong.', 'Square instead of round brackets.'],
    };
    expect(explanationForAnswer(q, 1, 'de')).toBe('Großschreibung ist falsch.');
    expect(explanationForAnswer(q, 2, 'de')).toBe('Eckige statt runde Klammern.');
    expect(explanationForAnswer(q, 1, 'en')).toBe('Capitalisation is wrong.');
    // Frage ohne optionExplanations fällt auf die geteilte Erklärung zurück
    const legacy = { type: 'multiple_choice', correctIndex: 0, options: ['a', 'b'], explanation: 'Geteilt.' };
    expect(explanationForAnswer(legacy, 1, 'de')).toBe('Geteilt.');
    // Multi-Select-Antworten (Array) nutzen immer die geteilte Erklärung
    const multi = {
      type: 'multiple_select',
      correctIndices: [0],
      options: ['a', 'b'],
      explanation: 'Geteilt für Multi-Select.',
    };
    expect(explanationForAnswer(multi, [1], 'de')).toBe('Geteilt für Multi-Select.');
  });

  test('Option-Shuffle hält Erklärung an ihrer Option fest', () => {
    const q = {
      type: 'multiple_choice',
      options: ['print("Hi")', 'Print("Hi")', 'print[Hi]'],
      correctIndex: 0,
      optionExplanations: [null, 'Großschreibung ist falsch.', 'Eckige Klammern statt runder.'],
    };
    const originalPairing = new Map(q.options.map((opt, i) => [opt, q.optionExplanations[i]]));
    for (let i = 0; i < 20; i++) {
      const shuffled = shuffleQuestionOptions(q);
      shuffled.options.forEach((opt, idx) => {
        expect(shuffled.optionExplanations[idx]).toBe(originalPairing.get(opt));
      });
      expect(shuffled.options[shuffled.correctIndex]).toBe('print("Hi")');
    }
  });
});
