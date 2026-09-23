<template>
  <div class="js-course-tour">
    <div v-if="loading" class="loading">{{ t('lessons.loading') }}</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <template v-else>
      <div v-if="!embedded" class="tour-header">
        <div class="tour-breadcrumb">
          <button class="breadcrumb-back" @click="$emit('change-week')">{{ t('jsGrundkurs.backToWeeks') }}</button>
          <span class="breadcrumb-week">{{ weekLabel }}</span>
          <span class="breadcrumb-sep">›</span>
          <span class="breadcrumb-lesson">{{ currentBreadcrumbLabel }}</span>
        </div>
        <span class="progress-count">{{ completedCount }} {{ t('lessons.completed') }}</span>
      </div>
      <div v-else class="tour-header tour-header-embedded">
        <span class="breadcrumb-lesson">{{ currentBreadcrumbLabel }}</span>
        <span class="progress-count">{{ completedCount }} / {{ lessons.length }} {{ t('lessons.completed') }}</span>
      </div>

      <div class="progress-stepper">
        <template v-for="(group, gi) in groupedLessons" :key="group.section">
          <div class="stepper-group">
            <span class="stepper-group-label">{{ t('lessons.section.' + group.section) }}</span>
            <div class="stepper-group-dots">
              <template v-for="(lesson, li) in group.lessons" :key="lesson.id">
                <button
                  class="stepper-step"
                  :class="{
                    done: isCompleted(lesson.id),
                    current: currentLesson?.id === lesson.id,
                    locked: !canOpen(lesson),
                  }"
                  :disabled="!canOpen(lesson)"
                  :title="lesson.title"
                  @click="selectLesson(lesson)"
                >
                  <span class="stepper-dot">{{ isCompleted(lesson.id) ? '✓' : group.startIndex + li + 1 }}</span>
                </button>
                <span
                  v-if="li < group.lessons.length - 1"
                  class="stepper-line"
                  :class="{ done: isCompleted(lesson.id) }"
                ></span>
              </template>
            </div>
          </div>
          <span v-if="gi < groupedLessons.length - 1" class="stepper-group-gap"></span>
        </template>
        <template v-if="hasCheck">
          <span class="stepper-group-gap"></span>
          <div class="stepper-group">
            <span class="stepper-group-label">{{ t('tab.check') }}</span>
            <div class="stepper-group-dots">
              <button class="stepper-step" data-open-check :title="t('tab.check')" @click="$emit('open-check')">
                <span class="stepper-dot">✅</span>
              </button>
            </div>
          </div>
        </template>
      </div>

      <main class="lesson-main" ref="mainEl">
        <div v-if="choosingBranch" class="branch-choice-page">
          <h3>{{ t('tour.branch.title') }}</h3>
          <p>{{ t('tour.branch.intro') }}</p>
          <div class="branch-tile-grid">
            <button class="branch-tile" data-branch="boss" @click="chooseBoss">
              <span class="branch-tile-icon">🔥</span>
              <strong>{{ t('tour.deepen') }}</strong>
              <span class="branch-tile-desc">{{ t('tour.branch.deepenDesc') }}</span>
            </button>
            <button class="branch-tile" data-branch="check" @click="$emit('open-check')">
              <span class="branch-tile-icon">✅</span>
              <strong>{{ t('tab.check') }}</strong>
              <span class="branch-tile-desc">{{ t('tour.branch.checkDesc') }}</span>
            </button>
          </div>
        </div>
        <LessonView
          v-else-if="currentLesson && engine === 'pyodide'"
          :lesson="currentLesson"
          :content-path="contentPath"
          :variant="contentPath"
          :course-id="courseId"
          :key="currentLesson.id"
          @completed="onLessonCompleted"
        />
        <JsLessonView
          v-else-if="currentLesson"
          :lesson="currentLesson"
          :content-path="contentPath"
          :variant="contentPath"
          :course-id="courseId"
          :show-canvas="showCanvas"
          :dom-mode="domMode"
          @completed="onLessonCompleted"
        />
      </main>

      <div class="tour-actions">
        <button @click="exportProgress" class="btn-export">{{ t('lessons.exportProgress') }}</button>
        <label class="btn-import">
          {{ t('lessons.import') }}
          <input type="file" accept=".json" class="file-input" @change="onImportFile" />
        </label>
      </div>
    </template>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import JsLessonView from './JsLessonView.vue';
import LessonView from './LessonView.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { exportSavedCode, importSavedCode } from '../composables/useSavedCode';

const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');

export default {
  name: 'JsCourseTour',
  components: { JsLessonView, LessonView },
  props: {
    courseId: { type: String, required: true },
    contentPath: { type: String, required: true },
    weekLabel: { type: String, default: '' },
    // 'js-sandbox' (JsLessonView) oder 'pyodide' (LessonView) - gleiche Tour, andere Ausfuehrung.
    engine: { type: String, default: 'js-sandbox' },
    // Eingebettet in eine andere Tour (z.B. WeekTourStepper): kein eigener Breadcrumb/Zurueck-Link.
    embedded: { type: Boolean, default: false },
    // true: keine sequenzielle Sperre, alle Lektionen sind frei anklickbar.
    freeNavigation: { type: Boolean, default: false },
    // true: der Wochen-Check existiert - er steht als letzter Punkt in der Leiste, und nach den
    // Missionen wird zwischen Extra-Herausforderung und Check gewaehlt.
    hasCheck: { type: Boolean, default: false },
    showCanvas: { type: Boolean, default: true },
    domMode: { type: Boolean, default: false },
  },
  emits: ['change-week', 'open-check'],
  setup(props, { emit }) {
    const { t } = useLanguage();
    const lessons = ref([]);
    const loading = ref(true);
    const error = ref(null);
    const currentLessonId = ref(null);
    const mainEl = ref(null);

    const { completedCount, isCompleted, isLessonUnlocked, exportProgress, importProgress } =
      useInteractiveProgress(props.contentPath, props.courseId);

    const currentLesson = computed(() =>
      lessons.value.find((l) => l.id === currentLessonId.value) || lessons.value[0]
    );

    // Stepper-Kullern gruppiert nach dem `section`-Feld (Lektion/Debug/Mission), mit einer
    // durchgehenden Nummerierung ueber alle Lektionen hinweg (startIndex) statt pro Gruppe neu
    // bei 1 zu beginnen - direkte Uebertragung des Python-Wochen-Tour-Stepper-Musters (siehe
    // WeekTourStepper.vue) auf diesen Kurs, wo eine "Lektion" fuenf einzelne Lektionen statt eines
    // einzelnen Notebooks sind.
    const groupedLessons = computed(() => {
      const groups = [];
      lessons.value.forEach((lesson, idx) => {
        const section = lesson.section || 'lektion';
        const last = groups[groups.length - 1];
        if (last && last.section === section) {
          last.lessons.push(lesson);
        } else {
          groups.push({ section, startIndex: idx, lessons: [lesson] });
        }
      });
      return groups;
    });

    const currentBreadcrumbLabel = computed(() => {
      if (!currentLesson.value) return '';
      const group = groupedLessons.value.find((g) => g.lessons.some((l) => l.id === currentLesson.value.id));
      if (!group) return currentLesson.value.title;
      const label = t('lessons.section.' + group.section);
      if (group.lessons.length === 1) return label;
      const posInGroup = group.lessons.findIndex((l) => l.id === currentLesson.value.id) + 1;
      return `${label} ${posInGroup}`;
    });

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
          // Bei jedem (Neu-)Mount auf der ersten noch nicht abgeschlossenen Lektion weitermachen,
          // nicht immer bei Lektion 1 - sonst geht die Position verloren, sobald diese Komponente
          // neu gemountet wird (z.B. eingebettet in WeekTourStepper.vue: Glossar/Lösungen öffnen
          // und zurück wechselt den v-if-Zweig und damit die Komponenten-Instanz).
          const firstOpen = lessons.value.find((l) => !isCompleted(l.id));
          currentLessonId.value = (firstOpen || lessons.value[0]).id;
        }
      } catch (e) {
        console.error('Could not load lessons:', e);
        error.value = t('lessons.loadError');
      } finally {
        loading.value = false;
      }
    };

    // Freie Navigation: alle Lektionen sind von Anfang an anklickbar (z.B. zum Umschauen).
    const canOpen = (lesson) => props.freeNavigation || isLessonUnlocked(lesson.id, lessons.value);

    const choosingBranch = ref(false);

    const selectLesson = (lesson) => {
      if (!canOpen(lesson)) return;
      choosingBranch.value = false;
      currentLessonId.value = lesson.id;
    };

    const onLessonCompleted = (lessonId) => {
      const idx = lessons.value.findIndex((l) => l.id === lessonId);
      const cur = lessons.value[idx];
      const next = lessons.value[idx + 1];
      if (props.hasCheck && cur?.section === 'mission' && next?.section === 'boss') {
        choosingBranch.value = true;
        return;
      }
      if (next) currentLessonId.value = next.id;
      else if (props.hasCheck) emit('open-check');
    };

    const chooseBoss = () => {
      choosingBranch.value = false;
      const firstBoss = lessons.value.find((l) => l.section === 'boss');
      if (firstBoss) currentLessonId.value = firstBoss.id;
    };

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
        try { importSavedCode(props.contentPath, JSON.parse(reader.result).savedCode); } catch { /* Fortschritt zaehlt */ }
        if (result.ok) alert(t('lessons.importSuccess'));
        else alert(t('lessons.importFailed') + (result.error || t('jupyter.unknownError')));
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    const exportProgressFile = () => {
      // Fortschritt + (noch gueltiger) zwischengespeicherter Code, damit man ihn mitnehmen kann
      const data = JSON.parse(exportProgress());
      const savedCode = exportSavedCode(props.contentPath);
      if (Object.keys(savedCode).length) data.savedCode = savedCode;
      const json = JSON.stringify(data, null, 2);
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `${props.contentPath}-fortschritt.json`;
      a.click();
      URL.revokeObjectURL(a.href);
    };

    onMounted(loadLessons);

    return {
      t,
      lessons,
      loading,
      error,
      mainEl,
      currentLesson,
      groupedLessons,
      currentBreadcrumbLabel,
      completedCount,
      isCompleted,
      canOpen,
      choosingBranch,
      chooseBoss,
      selectLesson,
      onLessonCompleted,
      onImportFile,
      exportProgress: exportProgressFile,
    };
  },
};
</script>

<style scoped>
.js-course-tour {
  max-width: 900px;
  margin: 0 auto;
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

.tour-header-embedded {
  margin-bottom: 4px;
  font-size: 0.92em;
  color: #7c5a94;
  font-weight: 600;
}

.tour-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.tour-breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.92em;
  color: #7c5a94;
  font-weight: 600;
}

.breadcrumb-back {
  background: none;
  border: none;
  padding: 0;
  font: inherit;
  font-weight: 600;
  color: #7c5a94;
  cursor: pointer;
  text-decoration: underline;
}

.breadcrumb-back:hover {
  color: var(--primary-purple, #4a2274);
}

.breadcrumb-sep {
  color: #c4b5d0;
}

.breadcrumb-lesson {
  color: var(--primary-purple, #4a2274);
}

.progress-count {
  font-weight: 600;
  color: #28a745;
}

/* ── Fortschritts-Leiste (Kullern + Linien), gruppiert nach Abschnitt ──────── */
.progress-stepper {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  margin: 18px 0 8px;
  overflow-x: auto;
  scrollbar-width: none;
}
.progress-stepper::-webkit-scrollbar { display: none; }

.stepper-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

.stepper-group-label {
  font-size: 0.75em;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #9ca3af;
}

.stepper-group-dots {
  display: flex;
  align-items: center;
}

.stepper-group-gap {
  width: 1px;
  align-self: center;
  height: 20px;
  background: #e5e7eb;
  margin-top: 14px;
}

.stepper-step {
  display: flex;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}

.stepper-step:disabled {
  cursor: not-allowed;
}

.stepper-dot {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #d1d5db;
  background: white;
  color: #9ca3af;
  font-weight: 700;
  font-size: 0.85em;
  transition: all 0.15s ease;
}

.stepper-step.done .stepper-dot {
  background: var(--primary-purple, #4a2274);
  border-color: var(--primary-purple, #4a2274);
  color: white;
}

.stepper-step.current .stepper-dot {
  background: var(--accent-orange, #ff9800);
  border-color: var(--accent-orange, #ff9800);
  color: white;
  box-shadow: 0 0 0 4px #fff3e0;
}

.stepper-step.locked .stepper-dot {
  opacity: 0.5;
}

.stepper-line {
  width: 20px;
  height: 3px;
  background: #e5e7eb;
}
.stepper-line.done { background: var(--primary-purple, #4a2274); }

.lesson-main {
  margin-top: 12px;
}

.tour-actions {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
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
.btn-import:hover { background: #e9ecef; }

.file-input { display: none; }

.branch-choice-page {
  padding: 24px 8px;
  text-align: center;
}
.branch-tile-grid {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 16px;
}
.branch-tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  width: 240px;
  padding: 20px 16px;
  background: #fff;
  border: 2px solid #e6dcef;
  border-radius: 12px;
  cursor: pointer;
  font: inherit;
  color: inherit;
}
.branch-tile:hover { border-color: var(--primary-purple, #4a2274); background: #f7f1fb; }
.branch-tile-icon { font-size: 2em; }
.branch-tile-desc { font-size: 0.85em; color: #666; }
</style>
