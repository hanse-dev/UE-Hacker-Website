<template>
  <section class="course-detail" v-if="course">
    <h1>{{ course.title }}</h1>
    <div v-if="description" v-html="description" class="course-description"></div>

    <CourseAppointments v-if="!isInteractiveCourse" :termine="courseTermine" />

    <div v-if="isInteractiveCourse" class="interactive-course-wrapper">
      <InteractiveCourse :content-path="course.contentPath" />
    </div>

    <FortschrittWidget v-else-if="isWeeklyCourse && fortschrittReady" />

    <div v-if="isWeeklyCourse" class="course-structure">
      <h2>Wie ist der Kurs aufgebaut?</h2>
      <p class="course-structure-intro">Jede Woche ist in 6 Bereiche aufgeteilt – arbeite sie am besten in dieser Reihenfolge durch:</p>
      <div class="course-structure-tabs">
        <div class="course-structure-tab" v-for="tab in COURSE_TABS" :key="tab.key">
          <span class="course-structure-icon">{{ tab.icon }}</span>
          <div class="course-structure-text">
            <strong>{{ tab.label }}</strong>
            <span>{{ tab.description }}</span>
          </div>
        </div>
      </div>
    </div>

    <WeekSection
      v-if="isWeeklyCourse"
      v-for="(week, index) in weeks"
      :key="index"
      :week="week"
      :index="index"
      :course-id="id"
      @toggle="toggleWeek(index)"
      @toggle-cheat-sheet="(csIndex) => toggleCheatSheet(week, csIndex)"
      @set-variant="(variant) => setVariant(week, variant)"
    />

    <div v-if="isWeeklyCourse" class="notebook-pack-download">
      <a href="/python-12-wochen-notebooks.zip" download class="notebook-pack-btn">
        📦 Alle Notebooks als Pack herunterladen
      </a>
      <p class="notebook-pack-hint">Zip mit allen 12 Wochen (Abenteuer, Pferde, Sci-Fi) + Cheat Sheets + Fortschritt-Skript – zum Arbeiten in Jupyter oder VS Code.</p>
    </div>
  </section>
  <div v-else class="course-loading">
    <p v-if="loading">Kurs wird geladen...</p>
    <p v-else class="course-error">
      Kurs konnte nicht geladen werden. Prüfe die Browser-Konsole (F12) für Details.
    </p>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import CourseAppointments from '../components/CourseAppointments.vue';
import FortschrittWidget from '../components/FortschrittWidget.vue';
import WeekSection from '../components/WeekSection.vue';
import InteractiveCourse from '../components/InteractiveCourse.vue';
import { loadCourseData } from '../composables/useCourseData';
import { loadWeeklyContent } from '../composables/useWeeklyContent';

const COURSE_TABS = [
  { key: '1_lektion',   label: 'Lektion',    icon: '📚', description: 'Neuer Stoff: lies und verstehe das Thema der Woche' },
  { key: '2_debug',     label: 'Debug',      icon: '🐛', description: 'Finde und fixe absichtliche Bugs im Code' },
  { key: '3_missionen', label: 'Missionen',  icon: '⭐', description: 'Kleine Aufgaben zum Üben des neuen Stoffs' },
  { key: '5_boss',      label: 'Boss-Quest', icon: '🐉', description: 'Die große Abschluss-Challenge – alles zusammen!' },
  { key: '6_loesungen', label: 'Lösungen',   icon: '🔧', description: 'Musterlösungen zu Missionen und Boss-Quest' },
  { key: '0_glossar',   label: 'Glossar',    icon: '📖', description: 'Alle Begriffe der Woche zum Nachschlagen – immer verfügbar' },
];

export default {
  name: 'CourseDetail',
  components: {
    CourseAppointments,
    FortschrittWidget,
    WeekSection,
    InteractiveCourse,
  },
  props: {
    id: { type: String, required: true },
  },
  setup(props) {
    const course = ref(null);
    const description = ref('');
    const weeks = ref([]);
    const courseTermine = ref([]);
    const fortschrittReady = ref(false);
    const loading = ref(true);

    const isWeeklyCourse = computed(() => props.id === 'python-12-wochen-grundkurs');
    const isInteractiveCourse = computed(() => props.id === 'python-grundlagen-interaktiv');

    const setVariant = (week, variant) => {
      week.selectedVariant = variant;
    };

    const toggleWeek = (index) => {
      weeks.value[index].expanded = !weeks.value[index].expanded;
    };

    const toggleCheatSheet = (week, csIndex) => {
      if (!week.expandedCheatSheets) week.expandedCheatSheets = {};
      week.expandedCheatSheets[csIndex] = !week.expandedCheatSheets[csIndex];
    };

    onMounted(async () => {
      try {
        const data = await loadCourseData(props.id);
        course.value = data.course;
        description.value = data.description;
        courseTermine.value = data.courseTermine;

        if (isWeeklyCourse.value) {
          weeks.value = await loadWeeklyContent();
        }
      } catch (e) {
        console.error('CourseDetail load error:', e);
      } finally {
        loading.value = false;
        fortschrittReady.value = true;
      }
    });

    return {
      course,
      description,
      weeks,
      courseTermine,
      fortschrittReady,
      loading,
      isWeeklyCourse,
      isInteractiveCourse,
      id: props.id,
      COURSE_TABS,
      setVariant,
      toggleWeek,
      toggleCheatSheet,
    };
  },
};
</script>

<style scoped>
.course-detail {
  padding: 20px;
}

.interactive-course-wrapper {
  margin-top: 20px;
  overflow: visible;
}

.course-description {
  margin-bottom: 40px;
  font-size: 1.1em;
}

.notebook-pack-download {
  background: linear-gradient(135deg, #e8f4f8 0%, #d4ebf2 100%);
  border: 2px solid #0ea5e9;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 40px;
}

.notebook-pack-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #0ea5e9;
  color: white;
  padding: 14px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05em;
  transition: all 0.2s;
}

.notebook-pack-btn:hover {
  background: #0284c7;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4);
}

.course-loading {
  padding: 20px;
}

.course-error {
  color: #b91c1c;
}

.notebook-pack-hint {
  margin: 12px 0 0 0;
  font-size: 0.9em;
  color: #555;
}

/* ── Course structure guide ────────────────────────────────────────────── */
.course-structure {
  margin: 0 0 40px;
}

.course-structure h2 {
  font-size: 1.4em;
  color: #333;
  margin-bottom: 8px;
}

.course-structure-intro {
  color: #555;
  margin-bottom: 16px;
  font-size: 0.95em;
}

.course-structure-tabs {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 10px;
}

.course-structure-tab {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 12px 14px;
}

.course-structure-icon {
  font-size: 1.5em;
  flex-shrink: 0;
  line-height: 1.2;
}

.course-structure-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.course-structure-text strong {
  font-size: 0.95em;
  color: #222;
}

.course-structure-text span {
  font-size: 0.82em;
  color: #666;
  line-height: 1.4;
}
</style>
