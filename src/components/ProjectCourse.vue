<template>
  <div class="project-course">
    <div v-if="loading" class="loading">{{ t('lessons.loading') }}</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="course-layout">
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
          <template v-for="(lesson, idx) in lessons" :key="lesson.id">
            <li v-if="isNewSection(idx)" class="section-header">
              {{ t('lessons.section.' + lesson.section) }}
            </li>
            <li
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
          </template>
        </ul>

        <div class="sidebar-actions">
          <button @click="exportProgress" class="btn-export">{{ t('lessons.exportProgress') }}</button>
          <label class="btn-import">
            {{ t('lessons.import') }}
            <input type="file" accept=".json" class="file-input" @change="onImportFile" />
          </label>
        </div>
      </aside>

      <main class="lesson-main" ref="mainEl">
        <div v-if="!currentLesson" class="no-lesson">
          <p>{{ t('lessons.selectFromList') }}</p>
          <p v-if="lessons.length">{{ t('lessons.startWithOne') }}</p>
        </div>
        <LessonView
          v-else-if="engine === 'pyodide'"
          :lesson="currentLesson"
          :content-path="contentPath"
          :variant="contentPath"
          :course-id="courseId"
          @completed="onLessonCompleted"
        />
        <JsLessonView
          v-else
          :lesson="currentLesson"
          :content-path="contentPath"
          :variant="contentPath"
          :course-id="courseId"
          :show-canvas="showCanvas"
          @completed="onLessonCompleted"
        />
      </main>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import LessonView from './LessonView.vue';
import JsLessonView from './JsLessonView.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';

const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

export default {
  name: 'ProjectCourse',
  components: { LessonView, JsLessonView },
  props: {
    courseId: { type: String, required: true },
    contentPath: { type: String, required: true },
    engine: { type: String, default: 'pyodide' },
    // Nur fuer engine: 'js-sandbox' relevant - ob das Canvas/iframe sichtbar sein soll (z.B. fuer
    // einen Spiele-Kurs) oder ausgeblendet bleibt, weil der Kurs nie zeichnet.
    showCanvas: { type: Boolean, default: true },
  },
  setup(props) {
    const { lang, t } = useLanguage();
    const lessons = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const currentLessonId = ref(null);
    const sidebarOpen = ref(false);
    const mainEl = ref(null);

    const { completedCount, isCompleted, isLessonUnlocked, exportProgress, importProgress } =
      useInteractiveProgress(props.contentPath, props.courseId);

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

    // Optionales `section`-Feld in lessons.json (z.B. 'lektion'/'debug'/'mission') gruppiert die
    // Sidebar-Liste mit Ueberschriften, ohne die zugrunde liegende sequenzielle Freischaltung zu
    // aendern - Kurse ohne dieses Feld (Cäsar-Chiffre, Morsecode, ...) zeigen weiterhin keine
    // Ueberschriften.
    const isNewSection = (idx) => {
      const lesson = lessons.value[idx];
      if (!lesson?.section) return false;
      return idx === 0 || lessons.value[idx - 1]?.section !== lesson.section;
    };

    const loadLessons = async () => {
      loading.value = true;
      error.value = null;
      try {
        const key = `../../content/${props.contentPath}/lessons.json`;
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

    // Wechselt man die Lektion (Sidebar-Klick oder "Weiter"-Button), soll man oben bei der neuen
    // Lektion landen statt an der Scroll-Position der alten (meist ganz unten, am "Weiter"-Button).
    // Kein Scroll beim allerersten Laden (oldId ist dann noch null). `flush: 'post'`, damit die neue
    // Lektion bereits gerendert ist, bevor wir dorthin scrollen (sonst greift der Scroll noch die
    // Position der alten Lektion ab).
    watch(currentLessonId, (newId, oldId) => {
      if (!oldId) return;
      mainEl.value?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, { flush: 'post' });

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = importProgress(reader.result);
        if (result.ok) alert(t('lessons.importSuccess'));
        else alert(t('lessons.importFailed') + (result.error || t('jupyter.unknownError')));
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    const exportProgressFile = () => {
      const json = exportProgress();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `${props.contentPath}-fortschritt.json`;
      a.click();
      URL.revokeObjectURL(a.href);
    };

    onMounted(loadLessons);

    return {
      lang,
      t,
      lessons,
      loading,
      error,
      sidebarOpen,
      mainEl,
      currentLesson,
      currentIndex,
      progressPercent,
      completedCount,
      isCompleted,
      isLessonUnlocked,
      isNewSection,
      selectLesson,
      onLessonCompleted,
      onImportFile,
      exportProgress: exportProgressFile,
    };
  },
};
</script>

<style>
/* Unscoped, damit die @import-Regeln denselben Klassennamen greifen wie im Template gerendert
   (siehe course-layout.css-Kommentar: @import in <style scoped> bekommt einen abweichenden
   Scope-Hash). Alle Klassen darin sind exklusiv für ProjectCourse.vue/InteractiveCourse.vue. */
@import '../assets/styles/course-layout.css';
</style>

<style scoped>
.project-course {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 0;
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
</style>
