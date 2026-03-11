<template>
  <div class="interactive-course">
    <div v-if="loading" class="loading">Lade Lektionen...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <template v-else>
      <div class="course-layout">
        <!-- Fortschrittsleiste oben -->
        <div class="progress-bar-full">
          <div class="progress-info">
            <span>Lektion {{ currentIndex + 1 }} von {{ lessons.length }}</span>
            <span class="progress-count">{{ completedCount }} abgeschlossen</span>
          </div>
          <div class="progress-track">
            <div
              class="progress-fill"
              :style="{ width: progressPercent + '%' }"
            ></div>
          </div>
        </div>

        <!-- Lektionen-Sidebar + Inhalt -->
        <aside class="lessons-sidebar">
          <h3>Lektionen</h3>
          <ul class="lessons-list">
            <li
              v-for="(lesson, idx) in lessons"
              :key="lesson.id"
              :class="[
                'lesson-item',
                {
                  active: currentLesson?.id === lesson.id,
                  completed: isCompleted(lesson.id),
                  locked: !isLessonUnlocked(lesson.id, lessons),
                },
              ]"
              @click="selectLesson(lesson)"
            >
              <span class="lesson-number">{{ idx + 1 }}</span>
              <span class="lesson-title">{{ lesson.title }}</span>
              <span v-if="isCompleted(lesson.id)" class="lesson-check">✓</span>
            </li>
          </ul>

          <div class="sidebar-actions">
            <button @click="exportProgress" class="btn-export">Fortschritt exportieren</button>
            <label class="btn-import">
              Importieren
              <input
                type="file"
                accept=".json"
                class="file-input"
                @change="onImportFile"
              />
            </label>
          </div>
        </aside>

        <main class="lesson-main">
          <div v-if="!currentLesson" class="no-lesson">
            <p>Wähle eine Lektion aus der Liste.</p>
            <p v-if="lessons.length">Starte mit Lektion 1!</p>
          </div>
          <LessonView
            v-else
            :lesson="currentLesson"
            :content-path="contentPath"
            @completed="onLessonCompleted"
          />
        </main>
      </div>
    </template>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import LessonView from './LessonView.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';

export default {
  name: 'InteractiveCourse',
  components: {
    LessonView,
  },
  props: {
    contentPath: {
      type: String,
      default: 'python-grundlagen-interaktiv',
    },
  },
  setup(props) {
    const lessons = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const currentLessonId = ref(null);

    const {
      isCompleted,
      isLessonUnlocked,
      completedCount,
      exportProgress: exportProgressData,
      importProgress,
    } = useInteractiveProgress();

    const currentIndex = computed(() => {
      const idx = lessons.value.findIndex((l) => l.id === currentLessonId.value);
      return idx >= 0 ? idx : 0;
    });

    const currentLesson = computed(() => {
      return lessons.value.find((l) => l.id === currentLessonId.value) || lessons.value[0];
    });

    const progressPercent = computed(() => {
      if (!lessons.value.length) return 0;
      return Math.round((completedCount.value / lessons.value.length) * 100);
    });

    const loadLessons = async () => {
      loading.value = true;
      error.value = null;
      try {
        const mod = await import('@content/python-grundlagen-interaktiv/lessons.json');
        lessons.value = mod.default || [];
        if (lessons.value.length && !currentLessonId.value) {
          currentLessonId.value = lessons.value[0].id;
        }
      } catch (e) {
        console.error('Could not load lessons:', e);
        error.value = 'Lektionen konnten nicht geladen werden.';
      } finally {
        loading.value = false;
      }
    };

    const selectLesson = (lesson) => {
      if (!isLessonUnlocked(lesson.id, lessons.value)) return;
      currentLessonId.value = lesson.id;
    };

    const onLessonCompleted = (lessonId) => {
      const nextId = lessons.value.find((l, i) => {
        const idx = lessons.value.findIndex((le) => le.id === lessonId);
        return i === idx + 1;
      })?.id;
      if (nextId) {
        currentLessonId.value = nextId;
      }
    };

    const exportProgress = () => {
      const json = exportProgressData();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'python-grundlagen-fortschritt.json';
      a.click();
      URL.revokeObjectURL(a.href);
    };

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = importProgress(reader.result);
        if (result.ok) {
          alert('Fortschritt wurde importiert.');
        } else {
          alert('Import fehlgeschlagen: ' + (result.error || 'Unbekannter Fehler'));
        }
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    onMounted(loadLessons);

    return {
      lessons,
      loading,
      error,
      currentLessonId,
      currentLesson,
      currentIndex,
      progressPercent,
      completedCount,
      isCompleted,
      isLessonUnlocked,
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
  margin-bottom: 0;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 16px 20px;
}

.progress-bar-full .progress-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 0.95em;
  color: #555;
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

@media (max-width: 768px) {
  .course-layout {
    grid-template-columns: 1fr;
  }
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

.lesson-item:hover:not(.locked) {
  background: #f8f9fa;
}

.lesson-item.active {
  background: rgba(74, 34, 116, 0.08);
  border-left: 3px solid var(--primary-purple, #4a2274);
}

.lesson-item.completed {
  color: #28a745;
}

.lesson-item.locked {
  opacity: 0.5;
  cursor: not-allowed;
}

.lesson-number {
  font-weight: 700;
  color: var(--primary-purple, #4a2274);
  min-width: 24px;
}

.lesson-title {
  flex: 1;
  font-size: 0.95em;
}

.lesson-check {
  color: #28a745;
  font-weight: bold;
}

.sidebar-actions {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.btn-export,
.btn-import {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.9em;
  cursor: pointer;
  text-align: center;
}

.btn-export:hover,
.btn-import:hover {
  background: #e9ecef;
}

.file-input {
  display: none;
}

.lesson-main {
  min-width: 0;
}

.no-lesson {
  background: #f8f9fa;
  border: 2px dashed #dee2e6;
  border-radius: 8px;
  padding: 60px 40px;
  text-align: center;
  color: #6c757d;
}
</style>
