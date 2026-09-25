<template>
  <div class="js-grundkurs-tour">
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
      :course-id="`js-grundkurs-woche${selectedWeekNumber}`"
      :content-path="`js-grundkurs-woche${selectedWeekNumber}`"
      :week-label="`${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`"
      :show-canvas="selectedWeekSandboxVisible"
      :dom-mode="selectedWeekSandboxVisible"
      @change-week="phase = 'week'"
    />
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import JsCourseTour from './JsCourseTour.vue';
import { useLanguage } from '../composables/useLanguage';

// Statische Titel-Liste statt eines Markdown-Frontmatter-Parsers wie beim Python-Kurs
// (useWeeklyContent.js) - lohnt sich dort nur wegen Themen-Varianten + Cheat-Sheets/Downloads,
// die es hier bewusst nicht gibt. Titel 1:1 aus KURSPLAN.md "JavaScript-Track: Grundkurs".
// `sandboxVisible`: nur Wochen, deren Aufgaben das feste DOM-Uebungs-Markup (#dom-uebung in
// useJsSandbox.js) brauchen, zeigen das Sandbox-iframe ueberhaupt an - alle anderen Wochen
// kommen ganz ohne sichtbaren Sandbox-Bereich aus (die Ausgabe-Box unter dem Editor reicht).
const WEEK_DEFS = [
  { number: 1, title: 'JS-Grundlagen' },
  { number: 2, title: 'Bedingungen' },
  { number: 3, title: 'Schleifen' },
  { number: 4, title: 'Funktionen' },
  { number: 5, title: 'Arrays' },
  { number: 6, title: 'Objekte' },
  { number: 7, title: 'DOM & Interaktivität', sandboxVisible: true },
  { number: 8, title: 'Objekte als Blaupause' },
  { number: 9, title: 'Abschlussprojekt', sandboxVisible: true },
];

// Gleiches Glob-Pattern wie in JsCourseTour.vue - hier nur zum Pruefen, welche Wochen ueberhaupt
// einen Content-Ordner haben (Verfuegbarkeit), nicht zum Laden der Lektionen selbst.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

export default {
  name: 'JsGrundkursTour',
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
        available: `../../content/js-grundkurs-woche${w.number}/lessons.json` in lessonJsonModules,
      }))
    );

    const selectedWeekTitle = computed(
      () => WEEK_DEFS.find((w) => w.number === selectedWeekNumber.value)?.title || ''
    );

    const selectedWeekSandboxVisible = computed(
      () => !!WEEK_DEFS.find((w) => w.number === selectedWeekNumber.value)?.sandboxVisible
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

    return { t, phase, weeks, selectedWeekNumber, selectedWeekTitle, selectedWeekSandboxVisible, selectWeek };
  },
};
</script>

<style scoped>
.js-grundkurs-tour {
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
