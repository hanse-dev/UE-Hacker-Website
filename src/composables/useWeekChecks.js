import { ref, computed, watch } from 'vue';
import { scoreQuizAnswers, isQuizPassed } from './useTaskValidation';
import { PROGRESS_APPLIED_EVENT, touchSyncKey } from './useProgressSync.js';

export { scoreQuizAnswers, isQuizPassed };

const STORAGE_KEY = 'ue-hacker-week-checks';

const checksModule = import.meta.glob('../../content/python-checks/weeks.json');

let cachedWeeks = null;

export async function loadWeekChecks() {
  // Always read fresh module so content edits show up after Vite HMR
  const key = '../../content/python-checks/weeks.json';
  const loader = checksModule[key];
  if (!loader) throw new Error('weeks.json not found');
  const mod = await loader();
  cachedWeeks = mod.default || mod;
  return cachedWeeks;
}

/** Clear cache (useful after hot reload / tests). */
export function clearWeekChecksCache() {
  cachedWeeks = null;
}

export function localizeQuestion(q, lang = 'de') {
  if (lang !== 'en') return q;
  return {
    ...q,
    question: q.question_en || q.question,
    options: q.options_en || q.options,
    explanation: q.explanation_en || q.explanation,
  };
}

/** Fisher–Yates shuffle (copy). */
export function shuffleList(items) {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

/**
 * Shuffle answer options and remap correctIndex / correctIndices
 * so the right answer(s) are not always in the same position.
 */
export function shuffleQuestionOptions(q) {
  if (!q || !Array.isArray(q.options) || q.options.length < 2) {
    return q;
  }
  if (q.type === 'true_false') return q;

  const indices = Array.isArray(q.correctIndices)
    ? q.correctIndices
    : [typeof q.correctIndex === 'number' ? q.correctIndex : 0];
  const correctTexts = indices.map((i) => q.options[i]);
  const options = shuffleList(q.options);
  const remapped = correctTexts
    .map((text) => options.indexOf(text))
    .filter((i) => i >= 0);

  if (q.type === 'multiple_select') {
    return { ...q, options, correctIndices: remapped };
  }
  return {
    ...q,
    options,
    correctIndex: remapped[0] ?? 0,
  };
}

export function sampleQuestions(questions, count) {
  if (!questions?.length) return [];
  const n = Math.max(0, count ?? questions.length);
  return shuffleList(questions).slice(0, Math.min(n, questions.length)).map(shuffleQuestionOptions);
}

/** Prefer keeping multi-select questions in the sample so checkbox UI appears. */
export function sampleWeekCheckQuestions(questions, count) {
  if (!questions?.length) return [];
  const n = Math.min(Math.max(0, count ?? questions.length), questions.length);
  const multi = questions.filter((q) => q.type === 'multiple_select');
  const single = questions.filter((q) => q.type !== 'multiple_select');
  const mustKeep = sampleQuestions(multi, Math.min(multi.length, n));
  const fill = sampleQuestions(single, Math.max(0, n - mustKeep.length));
  return shuffleList([...mustKeep, ...fill]);
}

export function getWeekQuestions(data, weekNumber, lang = 'de', { sample = true } = {}) {
  const week = data?.weeks?.[String(weekNumber)];
  if (!week?.questions) return [];
  // localize first; shuffle options once when building the final set
  const localized = week.questions.map((q) => localizeQuestion(q, lang));
  if (!sample) return localized.map(shuffleQuestionOptions);
  const count = data?.weekCheckCount ?? Math.min(5, localized.length);
  return sampleWeekCheckQuestions(localized, count);
}

export function getPlacementQuestions(data, lang = 'de') {
  if (!data?.weeks) return [];
  const perWeek = data.placementPerWeek ?? 1;
  const list = [];
  for (const [weekNum, week] of Object.entries(data.weeks)) {
    const pool = (week.questions || [])
      .filter((q) => q.inPlacement)
      .map((q) => ({
        ...localizeQuestion(q, lang),
        weekNumber: Number(weekNum),
        weekTitle: lang === 'en' && week.title_en ? week.title_en : week.title,
      }));
    list.push(...sampleQuestions(pool, perWeek));
  }
  // Stable week order; options/questions within week are randomized
  return list.sort((a, b) => a.weekNumber - b.weekNumber);
}

export function getProjectIdeas(data, lang = 'de') {
  return (data?.projects || []).map((p) => ({
    id: p.id,
    title: lang === 'en' && p.title_en ? p.title_en : p.title,
    description: lang === 'en' && p.description_en ? p.description_en : p.description,
    skills: lang === 'en' && p.skills_en ? p.skills_en : (p.skills || []),
  }));
}

export function hasWeekCheck(data, weekNumber) {
  return (data?.weeks?.[String(weekNumber)]?.questions?.length || 0) > 0;
}

function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : { version: 1, weeks: {}, placement: null };
  } catch {
    return { version: 1, weeks: {}, placement: null };
  }
}

function saveProgress(state) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    touchSyncKey(STORAGE_KEY);
  } catch (e) {
    console.error('Week checks progress save failed:', e);
  }
}

const progress = ref(loadProgress());
watch(progress, (s) => saveProgress(s), { deep: true });

if (typeof window !== 'undefined') {
  window.addEventListener(PROGRESS_APPLIED_EVENT, () => {
    progress.value = loadProgress();
  });
}

export function useWeekChecks() {
  const markWeekPassed = (weekNumber, scoreResult) => {
    progress.value = {
      ...progress.value,
      weeks: {
        ...progress.value.weeks,
        [String(weekNumber)]: {
          status: 'passed',
          score: scoreResult.score,
          correct: scoreResult.correct,
          total: scoreResult.total,
          at: new Date().toISOString(),
        },
      },
    };
  };

  const isWeekCheckPassed = (weekNumber) =>
    progress.value.weeks?.[String(weekNumber)]?.status === 'passed';

  const savePlacementResult = (weekScores) => {
    if (!weekScores) {
      progress.value = { ...progress.value, placement: null };
      return;
    }
    progress.value = {
      ...progress.value,
      placement: {
        completed: true,
        weekScores,
        session: null,
        at: new Date().toISOString(),
      },
    };
  };

  /** Save in-progress placement (questions + answers + checked flags). */
  const savePlacementSession = (session) => {
    if (!session) {
      const cur = progress.value.placement;
      if (cur?.completed) return;
      progress.value = { ...progress.value, placement: null };
      return;
    }
    progress.value = {
      ...progress.value,
      placement: {
        completed: false,
        weekScores: null,
        session: {
          questions: session.questions,
          answers: session.answers,
          checked: session.checked,
          at: new Date().toISOString(),
        },
        at: new Date().toISOString(),
      },
    };
  };

  const placementResult = computed(() => progress.value.placement);
  const placementSession = computed(() => progress.value.placement?.session || null);

  return {
    progress,
    markWeekPassed,
    isWeekCheckPassed,
    savePlacementResult,
    savePlacementSession,
    placementResult,
    placementSession,
    scoreQuizAnswers,
    isQuizPassed,
  };
}
