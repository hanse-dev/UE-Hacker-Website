<template>
  <div class="tour-stepper">
    <div class="tour-tabs">
      <button
        v-for="(step, i) in steps"
        :key="step.key"
        class="tour-tab"
        :class="{ active: !activeReference && viewingStepKey === step.key, reached: i <= furthestStepIndex }"
        :data-step-key="step.key"
        @click="viewStep(step.key)"
      >
        <span class="tour-tab-icon">{{ step.icon }}</span>
        <span class="tour-tab-label">{{ step.label }}</span>
      </button>
    </div>

    <div class="tour-body">
      <div class="tour-content">
        <div v-if="activeReference" class="tour-reference-banner">
          <span>{{ referenceLabel }}</span>
          <button class="tour-back-btn" @click="activeReference = null">{{ t('tour.backToTour') }}</button>
        </div>

        <WeekCheckPanel
          v-if="!activeReference && viewingStepKey === '4_check'"
          :week-number="weekNumber"
        />
        <JupyterNotebook
          v-else-if="activeContentUrl"
          :notebook-path="activeContentUrl"
          :notebook-url="activeContentDownloadUrl"
          :download-name="activeContentDownloadName"
          :week-number="weekNumber"
          :variant="variant"
          :course-id="courseId"
          :key="`${weekNumber}-${variant}-${activeContentKey}`"
        />

        <div v-if="!activeReference" class="tour-next-area">
          <button v-if="nextStep" class="tour-next-btn" @click="goNext">
            {{ t('tour.next').replace('{step}', nextStep.label) }} →
          </button>
          <p v-else class="tour-done-msg">{{ t('tour.done') }}</p>
        </div>
      </div>

      <WeekTourSideMenu
        :steps="steps"
        :current-step-key="viewingStepKey"
        :furthest-index="furthestStepIndex"
        :headings="headings"
        :reference-items="referenceItems"
        :active-reference="activeReference"
        @select-step="viewStep"
        @select-heading="scrollToCell"
        @select-reference="viewReference"
      />
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import JupyterNotebook from '../JupyterNotebook.vue';
import WeekCheckPanel from '../WeekCheckPanel.vue';
import WeekTourSideMenu from './WeekTourSideMenu.vue';
import { useLanguage } from '../../composables/useLanguage.js';
import { useNotebookHeadings } from '../../composables/experiment/useNotebookHeadings.js';
import { loadWeekChecks, hasWeekCheck } from '../../composables/useWeekChecks.js';

const TOUR_STEPS_CONFIG = [
  { key: '1_lektion',   icon: '📚', labelKey: 'tab.lesson' },
  { key: '2_debug',     icon: '🐛', labelKey: 'tab.debug' },
  { key: '3_missionen', icon: '⭐', labelKey: 'tab.missions' },
  { key: '5_boss',      icon: '🐉', labelKey: 'tab.boss' },
  { key: '4_check',     icon: '✅', labelKey: 'tab.check' },
];

const REFERENCE_CONFIG = [
  { key: '0_glossar',   icon: '📖', labelKey: 'tab.glossary' },
  { key: '6_loesungen', icon: '🔧', labelKey: 'tab.solutions' },
];

export default {
  name: 'WeekTourStepper',
  components: { JupyterNotebook, WeekCheckPanel, WeekTourSideMenu },
  props: {
    week: { type: Object, required: true },
    weekNumber: { type: Number, required: true },
    variant: { type: String, required: true },
    courseId: { type: String, required: true },
    initialStep: { type: String, default: null },
  },
  setup(props) {
    const { t } = useLanguage();
    const checksData = ref(null);
    const hasCheck = computed(() => hasWeekCheck(checksData.value, props.weekNumber));

    const notebooksForVariant = computed(() => props.week.notebooks?.[props.variant] ?? {});

    const steps = computed(() =>
      TOUR_STEPS_CONFIG
        .filter((step) => step.key === '4_check' ? hasCheck.value : !!notebooksForVariant.value[step.key]?.renderUrl)
        .map((step) => ({ ...step, label: t(step.labelKey) }))
    );

    const referenceItems = computed(() =>
      REFERENCE_CONFIG
        .filter((ref_) => !!notebooksForVariant.value[ref_.key]?.renderUrl)
        .map((ref_) => ({ ...ref_, label: t(ref_.labelKey) }))
    );

    const viewingStepKey = ref(null);
    const furthestStepIndex = ref(0);
    const activeReference = ref(null);
    let usedInitialStep = false;

    const resetForWeekVariant = () => {
      activeReference.value = null;
      const initialIdx = !usedInitialStep && props.initialStep
        ? steps.value.findIndex((s) => s.key === props.initialStep)
        : -1;
      usedInitialStep = true;
      if (initialIdx >= 0) {
        viewingStepKey.value = props.initialStep;
        furthestStepIndex.value = initialIdx;
      } else {
        furthestStepIndex.value = 0;
        viewingStepKey.value = steps.value[0]?.key ?? null;
      }
    };

    const load = async () => {
      try { checksData.value = await loadWeekChecks(); } catch { checksData.value = null; }
    };

    watch(() => [props.weekNumber, props.variant], resetForWeekVariant);
    watch(steps, () => {
      if (!viewingStepKey.value && steps.value.length) viewingStepKey.value = steps.value[0].key;
    });

    load().then(resetForWeekVariant);

    const viewStep = (key) => {
      activeReference.value = null;
      viewingStepKey.value = key;
      const idx = steps.value.findIndex((s) => s.key === key);
      if (idx > furthestStepIndex.value) furthestStepIndex.value = idx;
    };

    const viewReference = (key) => {
      activeReference.value = activeReference.value === key ? null : key;
    };

    const currentStepIndex = computed(() => steps.value.findIndex((s) => s.key === viewingStepKey.value));
    const nextStep = computed(() => steps.value[currentStepIndex.value + 1] ?? null);

    const goNext = () => {
      if (nextStep.value) viewStep(nextStep.value.key);
    };

    const activeContentKey = computed(() => activeReference.value ?? viewingStepKey.value);
    const activeContentUrl = computed(() => {
      if (activeContentKey.value === '4_check') return null;
      return notebooksForVariant.value[activeContentKey.value]?.renderUrl ?? null;
    });
    const activeContentDownloadUrl = computed(() => notebooksForVariant.value[activeContentKey.value]?.downloadUrl ?? null);
    const activeContentDownloadName = computed(() => notebooksForVariant.value[activeContentKey.value]?.downloadName ?? null);

    const { headings } = useNotebookHeadings(activeContentUrl);

    const scrollToCell = (cellIndex) => {
      const el = document.getElementById(`cell-${cellIndex}`);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const referenceLabel = computed(() => {
      const item = referenceItems.value.find((r) => r.key === activeReference.value);
      return item ? `${item.icon} ${item.label}` : '';
    });

    return {
      t, steps, referenceItems, viewingStepKey, furthestStepIndex, activeReference,
      viewStep, viewReference, nextStep, goNext,
      activeContentKey, activeContentUrl, activeContentDownloadUrl, activeContentDownloadName,
      headings, scrollToCell, referenceLabel,
    };
  },
};
</script>

<style scoped>
.tour-stepper {
  margin-top: 16px;
}

.tour-tabs {
  display: flex;
  gap: 0;
  border-bottom: 2px solid #dee2e6;
  overflow-x: auto;
  scrollbar-width: none;
}
.tour-tabs::-webkit-scrollbar { display: none; }

.tour-tab {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 10px 16px;
  border: none;
  border-bottom: 3px solid transparent;
  background: transparent;
  cursor: pointer;
  font-size: 0.88em;
  font-weight: 500;
  color: #666;
  white-space: nowrap;
  transition: all 0.18s ease;
  margin-bottom: -2px;
}

.tour-tab:hover { color: #333; background: #f8f9fa; }
.tour-tab.reached { color: var(--primary-purple, #4a2274); }
.tour-tab.active {
  color: var(--accent-orange, #ff9800);
  border-bottom-color: var(--accent-orange, #ff9800);
  font-weight: 700;
  background: #fff8ec;
}

.tour-body {
  display: flex;
  gap: 24px;
  margin-top: 16px;
  align-items: flex-start;
}

.tour-content {
  flex: 1;
  min-width: 0;
}

.tour-reference-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  background: #f3eef8;
  border: 1px solid #c4a8e0;
  border-radius: 8px 8px 0 0;
  padding: 10px 16px;
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.tour-back-btn {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 600;
}
.tour-back-btn:hover { background: #3d1b5c; }

.tour-next-area {
  padding: 18px 4px 4px;
}

.tour-next-btn {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 12px 22px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  font-weight: 700;
}
.tour-next-btn:hover { background: #fb8c00; }

.tour-done-msg {
  background: #fff3cd;
  border: 1px solid #ffe69c;
  border-radius: 8px;
  padding: 14px 18px;
  font-weight: 600;
  color: #664d03;
}

@media (max-width: 900px) {
  .tour-body { flex-direction: column; }
}
</style>
