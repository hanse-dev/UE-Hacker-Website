import { ref, computed, watch } from 'vue';
import { PROGRESS_APPLIED_EVENT, touchSyncKey } from './useProgressSync.js';

const COURSE_ID = 'python-grundlagen-interaktiv';

function storageKey(variant) {
  return `ue-hacker-interactive-progress-${variant}`;
}

function defaultState(variant, courseId = COURSE_ID) {
  return { version: 1, courseId, variant, completedLessonIds: [] };
}

function loadFromStorage(variant, courseId) {
  try {
    const raw = localStorage.getItem(storageKey(variant));
    if (!raw) return defaultState(variant, courseId);
    const parsed = JSON.parse(raw);
    return { ...defaultState(variant, courseId), ...parsed };
  } catch {
    return defaultState(variant, courseId);
  }
}

function saveToStorage(variant, state) {
  try {
    localStorage.setItem(storageKey(variant), JSON.stringify(state));
    touchSyncKey(storageKey(variant));
  } catch (e) {
    console.error('Fortschritt konnte nicht gespeichert werden:', e);
  }
}

const states = {};

function getVariantState(variant, courseId) {
  if (!states[variant]) {
    states[variant] = ref(loadFromStorage(variant, courseId));
    watch(states[variant], (s) => saveToStorage(variant, s), { deep: true });
    if (typeof window !== 'undefined') {
      window.addEventListener(PROGRESS_APPLIED_EVENT, () => {
        states[variant].value = loadFromStorage(variant, courseId);
      });
    }
  }
  return states[variant];
}

export function useInteractiveProgress(variant = 'kinder', courseId = COURSE_ID) {
  const state = getVariantState(variant, courseId);

  const completedLessonIds = computed(() => state.value.completedLessonIds || []);
  const isCompleted = (lessonId) => completedLessonIds.value.includes(lessonId);

  const markCompleted = (lessonId) => {
    const ids = state.value.completedLessonIds || [];
    if (ids.includes(lessonId)) return true;
    state.value = { ...state.value, completedLessonIds: [...ids, lessonId] };
    return true;
  };

  const isLessonUnlocked = (lessonId, lessons) => {
    if (!lessons?.length) return false;
    const index = lessons.findIndex((l) => l.id === lessonId);
    if (index < 0) return false;
    if (index === 0) return true;
    return isCompleted(lessons[index - 1].id);
  };

  const getNextLessonId = (currentLessonId, lessons) => {
    if (!lessons?.length) return null;
    const index = lessons.findIndex((l) => l.id === currentLessonId);
    if (index < 0 || index >= lessons.length - 1) return null;
    return lessons[index + 1].id;
  };

  const resetProgress = () => { state.value = defaultState(variant, courseId); };

  const exportProgress = () => JSON.stringify(state.value, null, 2);

  const importProgress = (jsonStringOrObject) => {
    try {
      const data = typeof jsonStringOrObject === 'string'
        ? JSON.parse(jsonStringOrObject)
        : jsonStringOrObject;
      const incoming = data.completedLessonIds || [];
      const existing = new Set(state.value.completedLessonIds || []);
      for (const id of incoming) existing.add(id);
      state.value = { ...defaultState(variant, courseId), completedLessonIds: [...existing] };
      return { ok: true };
    } catch (e) {
      return { ok: false, error: e.message };
    }
  };

  const completedCount = computed(() => (state.value.completedLessonIds || []).length);

  return {
    state,
    completedLessonIds,
    completedCount,
    isCompleted,
    markCompleted,
    isLessonUnlocked,
    getNextLessonId,
    resetProgress,
    save: () => saveToStorage(variant, state.value),
    exportProgress,
    importProgress,
  };
}
