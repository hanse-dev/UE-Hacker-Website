<template>
  <div v-if="missionIds.length > 0" class="missionen-panel">
    <div class="missionen-panel-header" @click="expanded = !expanded">
      <span class="missionen-title">{{ t('mission.panel.title') }}</span>
      <span class="missionen-toggle">{{ expanded ? '−' : '+' }}</span>
    </div>
    <div v-show="expanded" class="missionen-panel-content">
      <p class="missionen-panel-hint">{{ t('mission.panel.hint') }}</p>
      <p v-if="hasCheck && !checkPassed" class="checkpoint-mission-hint">
        {{ t('mission.check.hint') }}
      </p>
      <p v-else-if="hasCheck && checkPassed" class="checkpoint-mission-done">
        {{ t('mission.check.done') }}
      </p>
      <div class="missionen-list">
        <div
          v-for="m in missionen"
          :key="m.id"
          class="mission-item"
          :class="{ claimed: isDone(m.id) }"
        >
          <span class="mission-label">{{ m.label }}</span>
          <div class="mission-actions">
            <button v-if="!isDone(m.id)" @click.stop="markDone(variant, m.id)" class="btn-claim">
              {{ t('mission.done.mark') }}
            </button>
            <template v-else>
              <span class="mission-claimed">✅</span>
              <button @click.stop="markUndone(variant, m.id)" class="btn-unclaim" :title="t('mission.done.unmark')">↩</button>
            </template>
          </div>
        </div>
      </div>
      <p v-if="certificateEarned" class="certificate-earned">
        {{ t('mission.certificate.earned') }}
      </p>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useFortschritt } from '../composables/useFortschritt';
import { useZertifikate } from '../composables/useZertifikate';
import { useLanguage } from '../composables/useLanguage.js';
import { loadWeekChecks, hasWeekCheck, useWeekChecks } from '../composables/useWeekChecks.js';

export default {
  name: 'MissionenPanel',
  props: {
    weekNumber: { type: Number, required: true },
    variant:    { type: String, default: null },
    courseId:   { type: String, default: null },
  },
  setup(props) {
    const { t, lang } = useLanguage();
    const expanded = ref(false);
    const checksData = ref(null);
    const { markDone: doMarkDone, markUndone: doMarkUndone, isDone: checkDone } = useFortschritt();
    const { isWeekCheckPassed } = useWeekChecks();
    const { ensureManifestLoaded, getWeekMissionsAndBosses, getWeekMissionIds, isCertificateEarned } = useZertifikate();

    const missionIds = computed(() => {
      if (!props.variant || props.courseId !== 'python-12-wochen-grundkurs') return [];
      return getWeekMissionIds(lang.value, props.variant, props.weekNumber);
    });

    const missionen = computed(() => {
      if (!props.variant || props.courseId !== 'python-12-wochen-grundkurs') return [];
      const { missions, bossQuests } = getWeekMissionsAndBosses(lang.value, props.variant, props.weekNumber);
      const missionItems = missions.map((id, i) => ({ id, label: `${t('mission.label')} ${i + 1}` }));
      const bossItems = bossQuests.map((id, i) => ({ id, label: `${t('mission.boss.label')} ${i + 1}` }));
      return [...missionItems, ...bossItems];
    });

    const isDone = (id) => checkDone(props.variant, id);
    const markDone = (variant, id) => doMarkDone(variant, id);
    const markUndone = (variant, id) => doMarkUndone(variant, id);

    const hasCheck = computed(() => hasWeekCheck(checksData.value, props.weekNumber));
    const checkPassed = computed(() => isWeekCheckPassed(props.weekNumber));

    const certificateEarned = computed(() => isCertificateEarned(props.weekNumber));

    onMounted(async () => {
      ensureManifestLoaded(lang.value);
      try {
        checksData.value = await loadWeekChecks();
      } catch (e) { /* silent */ }
    });
    watch(lang, () => ensureManifestLoaded(lang.value));

    return {
      expanded, missionIds, missionen, isDone, markDone, markUndone, t, variant: props.variant,
      hasCheck, checkPassed, certificateEarned,
    };
  },
};
</script>

<style scoped>
.missionen-panel {
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 8px;
  margin-bottom: 12px;
  overflow: hidden;
}

.missionen-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  cursor: pointer;
  user-select: none;
  transition: background 0.15s;
}

.missionen-panel-header:hover { background: #fef3c7; }

.missionen-title { font-weight: 600; font-size: 0.9em; color: #92400e; }
.missionen-toggle { font-size: 1.1em; color: #92400e; font-weight: bold; }

.missionen-panel-content { padding: 6px 16px 12px; border-top: 1px solid #fde68a; }

.missionen-panel-hint {
  margin: 8px 0;
  font-size: 0.8em;
  color: #92400e;
  font-style: italic;
}

.checkpoint-mission-hint {
  margin: 8px 0 10px 0;
  padding: 10px 12px;
  background: #e0f2fe;
  border: 1px solid #7dd3fc;
  border-radius: 6px;
  font-size: 0.85em;
  color: #0c4a6e;
  line-height: 1.4;
}

.checkpoint-mission-done {
  margin: 8px 0 10px 0;
  padding: 10px 12px;
  background: #d4edda;
  border: 1px solid #c3e6cb;
  border-radius: 6px;
  font-size: 0.85em;
  color: #155724;
  line-height: 1.4;
}

.missionen-list { display: flex; flex-direction: column; gap: 6px; margin-top: 6px; }

.mission-item {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 7px 10px;
  background: white;
  border-radius: 6px;
  border: 1px solid #f3f4f6;
  font-size: 0.85em;
}

.mission-item.claimed { background: #f0fdf4; border-color: #bbf7d0; }

.mission-label { font-weight: 600; color: #374151; min-width: 80px; }
.mission-actions { display: flex; align-items: center; gap: 6px; margin-left: auto; }

.btn-claim {
  background: #fbbf24; color: #1f2937; border: none;
  padding: 4px 12px; border-radius: 5px; font-size: 0.85em;
  font-weight: 600; cursor: pointer; transition: background 0.15s;
}
.btn-claim:hover { background: #f59e0b; }

.btn-unclaim {
  background: transparent; color: #9ca3af; border: 1px solid #d1d5db;
  padding: 3px 8px; border-radius: 4px; font-size: 0.8em; cursor: pointer;
}
.btn-unclaim:hover { background: #fee2e2; color: #dc2626; border-color: #fca5a5; }

.mission-claimed { color: #16a34a; font-size: 1em; }

.certificate-earned {
  margin: 12px 0 0 0;
  padding: 10px 14px;
  background: #ede9fe;
  border: 1px solid #c4b5fd;
  border-radius: 8px;
  font-weight: 600;
  color: #5b21b6;
  text-align: center;
}
</style>
