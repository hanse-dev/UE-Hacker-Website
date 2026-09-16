<template>
  <section class="week-tour">
    <h1>{{ t('tour.title') }}</h1>
    <p class="tour-intro">{{ t('tour.intro') }}</p>

    <p v-if="loading" class="tour-loading">{{ t('tour.loading') }}</p>

    <template v-else>
      <div class="week-rail">
        <h2 class="section-label">{{ t('tour.pickWeek') }}</h2>
        <div class="week-rail-list">
          <button
            v-for="(week, index) in weeks"
            :key="index"
            class="week-chip"
            :class="{ active: selectedWeekIndex === index }"
            :data-week="index + 1"
            @click="selectWeek(index)"
          >
            <strong>{{ t('week.label') }} {{ index + 1 }}</strong>
            <span>{{ weekTheme(week) }}</span>
          </button>
        </div>
      </div>

      <div v-if="selectedWeek" class="variant-area">
        <h2 class="section-label">{{ t('tour.pickVariant') }}</h2>
        <VariantSelector :week="selectedWeek" @set-variant="setVariant" />
      </div>

      <WeekTourStepper
        v-if="selectedWeek && selectedWeek.selectedVariant"
        :week="selectedWeek"
        :week-number="selectedWeekIndex + 1"
        :variant="selectedWeek.selectedVariant"
        :course-id="courseId"
        :initial-step="initialStep"
        :key="selectedWeekIndex"
      />
    </template>
  </section>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import VariantSelector from '../../components/VariantSelector.vue';
import WeekTourStepper from '../../components/experiment/WeekTourStepper.vue';
import { loadWeeklyContent } from '../../composables/useWeeklyContent.js';
import { useLanguage } from '../../composables/useLanguage.js';

const COURSE_ID = 'python-12-wochen-grundkurs';

export default {
  name: 'WeekTourView',
  components: { VariantSelector, WeekTourStepper },
  setup() {
    const { lang, t } = useLanguage();
    const route = useRoute();
    const router = useRouter();

    const weeks = ref([]);
    const loading = ref(true);
    const selectedWeekIndex = ref(null);
    const initialStep = ref(null);

    const selectedWeek = computed(() =>
      selectedWeekIndex.value != null ? weeks.value[selectedWeekIndex.value] : null
    );

    const weekTheme = (week) => {
      const raw = week.title ?? '';
      if (!raw.includes(':')) return raw;
      return raw.split(':').slice(1).join(':').trim();
    };

    const selectWeek = (index) => {
      selectedWeekIndex.value = index;
      initialStep.value = null;
      router.replace({ query: { ...route.query, week: index + 1, variant: weeks.value[index]?.selectedVariant, step: undefined } });
    };

    const setVariant = (variant) => {
      if (!selectedWeek.value) return;
      selectedWeek.value.selectedVariant = variant;
      router.replace({ query: { ...route.query, week: selectedWeekIndex.value + 1, variant, step: undefined } });
    };

    const applyDeepLink = () => {
      const weekNum = Number(route.query.week);
      if (weekNum && weekNum >= 1 && weekNum <= weeks.value.length) {
        selectedWeekIndex.value = weekNum - 1;
        const variant = String(route.query.variant || '');
        if (variant && weeks.value[weekNum - 1].notebooks[variant]) {
          weeks.value[weekNum - 1].selectedVariant = variant;
        }
        const step = String(route.query.step || '');
        initialStep.value = step || null;
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
      t, weeks, loading, selectedWeekIndex, selectedWeek, initialStep,
      weekTheme, selectWeek, setVariant, courseId: COURSE_ID,
    };
  },
};
</script>

<style scoped>
.week-tour {
  padding: 20px;
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
  font-size: 1em;
  color: var(--primary-purple, #4a2274);
  margin: 0 0 10px;
  border-bottom: none;
}

.week-rail {
  margin-bottom: 24px;
}

.week-rail-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 8px;
}

.week-chip {
  display: flex;
  flex-direction: column;
  gap: 2px;
  text-align: left;
  background: #f8f9fa;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  padding: 10px 12px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.week-chip:hover {
  border-color: #d9c7ea;
  background: #f7f1fb;
}

.week-chip.active {
  border-color: var(--primary-purple, #4a2274);
  background: #efe3f6;
}

.week-chip strong {
  font-size: 0.88em;
  color: var(--primary-purple, #4a2274);
}

.week-chip span {
  font-size: 0.78em;
  color: #6b7280;
}

.variant-area {
  margin-bottom: 8px;
}
</style>
