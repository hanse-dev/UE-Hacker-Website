<template>
  <section class="course-detail" v-if="course">
    <h1>{{ courseTitle }}</h1>
    <div v-if="description || isWeeklyCourse" class="course-description">
      <div v-if="description" v-html="description"></div>
      <div v-if="isWeeklyCourse" class="course-structure">
        <p class="course-structure-intro">{{ t('course.structure.intro') }}</p>
        <div class="course-structure-tabs">
          <div class="course-structure-tab" v-for="tab in courseTabs" :key="tab.key">
            <span class="course-structure-icon">{{ tab.icon }}</span>
            <div class="course-structure-text">
              <strong>{{ tab.label }}</strong>
              <span>{{ tab.description }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <CourseAppointments v-if="!isInteractiveCourse" :termine="courseTermine" />

    <div v-if="isInteractiveCourse" class="interactive-course-wrapper">
      <InteractiveCourse :content-path="course.contentPath" />
    </div>

    <FortschrittWidget v-else-if="isWeeklyCourse && fortschrittReady" />

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
        {{ t('course.download.btn') }}
      </a>
      <p class="notebook-pack-hint">{{ t('course.download.hint') }}</p>
    </div>
  </section>
  <div v-else class="course-loading">
    <p v-if="loading">{{ t('course.loading') }}</p>
    <p v-else class="course-error">{{ t('course.error') }}</p>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch } from 'vue';
import CourseAppointments from '../components/CourseAppointments.vue';
import FortschrittWidget from '../components/FortschrittWidget.vue';
import WeekSection from '../components/WeekSection.vue';
import InteractiveCourse from '../components/InteractiveCourse.vue';
import { loadCourseData } from '../composables/useCourseData';
import { loadWeeklyContent } from '../composables/useWeeklyContent';
import { useLanguage } from '../composables/useLanguage.js';

const TABS_CONFIG = [
  { key: '1_lektion',   icon: '📚', labelKey: 'tab.lesson',    descKey: 'tab.lesson.desc' },
  { key: '2_debug',     icon: '🐛', labelKey: 'tab.debug',     descKey: 'tab.debug.desc' },
  { key: '3_missionen', icon: '⭐', labelKey: 'tab.missions',  descKey: 'tab.missions.desc' },
  { key: '5_boss',      icon: '🐉', labelKey: 'tab.boss',      descKey: 'tab.boss.desc' },
  { key: '6_loesungen', icon: '🔧', labelKey: 'tab.solutions', descKey: 'tab.solutions.desc' },
  { key: '0_glossar',   icon: '📖', labelKey: 'tab.glossary',  descKey: 'tab.glossary.desc' },
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
    const { lang, t } = useLanguage();

    const course = ref(null);
    const description = ref('');
    const weeks = ref([]);
    const courseTermine = ref([]);
    const fortschrittReady = ref(false);
    const loading = ref(true);

    const isWeeklyCourse = computed(() => props.id === 'python-12-wochen-grundkurs');
    const isInteractiveCourse = computed(() => props.id === 'python-grundlagen-interaktiv');

    const courseTabs = computed(() =>
      TABS_CONFIG.map(tab => ({ ...tab, label: t(tab.labelKey), description: t(tab.descKey) }))
    );

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

    const courseTitle = computed(() =>
      lang.value === 'en' && course.value?.title_en
        ? course.value.title_en
        : course.value?.title ?? ''
    );

    const loadContent = async () => {
      if (isWeeklyCourse.value) {
        weeks.value = await loadWeeklyContent(lang.value);
      }
    };

    onMounted(async () => {
      try {
        const data = await loadCourseData(props.id, lang.value);
        course.value = data.course;
        description.value = data.description;
        courseTermine.value = data.courseTermine;
        await loadContent();
      } catch (e) {
        console.error('CourseDetail load error:', e);
      } finally {
        loading.value = false;
        fortschrittReady.value = true;
      }
    });

    watch(lang, async () => {
      if (course.value) {
        const data = await loadCourseData(props.id, lang.value);
        description.value = data.description;
      }
      await loadContent();
    });

    return {
      course,
      courseTitle,
      description,
      weeks,
      courseTermine,
      fortschrittReady,
      loading,
      isWeeklyCourse,
      isInteractiveCourse,
      id: props.id,
      courseTabs,
      t,
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
  margin-top: 8px;
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
