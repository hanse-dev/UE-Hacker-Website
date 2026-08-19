import { ref, computed, watch } from 'vue';

const COURSE_ID = 'python-lernpfad';
const STORAGE_KEY = 'ue-hacker-learner-progress';

function defaultState(variant) {
  return {
    version: 1,
    courseId: COURSE_ID,
    variant,
    placementCompleted: false,
    placementTopicScores: {},
    topics: {},
  };
}

function loadFromStorage(variant) {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultState(variant);
    const parsed = JSON.parse(raw);
    const variantData = parsed[variant] || {};
    return { ...defaultState(variant), ...variantData };
  } catch {
    return defaultState(variant);
  }
}

function saveToStorage(variant, state, allVariants) {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    const existing = raw ? JSON.parse(raw) : {};
    existing[variant] = state;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(existing));
  } catch (e) {
    console.error('Learner progress could not be saved:', e);
  }
}

const states = {};

function getVariantState(variant) {
  if (!states[variant]) {
    states[variant] = ref(loadFromStorage(variant));
    watch(states[variant], (s) => saveToStorage(variant, s), { deep: true });
  }
  return states[variant];
}

function ensureTopic(state, topicId) {
  if (!state.topics[topicId]) {
    state.topics[topicId] = {
      status: 'not_started',
      skipScore: null,
      completedSteps: [],
    };
  }
  return state.topics[topicId];
}

export function useLearnerProgress(variant = 'kinder') {
  const state = getVariantState(variant);

  const getTopicStatus = (topicId) => {
    const t = state.value.topics[topicId];
    return t?.status || 'not_started';
  };

  const isTopicDone = (topicId) => {
    const status = getTopicStatus(topicId);
    return status === 'completed' || status === 'skipped';
  };

  const markTopicInProgress = (topicId) => {
    const topics = { ...state.value.topics };
    const t = ensureTopic({ topics }, topicId);
    if (t.status === 'not_started') {
      topics[topicId] = { ...t, status: 'in_progress' };
      state.value = { ...state.value, topics };
    }
  };

  const markStepCompleted = (topicId, stepId) => {
    const topics = { ...state.value.topics };
    const t = ensureTopic({ topics }, topicId);
    const steps = t.completedSteps.includes(stepId)
      ? t.completedSteps
      : [...t.completedSteps, stepId];
    topics[topicId] = { ...t, status: 'in_progress', completedSteps: steps };
    state.value = { ...state.value, topics };
  };

  const markTopicCompleted = (topicId) => {
    const topics = { ...state.value.topics };
    const t = ensureTopic({ topics }, topicId);
    topics[topicId] = { ...t, status: 'completed', completedAt: new Date().toISOString() };
    state.value = { ...state.value, topics };
  };

  const markTopicSkipped = (topicId, skipScore) => {
    const topics = { ...state.value.topics };
    const t = ensureTopic({ topics }, topicId);
    topics[topicId] = {
      ...t,
      status: 'skipped',
      skipScore,
      completedAt: new Date().toISOString(),
    };
    state.value = { ...state.value, topics };
  };

  const markPlacementCompleted = (topicScores = {}) => {
    state.value = {
      ...state.value,
      placementCompleted: true,
      placementTopicScores: topicScores,
    };
  };

  const completedTopicIds = computed(() =>
    Object.entries(state.value.topics || {})
      .filter(([, t]) => t.status === 'completed' || t.status === 'skipped')
      .map(([id]) => id)
  );

  const completedCount = computed(() => completedTopicIds.value.length);

  const getRecommendedTopics = (allTopics, limit = 3) => {
    if (!allTopics?.length) return [];
    return allTopics
      .filter((topic) => !isTopicDone(topic.id))
      .sort((a, b) => (a.order ?? 0) - (b.order ?? 0))
      .slice(0, limit);
  };

  const getNextRecommendedTopic = (allTopics) => {
    const rec = getRecommendedTopics(allTopics, 1);
    return rec[0] || null;
  };

  const isStepCompleted = (topicId, stepId) => {
    const t = state.value.topics[topicId];
    return t?.completedSteps?.includes(stepId) ?? false;
  };

  const resetProgress = () => {
    state.value = defaultState(variant);
  };

  const exportProgress = () => JSON.stringify(state.value, null, 2);

  const importProgress = (jsonStringOrObject) => {
    try {
      const data = typeof jsonStringOrObject === 'string'
        ? JSON.parse(jsonStringOrObject)
        : jsonStringOrObject;
      state.value = { ...defaultState(variant), ...data };
      return { ok: true };
    } catch (e) {
      return { ok: false, error: e.message };
    }
  };

  return {
    state,
    completedTopicIds,
    completedCount,
    getTopicStatus,
    isTopicDone,
    markTopicInProgress,
    markStepCompleted,
    markTopicCompleted,
    markTopicSkipped,
    markPlacementCompleted,
    getRecommendedTopics,
    getNextRecommendedTopic,
    isStepCompleted,
    resetProgress,
    exportProgress,
    importProgress,
  };
}

/** Map week numbers to topic IDs for 12-week checkpoint links. */
export function getTopicsForWeek(weekNumber, allTopics) {
  if (!allTopics?.length) return [];
  return allTopics.filter((t) => t.links?.weekNumbers?.includes(weekNumber));
}
