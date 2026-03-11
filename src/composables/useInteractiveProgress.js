import { ref, computed, watch } from 'vue';

const STORAGE_KEY = 'ue-hacker-interactive-progress';
const COURSE_ID = 'python-grundlagen-interaktiv';

const defaultState = () => ({
  version: 1,
  courseId: COURSE_ID,
  completedLessonIds: [],
});

function loadFromStorage() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultState();
    const parsed = JSON.parse(raw);
    if (parsed.courseId !== COURSE_ID) return defaultState();
    return { ...defaultState(), ...parsed };
  } catch {
    return defaultState();
  }
}

function saveToStorage(state) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) {
    console.error('Fortschritt konnte nicht gespeichert werden:', e);
  }
}

const state = ref(loadFromStorage());

/**
 * Composable für Fortschritt im interaktiven Python-Grundlagen-Kurs.
 * Speichert gelöste Lektionen in localStorage.
 */
export function useInteractiveProgress() {
  const save = () => saveToStorage(state.value);

  watch(state, (s) => saveToStorage(s), { deep: true });

  const completedLessonIds = computed(() => state.value.completedLessonIds || []);

  const isCompleted = (lessonId) => completedLessonIds.value.includes(lessonId);

  const markCompleted = (lessonId) => {
    const ids = state.value.completedLessonIds || [];
    if (ids.includes(lessonId)) return true;
    state.value = {
      ...state.value,
      completedLessonIds: [...ids, lessonId],
    };
    return true;
  };

  /**
   * Prüft, ob eine Lektion freigeschaltet ist (erste Lektion oder vorherige abgeschlossen).
   * @param {string} lessonId - ID der Lektion
   * @param {Array<{id: string}>} lessons - Alle Lektionen in Reihenfolge
   */
  const isLessonUnlocked = (lessonId, lessons) => {
    if (!lessons?.length) return false;
    const index = lessons.findIndex((l) => l.id === lessonId);
    if (index < 0) return false;
    if (index === 0) return true;
    const prevId = lessons[index - 1].id;
    return isCompleted(prevId);
  };

  const getNextLessonId = (currentLessonId, lessons) => {
    if (!lessons?.length) return null;
    const index = lessons.findIndex((l) => l.id === currentLessonId);
    if (index < 0 || index >= lessons.length - 1) return null;
    return lessons[index + 1].id;
  };

  const resetProgress = () => {
    state.value = defaultState();
  };

  const exportProgress = () => JSON.stringify(state.value, null, 2);

  const importProgress = (jsonStringOrObject) => {
    try {
      const data =
        typeof jsonStringOrObject === 'string'
          ? JSON.parse(jsonStringOrObject)
          : jsonStringOrObject;
      if (data.courseId !== COURSE_ID) return { ok: false, error: 'Falscher Kurs' };
      const incoming = data.completedLessonIds || [];
      const existing = new Set(state.value.completedLessonIds || []);
      for (const id of incoming) {
        existing.add(id);
      }
      state.value = {
        ...defaultState(),
        completedLessonIds: [...existing],
      };
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
    save,
    exportProgress,
    importProgress,
  };
}
