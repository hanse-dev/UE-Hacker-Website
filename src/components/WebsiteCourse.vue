<template>
  <div class="website-course">
    <div v-if="!stufe" class="stufe-selector">
      <h2>{{ t('website.chooseTitle') }}</h2>
      <p class="stufe-intro">{{ t('website.chooseIntro') }}</p>
      <div class="stufe-cards">
        <button class="stufe-card" data-stufe="einfach" @click="choose('einfach')">
          <span class="stufe-icon">🌱</span>
          <strong>{{ t('website.easy.title') }}</strong>
          <span class="stufe-age">{{ t('website.easy.age') }}</span>
          <ul class="stufe-features">
            <li>{{ t('website.easy.f1') }}</li>
            <li>{{ t('website.easy.f2') }}</li>
            <li>{{ t('website.easy.f3') }}</li>
          </ul>
        </button>
        <button class="stufe-card" data-stufe="intensiv" @click="choose('intensiv')">
          <span class="stufe-icon">🚀</span>
          <strong>{{ t('website.intense.title') }}</strong>
          <span class="stufe-age">{{ t('website.intense.age') }}</span>
          <ul class="stufe-features">
            <li>{{ t('website.intense.f1') }}</li>
            <li>{{ t('website.intense.f2') }}</li>
            <li>{{ t('website.intense.f3') }}</li>
          </ul>
        </button>
      </div>
    </div>

    <template v-else>
      <div class="stufe-bar">
        <span class="stufe-current">{{ t('website.current') }} <strong>{{ t(stufe === 'einfach' ? 'website.easy.title' : 'website.intense.title') }}</strong></span>
        <button class="btn-change-stufe" @click="reset">{{ t('website.change') }}</button>
      </div>
      <ProjectCourse
        v-if="stufe === 'einfach'"
        :course-id="course.id"
        :content-path="course.contentPath"
        engine="js-sandbox"
        :web-mode="true"
        :language="course.language"
        :is-project="false"
        :final-check="course.contentPath"
        :final-check-title="{ de: course.title, en: course.title_en }"
      />
      <WeeklyCourseTour
        v-else
        :weeks="WEB_GRUNDKURS_WEEKS"
        week-prefix="web-grundkurs-woche"
        course-key="web-grundkurs"
        :course-title="WEB_GRUNDKURS_COURSE_TITLE"
        engine="js-sandbox"
        :web-mode="true"
        concept-language="html"
        concept-course="web-grundkurs"
      />
    </template>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ProjectCourse from './ProjectCourse.vue';
import WeeklyCourseTour from './WeeklyCourseTour.vue';
import { useLanguage } from '../composables/useLanguage';
import { WEB_GRUNDKURS_WEEKS, WEB_GRUNDKURS_COURSE_TITLE } from '../data/webGrundkursWeeks.js';

const STUFE_KEY = 'ue-hacker-website-stufe';
const STUFEN = ['einfach', 'intensiv'];

function readStoredStufe() {
  try {
    const value = localStorage.getItem(STUFE_KEY);
    return STUFEN.includes(value) ? value : null;
  } catch {
    return null;
  }
}

/**
 * „Meine erste Website“ in zwei Stufen: Einfach = 8 Lektionen + Abschluss-Check (ProjectCourse.vue,
 * Inhalt content/web-erste-website/), Intensiv = 9 Wochen mit Wochen-Checks (WeeklyCourseTour.vue,
 * content/web-grundkurs-woche{N}/ + content/web-grundkurs-checks/). Die Wahl steht in ?stufe= und
 * wird lokal gemerkt; ein Deep-Link mit ?week= ohne ?stufe= stammt aus der Zeit vor Intensiv und
 * gehoert zu Einfach (Abschluss-Check).
 */
export default {
  name: 'WebsiteCourse',
  components: { ProjectCourse, WeeklyCourseTour },
  props: {
    // Eintrag aus kurse.json
    course: { type: Object, required: true },
  },
  setup() {
    const { t } = useLanguage();
    const route = useRoute();
    const router = useRouter();

    const fromQuery = STUFEN.includes(route.query.stufe) ? route.query.stufe : null;
    const stufe = ref(fromQuery || (route.query.week ? 'einfach' : readStoredStufe()));

    const choose = (value) => {
      stufe.value = value;
      try { localStorage.setItem(STUFE_KEY, value); } catch { /* nur Komfort */ }
      router.replace({ query: { ...route.query, stufe: value } });
    };

    const reset = () => {
      stufe.value = null;
      try { localStorage.removeItem(STUFE_KEY); } catch { /* nur Komfort */ }
      const query = { ...route.query };
      delete query.stufe;
      delete query.week;
      router.replace({ query });
    };

    return { t, stufe, choose, reset, WEB_GRUNDKURS_WEEKS, WEB_GRUNDKURS_COURSE_TITLE };
  },
};
</script>

<style scoped>
.stufe-selector {
  text-align: center;
  padding: 40px 20px;
}

.stufe-selector h2 {
  font-size: 1.6em;
  margin-bottom: 8px;
}

.stufe-intro {
  color: #666;
  margin-bottom: 32px;
}

.stufe-cards {
  display: flex;
  gap: 24px;
  justify-content: center;
  flex-wrap: wrap;
}

.stufe-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 260px;
  padding: 28px 20px;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  background: #fff;
  cursor: pointer;
  transition: all 0.15s ease;
  text-align: center;
  font: inherit;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.stufe-card:hover {
  border-color: #d9c7ea;
  background: #f7f1fb;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(74, 34, 116, 0.12);
}

.stufe-icon {
  font-size: 2.4em;
}

.stufe-card strong {
  font-size: 1.1em;
  color: #222;
}

.stufe-age {
  font-size: 0.85em;
  color: #888;
}

.stufe-features {
  list-style: none;
  padding: 0;
  margin: 8px 0 0;
  text-align: left;
  font-size: 0.88em;
  color: #555;
}

.stufe-features li::before {
  content: '✓ ';
  color: var(--primary-purple, #4a2274);
  font-weight: bold;
}

.stufe-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  max-width: 1320px;
  margin: 0 auto 16px;
  padding: 10px 14px;
  background: #f7f1fb;
  border: 1px solid #d9c7ea;
  border-radius: 8px;
}

.btn-change-stufe {
  background: transparent;
  color: var(--primary-purple, #4a2274);
  border: 1px solid #d9c7ea;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  font: inherit;
  font-size: 0.9em;
}

.btn-change-stufe:hover {
  background: #fff;
}
</style>
