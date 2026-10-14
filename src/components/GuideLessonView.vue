<template>
  <div class="lesson-view guide-lesson" :class="'modus-' + mode">
    <div v-if="hasVariants" class="guide-mode-switch" role="group" :aria-label="t('guide.modeLabel')">
      <span class="guide-mode-label">{{ t('guide.modeLabel') }}</span>
      <button
        v-for="m in MODES"
        :key="m"
        type="button"
        class="guide-mode-btn"
        :class="{ active: mode === m }"
        :data-mode="m"
        :aria-pressed="mode === m"
        @click="setMode(m)"
      >
        {{ t('guide.mode.' + m) }}
      </button>
    </div>

    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
      <div v-else v-html="guideHtml"></div>
    </div>

    <div v-if="tasks.length" class="lesson-editor-section guide-tasks">
      <p class="editor-hint">{{ t('guide.checkHint') }}</p>
      <label
        v-for="(task, idx) in tasks"
        :key="lesson.id + '-' + idx"
        class="guide-task"
        :class="{ 'guide-task-done': isChecked(idx) }"
      >
        <input
          type="checkbox"
          class="guide-task-check"
          :checked="isChecked(idx)"
          @change="toggleTask(idx, $event.target.checked)"
        />
        <span class="guide-task-text">
          <span v-if="task.isBonus" class="task-bonus-badge">Bonus</span>
          {{ task.instruction }}
        </span>
      </label>

      <div v-if="allTasksComplete" class="lesson-complete-box">
        <p class="lesson-summary">{{ lessonSummary }}</p>
        <ProjectCompletionBox v-if="isProjectCourse && isLastLesson" :next-course-id="lesson.nextCourseId" />
        <button v-else @click="goToNext" class="btn-next">{{ t('lesson.nextLesson') }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, computed, onMounted, onBeforeUnmount } from 'vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { useLessonContent } from '../composables/useLessonContent';
import ProjectCompletionBox from './ProjectCompletionBox.vue';

// Anzeige-Vorliebe (Bloecke oder Python), kein Fortschritt - bewusst nicht Teil des Syncs.
const MODE_KEY = 'ue-hacker-guide-mode';
const MODES = ['bloecke', 'python'];

function loadMode() {
  try {
    const saved = localStorage.getItem(MODE_KEY);
    return MODES.includes(saved) ? saved : MODES[0];
  } catch {
    return MODES[0];
  }
}

// Ein ```bloecke-Codeblock beschreibt MakeCode-Bloecke als Text: pro Zeile `[kategorie] Beschriftung`,
// zwei Leerzeichen Einrueckung je Verschachtelungsebene. Daraus werden farbige Block-Zeilen.
function renderBlocks(code) {
  const rows = code.replace(/\n$/, '').split('\n').filter((line) => line.trim()).map((line) => {
    const indent = Math.floor(line.match(/^ */)[0].length / 2);
    const m = line.trim().match(/^\[([a-z]+)\]\s*(.*)$/);
    const category = m ? m[1] : 'grundlagen';
    const label = m ? m[2] : line.trim();
    return `<div class="mc-block mc-${category}" style="margin-left:${indent * 24}px">${label}</div>`;
  });
  return `<div class="mc-blocks">${rows.join('')}</div>`;
}

// `:::bloecke` / `:::python` ... `:::` im Markdown (jeweils als eigener Absatz) grenzen Abschnitte ab,
// die nur in der gewaehlten Ansicht sichtbar sind.
function toGuideHtml(html) {
  return html
    .replace(/<pre><code class="language-bloecke">([\s\S]*?)<\/code><\/pre>/g, (_, code) => renderBlocks(code))
    .replace(/<p>:::(bloecke|python)<\/p>/g, '<div class="variante variante-$1">')
    .replace(/<p>:::<\/p>/g, '</div>');
}

export default {
  name: 'GuideLessonView',
  components: { ProjectCompletionBox },
  props: {
    lesson: { type: Object, required: true },
    contentPath: { type: String, required: true },
    variant: { type: String, required: true },
    courseId: { type: String, required: true },
    isProjectCourse: { type: Boolean, default: false },
    isLastLesson: { type: Boolean, default: false },
  },
  emits: ['completed'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const { markCompleted, unmarkCompleted, isCompleted, getPartialChecks, setPartialChecks } = useInteractiveProgress(props.variant, props.courseId);
    const isMounted = ref(true);
    const { lessonContent, loadContent } = useLessonContent(isMounted);

    const mode = ref(loadMode());
    const setMode = (m) => {
      mode.value = m;
      try {
        localStorage.setItem(MODE_KEY, m);
      } catch {
        // Ohne localStorage gilt die Wahl nur bis zum Neuladen.
      }
    };

    const guideHtml = computed(() => toGuideHtml(lessonContent.value));
    const hasVariants = computed(() => guideHtml.value.includes('class="variante '));

    const tasks = computed(() => (Array.isArray(props.lesson?.tasks) ? props.lesson.tasks : []));
    const requiredIdx = computed(() =>
      tasks.value.map((task, idx) => (task.isBonus ? -1 : idx)).filter((idx) => idx >= 0));
    const checked = ref(new Set());
    const isChecked = (idx) => checked.value.has(idx);

    const allTasksComplete = computed(() =>
      requiredIdx.value.length > 0 && requiredIdx.value.every((idx) => isChecked(idx)));

    // Haken kommen aus dem gespeicherten Stand (ohne Account nur einen Tag lang, siehe
    // useInteractiveProgress). Eine schon abgeschlossene Stufe zeigt in jedem Fall alle
    // Pflicht-Haken an - auch wenn Abschluss oder Haken erst per Sync nachkommen.
    watch(
      [() => props.lesson?.id, () => isCompleted(props.lesson.id), () => getPartialChecks(props.lesson.id).join(',')],
      ([id, done], [oldId]) => {
        const next = oldId === id ? new Set(checked.value) : new Set();
        getPartialChecks(id).forEach((idx) => next.add(idx));
        if (done) requiredIdx.value.forEach((idx) => next.add(idx));
        checked.value = next;
      },
      { immediate: true }
    );

    const toggleTask = (idx, value) => {
      const next = new Set(checked.value);
      if (value) next.add(idx);
      else next.delete(idx);
      checked.value = next;
      setPartialChecks(props.lesson.id, [...next]);
      // Ein zurückgenommener Pflicht-Haken nimmt auch den Abschluss der Stufe zurück.
      if (allTasksComplete.value) markCompleted(props.lesson.id);
      else unmarkCompleted(props.lesson.id);
    };

    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));
    const goToNext = () => emit('completed', props.lesson.id);

    watch(
      () => props.lesson?.id,
      () => loadContent(props.lesson, props.contentPath)
    );

    onMounted(() => loadContent(props.lesson, props.contentPath));
    onBeforeUnmount(() => {
      isMounted.value = false;
    });

    return {
      lang,
      t,
      MODES,
      mode,
      setMode,
      lessonContent,
      guideHtml,
      hasVariants,
      tasks,
      isChecked,
      toggleTask,
      allTasksComplete,
      lessonSummary,
      goToNext,
    };
  },
};
</script>

<style scoped>
.lesson-view {
  max-width: 800px;
  margin: 0 auto;
}

.guide-mode-switch {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
}

.guide-mode-label {
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.guide-mode-btn {
  padding: 6px 16px;
  border: 2px solid var(--primary-purple, #4a2274);
  border-radius: 20px;
  background: #fff;
  color: var(--primary-purple, #4a2274);
  font-weight: 600;
  cursor: pointer;
}

.guide-mode-btn.active {
  background: var(--primary-purple, #4a2274);
  color: #fff;
}

.lesson-content {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 20px;
  line-height: 1.6;
}

.lesson-loading {
  color: #6c757d;
  font-style: italic;
}

.lesson-content :deep(h1) {
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 1em;
  border-bottom: 2px solid var(--accent-yellow, #fdd835);
  padding-bottom: 0.3em;
}

.lesson-content :deep(h2) {
  font-size: 1.2em;
  margin-top: 1.2em;
  margin-bottom: 0.5em;
}

.lesson-content :deep(code) {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

.lesson-content :deep(pre) {
  background: #f8f9fa;
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}

.lesson-content :deep(pre code) {
  background: none;
  padding: 0;
}

.lesson-content :deep(blockquote) {
  margin: 12px 0;
  padding: 8px 14px;
  border-left: 4px solid var(--accent-orange, #ff9800);
  background: #fff8e1;
  border-radius: 0 6px 6px 0;
}

.lesson-content :deep(blockquote p) {
  margin: 4px 0;
}

.lesson-content :deep(table) {
  border-collapse: collapse;
  margin: 12px 0;
}

.lesson-content :deep(th),
.lesson-content :deep(td) {
  border: 1px solid #dee2e6;
  padding: 6px 10px;
  text-align: left;
}

.lesson-content :deep(details) {
  margin: 12px 0;
  padding: 10px 14px;
  border: 1px dashed var(--primary-purple, #4a2274);
  border-radius: 6px;
  background: #faf7fd;
}

.lesson-content :deep(summary) {
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
  cursor: pointer;
}

.modus-bloecke .lesson-content :deep(.variante-python),
.modus-python .lesson-content :deep(.variante-bloecke) {
  display: none;
}

.lesson-content :deep(.mc-blocks) {
  margin: 12px 0;
  padding: 12px;
  background: #f8f9fa;
  border-radius: 6px;
  overflow-x: auto;
}

.lesson-content :deep(.mc-block) {
  width: fit-content;
  margin-top: 3px;
  padding: 6px 12px;
  border-radius: 6px;
  color: #fff;
  font-weight: 600;
  font-size: 0.9em;
  white-space: nowrap;
  background: #1e90ff;
}

/* Farben wie die Kategorien in der MakeCode-Werkzeugleiste. */
.lesson-content :deep(.mc-grundlagen) { background: #1e90ff; }
.lesson-content :deep(.mc-eingabe) { background: #d400d4; }
.lesson-content :deep(.mc-schleifen) { background: #00aa00; }
.lesson-content :deep(.mc-logik) { background: #00a4a6; }
.lesson-content :deep(.mc-variablen) { background: #dc143c; }
.lesson-content :deep(.mc-mathematik) { background: #9400d3; }
.lesson-content :deep(.mc-minicar) { background: #aa278d; }
.lesson-content :deep(.mc-funktionen) { background: #3455db; }
.lesson-content :deep(.mc-musik) { background: #e63022; }

.lesson-editor-section {
  background: #f8f9fa;
  border: 2px solid var(--primary-purple, #4a2274);
  border-radius: 8px;
  padding: 20px;
}

.editor-hint {
  margin: 0 0 12px 0;
  font-size: 0.9em;
  color: #555;
}

.guide-task {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  margin-bottom: 8px;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  cursor: pointer;
  line-height: 1.4;
}

.guide-task-done {
  background: #eaf7ed;
  border-color: #c3e6cb;
}

.guide-task-check {
  flex: none;
  width: 22px;
  height: 22px;
  margin: 0;
  accent-color: #28a745;
}

.task-bonus-badge {
  display: inline-block;
  background: var(--accent-orange, #ff9800);
  color: white;
  font-size: 0.72em;
  font-weight: 700;
  padding: 1px 7px;
  border-radius: 10px;
  margin-right: 6px;
  vertical-align: middle;
  letter-spacing: 0.03em;
}

.lesson-complete-box {
  margin-top: 24px;
  padding: 20px;
  background: #d4edda;
  border: 1px solid #c3e6cb;
  border-radius: 8px;
}

.lesson-summary {
  margin: 0 0 16px 0;
  font-size: 1.05em;
  color: #155724;
  font-weight: 500;
}

.btn-next {
  padding: 10px 24px;
  background: var(--primary-purple, #4a2274);
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}
</style>
