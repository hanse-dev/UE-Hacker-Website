<template>
  <div ref="rootEl" class="lesson-view spiel-lesson" :class="'modus-' + mode">
    <div class="spiel-mode-switch" role="group" :aria-label="t('spiel.modeLabel')">
      <span class="spiel-mode-label">{{ t('spiel.modeLabel') }}</span>
      <button
        v-for="m in MODES"
        :key="m"
        type="button"
        class="spiel-mode-btn"
        :class="{ active: mode === m }"
        :data-mode="m"
        :aria-pressed="mode === m"
        @click="setMode(m)"
      >
        {{ t('guide.mode.' + m) }}
      </button>
    </div>

    <div class="spiel-grid">
      <div class="lesson-content">
        <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
        <div v-else v-lerntext="contentHtml"></div>
        <ConceptBox v-if="lessonContent && conceptList.length" :concepts="conceptList" />
      </div>

      <div class="lesson-editor-section">
        <p class="editor-hint">{{ t('spiel.editorHint') }}</p>
        <p v-if="!kernelReady" class="editor-hint spiel-kernel">{{ kernelStatus || t('spiel.kernelStarting') }}</p>

        <template v-for="(task, idx) in tasks" :key="lesson.id + '-' + idx">
          <div
            class="task-block"
            :class="[task.example ? 'task-example' : 'task-required', { 'task-active': activeIdx === idx }]"
            :style="{ order: 10 + idx * 2 }"
          >
            <span class="task-badge" :class="task.example ? 'badge-example' : 'badge-required'">
              {{ task.example ? t('spiel.badgeExample') : t('jsLesson.badgeRequired') }}
            </span>
            <p class="task-instruction">
              <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
              <span v-else-if="skippedTasks.has(idx)" class="task-skipped">⏭</span>
              <span v-else class="task-pending">○</span>
              <span v-if="task.isBonus" class="task-bonus-badge">Bonus</span>
              <span v-lerntext="instructionWithGlossary(instructionFor(task) || t('lesson.taskPrefix') + (idx + 1))"></span>
              <span v-if="completedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskDone') }}</span>
              <span v-else-if="skippedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskSkipped') }}</span>
            </p>

            <div v-if="mode === 'bloecke'" class="spiel-bloecke-wrapper">
              <p v-if="bloeckeFehler[idx]" class="feedback feedback-error">{{ bloeckeFehler[idx] }}</p>
              <p v-else-if="!bloeckeInhalt[idx]" class="spiel-warten">{{ t('spiel.blocksLoading') }}</p>
              <SpielBloecke
                v-else
                :key="lesson.id + '-' + idx + '-' + bloeckeVersion[idx]"
                :inhalt="bloeckeInhalt[idx]"
                @aenderung="onBloeckeAenderung(idx, $event)"
                @bereit="bloeckePython[idx] = $event.python"
              />
              <details class="spiel-python-ansehen">
                <summary>{{ t('spiel.showPython') }}</summary>
                <pre class="solution-code">{{ bloeckePython[idx] }}</pre>
              </details>
            </div>
            <div v-else class="code-editor-wrapper">
              <CodeCell v-model="taskCodes[idx]" />
            </div>

            <div class="editor-actions">
              <button
                v-if="laeuftIdx !== idx"
                type="button"
                class="btn-run btn-spielen"
                :disabled="!kernelReady || checking"
                @click="spiele(idx)"
              >
                ▶ {{ t('spiel.play') }}
              </button>
              <button v-else type="button" class="btn-run btn-stopp" @click="stoppeSpiel">
                ■ {{ t('spiel.stop') }}
              </button>
              <button
                v-if="!task.example"
                type="button"
                class="btn-check"
                :disabled="(!kernelReady && !devSkipChecks) || checking"
                @click="checkTask(idx)"
              >
                {{ checking ? t('editor.checking') : t('editor.check') }}
              </button>
              <button
                v-if="!task.example && !isTaskDone(idx) && (taskAttempts[idx] || 0) >= 2"
                type="button"
                class="btn-skip"
                :disabled="checking"
                @click="skipTask(idx)"
              >
                {{ t('lesson.skipTask') }}
              </button>
              <button
                v-if="isChanged(idx)"
                type="button"
                class="btn-reset"
                :disabled="checking"
                @click="resetTask(idx)"
              >
                {{ t('editor.reset') }}
              </button>
            </div>

            <details v-if="task.solution" class="solution-reveal" @toggle="onSolutionToggle($event, idx)">
              <summary>{{ t('jsLesson.showSolution') }}</summary>
              <template v-if="mode === 'bloecke'">
                <SpielBloecke v-if="loesungBloecke[idx]" :inhalt="loesungBloecke[idx]" read-only :hoehe="320" />
              </template>
              <pre v-else class="solution-code">{{ task.solution }}</pre>
            </details>

            <div v-if="taskOutputs[idx]" class="output-display">
              <strong>{{ t('editor.output') }}</strong>
              <pre class="output-content">{{ taskOutputs[idx] }}</pre>
            </div>
            <p v-if="runOnly[idx] && !task.example && !isTaskDone(idx)" class="run-then-check">💡 {{ t('spiel.runThenCheck') }}</p>
            <div v-if="taskFeedback[idx]" :class="['feedback', taskFeedback[idx].success ? 'feedback-success' : 'feedback-error']">
              {{ taskFeedback[idx].message }}
              <button
                v-if="taskFeedback[idx].success && !allTasksComplete && nextOpenTask(tasks, isTaskDone, idx) >= 0"
                type="button"
                class="btn-next-task"
                @click="goToTask(nextOpenTask(tasks, isTaskDone, idx))"
              >
                {{ t('lesson.nextTask').replace('{n}', nextOpenTask(tasks, isTaskDone, idx) + 1) }}
              </button>
            </div>
          </div>
        </template>

        <!-- Buehne: EINE fuer die ganze Lektion. Breit rechts als mitlaufende Spalte, schmal per
             CSS-`order` unter der zuletzt gespielten Aufgabe (wie die Arbeitsflaeche in JsLessonView). -->
        <div class="spiel-buehne" :style="{ order: activeIdx === null ? 9998 : 11 + activeIdx * 2 }">
          <div class="spiel-buehne-inner">
            <p class="spiel-buehne-titel">
              {{ t('spiel.stage') }}<span v-if="activeIdx !== null" class="spiel-buehne-aufgabe"> · {{ t('jsLesson.workspaceTask').replace('{n}', activeIdx + 1) }}</span>
            </p>
            <canvas
              ref="canvasEl"
              class="spiel-canvas"
              width="400"
              height="400"
              tabindex="0"
              :aria-label="t('spiel.stage')"
              @keydown="onTaste($event, true)"
              @keyup="onTaste($event, false)"
              @blur="gedrueckt.clear()"
            ></canvas>
            <div class="spiel-tasten" :aria-label="t('spiel.touchKeys')">
              <button
                v-for="k in TOUCH_TASTEN"
                :key="k.name"
                type="button"
                class="spiel-taste"
                :data-taste="k.name"
                @pointerdown.prevent="gedrueckt.add(k.name)"
                @pointerup="gedrueckt.delete(k.name)"
                @pointerleave="gedrueckt.delete(k.name)"
                @pointercancel="gedrueckt.delete(k.name)"
              >
                {{ k.zeichen }}
              </button>
            </div>
            <p class="spiel-buehne-hinweis">{{ laeuftIdx !== null ? t('spiel.keysHint') : t('spiel.stageEmpty') }}</p>
          </div>
        </div>

        <div v-if="allTasksComplete" class="lesson-complete-box" :style="{ order: 99999 }">
          <p class="lesson-summary">{{ lessonSummary }}</p>
          <ProjectCompletionBox v-if="isProjectCourse && isLastLesson" :next-course-id="lesson.nextCourseId" />
          <button v-else @click="goToNext" class="btn-next">{{ t('lesson.nextLesson') }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, computed, onMounted, onBeforeUnmount } from 'vue';
import CodeCell from './CodeCell.vue';
import SpielBloecke from './SpielBloecke.vue';
import ProjectCompletionBox from './ProjectCompletionBox.vue';
import ConceptBox from './ConceptBox.vue';
import { usePyodide } from '../composables/usePyodide';
import { useSpiel, spielFehlertext } from '../composables/useSpiel';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { useLessonContent } from '../composables/useLessonContent';
import { validateSpiel } from '../composables/useTaskValidation';
import { DEV_SKIP_CHECKS } from '../composables/devSkipChecks.js';
import { loadSavedCode, saveLessonCode } from '../composables/useSavedCode';
import { conceptsInText, mergeConcepts } from '../composables/useConcepts';
import { reportLessonOpen, reportTaskEvent } from '../composables/useTaskStats';
import { nextOpenTask, focusTask } from '../composables/useTaskFlow';
import { renderBlockListings } from '../utils/bloeckeListing';

// Ansicht Bloecke/Python: dieselbe gemerkte Wahl wie bei den micro:bit-Anleitungen
// (GuideLessonView.vue) - wer dort Bloecke nimmt, startet hier auch mit Bloecken. Nur Anzeige,
// kein Fortschritt: eine Aufgabe gilt als geloest, egal in welcher Ansicht sie geprueft wurde.
const MODE_KEY = 'ue-hacker-guide-mode';
const MODES = ['bloecke', 'python'];
const TASTEN_CODES = { ArrowLeft: 'links', ArrowRight: 'rechts', ArrowUp: 'oben', ArrowDown: 'unten', ' ': 'leertaste' };
const TOUCH_TASTEN = [
  { name: 'links', zeichen: '←' },
  { name: 'oben', zeichen: '↑' },
  { name: 'unten', zeichen: '↓' },
  { name: 'rechts', zeichen: '→' },
];

function loadMode() {
  try {
    const saved = localStorage.getItem(MODE_KEY);
    return MODES.includes(saved) ? saved : MODES[0];
  } catch {
    return MODES[0];
  }
}

export default {
  name: 'SpielLessonView',
  components: { CodeCell, SpielBloecke, ProjectCompletionBox, ConceptBox },
  props: {
    lesson: { type: Object, required: true },
    contentPath: { type: String, required: true },
    variant: { type: String, required: true },
    courseId: { type: String, required: true },
    isProjectCourse: { type: Boolean, default: false },
    isLastLesson: { type: Boolean, default: false },
    conceptLanguage: { type: String, default: '' },
  },
  emits: ['completed'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const { kernelReady, kernelStatus, initializeKernel } = usePyodide();
    const { starte, stoppe, pruefe, zuBloecken, zeichneLeer } = useSpiel();
    const { markCompleted } = useInteractiveProgress(props.variant, props.courseId);
    const conceptOptions = computed(() => (props.conceptLanguage && lang.value !== 'en'
      ? { language: props.conceptLanguage }
      : null));
    const isMounted = ref(true);
    const { lessonContent, lessonConcepts, loadGlossary, loadContent, instructionWithGlossary } = useLessonContent(
      isMounted,
      { conceptOptions: () => conceptOptions.value },
    );

    const savedMode = ref(loadMode());
    const mode = computed(() => savedMode.value);
    const setMode = (m) => {
      savedMode.value = m;
      try {
        localStorage.setItem(MODE_KEY, m);
      } catch {
        // Ohne localStorage gilt die Wahl nur bis zum Neuladen.
      }
    };

    // `:::bloecke` / `:::python` ... `:::` im Markdown grenzen Abschnitte ab, die nur eine Ansicht zeigt.
    const contentHtml = computed(() => renderBlockListings(lessonContent.value || '')
      .replace(/<p>:::(bloecke|python)<\/p>/g, '<div class="variante variante-$1">')
      .replace(/<p>:::<\/p>/g, '</div>'));

    const tasks = computed(() => props.lesson?.tasks || []);
    const instructionFor = (task) => (mode.value === 'bloecke' && task.instructionBloecke) || task.instruction;
    const conceptList = computed(() => (conceptOptions.value
      ? mergeConcepts(lessonConcepts.value, ...tasks.value.map((task) => conceptsInText(task.instruction, conceptOptions.value)))
      : []));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const taskAttempts = ref([]);
    const runOnly = ref([]);
    const completedTasks = ref(new Set());
    const skippedTasks = ref(new Set());
    const checking = ref(false);
    const activeIdx = ref(null);
    const laeuftIdx = ref(null);
    const rootEl = ref(null);
    const canvasEl = ref(null);
    const gedrueckt = new Set();

    // Bloecke je Aufgabe: Inhalt zum Laden (gespeichert oder aus der Python-Vorlage erzeugt), der
    // zuletzt gespeicherte Stand (fuer useSavedCode) und das daraus erzeugte Python.
    const bloeckeInhalt = ref([]);
    const bloeckeVorlage = ref([]);
    const bloeckeGespeichert = ref([]);
    const bloeckePython = ref([]);
    const bloeckeVersion = ref([]);
    const bloeckeFehler = ref([]);
    const loesungBloecke = ref([]);
    const bloeckePfad = computed(() => `${props.contentPath}-bloecke`);

    const isTaskDone = (idx) => completedTasks.value.has(idx) || skippedTasks.value.has(idx);
    const doneCount = computed(() => new Set([...completedTasks.value, ...skippedTasks.value]).size);
    const allTasksComplete = computed(() => tasks.value.length > 0 && doneCount.value === tasks.value.length);
    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));
    const goToTask = (idx) => focusTask(rootEl.value, idx);

    const codeFor = (idx) => (mode.value === 'bloecke' ? bloeckePython.value[idx] || '' : taskCodes.value[idx] || '');
    const isChanged = (idx) => (mode.value === 'bloecke'
      ? !!bloeckeGespeichert.value[idx]
      : taskCodes.value[idx] !== (tasks.value[idx]?.codeTemplate ?? ''));

    const stoppeSpiel = () => {
      stoppe();
      laeuftIdx.value = null;
      gedrueckt.clear();
    };

    const vorlagenBloecke = async () => {
      const lessonId = props.lesson?.id;
      const gespeichert = loadSavedCode(bloeckePfad.value)[lessonId]?.codes || [];
      for (const [idx, task] of tasks.value.entries()) {
        try {
          const vorlage = await zuBloecken(task.codeTemplate || 'from spiel import *\n');
          if (props.lesson?.id !== lessonId) return;
          bloeckeVorlage.value[idx] = vorlage;
          bloeckeInhalt.value[idx] = gespeichert[idx] || vorlage;
          bloeckeGespeichert.value[idx] = gespeichert[idx] || '';
        } catch (e) {
          bloeckeFehler.value[idx] = t('spiel.blocksError') + spielFehlertext(e);
        }
      }
    };

    const initTaskState = () => {
      stoppeSpiel();
      const list = tasks.value;
      const templates = list.map((x) => x.codeTemplate ?? '');
      const saved = loadSavedCode(props.contentPath)[props.lesson?.id];
      taskCodes.value = saved && saved.codes.length === templates.length ? [...saved.codes] : templates;
      taskOutputs.value = list.map(() => '');
      taskFeedback.value = list.map(() => null);
      taskAttempts.value = list.map(() => 0);
      runOnly.value = list.map(() => false);
      bloeckeInhalt.value = list.map(() => '');
      bloeckeVorlage.value = list.map(() => '');
      bloeckeGespeichert.value = list.map(() => '');
      bloeckePython.value = list.map(() => '');
      bloeckeVersion.value = list.map(() => 0);
      bloeckeFehler.value = list.map(() => '');
      loesungBloecke.value = list.map(() => '');
      completedTasks.value = new Set();
      skippedTasks.value = new Set();
      activeIdx.value = null;
      if (canvasEl.value) zeichneLeer(canvasEl.value);
      if (kernelReady.value) vorlagenBloecke();
    };

    const onBloeckeAenderung = (idx, { json, python }) => {
      bloeckePython.value[idx] = python;
      bloeckeGespeichert.value[idx] = json;
      runOnly.value[idx] = false;
      saveLessonCode(bloeckePfad.value, props.lesson.id, bloeckeGespeichert.value, tasks.value.map(() => ''));
    };

    watch(taskCodes, (codes) => {
      if (!props.lesson?.id || !codes.length) return;
      saveLessonCode(props.contentPath, props.lesson.id, codes, tasks.value.map((x) => x.codeTemplate ?? ''));
    }, { deep: true });

    watch(kernelReady, (bereit) => {
      if (bereit) vorlagenBloecke();
    });

    watch(() => props.lesson, (neu) => {
      initTaskState();
      loadContent(neu, props.contentPath);
      reportLessonOpen(props.contentPath, neu);
    }, { immediate: true });

    const markExampleDone = (idx) => {
      if (completedTasks.value.has(idx)) return;
      completedTasks.value = new Set([...completedTasks.value, idx]);
      if (allTasksComplete.value) markCompleted(props.lesson.id);
    };

    const spiele = async (idx) => {
      if (!kernelReady.value || !canvasEl.value) return;
      stoppeSpiel();
      activeIdx.value = idx;
      taskOutputs.value[idx] = '';
      taskFeedback.value[idx] = null;
      const ergebnis = await starte(codeFor(idx), canvasEl.value, () => [...gedrueckt], (fehler) => {
        laeuftIdx.value = null;
        if (fehler) taskOutputs.value[idx] = t('editor.errorPrefix') + fehler;
      });
      if (!isMounted.value) return;
      if (!ergebnis.success) {
        taskOutputs.value[idx] = t('editor.errorPrefix') + spielFehlertext(ergebnis.error);
        return;
      }
      taskOutputs.value[idx] = ergebnis.output || '';
      runOnly.value[idx] = true;
      if (ergebnis.laeuft) {
        laeuftIdx.value = idx;
        canvasEl.value.focus({ preventScroll: true });
      }
      if (tasks.value[idx]?.example) markExampleDone(idx);
    };

    const onTaste = (event, gedrueckt_) => {
      const name = TASTEN_CODES[event.key];
      if (!name) return;
      event.preventDefault();
      if (gedrueckt_) gedrueckt.add(name);
      else gedrueckt.delete(name);
    };

    const checkTask = async (idx) => {
      if (!kernelReady.value && !DEV_SKIP_CHECKS) return;
      stoppeSpiel();
      checking.value = true;
      taskFeedback.value[idx] = null;
      runOnly.value[idx] = false;
      const validation = tasks.value[idx]?.validation;
      const ergebnis = DEV_SKIP_CHECKS ? { ok: true } : await pruefe(codeFor(idx), validation?.checks || []);
      if (!isMounted.value) return;
      checking.value = false;
      if (ergebnis.output) taskOutputs.value[idx] = ergebnis.output;
      const res = validateSpiel(validation, ergebnis);

      if (res.ok) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
        reportTaskEvent(props.contentPath, props.lesson?.id, idx, 'solved');
        if (skippedTasks.value.has(idx)) {
          const next = new Set(skippedTasks.value);
          next.delete(idx);
          skippedTasks.value = next;
        }
        if (allTasksComplete.value) {
          markCompleted(props.lesson.id);
          taskFeedback.value[idx] = { success: true, message: t('lesson.allTasksDone') };
        } else {
          taskFeedback.value[idx] = {
            success: true,
            message: t('lesson.taskDoneRemaining').replace('{n}', idx + 1).replace('{r}', tasks.value.length - doneCount.value),
          };
        }
        return;
      }

      taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
      reportTaskEvent(props.contentPath, props.lesson?.id, idx, 'fail');
      let message;
      if (ergebnis.schritt === -1) message = t('editor.errorPrefix') + spielFehlertext(res.error);
      else if (res.error) message = t('spiel.errorInGame') + spielFehlertext(res.error);
      else message = res.hint || t('lesson.hintSoft');
      taskFeedback.value[idx] = { success: false, message };
    };

    const skipTask = (idx) => {
      if (isTaskDone(idx)) return;
      skippedTasks.value = new Set([...skippedTasks.value, idx]);
      taskFeedback.value[idx] = null;
      reportTaskEvent(props.contentPath, props.lesson?.id, idx, 'skip');
      if (allTasksComplete.value) markCompleted(props.lesson.id);
    };

    const resetTask = (idx) => {
      if (laeuftIdx.value === idx) stoppeSpiel();
      if (mode.value === 'bloecke') {
        bloeckeGespeichert.value[idx] = '';
        bloeckeInhalt.value[idx] = bloeckeVorlage.value[idx];
        bloeckeVersion.value[idx] += 1;
        saveLessonCode(bloeckePfad.value, props.lesson.id, bloeckeGespeichert.value, tasks.value.map(() => ''));
      } else {
        taskCodes.value[idx] = tasks.value[idx]?.codeTemplate ?? '';
      }
      taskOutputs.value[idx] = '';
      taskFeedback.value[idx] = null;
      runOnly.value[idx] = false;
    };

    const onSolutionToggle = async (event, idx) => {
      if (!event.target.open) return;
      reportTaskEvent(props.contentPath, props.lesson?.id, idx, 'solution');
      if (mode.value === 'bloecke' && !loesungBloecke.value[idx] && kernelReady.value) {
        try {
          loesungBloecke.value[idx] = await zuBloecken(tasks.value[idx].solution);
        } catch (e) {
          console.error('Loesung nicht als Bloecke darstellbar:', e);
        }
      }
    };

    // Ansicht gewechselt: ein laufendes Spiel gehoert zur alten Ansicht.
    watch(mode, () => stoppeSpiel());

    onMounted(() => {
      initializeKernel();
      loadGlossary(props.contentPath);
      if (canvasEl.value) zeichneLeer(canvasEl.value);
    });

    onBeforeUnmount(() => {
      isMounted.value = false;
      stoppeSpiel();
    });

    const goToNext = () => emit('completed', props.lesson.id);

    return {
      t,
      MODES,
      TOUCH_TASTEN,
      mode,
      setMode,
      lessonContent,
      contentHtml,
      conceptList,
      tasks,
      instructionFor,
      instructionWithGlossary,
      kernelReady,
      kernelStatus,
      devSkipChecks: DEV_SKIP_CHECKS,
      taskCodes,
      taskOutputs,
      taskFeedback,
      taskAttempts,
      runOnly,
      completedTasks,
      skippedTasks,
      checking,
      activeIdx,
      laeuftIdx,
      rootEl,
      canvasEl,
      gedrueckt,
      bloeckeInhalt,
      bloeckePython,
      bloeckeVersion,
      bloeckeFehler,
      loesungBloecke,
      isTaskDone,
      isChanged,
      allTasksComplete,
      lessonSummary,
      nextOpenTask,
      goToTask,
      onBloeckeAenderung,
      spiele,
      stoppeSpiel,
      onTaste,
      checkTask,
      skipTask,
      resetTask,
      onSolutionToggle,
      goToNext,
    };
  },
};
</script>

<style scoped>
.lesson-view {
  max-width: 1320px;
  margin: 0 auto;
  container-type: inline-size;
}

.spiel-mode-switch {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}

.spiel-mode-label {
  font-weight: 600;
  color: var(--text-muted);
}

.spiel-mode-btn {
  border: 2px solid var(--brand-text);
  background: var(--surface);
  color: var(--brand-text);
  border-radius: 999px;
  padding: 6px 16px;
  font-weight: 600;
  cursor: pointer;
}

.spiel-mode-btn.active {
  background: var(--primary-purple);
  border-color: var(--primary-purple);
  color: var(--text-light);
}

.spiel-grid {
  position: relative;
}

/* Abschnitte nur fuer eine Ansicht (`:::bloecke` / `:::python` im Markdown). */
.modus-bloecke .lesson-content :deep(.variante-python),
.modus-python .lesson-content :deep(.variante-bloecke) {
  display: none;
}

.lesson-content {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 20px;
  line-height: 1.6;
}

.lesson-loading {
  color: var(--text-muted);
  font-style: italic;
}

.lesson-content :deep(h1) {
  font-size: 1.5em;
  margin-top: 0;
  margin-bottom: 1em;
  border-bottom: 2px solid var(--accent-yellow);
  padding-bottom: 0.3em;
}

.lesson-content :deep(h2) {
  font-size: 1.2em;
  margin-top: 1em;
  margin-bottom: 0.5em;
}

.lesson-content :deep(code) {
  background: var(--surface-muted);
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

.lesson-content :deep(pre) {
  background: var(--surface-muted);
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}

.lesson-content :deep(pre code) {
  padding: 0;
}

.lesson-content :deep(img) {
  max-width: 100%;
  height: auto;
}

.lesson-content :deep(.mc-blocks) {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 3px;
  margin: 0.5em 0 1em;
}

/* Block-Listings (```bloecke im Markdown): Farben wie die Kategorien im Werkzeugkasten
   (src/spiel/bloecke.js) - wie Sandbox-Inhalte unabhaengig vom Theme. */
.lesson-content :deep(.mc-block) {
  padding: 4px 10px;
  border-radius: 6px;
  color: #fff;
  font-size: 0.9em;
  font-weight: 600;
}

.lesson-content :deep(.mc-spiel) { background: #d97706; }
.lesson-content :deep(.mc-figuren) { background: #2563eb; }
.lesson-content :deep(.mc-aktion) { background: #7c3aed; }
.lesson-content :deep(.mc-logik) { background: #5b80a5; }
.lesson-content :deep(.mc-schleifen) { background: #5ba55b; }
.lesson-content :deep(.mc-rechnen) { background: #5b67a5; }
.lesson-content :deep(.mc-text) { background: #5ba58c; }
.lesson-content :deep(.mc-listen) { background: #745ba5; }
.lesson-content :deep(.mc-variablen) { background: #a55b80; }

.lesson-content :deep(.concept-link) {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px dotted var(--brand-text);
}

.lesson-content :deep(.concept-link)::after {
  content: '↗';
  font-size: 0.75em;
  margin-left: 1px;
  color: var(--brand-text);
}

.lesson-editor-section {
  display: flex;
  flex-direction: column;
  background: var(--surface-muted);
  border: 2px solid var(--brand-text);
  border-radius: 8px;
  padding: 20px;
}

.editor-hint {
  margin: 0 0 12px 0;
  font-size: 0.9em;
  color: var(--text-muted);
}

.spiel-kernel {
  color: var(--brand-text);
  font-weight: 600;
}

.task-block {
  margin-bottom: 24px;
  padding-bottom: 24px;
  padding-left: 14px;
  border-bottom: 1px solid var(--border);
  border-left: 4px solid transparent;
}

.task-block.task-required {
  border-left-color: var(--task-accent);
}

.task-block.task-example {
  border-left-color: var(--example-accent);
}

.task-badge {
  display: inline-block;
  margin-bottom: 6px;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.72em;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}

.badge-example {
  background: var(--example-badge-bg);
  color: var(--example-badge-text);
}

.badge-required {
  background: var(--task-badge-bg);
  color: var(--task-badge-text);
}

.task-instruction {
  display: block;
  font-weight: 600;
  color: var(--brand-text);
  margin: 0 0 8px 0;
  font-size: 0.95em;
  line-height: 1.4;
}

.task-done {
  color: var(--success);
  margin-right: 6px;
}

.task-pending {
  color: var(--text-faint);
  margin-right: 6px;
}

.task-skipped {
  color: var(--accent-orange);
  margin-right: 6px;
}

.task-bonus-badge {
  display: inline-block;
  margin-right: 6px;
  padding: 1px 8px;
  border-radius: 10px;
  background: var(--warning-bg);
  color: var(--warning-text);
  font-size: 0.8em;
}

.task-status-label {
  margin-left: 0.35em;
  font-weight: 400;
  color: var(--text-muted);
  font-size: 0.9em;
}

.spiel-warten {
  color: var(--text-muted);
  font-style: italic;
}

.spiel-python-ansehen {
  margin: 8px 0 12px;
}

.spiel-python-ansehen summary,
.solution-reveal summary {
  cursor: pointer;
  padding: 6px 0;
  font-weight: 600;
  font-size: 0.85em;
  color: var(--brand-text);
  user-select: none;
}

.solution-reveal {
  margin: 0 0 12px 0;
  padding: 0 12px;
  border: 1px dashed var(--border-tint);
  border-radius: 6px;
  background: var(--surface-tint);
}

.solution-reveal :deep(.spiel-bloecke) {
  margin-bottom: 12px;
}

.solution-code {
  margin: 0 0 12px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 0.85em;
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--text);
}

.code-editor-wrapper {
  margin-bottom: 12px;
}

.editor-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin: 12px 0;
}

.btn-run,
.btn-check,
.btn-skip,
.btn-reset {
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  color: white;
}

.btn-run {
  background: var(--success);
}

.btn-stopp {
  background: var(--danger);
}

.btn-check {
  background: var(--primary-purple);
}

.btn-skip,
.btn-reset {
  background: var(--surface);
  color: var(--text-muted);
  border: 1px solid var(--border-strong);
  font-size: 14px;
  padding: 8px 14px;
}

.btn-run:disabled,
.btn-check:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.output-display {
  margin: 0 0 12px;
  padding: 10px 12px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
}

.output-content {
  margin: 6px 0 0;
  white-space: pre-wrap;
  font-size: 0.9em;
}

.run-then-check {
  margin: 0 0 8px;
  font-size: 0.9em;
  color: var(--text-muted);
}

.feedback {
  padding: 10px 12px;
  border-radius: 6px;
  margin: 0 0 8px;
}

.feedback-success {
  background: var(--success-bg);
  color: var(--success-text);
  border: 1px solid var(--success-border);
}

.feedback-error {
  background: var(--danger-bg);
  color: var(--danger-text);
  border: 1px solid var(--danger-border);
}

.btn-next-task,
.btn-next {
  display: block;
  margin-top: 10px;
  background: var(--primary-purple);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.lesson-complete-box {
  margin-top: 24px;
  padding: 20px;
  background: var(--success-bg);
  border: 1px solid var(--success-border);
  border-radius: 8px;
}

.lesson-summary {
  margin: 0 0 16px 0;
  font-size: 1.05em;
  color: var(--success-text);
  font-weight: 500;
}

/* Buehne: schmal unter der aktiven Aufgabe, breit als mitlaufende Spalte rechts. */
.spiel-buehne {
  margin: -8px 0 24px 0;
}

.spiel-buehne-inner {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
}

.spiel-buehne-titel {
  margin: 0 0 8px 0;
  font-weight: 600;
  color: var(--brand-text);
}

.spiel-buehne-aufgabe {
  font-weight: 400;
  color: var(--text-muted);
}

.spiel-canvas {
  display: block;
  width: 100%;
  max-width: 400px;
  aspect-ratio: 1;
  border-radius: 6px;
  outline: none;
  /* Sandbox-Inhalt: feste Farbe vor dem ersten Bild, unabhaengig vom Theme (HANDOFF 3.122). */
  background: #0f172a;
}

.spiel-canvas:focus-visible {
  box-shadow: 0 0 0 3px var(--accent-blue);
}

.spiel-tasten {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.spiel-taste {
  flex: 1;
  max-width: 92px;
  padding: 10px 0;
  font-size: 20px;
  border: 1px solid var(--border-strong);
  border-radius: 8px;
  background: var(--surface-muted);
  color: var(--text);
  cursor: pointer;
  touch-action: none;
  user-select: none;
}

.spiel-buehne-hinweis {
  margin: 8px 0 0;
  font-size: 0.85em;
  color: var(--text-muted);
}

@container (min-width: 920px) {
  .spiel-grid {
    padding-right: 446px;
  }

  .spiel-buehne {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    width: 426px;
    margin: 0;
  }

  .spiel-buehne-inner {
    position: sticky;
    top: 16px;
  }

  .spiel-tasten {
    display: none;
  }
}

@media (pointer: coarse) {
  .spiel-tasten {
    display: flex !important;
  }
}
</style>
