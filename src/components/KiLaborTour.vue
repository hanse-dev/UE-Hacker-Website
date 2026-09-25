<template>
  <div class="ki-labor-tour">
    <template v-if="phase === 'week'">
      <p class="choose-week-title">{{ t('weekPicker.chooseWeekTitle') }}</p>
      <div class="week-grid">
        <button
          v-for="week in weeks"
          :key="week.number"
          class="week-tile"
          :class="{ locked: !week.available }"
          :disabled="!week.available"
          @click="selectWeek(week.number)"
        >
          <span class="week-tile-number">{{ t('week.label') }} {{ week.number }}</span>
          <span class="week-tile-title">{{ week.title }}</span>
          <span v-if="!week.available" class="week-tile-badge">{{ t('weekPicker.comingSoon') }}</span>
        </button>
      </div>
    </template>

    <JsCourseTour
      v-else
      engine="pyodide"
      :course-id="`ki-labor-woche${selectedWeekNumber}`"
      :content-path="`ki-labor-woche${selectedWeekNumber}`"
      :week-label="`${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`"
      @change-week="phase = 'week'"
    />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import JsCourseTour from './JsCourseTour.vue';
import { useLanguage } from '../composables/useLanguage';

// Gleiches Muster wie JsGrundkursTour.vue: statische Titel-Liste statt Markdown-Frontmatter-Parser
// (lohnt sich nur bei Themen-Varianten/Cheat-Sheets, die es hier bewusst nicht gibt), Titel 1:1
// aus KURSPLAN.md "KI-Track: KI-Grundlagen". engine="pyodide" statt js-sandbox - gleiche Tour
// (JsCourseTour.vue), andere Ausfuehrung (LessonView.vue statt JsLessonView.vue).
const WEEK_DEFS = [
  { number: 1, title: 'Was ist KI?' },
  { number: 2, title: 'Daten sind alles' },
  { number: 3, title: 'Nächste Nachbarn (k-NN)' },
  { number: 4, title: 'Training & Test' },
  { number: 5, title: 'Entscheidungsbäume' },
  { number: 6, title: 'Neuronale Netze I' },
  { number: 7, title: 'Neuronale Netze II' },
  { number: 8, title: 'Grenzen & Ethik' },
];

// Gleiches Glob-Pattern wie in JsCourseTour.vue - hier nur zum Pruefen, welche Wochen ueberhaupt
// einen Content-Ordner haben (Verfuegbarkeit), nicht zum Laden der Lektionen selbst.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

export default {
  name: 'KiLaborTour',
  components: { JsCourseTour },
  setup() {
    const { t } = useLanguage();
    const route = useRoute();
    const router = useRouter();
    const phase = ref('week');
    const selectedWeekNumber = ref(null);

    const weeks = computed(() =>
      WEEK_DEFS.map((w) => ({
        ...w,
        available: `../../content/ki-labor-woche${w.number}/lessons.json` in lessonJsonModules,
      }))
    );

    const selectedWeekTitle = computed(
      () => WEEK_DEFS.find((w) => w.number === selectedWeekNumber.value)?.title || ''
    );

    const selectWeek = (number) => {
      const week = weeks.value.find((w) => w.number === number);
      if (!week?.available) return;
      selectedWeekNumber.value = number;
      phase.value = 'tour';
      router.replace({ query: { week: number } });
    };

    onMounted(() => {
      const weekNum = Number(route.query.week);
      if (weekNum && weeks.value.some((w) => w.number === weekNum && w.available)) {
        selectedWeekNumber.value = weekNum;
        phase.value = 'tour';
      }
    });

    return { t, phase, weeks, selectedWeekNumber, selectedWeekTitle, selectWeek };
  },
};
</script>

<style scoped>
.ki-labor-tour {
  max-width: 1200px;
  margin: 0 auto;
}

.choose-week-title {
  text-align: center;
  margin-bottom: 24px;
  color: #555;
}

.week-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px;
  max-width: 900px;
  margin: 0 auto;
}

.week-tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 16px 10px;
  background: white;
  border: 2px solid var(--primary-purple, #4a2274);
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
}

.week-tile:hover:not(:disabled) {
  background: #f7f1fb;
}

.week-tile.locked {
  border-color: #dee2e6;
  cursor: not-allowed;
  opacity: 0.7;
}

.week-tile-number {
  font-size: 0.8em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: var(--accent-orange, #ff9800);
}

.week-tile.locked .week-tile-number {
  color: #adb5bd;
}

.week-tile-title {
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.week-tile.locked .week-tile-title {
  color: #868e96;
}

.week-tile-badge {
  font-size: 0.75em;
  color: #868e96;
}
</style>
