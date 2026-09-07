<template>
  <div class="interactive-course">
    <!-- Variant selector -->
    <div v-if="!variant" class="variant-selector">
      <h2>{{ t('interactive.whoFor') }}</h2>
      <p class="variant-intro">{{ t('interactive.chooseVersion') }}</p>
      <div class="variant-cards">
        <button class="variant-card" @click="selectVariant('kinder')">
          <span class="variant-icon">🌟</span>
          <strong>{{ t('interactive.kids.title') }}</strong>
          <span class="variant-age">{{ t('interactive.kids.age') }}</span>
          <ul class="variant-features">
            <li>{{ t('interactive.kids.f1') }}</li>
            <li>{{ t('interactive.kids.f2') }}</li>
            <li>{{ t('interactive.kids.f3') }}</li>
          </ul>
        </button>
        <button class="variant-card" @click="selectVariant('jugendliche')">
          <span class="variant-icon">🚀</span>
          <strong>{{ t('interactive.teens.title') }}</strong>
          <span class="variant-age">{{ t('interactive.teens.age') }}</span>
          <ul class="variant-features">
            <li>{{ t('interactive.teens.f1') }}</li>
            <li>{{ t('interactive.teens.f2') }}</li>
            <li>{{ t('interactive.teens.f3') }}</li>
          </ul>
        </button>
      </div>
    </div>

    <template v-else>
      <div v-if="loading" class="loading">{{ t('lessons.loading') }}</div>
      <div v-else-if="error" class="error">{{ error }}</div>

      <template v-else>
        <div class="course-layout">
          <div class="progress-bar-full">
            <div class="progress-info">
              <span>{{ t('lessons.lesson') }} {{ currentIndex + 1 }} {{ t('lessons.of') }} {{ lessons.length }}</span>
              <div class="progress-info-right">
                <span class="progress-count">{{ completedCount }} {{ t('lessons.completed') }}</span>
                <button class="btn-sidebar-toggle" @click="sidebarOpen = !sidebarOpen">
                  {{ sidebarOpen ? t('lessons.sidebarClose') : t('lessons.sidebarOpen') }}
                </button>
              </div>
            </div>
            <div class="progress-track">
              <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
            </div>
          </div>

          <aside class="lessons-sidebar" :class="{ 'sidebar-mobile-open': sidebarOpen }">
            <h3>{{ t('lessons.title') }}</h3>
            <ul class="lessons-list">
              <li
                v-for="(lesson, idx) in lessons"
                :key="lesson.id"
                :class="['lesson-item', {
                  active: currentLesson?.id === lesson.id,
                  completed: isCompleted(lesson.id),
                  locked: !isLessonUnlocked(lesson.id, lessons),
                }]"
                @click="selectLesson(lesson)"
              >
                <span class="lesson-number">{{ idx + 1 }}</span>
                <span class="lesson-title">{{ lesson.title }}</span>
                <span v-if="isCompleted(lesson.id)" class="lesson-check">✓</span>
              </li>
            </ul>

            <div class="sidebar-actions">
              <button @click="exportProgress" class="btn-export">{{ t('lessons.exportProgress') }}</button>
              <label class="btn-import">
                {{ t('lessons.import') }}
                <input type="file" accept=".json" class="file-input" @change="onImportFile" />
              </label>
              <button @click="switchVariant" class="btn-switch">{{ t('interactive.switchVersion') }}</button>
            </div>
          </aside>

          <main class="lesson-main">
            <div v-if="!currentLesson" class="no-lesson">
              <p>{{ t('lessons.selectFromList') }}</p>
              <p v-if="lessons.length">{{ t('lessons.startWithOne') }}</p>
            </div>
            <LessonView
              v-else
              :lesson="currentLesson"
              :content-path="contentPathForVariant"
              :variant="variant"
              @completed="onLessonCompleted"
            />
          </main>
        </div>
      </template>
    </template>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import LessonView from './LessonView.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';

const VARIANT_STORAGE_KEY = 'ue-hacker-interactive-variant';

const VARIANT_CONTENT_PATH = {
  kinder:             'python-grundlagen-interaktiv-kinder',
  jugendliche:        'python-grundlagen-interaktiv-jugendliche',
  'kinder-en':        'python-grundlagen-interaktiv-kinder-en',
  'jugendliche-en':   'python-grundlagen-interaktiv-jugendliche-en',
};

const lessonJsonModules = import.meta.glob([
  '../../content/python-grundlagen-interaktiv-kinder/lessons.json',
  '../../content/python-grundlagen-interaktiv-jugendliche/lessons.json',
  '../../content/python-grundlagen-interaktiv-kinder-en/lessons.json',
  '../../content/python-grundlagen-interaktiv-jugendliche-en/lessons.json',
]);

export default {
  name: 'InteractiveCourse',
  components: { LessonView },
  setup() {
    const { lang, t } = useLanguage();
    const variant = ref(localStorage.getItem(VARIANT_STORAGE_KEY) || null);
    const lessons = ref([]);
    const loading = ref(false);
    const error = ref(null);
    const currentLessonId = ref(null);
    const sidebarOpen = ref(false);

    const contentPathForVariant = computed(() => {
      if (!variant.value) return null;
      const key = lang.value === 'en' ? `${variant.value}-en` : variant.value;
      return VARIANT_CONTENT_PATH[key] || VARIANT_CONTENT_PATH[variant.value] || null;
    });

    // Pre-create both progress instances — composables must not be called inside computed()
    const progressKinder      = useInteractiveProgress('kinder');
    const progressJugendliche = useInteractiveProgress('jugendliche');
    const activeProgress      = computed(() =>
      variant.value === 'jugendliche' ? progressJugendliche : progressKinder
    );

    const isCompleted      = (id) => activeProgress.value.isCompleted(id);
    const isLessonUnlocked = (id, ls) => activeProgress.value.isLessonUnlocked(id, ls);
    const completedCount   = computed(() => activeProgress.value.completedCount.value);

    const currentIndex = computed(() => {
      const idx = lessons.value.findIndex((l) => l.id === currentLessonId.value);
      return idx >= 0 ? idx : 0;
    });

    const currentLesson = computed(() =>
      lessons.value.find((l) => l.id === currentLessonId.value) || lessons.value[0]
    );

    const progressPercent = computed(() => {
      if (!lessons.value.length) return 0;
      return Math.round((completedCount.value / lessons.value.length) * 100);
    });

    const loadLessons = async () => {
      if (!variant.value) return;
      loading.value = true;
      error.value = null;
      try {
        const key = `../../content/${contentPathForVariant.value}/lessons.json`;
        const loader = lessonJsonModules[key];
        if (!loader) throw new Error(`lessons.json nicht gefunden: ${key}`);
        const mod = await loader();
        lessons.value = mod.default || [];
        if (lessons.value.length && !currentLessonId.value) {
          currentLessonId.value = lessons.value[0].id;
        }
      } catch (e) {
        console.error('Could not load lessons:', e);
        error.value = t('lessons.loadError');
      } finally {
        loading.value = false;
      }
    };

    const selectVariant = (v) => {
      variant.value = v;
      localStorage.setItem(VARIANT_STORAGE_KEY, v);
      currentLessonId.value = null;
      lessons.value = [];
      loadLessons();
    };

    const switchVariant = () => {
      variant.value = null;
      localStorage.removeItem(VARIANT_STORAGE_KEY);
      lessons.value = [];
      currentLessonId.value = null;
    };

    const selectLesson = (lesson) => {
      if (!isLessonUnlocked(lesson.id, lessons.value)) return;
      currentLessonId.value = lesson.id;
      sidebarOpen.value = false;
    };

    const onLessonCompleted = (lessonId) => {
      const idx = lessons.value.findIndex((l) => l.id === lessonId);
      const nextId = lessons.value[idx + 1]?.id;
      if (nextId) currentLessonId.value = nextId;
    };

    const exportProgress = () => {
      const json = activeProgress.value.exportProgress();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `python-grundlagen-fortschritt-${variant.value}.json`;
      a.click();
      URL.revokeObjectURL(a.href);
    };

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = activeProgress.value.importProgress(reader.result);
        if (result.ok) alert(t('lessons.importSuccess'));
        else alert(t('lessons.importFailed') + (result.error || t('jupyter.unknownError')));
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    onMounted(loadLessons);
    watch(variant, loadLessons);
    watch(lang, () => {
      currentLessonId.value = null;
      loadLessons();
    });

    return {
      lang,
      t,
      variant,
      lessons,
      loading,
      error,
      currentLessonId,
      sidebarOpen,
      currentLesson,
      currentIndex,
      progressPercent,
      completedCount,
      contentPathForVariant,
      isCompleted,
      isLessonUnlocked,
      selectVariant,
      switchVariant,
      selectLesson,
      onLessonCompleted,
      exportProgress,
      onImportFile,
    };
  },
};
</script>

<style scoped>
.interactive-course {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 0;
}

/* ── Variant Selector ─────────────────────────────── */
.variant-selector {
  text-align: center;
  padding: 40px 20px;
}

.variant-selector h2 {
  font-size: 1.6em;
  margin-bottom: 8px;
}

.variant-intro {
  color: #666;
  margin-bottom: 32px;
}

.variant-cards {
  display: flex;
  gap: 24px;
  justify-content: center;
  flex-wrap: wrap;
}

.variant-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 220px;
  padding: 28px 20px;
  border: 2px solid #dee2e6;
  border-radius: 12px;
  background: #fff;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
  text-align: center;
}

.variant-card:hover {
  border-color: var(--primary-purple, #4a2274);
  box-shadow: 0 4px 16px rgba(74,34,116,0.12);
}

.variant-icon {
  font-size: 2.4em;
}

.variant-card strong {
  font-size: 1.1em;
  color: #222;
}

.variant-age {
  font-size: 0.85em;
  color: #888;
}

.variant-features {
  list-style: none;
  padding: 0;
  margin: 8px 0 0;
  text-align: left;
  font-size: 0.88em;
  color: #555;
}

.variant-features li::before {
  content: '✓ ';
  color: var(--primary-purple, #4a2274);
  font-weight: bold;
}

.loading,
.error {
  padding: 40px;
  text-align: center;
  font-size: 18px;
}

.error {
  color: #dc3545;
  background: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 8px;
}

.btn-switch {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.9em;
  cursor: pointer;
  text-align: center;
  border-color: var(--primary-purple, #4a2274);
  color: var(--primary-purple, #4a2274);
}

.btn-switch:hover { background: rgba(74,34,116,0.06); }

@media (max-width: 768px) {
  .variant-cards { flex-direction: column; align-items: center; }
}
</style>

<style>
/* Unscoped, damit die @import-Regeln denselben Klassennamen greifen wie im Template gerendert
   (siehe course-layout.css-Kommentar: @import in <style scoped> bekommt einen abweichenden
   Scope-Hash). Alle Klassen darin sind exklusiv für ProjectCourse.vue/InteractiveCourse.vue. */
@import '../assets/styles/course-layout.css';
</style>
