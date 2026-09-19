<template>
  <section class="course-detail" v-if="course">
    <h1>{{ courseTitle }}</h1>
    <div v-if="description || isWeeklyCourse" class="course-description">
      <div v-if="description" v-html="description"></div>

      <div v-if="isWeeklyCourse || isInteractiveCourse" class="placement-banner">
        <p>{{ t('course.placement.banner') }}</p>
        <router-link to="/kurs/python-einstufung" class="placement-banner-link">
          {{ t('course.placement.link') }}
        </router-link>
      </div>

      <div v-if="isWeeklyCourse" class="course-structure">
        <p class="course-structure-intro">{{ t('course.structure.intro') }}</p>
        <div class="course-structure-tabs">
          <div class="course-structure-tab" v-for="step in courseStructureSteps" :key="step.key">
            <span class="course-structure-icon">{{ step.icon }}</span>
            <div class="course-structure-text">
              <strong>{{ step.title }}</strong>
              <span>{{ step.desc }}</span>
            </div>
          </div>
        </div>
        <p class="course-structure-reference">{{ t('course.structure.reference') }}</p>
      </div>
    </div>

    <CourseAppointments v-if="!isInteractiveCourse && !isPlacementCourse && !isProjectCourse && !isJsGrundkurs" :termine="courseTermine" />

    <div v-if="isInteractiveCourse" class="interactive-course-wrapper">
      <InteractiveCourse :content-path="course.contentPath" />
    </div>

    <div v-else-if="isPlacementCourse" class="placement-course-wrapper">
      <PlacementCourse />
    </div>

    <div v-else-if="isProjectCourse" class="project-course-wrapper">
      <ProjectCourse :course-id="id" :content-path="course.contentPath" :engine="course.engine" />
    </div>

    <WeekTour v-else-if="isWeeklyCourse" />

    <div v-else-if="isJsGrundkurs" class="js-grundkurs-wrapper">
      <JsGrundkursTour />
    </div>

    <div v-if="isWeeklyCourse" class="notebook-pack-download">
      <a href="/python-12-wochen-notebooks.zip" download class="notebook-pack-btn">
        {{ t('course.download.btn') }}
      </a>
      <p class="notebook-pack-hint">{{ t('course.download.hint') }}</p>
    </div>

    <div v-if="isWeeklyCourse" class="project-banner">
      <div class="project-banner-text">
        <strong>{{ t('course.project.banner.title') }}</strong>
        <p>{{ t('course.project.banner.desc') }}</p>
      </div>
      <router-link to="/projekte" class="project-banner-link">
        {{ t('course.project.banner.link') }}
      </router-link>
    </div>
  </section>
  <div v-else class="course-loading">
    <p v-if="loading">{{ t('course.loading') }}</p>
    <p v-else class="course-error">{{ t('course.error') }}</p>
  </div>
</template>

<script>
import { ref, onMounted, computed, watch, toRef } from 'vue';
import CourseAppointments from '../components/CourseAppointments.vue';
import WeekTour from '../components/WeekTour.vue';
import InteractiveCourse from '../components/InteractiveCourse.vue';
import PlacementCourse from '../components/PlacementCourse.vue';
import ProjectCourse from '../components/ProjectCourse.vue';
import JsGrundkursTour from '../components/JsGrundkursTour.vue';
import { loadCourseData } from '../composables/useCourseData';
import { useLanguage } from '../composables/useLanguage.js';

const STRUCTURE_STEPS_CONFIG = [
  { key: 'week',    icon: '🗺️', titleKey: 'course.structure.step.week.title',    descKey: 'course.structure.step.week.desc' },
  { key: 'variant', icon: '🧭', titleKey: 'course.structure.step.variant.title', descKey: 'course.structure.step.variant.desc' },
  { key: 'lesson',  icon: '📚', titleKey: 'course.structure.step.lesson.title',  descKey: 'course.structure.step.lesson.desc' },
  { key: 'debug',   icon: '🐛', titleKey: 'course.structure.step.debug.title',   descKey: 'course.structure.step.debug.desc' },
  { key: 'mission', icon: '⭐', titleKey: 'course.structure.step.mission.title', descKey: 'course.structure.step.mission.desc' },
  { key: 'branch',  icon: '🔥', titleKey: 'course.structure.step.branch.title',  descKey: 'course.structure.step.branch.desc' },
  { key: 'cert',    icon: '🎓', titleKey: 'course.structure.step.cert.title',    descKey: 'course.structure.step.cert.desc' },
];

export default {
  name: 'CourseDetail',
  components: {
    CourseAppointments,
    WeekTour,
    InteractiveCourse,
    PlacementCourse,
    ProjectCourse,
    JsGrundkursTour,
  },
  props: {
    id: { type: String, required: true },
  },
  setup(props) {
    const { lang, t } = useLanguage();

    const course = ref(null);
    const description = ref('');
    const courseTermine = ref([]);
    const loading = ref(true);

    const isWeeklyCourse = computed(() => props.id === 'python-12-wochen-grundkurs');
    const isInteractiveCourse = computed(() => props.id === 'python-grundlagen-interaktiv');
    const isPlacementCourse = computed(() => props.id === 'python-einstufung');
    const isProjectCourse = computed(() => course.value?.type === 'projekt');
    const isJsGrundkurs = computed(() => props.id === 'js-grundkurs');

    const courseStructureSteps = computed(() =>
      STRUCTURE_STEPS_CONFIG.map((step) => ({ ...step, title: t(step.titleKey), desc: t(step.descKey) }))
    );

    const courseTitle = computed(() =>
      lang.value === 'en' && course.value?.title_en
        ? course.value.title_en
        : course.value?.title ?? ''
    );

    const loadCourse = async () => {
      loading.value = true;
      course.value = null;
      description.value = '';
      courseTermine.value = [];
      try {
        const data = await loadCourseData(props.id, lang.value);
        course.value = data.course;
        description.value = data.description;
        courseTermine.value = data.courseTermine;
      } catch (e) {
        console.error('CourseDetail load error:', e);
      } finally {
        loading.value = false;
      }
    };

    onMounted(loadCourse);

    // Same component instance is reused when switching /kurs/:id → must reload
    watch(() => props.id, loadCourse);

    watch(lang, async () => {
      if (course.value) {
        const data = await loadCourseData(props.id, lang.value);
        description.value = data.description;
      }
    });

    return {
      course,
      courseTitle,
      description,
      courseTermine,
      loading,
      isWeeklyCourse,
      isInteractiveCourse,
      isPlacementCourse,
      isProjectCourse,
      isJsGrundkurs,
      id: toRef(props, 'id'),
      courseStructureSteps,
      t,
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

.project-course-wrapper {
  margin-top: 20px;
  overflow: visible;
}

.js-grundkurs-wrapper {
  margin-top: 20px;
  overflow: visible;
}

.placement-course-wrapper {
  margin-top: 20px;
  overflow: visible;
}

.course-description {
  margin-bottom: 40px;
  font-size: 1.1em;
}

.placement-banner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin: 20px 0 0 0;
  padding: 14px 16px;
  background: #f0f4ff;
  border: 2px solid #6c8ebf;
  border-radius: 10px;
}

.placement-banner p {
  margin: 0;
  flex: 1;
  font-size: 0.95em;
  color: #334;
  line-height: 1.4;
}

.placement-banner-link {
  background: var(--primary-purple, #4a2274);
  color: white;
  text-decoration: none;
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9em;
  white-space: nowrap;
}

.placement-banner-link:hover {
  background: #3d1b5c;
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

.project-banner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 40px;
  padding: 18px 20px;
  background: #f3eef8;
  border: 2px solid #c4a8e0;
  border-radius: 10px;
}

.project-banner-text strong {
  display: block;
  color: var(--primary-purple, #4a2274);
  margin-bottom: 4px;
}

.project-banner-text p {
  margin: 0;
  color: #444;
  font-size: 0.95em;
}

.project-banner-link {
  background: var(--primary-purple, #4a2274);
  color: white;
  text-decoration: none;
  padding: 10px 16px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9em;
  white-space: nowrap;
}

.project-banner-link:hover {
  background: #3d1b5c;
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

.course-structure-reference {
  margin: 14px 0 0;
  color: #6b7280;
  font-size: 0.85em;
  font-style: italic;
}
</style>
