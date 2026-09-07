import { ref, computed, watch } from 'vue';
import { scoreQuizAnswers, isQuizPassed } from './useTaskValidation';
import { PROGRESS_APPLIED_EVENT, touchSyncKey } from './useProgressSync.js';

export { scoreQuizAnswers, isQuizPassed };

const STORAGE_KEY = 'ue-hacker-week-checks';

const configModule = import.meta.glob('../../content/python-checks/config.json');
const weekModules = import.meta.glob('../../content/python-checks/week-*.json');

let cachedWeeks = null;

export async function loadWeekChecks() {
  // Always read fresh modules so content edits show up after Vite HMR
  const configLoader = configModule['../../content/python-checks/config.json'];
  if (!configLoader) throw new Error('config.json not found');
  const configMod = await configLoader();
  const config = configMod.default || configMod;

  const weeks = {};
  await Promise.all(
    Object.entries(weekModules).map(async ([key, loader]) => {
      const num = key.match(/week-(\d+)\.json$/)[1];
      const mod = await loader();
      weeks[num] = mod.default || mod;
    })
  );

  cachedWeeks = { ...config, weeks };
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
    optionExplanations: q.optionExplanations_en || q.optionExplanations,
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

  // Options and their per-option explanations must move together, so pair
  // them up before shuffling rather than shuffling two arrays in parallel.
  const hasExplanations = Array.isArray(q.optionExplanations)
    && q.optionExplanations.length === q.options.length;
  const pairs = shuffleList(
    q.options.map((opt, i) => [opt, hasExplanations ? q.optionExplanations[i] : undefined])
  );
  const options = pairs.map(([opt]) => opt);
  const optionExplanations = hasExplanations ? pairs.map(([, expl]) => expl) : q.optionExplanations;
  const remapped = correctTexts
    .map((text) => options.indexOf(text))
    .filter((i) => i >= 0);

  if (q.type === 'multiple_select') {
    return { ...q, options, optionExplanations, correctIndices: remapped };
  }
  return {
    ...q,
    options,
    optionExplanations,
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

/** Score-Zeile fürs Wochen-Ergebnis-Raster der Einstufung (geteilte Form für frisch berechnete
 *  und aus dem Speicher wiederhergestellte Ergebnisse, siehe computePlacementResults/
 *  weekScoresToRows). */
function scoreRow(weekNumber, title, result, threshold) {
  return {
    weekNumber: Number(weekNumber),
    title,
    score: result.score,
    correct: result.correct,
    total: result.total,
    ok: isQuizPassed(result.score, threshold),
  };
}

/** Gruppiert beantwortete Einstufungsfragen nach Woche und bewertet jede Woche einzeln. */
export function computePlacementResults(questions, answers, threshold) {
  const byWeek = {};
  questions.forEach((q, i) => {
    const w = q.weekNumber;
    if (!byWeek[w]) byWeek[w] = { questions: [], answers: [], title: q.weekTitle };
    byWeek[w].questions.push(q);
    byWeek[w].answers.push(answers[i]);
  });

  const scores = {};
  const rows = [];
  for (const [weekNumber, group] of Object.entries(byWeek)) {
    const result = scoreQuizAnswers(group.questions, group.answers);
    scores[weekNumber] = { ...result, title: group.title };
    rows.push(scoreRow(weekNumber, group.title, result, threshold));
  }
  rows.sort((a, b) => a.weekNumber - b.weekNumber);
  return { scores, rows };
}

/** Wandelt gespeicherte Wochen-Scores (aus savePlacementResult) zurück in Raster-Zeilen. */
export function weekScoresToRows(weekScores, threshold) {
  return Object.entries(weekScores)
    .map(([weekNumber, s]) => scoreRow(weekNumber, s.title, s, threshold))
    .sort((a, b) => a.weekNumber - b.weekNumber);
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
  // Der Wochen-Check besteht aus zwei unabhängig abschließbaren Teilen: Quiz + Coding-Aufgaben.
  // Es gibt pro Woche mehrere Coding-Aufgaben (aktuell 2: leicht + schwerer) — codingPassed hält
  // pro Challenge-Index ein eigenes Flag. isWeekCheckPassed() ist die "vollständig bestanden"-
  // Abfrage: Quiz UND alle Coding-Aufgaben der Woche.
  const markQuizPassed = (weekNumber, scoreResult) => {
    const key = String(weekNumber);
    const existing = progress.value.weeks?.[key] || {};
    progress.value = {
      ...progress.value,
      weeks: {
        ...progress.value.weeks,
        [key]: {
          ...existing,
          quizPassed: true,
          score: scoreResult.score,
          correct: scoreResult.correct,
          total: scoreResult.total,
          at: new Date().toISOString(),
        },
      },
    };
  };

  const markCodingPassed = (weekNumber, challengeIndex = 0) => {
    const key = String(weekNumber);
    const existing = progress.value.weeks?.[key] || {};
    progress.value = {
      ...progress.value,
      weeks: {
        ...progress.value.weeks,
        [key]: {
          ...existing,
          codingPassed: { ...existing.codingPassed, [challengeIndex]: true },
          at: new Date().toISOString(),
        },
      },
    };
  };

  const isQuizPassedForWeek = (weekNumber) =>
    progress.value.weeks?.[String(weekNumber)]?.quizPassed === true;

  const isCodingChallengePassed = (weekNumber, challengeIndex = 0) =>
    progress.value.weeks?.[String(weekNumber)]?.codingPassed?.[challengeIndex] === true;

  /** Alle Coding-Aufgaben der Woche bestanden (totalChallenges = wie viele es davon gibt). */
  const isCodingPassedForWeek = (weekNumber, totalChallenges = 2) => {
    for (let i = 0; i < totalChallenges; i += 1) {
      if (!isCodingChallengePassed(weekNumber, i)) return false;
    }
    return true;
  };

  const isWeekCheckPassed = (weekNumber, totalChallenges = 2) =>
    isQuizPassedForWeek(weekNumber) && isCodingPassedForWeek(weekNumber, totalChallenges);

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
    markQuizPassed,
    markCodingPassed,
    isQuizPassedForWeek,
    isCodingChallengePassed,
    isCodingPassedForWeek,
    isWeekCheckPassed,
    savePlacementResult,
    savePlacementSession,
    placementResult,
    placementSession,
    scoreQuizAnswers,
    isQuizPassed,
  };
}
