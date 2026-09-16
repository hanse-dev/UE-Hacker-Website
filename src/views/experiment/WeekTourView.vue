<template>
  <section class="week-tour">
    <h1>{{ t('tour.title') }}</h1>

    <p v-if="loading" class="tour-loading">{{ t('tour.loading') }}</p>

    <template v-else>
      <!-- Seite 1: Woche wählen -->
      <div v-if="phase === 'week'" class="tour-page">
        <p class="tour-intro">{{ t('tour.intro') }}</p>
        <h2 class="section-label">{{ t('tour.pickWeek') }}</h2>
        <div class="tile-grid week-tile-grid">
          <button
            v-for="(week, index) in weeks"
            :key="index"
            class="tile week-tile"
            :class="{ active: selectedWeekIndex === index }"
            :data-week="index + 1"
            @click="selectWeek(index)"
          >
            <strong>{{ t('week.label') }} {{ index + 1 }}</strong>
            <span>{{ weekTheme(week) }}</span>
          </button>
        </div>
      </div>

      <!-- Seite 2: Thema wählen -->
      <div v-else-if="phase === 'variant' && selectedWeek" class="tour-page">
        <button class="breadcrumb-back" @click="phase = 'week'">← {{ t('tour.pickWeek') }}</button>
        <h2 class="section-label">{{ t('week.label') }} {{ selectedWeekIndex + 1 }}: {{ weekTheme(selectedWeek) }}</h2>
        <p class="tour-intro">{{ t('tour.pickVariant') }}</p>
        <div class="tile-grid variant-tile-grid">
          <button
            v-for="v in availableVariants"
            :key="v.key"
            class="tile variant-tile"
            :class="{ active: selectedWeek.selectedVariant === v.key }"
            :data-variant="v.key"
            @click="selectVariant(v.key)"
          >
            {{ v.label }}
          </button>
        </div>
      </div>

      <!-- Seite 3+: Kursinhalt (geführte Tour) -->
      <WeekTourStepper
        v-else-if="phase === 'tour' && selectedWeek && selectedWeek.selectedVariant"
        :week="selectedWeek"
        :week-number="selectedWeekIndex + 1"
        :week-theme="weekTheme(selectedWeek)"
        :variant="selectedWeek.selectedVariant"
        :variant-label="selectedVariantLabel"
        :course-id="courseId"
        :initial-step="initialStep"
        :key="selectedWeekIndex"
        @change-week="phase = 'week'"
        @change-variant="phase = 'variant'"
      />
    </template>
  </section>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import WeekTourStepper from '../../components/experiment/WeekTourStepper.vue';
import { loadWeeklyContent } from '../../composables/useWeeklyContent.js';
import { useLanguage } from '../../composables/useLanguage.js';

const COURSE_ID = 'python-12-wochen-grundkurs';

const VARIANT_CONFIG = [
  { key: 'abenteuer', flagKey: 'hasAbenteuerVariant', labelKey: 'variant.adventure' },
  { key: 'pferde',    flagKey: 'hasPferdeVariant',    labelKey: 'variant.horses' },
  { key: 'scifi',     flagKey: 'hasScifiVariant',     labelKey: 'variant.scifi' },
];

export default {
  name: 'WeekTourView',
  components: { WeekTourStepper },
  setup() {
    const { lang, t } = useLanguage();
    const route = useRoute();
    const router = useRouter();

    const weeks = ref([]);
    const loading = ref(true);
    const selectedWeekIndex = ref(null);
    const initialStep = ref(null);
    const phase = ref('week'); // 'week' | 'variant' | 'tour'

    const selectedWeek = computed(() =>
      selectedWeekIndex.value != null ? weeks.value[selectedWeekIndex.value] : null
    );

    const availableVariants = computed(() => {
      if (!selectedWeek.value) return [];
      return VARIANT_CONFIG
        .filter((v) => selectedWeek.value[v.flagKey])
        .map((v) => ({ key: v.key, label: t(v.labelKey) }));
    });

    const selectedVariantLabel = computed(() =>
      availableVariants.value.find((v) => v.key === selectedWeek.value?.selectedVariant)?.label ?? ''
    );

    const weekTheme = (week) => {
      const raw = week.title ?? '';
      if (!raw.includes(':')) return raw;
      return raw.split(':').slice(1).join(':').trim();
    };

    const selectWeek = (index) => {
      selectedWeekIndex.value = index;
      phase.value = 'variant';
    };

    const selectVariant = (variant) => {
      if (!selectedWeek.value) return;
      selectedWeek.value.selectedVariant = variant;
      initialStep.value = null;
      phase.value = 'tour';
      router.replace({ query: { week: selectedWeekIndex.value + 1, variant } });
    };

    const applyDeepLink = () => {
      const weekNum = Number(route.query.week);
      if (!weekNum || weekNum < 1 || weekNum > weeks.value.length) {
        phase.value = 'week';
        return;
      }
      selectedWeekIndex.value = weekNum - 1;
      const variant = String(route.query.variant || '');
      if (variant && weeks.value[weekNum - 1].notebooks[variant]) {
        weeks.value[weekNum - 1].selectedVariant = variant;
        initialStep.value = String(route.query.step || '') || null;
        phase.value = 'tour';
      } else {
        phase.value = 'variant';
      }
    };

    const load = async () => {
      loading.value = true;
      weeks.value = await loadWeeklyContent(lang.value);
      applyDeepLink();
      loading.value = false;
    };

    onMounted(load);
    watch(lang, load);

    return {
      t, weeks, loading, phase, selectedWeekIndex, selectedWeek, availableVariants, initialStep,
      selectedVariantLabel, weekTheme, selectWeek, selectVariant, courseId: COURSE_ID,
    };
  },
};
</script>

<style scoped>
.week-tour {
  padding: 20px;
}

.tour-page {
  animation: tour-page-in 0.18s ease;
}

@keyframes tour-page-in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.tour-intro {
  color: #555;
  margin-bottom: 24px;
}

.tour-loading {
  color: #9ca3af;
  font-style: italic;
}

.section-label {
  font-size: 1.3em;
  color: var(--primary-purple, #4a2274);
  margin: 0 0 10px;
  border-bottom: none;
}

.breadcrumb-back {
  background: transparent;
  border: none;
  color: #7c5a94;
  font-size: 0.9em;
  cursor: pointer;
  padding: 0 0 14px;
}
.breadcrumb-back:hover { color: var(--primary-purple, #4a2274); text-decoration: underline; }

.tile-grid {
  display: grid;
  gap: 14px;
}

.week-tile-grid {
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
}

.variant-tile-grid {
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  max-width: 760px;
}

.tile {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 20px 18px;
  cursor: pointer;
  transition: all 0.15s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.tile:hover {
  border-color: #d9c7ea;
  background: #f7f1fb;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(74, 34, 116, 0.12);
}

.tile.active {
  border-color: var(--primary-purple, #4a2274);
  background: #efe3f6;
}

.week-tile strong {
  font-size: 1.05em;
  color: var(--primary-purple, #4a2274);
}

.week-tile span {
  font-size: 0.85em;
  color: #6b7280;
}

.variant-tile {
  align-items: center;
  text-align: center;
  font-size: 1.15em;
  font-weight: 600;
  color: #374151;
  padding: 26px 18px;
}
</style>
