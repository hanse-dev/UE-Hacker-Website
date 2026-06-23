<template>
  <div class="interactive-course">
    <!-- Variant selector -->
    <div v-if="!variant" class="variant-selector">
      <h2>{{ lang === 'en' ? 'Who is this course for?' : 'Für wen ist dieser Kurs?' }}</h2>
      <p class="variant-intro">{{ lang === 'en' ? 'Choose your version – you can switch later.' : 'Wähle deine Version – du kannst später wechseln.' }}</p>
      <div class="variant-cards">
        <button class="variant-card" @click="selectVariant('kinder')">
          <span class="variant-icon">🌟</span>
          <strong>{{ lang === 'en' ? 'For Kids' : 'Für Kinder' }}</strong>
          <span class="variant-age">{{ lang === 'en' ? '8–12 years' : '8–12 Jahre' }}</span>
          <ul class="variant-features">
            <li>{{ lang === 'en' ? 'Simple explanations' : 'Einfache Erklärungen' }}</li>
            <li>{{ lang === 'en' ? 'Animals &amp; game examples' : 'Tiere &amp; Spielbeispiele' }}</li>
            <li>{{ lang === 'en' ? 'Code templates to fill in' : 'Code-Vorlagen zum Ausfüllen' }}</li>
          </ul>
        </button>
        <button class="variant-card" @click="selectVariant('jugendliche')">
          <span class="variant-icon">🚀</span>
          <strong>{{ lang === 'en' ? 'For Teenagers' : 'Für Jugendliche' }}</strong>
          <span class="variant-age">{{ lang === 'en' ? '13–17 years' : '13–17 Jahre' }}</span>
          <ul class="variant-features">
            <li>{{ lang === 'en' ? 'Direct approach' : 'Direkter Einstieg' }}</li>
            <li>{{ lang === 'en' ? 'Everyday &amp; app examples' : 'Alltags- &amp; App-Beispiele' }}</li>
            <li>{{ lang === 'en' ? 'Bonus tasks per lesson' : 'Bonus-Aufgaben pro Lektion' }}</li>
          </ul>
        </button>
      </div>
    </div>

    <template v-else>
      <div v-if="loading" class="loading">{{ lang === 'en' ? 'Loading lessons...' : 'Lade Lektionen...' }}</div>
      <div v-else-if="error" class="error">{{ error }}</div>

      <template v-else>
        <div class="course-layout">
          <div class="progress-bar-full">
            <div class="progress-info">
              <span>{{ lang === 'en' ? 'Lesson' : 'Lektion' }} {{ currentIndex + 1 }} {{ lang === 'en' ? 'of' : 'von' }} {{ lessons.length }}</span>
              <div class="progress-info-right">
                <span class="progress-count">{{ completedCount }} {{ lang === 'en' ? 'completed' : 'abgeschlossen' }}</span>
                <button class="btn-sidebar-toggle" @click="sidebarOpen = !sidebarOpen">
                  {{ sidebarOpen ? (lang === 'en' ? '✕ Close' : '✕ Schließen') : (lang === 'en' ? '☰ Lessons' : '☰ Lektionen') }}
                </button>
              </div>
            </div>
            <div class="progress-track">
              <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
            </div>
          </div>

          <aside class="lessons-sidebar" :class="{ 'sidebar-mobile-open': sidebarOpen }">
            <h3>{{ lang === 'en' ? 'Lessons' : 'Lektionen' }}</h3>
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
              <button @click="exportProgress" class="btn-export">{{ lang === 'en' ? 'Export progress' : 'Fortschritt exportieren' }}</button>
              <label class="btn-import">
                {{ lang === 'en' ? 'Import' : 'Importieren' }}
                <input type="file" accept=".json" class="file-input" @change="onImportFile" />
              </label>
              <button @click="switchVariant" class="btn-switch">{{ lang === 'en' ? 'Switch version' : 'Version wechseln' }}</button>
            </div>
          </aside>

          <main class="lesson-main">
            <div v-if="!currentLesson" class="no-lesson">
              <p>{{ lang === 'en' ? 'Select a lesson from the list.' : 'Wähle eine Lektion aus der Liste.' }}</p>
              <p v-if="lessons.length">{{ lang === 'en' ? 'Start with Lesson 1!' : 'Starte mit Lektion 1!' }}</p>
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
  '../../content/python-grundlagen-interaktiv/lessons.json',
  '../../content/python-grundlagen-interaktiv-kinder/lessons.json',
  '../../content/python-grundlagen-interaktiv-jugendliche/lessons.json',
  '../../content/python-grundlagen-interaktiv-kinder-en/lessons.json',
  '../../content/python-grundlagen-interaktiv-jugendliche-en/lessons.json',
]);

export default {
  name: 'InteractiveCourse',
  components: { LessonView },
  props: {
    contentPath: { type: String, default: 'python-grundlagen-interaktiv' },
  },
  setup() {
    const { lang } = useLanguage();
    const variant = ref(localStorage.getItem(VARIANT_STORAGE_KEY) || null);
    const lessons = ref([]);
    const loading = ref(false);
    const error = ref(null);
    const currentLessonId = ref(null);
    const sidebarOpen = ref(false);

    const contentPathForVariant = computed(() => {
      if (!variant.value) return 'python-grundlagen-interaktiv';
      const key = lang.value === 'en' ? `${variant.value}-en` : variant.value;
      return VARIANT_CONTENT_PATH[key] || VARIANT_CONTENT_PATH[variant.value] || 'python-grundlagen-interaktiv';
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
        error.value = lang.value === 'en' ? 'Could not load lessons.' : 'Lektionen konnten nicht geladen werden.';
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
        if (result.ok) alert(lang.value === 'en' ? 'Progress imported.' : 'Fortschritt wurde importiert.');
        else alert((lang.value === 'en' ? 'Import failed: ' : 'Import fehlgeschlagen: ') + (result.error || (lang.value === 'en' ? 'Unknown error' : 'Unbekannter Fehler')));
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

/* ── Course Layout ────────────────────────────────── */
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

.progress-count {
  font-weight: 600;
  color: #28a745;
}

.course-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: auto 1fr;
  gap: 24px;
  background: var(--white, #fff);
  border: 1px solid var(--border-color, #e0e0e0);
  border-radius: 12px;
  padding: 24px;
  min-height: 500px;
}

.progress-bar-full {
  grid-column: 1 / -1;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 16px 20px;
}

.progress-bar-full .progress-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  font-size: 0.95em;
  color: #555;
}

.progress-info-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-sidebar-toggle {
  display: none;
  align-items: center;
  gap: 4px;
  background: transparent;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 0.85em;
  cursor: pointer;
  color: var(--primary-purple, #4a2274);
  white-space: nowrap;
}

.progress-bar-full .progress-track {
  height: 8px;
  background: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar-full .progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-purple, #4a2274), var(--accent-orange, #ff9800));
  transition: width 0.3s ease;
}


.lessons-sidebar {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 20px;
  height: fit-content;
  position: sticky;
  top: 20px;
}

.lessons-sidebar h3 {
  margin: 0 0 16px 0;
  font-size: 1.1em;
  color: #333;
}

.lessons-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.lesson-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  margin-bottom: 4px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.2s;
}

.lesson-item:hover:not(.locked) { background: #f8f9fa; }
.lesson-item.active {
  background: rgba(74, 34, 116, 0.08);
  border-left: 3px solid var(--primary-purple, #4a2274);
}
.lesson-item.completed { color: #28a745; }
.lesson-item.locked { opacity: 0.5; cursor: not-allowed; }

.lesson-number {
  font-weight: 700;
  color: var(--primary-purple, #4a2274);
  min-width: 24px;
}

.lesson-title { flex: 1; font-size: 0.95em; }
.lesson-check { color: #28a745; font-weight: bold; }

.sidebar-actions {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.btn-export,
.btn-import,
.btn-switch {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.9em;
  cursor: pointer;
  text-align: center;
}

.btn-export:hover,
.btn-import:hover { background: #e9ecef; }

.btn-switch {
  border-color: var(--primary-purple, #4a2274);
  color: var(--primary-purple, #4a2274);
}

.btn-switch:hover { background: rgba(74,34,116,0.06); }

.file-input { display: none; }
.lesson-main { min-width: 0; }

.no-lesson {
  background: #f8f9fa;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  padding: 60px 40px;
  text-align: center;
  color: #6c757d;
}

@media (max-width: 768px) {
  .course-layout {
    grid-template-columns: 1fr;
    grid-template-rows: unset;
    min-height: unset;
    padding: 16px;
    gap: 16px;
  }

  /* Reorder: progress → sidebar (toggle) → main content */
  .progress-bar-full { order: 1; }
  .lessons-sidebar {
    order: 2;
    position: static;
    display: none;
  }
  .lesson-main { order: 3; }
  .lessons-sidebar.sidebar-mobile-open { display: block; }

  .btn-sidebar-toggle { display: inline-flex; }

  .variant-cards { flex-direction: column; align-items: center; }
}
</style>
