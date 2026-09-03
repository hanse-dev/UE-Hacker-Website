import { ref, watch } from 'vue';
import { PROGRESS_APPLIED_EVENT, touchSyncKey } from './useProgressSync.js';

const STORAGE_KEY = 'ue-hacker-fortschritt';
const COURSE_ID = 'python-12-wochen-grundkurs';

// Version 3: keine Punkte/Items mehr, nur noch erledigte Missions-/Boss-Quest-IDs pro Variante.
// Ersetzt das frühere Punkte-/Sammelsystem — Belohnung ist jetzt das Wochen-Zertifikat
// (siehe useZertifikate.js), das an alle erledigten Missionen + bestandenen Wochen-Check koppelt.
const defaultState = () => ({
  version: 3,
  courseId: COURSE_ID,
  variants: {
    abenteuer: { done: [] },
    pferde: { done: [] },
    scifi: { done: [] },
  },
});

function loadFromStorage() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultState();
    const parsed = JSON.parse(raw);
    if (parsed.courseId !== COURSE_ID || parsed.version !== 3) return defaultState();
    return { ...defaultState(), ...parsed };
  } catch {
    return defaultState();
  }
}

function saveToStorage(state) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    touchSyncKey(STORAGE_KEY);
  } catch (e) {
    console.error('Fortschritt konnte nicht gespeichert werden:', e);
  }
}

// Shared state across all components
const state = ref(loadFromStorage());

if (typeof window !== 'undefined') {
  window.addEventListener(PROGRESS_APPLIED_EVENT, () => {
    state.value = loadFromStorage();
  });
}

export function useFortschritt() {

  const save = () => saveToStorage(state.value);

  watch(state, (s) => saveToStorage(s), { deep: true });

  const markDone = (variant, missionId) => {
    const v = state.value.variants[variant];
    if (!v) return false;
    const done = v.done || [];
    if (done.includes(missionId)) return false;
    v.done = [...done, missionId];
    state.value = { ...state.value };
    return true;
  };

  const markUndone = (variant, missionId) => {
    const v = state.value.variants[variant];
    if (!v?.done) return false;
    const idx = v.done.indexOf(missionId);
    if (idx === -1) return false;
    v.done.splice(idx, 1);
    state.value = { ...state.value };
    return true;
  };

  const isDone = (variant, missionId) => {
    return state.value.variants[variant]?.done?.includes(missionId) ?? false;
  };

  /** Prüft, ob alle übergebenen Mission-IDs für die Variante erledigt sind. */
  const isWeekComplete = (variant, missionIds) => {
    if (!missionIds?.length) return false;
    return missionIds.every((id) => isDone(variant, id));
  };

  const getVariantProgress = (variant) => {
    const v = state.value.variants[variant];
    return { done: [...(v?.done || [])] };
  };

  const resetProgress = (variant = null) => {
    if (variant) {
      state.value.variants[variant] = { done: [] };
    } else {
      state.value = defaultState();
    }
    state.value = { ...state.value };
  };

  const exportProgress = () => {
    return JSON.stringify(state.value, null, 2);
  };

  const importProgress = (jsonStringOrObject) => {
    try {
      const data = typeof jsonStringOrObject === 'string'
        ? JSON.parse(jsonStringOrObject)
        : jsonStringOrObject;
      if (data.courseId !== COURSE_ID) return { ok: false, error: 'Falscher Kurs' };
      for (const v of ['abenteuer', 'pferde', 'scifi']) {
        const existing = new Set(state.value.variants[v]?.done || []);
        const incoming = data.variants?.[v]?.done || [];
        for (const id of incoming) existing.add(id);
        state.value.variants[v].done = [...existing];
      }
      state.value = { ...state.value };
      return { ok: true };
    } catch (e) {
      return { ok: false, error: e.message };
    }
  };

  return {
    state,
    markDone,
    markUndone,
    isDone,
    isWeekComplete,
    getVariantProgress,
    resetProgress,
    save,
    exportProgress,
    importProgress,
  };
}
