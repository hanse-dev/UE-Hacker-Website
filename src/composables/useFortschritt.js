import { ref, computed, watch } from 'vue';

const STORAGE_KEY = 'ue-hacker-fortschritt';
const COURSE_ID = 'python-12-wochen-grundkurs';

const defaultState = () => ({
  version: 2,
  courseId: COURSE_ID,
  variants: {
    abenteuer: { claims: [] },
    pferde: { claims: [] },
    scifi: { claims: [] },
  },
});

function migrateFromV1(parsed) {
  const migrated = defaultState();
  for (const v of ['abenteuer', 'pferde', 'scifi']) {
    const old = parsed.variants?.[v];
    if (!old?.claimedMissions?.length) continue;
    migrated.variants[v].claims = (old.claimedMissions || []).map((missionId, i) => ({
      missionId,
      points: 0,
      item: (old.items || [])[i] || '–',
    }));
  }
  return migrated;
}

function loadFromStorage() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultState();
    const parsed = JSON.parse(raw);
    if (parsed.courseId !== COURSE_ID) return defaultState();
    if (parsed.version === 2) return { ...defaultState(), ...parsed };
    return migrateFromV1(parsed);
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

// Shared state across all components
const state = ref(loadFromStorage());

export function useFortschritt() {

  const save = () => saveToStorage(state.value);

  watch(state, (s) => saveToStorage(s), { deep: true });

  const claimMission = (variant, missionId, points, item, missionLabel = null) => {
    const v = state.value.variants[variant];
    if (!v) return false;
    const claims = v.claims || [];
    if (claims.some((c) => c.missionId === missionId)) return false;

    claims.push({ missionId, points, item, missionLabel });
    v.claims = claims;
    state.value = { ...state.value };
    return true;
  };

  const unclaimMission = (variant, missionId) => {
    const v = state.value.variants[variant];
    if (!v?.claims) return false;
    const idx = v.claims.findIndex((c) => c.missionId === missionId);
    if (idx === -1) return false;
    v.claims.splice(idx, 1);
    state.value = { ...state.value };
    return true;
  };

  const isClaimed = (variant, missionId) => {
    return state.value.variants[variant]?.claims?.some((c) => c.missionId === missionId) ?? false;
  };

  const getVariantProgress = (variant) => {
    const v = state.value.variants[variant];
    const claims = v?.claims || [];
    return {
      totalPoints: claims.reduce((sum, c) => sum + (c.points || 0), 0),
      claims: [...claims],
      items: claims.map((c) => c.item).filter(Boolean),
    };
  };

  const getTotalPointsAllVariants = computed(() => {
    const v = state.value.variants;
    return ['abenteuer', 'pferde', 'scifi'].reduce(
      (sum, key) => sum + (getVariantProgress(key).totalPoints || 0),
      0
    );
  });

  const resetProgress = (variant = null) => {
    if (variant) {
      state.value.variants[variant] = { claims: [] };
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
      const imported = data.version === 2 ? data : migrateFromV1(data);
      for (const v of ['abenteuer', 'pferde', 'scifi']) {
        const existing = state.value.variants[v]?.claims || [];
        const incoming = imported.variants?.[v]?.claims || [];
        const existingIds = new Set(existing.map((c) => c.missionId));
        for (const c of incoming) {
          if (!existingIds.has(c.missionId)) {
            existing.push(c);
            existingIds.add(c.missionId);
          }
        }
        state.value.variants[v].claims = existing;
      }
      state.value = { ...state.value };
      return { ok: true };
    } catch (e) {
      return { ok: false, error: e.message };
    }
  };

  return {
    state,
    claimMission,
    unclaimMission,
    isClaimed,
    getVariantProgress,
    getTotalPointsAllVariants,
    resetProgress,
    save,
    exportProgress,
    importProgress,
  };
}
