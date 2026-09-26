<template>
  <div class="lesson-view js-lesson-view">
    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
      <div v-else v-html="lessonContent"></div>
    </div>

    <div class="lesson-editor-section">
      <p class="editor-hint">{{ t('jsLesson.editorHint') }}</p>
      <p class="editor-hint editor-hint-ran">{{ t('jsLesson.ranExplainer') }}</p>

      <template v-for="(task, idx) in tasks" :key="idx">
        <div class="task-block" :class="isExample(idx) ? 'task-example' : 'task-required'">
          <span class="task-badge" :class="isExample(idx) ? 'badge-example' : 'badge-required'">
            {{ isExample(idx) ? t('jsLesson.badgeExample') : t('jsLesson.badgeRequired') }}
          </span>
          <p class="task-instruction">
            <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
            <span v-else-if="skippedTasks.has(idx)" class="task-skipped">⏭</span>
            <span v-else class="task-pending">○</span>
            <span v-html="instructionWithGlossary(task.instruction || t('lesson.taskPrefix') + (idx + 1))"></span>
            <span v-if="completedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskDone') }}</span>
            <span v-else-if="skippedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskSkipped') }}</span>
            <span v-else-if="completedTasks.size > 0" class="task-status-label">{{ t('lesson.taskPending') }}</span>
          </p>
          <div class="code-editor-wrapper" :class="{ 'code-editor-ran': taskRan[idx] }">
            <JsCodeCell v-model="taskCodes[idx]" />
          </div>
          <p v-if="taskRan[idx]" class="code-ran-note">▶ {{ t('jsLesson.alreadyRan') }}</p>
          <div class="editor-actions">
            <button @click="runTask(idx)" :disabled="checking" class="btn-run">
              {{ t('editor.run') }}
            </button>
            <button
              v-if="!isExample(idx)"
              @click="checkTask(idx)"
              :disabled="checking"
              class="btn-check"
            >
              {{ checking ? t('editor.checking') : t('editor.check') }}
            </button>
            <button
              v-if="!isExample(idx) && !isTaskDone(idx) && (taskAttempts[idx] || 0) >= 2"
              @click="skipTask(idx)"
              :disabled="checking"
              class="btn-skip"
            >
              {{ t('lesson.skipTask') }}
            </button>
          </div>
          <JsSandboxFrame v-if="taskRan[idx]" :ref="(el) => setSandboxRef(idx, el)" :show-canvas="showCanvas" :dom-mode="domMode" />
          <details v-if="task.solution" class="solution-reveal">
            <summary>{{ t('jsLesson.showSolution') }}</summary>
            <pre class="solution-code">{{ task.solution }}</pre>
          </details>
          <div v-if="taskOutputs[idx] !== null" class="output-display">
            <strong>{{ t('editor.output') }}</strong>
            <pre class="output-content">{{ taskOutputs[idx] }}</pre>
          </div>
          <div v-if="taskFeedback[idx]" :class="['feedback', taskFeedback[idx].success ? 'feedback-success' : 'feedback-error']">
            {{ taskFeedback[idx].message }}
          </div>
        </div>
      </template>

      <div v-if="allTasksComplete" class="lesson-complete-box">
        <p class="lesson-summary">{{ lessonSummary }}</p>
        <ProjectCompletionBox v-if="isProjectCourse && isLastLesson" :next-course-id="lesson.nextCourseId" />
        <template v-else>
          <router-link
            v-if="lesson.nextCourseId"
            :to="'/kurs/' + lesson.nextCourseId"
            class="btn-next"
          >
            {{ t('lesson.goToWeeklyCourse') }}
          </router-link>
          <button v-else @click="goToNext" class="btn-next">{{ t('lesson.nextLesson') }}</button>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onBeforeUnmount, computed, nextTick } from 'vue';
import JsSandboxFrame from './JsSandboxFrame.vue';
import JsCodeCell from './JsCodeCell.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { validateOutput } from '../composables/useTaskValidation';
import { useLessonContent } from '../composables/useLessonContent';
import ProjectCompletionBox from './ProjectCompletionBox.vue';

export default {
  name: 'JsLessonView',
  components: { JsSandboxFrame, JsCodeCell, ProjectCompletionBox },
  props: {
    lesson: { type: Object, required: true },
    contentPath: { type: String, required: true },
    variant: { type: String, default: 'kinder' },
    courseId: { type: String, default: 'python-grundlagen-interaktiv' },
    showCanvas: { type: Boolean, default: true },
    domMode: { type: Boolean, default: false },
    // true nur bei ProjectCourse.vue (Projekt-Kurse) - steuert, ob am Ende der letzten Lektion
    // ProjectCompletionBox (Abzeichen-Hinweis + zurueck zu /projekte) statt des generischen
    // "Weiter"-Buttons erscheint.
    isProjectCourse: { type: Boolean, default: false },
    isLastLesson: { type: Boolean, default: false },
  },
  emits: ['completed', 'next'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const { markCompleted } = useInteractiveProgress(props.variant, props.courseId);

    // Eine eigene Sandbox-Instanz pro Aufgabe statt einer geteilten am Lektionsanfang - jeder Lauf
    // baut das iframe ohnehin komplett neu auf (kein geteilter Zustand zwischen Laeufen, siehe
    // useJsSandbox.js), es gibt also nichts zu teilen. Dadurch entfaellt das Hin-und-Herspringen
    // zwischen einer Canvas oben und der gerade bearbeiteten Aufgabe weiter unten.
    const sandboxEls = ref([]);
    const setSandboxRef = (idx, el) => { sandboxEls.value[idx] = el; };
    const checking = ref(false);
    const isMounted = ref(true);
    const { lessonContent, loadGlossary, loadContent, instructionWithGlossary } = useLessonContent(isMounted);

    const tasks = computed(() => {
      const list = props.lesson?.tasks;
      return Array.isArray(list) ? list : [];
    });

    // Beispiel-Aufgaben (bereits fertiger, unveraenderter codeTemplate zum Anschauen) brauchen
    // keinen "Pruefen"-Button - nur "Ausfuehren". Deine-Aufgabe-Aufgaben (leerer/unfertiger
    // codeTemplate, echte Erwartung) brauchen beides. Reines Anzeige-/Verhaltensmerkmal, keine
    // eigene Validierung - jede Aufgabe hat weiterhin ein `validation`-Objekt.
    const isExample = (idx) => !!tasks.value[idx]?.example;

    // Uebersprungene Aufgaben zaehlen fuer den Lektions-Abschluss wie erledigt (damit man nicht
    // blockiert bleibt), bleiben aber optisch als "uebersprungen" erkennbar statt als geloest -
    // gilt bewusst nur fuer normale Lektionsaufgaben, nicht fuer den Wochen-Check (CodeChallenge.vue).
    const doneCount = computed(() => new Set([...completedTasks.value, ...skippedTasks.value]).size);
    const isTaskDone = (idx) => completedTasks.value.has(idx) || skippedTasks.value.has(idx);

    const allTasksComplete = computed(() => {
      const list = tasks.value;
      return list.length > 0 && doneCount.value === list.length;
    });

    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const taskAttempts = ref([]);
    const taskRan = ref([]);
    const completedTasks = ref(new Set());
    const skippedTasks = ref(new Set());

    const initTaskState = () => {
      const list = tasks.value;
      taskCodes.value = list.map((x) => x.codeTemplate ?? '');
      taskOutputs.value = list.map(() => null);
      taskFeedback.value = list.map(() => null);
      taskAttempts.value = list.map(() => 0);
      taskRan.value = list.map(() => false);
      completedTasks.value = new Set();
      skippedTasks.value = new Set();
      sandboxEls.value = [];
    };

    const skipTask = (idx) => {
      if (isTaskDone(idx)) return;
      skippedTasks.value = new Set([...skippedTasks.value, idx]);
      taskFeedback.value[idx] = null;
      if (doneCount.value === tasks.value.length) markCompleted(props.lesson.id);
    };

    onMounted(() => {
      loadGlossary(props.contentPath);
    });

    onBeforeUnmount(() => {
      isMounted.value = false;
    });

    watch(
      () => props.lesson,
      (newLesson) => {
        initTaskState();
        loadContent(newLesson, props.contentPath);
      },
      { immediate: true }
    );

    // Ein Rechteck zu zeichnen erzeugt keine console.log-Ausgabe - ohne diesen Hinweis wirkt die
    // "Ausgabe"-Box faelschlich leer, obwohl oben im Spielfeld sichtbar etwas passiert ist. Nur
    // relevant, wenn diese Lektion ueberhaupt ein sichtbares Canvas hat (showCanvas).
    const withCanvasNote = async (idx, rawOutput) => {
      const trimmed = (rawOutput || '').trim();
      if (!props.showCanvas) return trimmed || t('jsLesson.noOutput');
      const drew = await sandboxEls.value[idx].checkCanvasNotBlank();
      if (drew) return trimmed ? `${trimmed}\n\n${t('jsLesson.canvasNote')}` : t('jsLesson.canvasNote');
      return trimmed || t('jsLesson.noOutput');
    };

    const runTask = async (idx) => {
      if (checking.value) return;
      checking.value = true;
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;
      // Sandbox-Frame wird erst bei der ersten Ausfuehrung ueberhaupt gemountet (v-if="taskRan[idx]")
      // - vorher gibt es nichts zu sehen, und jedes gemountete Frame startet eine dauerhaft
      // laufende requestAnimationFrame-Heartbeat-Schleife (useJsSandbox.js), die sonst fuer jede
      // Aufgabe einer Lektion gleichzeitig liefe, auch fuer noch nie angeklickte.
      taskRan.value[idx] = true;
      await nextTick();
      sandboxEls.value[idx].scrollIntoView();

      const result = await sandboxEls.value[idx].run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      taskOutputs.value[idx] = result.success
        ? await withCanvasNote(idx, result.output)
        : t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
      // Beispiel-Aufgaben haben keinen "Pruefen"-Button - ein erfolgreicher Lauf zaehlt hier schon
      // als "gesehen/erledigt", damit die Lektion trotzdem abschliessbar bleibt.
      if (result.success && isExample(idx)) markExampleDone(idx);
      checking.value = false;
    };

    const markExampleDone = (idx) => {
      if (completedTasks.value.has(idx)) return;
      completedTasks.value = new Set([...completedTasks.value, idx]);
      if (doneCount.value === tasks.value.length) markCompleted(props.lesson.id);
    };

    const checkTask = async (idx) => {
      if (checking.value) return;
      checking.value = true;
      taskFeedback.value[idx] = null;
      taskRan.value[idx] = true;
      await nextTick();
      sandboxEls.value[idx].scrollIntoView();

      const validation = tasks.value[idx]?.validation || {};
      const result = await sandboxEls.value[idx].run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (!result.success) {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        const errMsg = t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
        taskOutputs.value[idx] = errMsg;
        taskFeedback.value[idx] = { success: false, message: errMsg };
        checking.value = false;
        return;
      }
      taskOutputs.value[idx] = await withCanvasNote(idx, result.output);

      // Canvas- und DOM-Checks laufen ausserhalb von validateOutput() - beide fragen den lebenden
      // Sandbox-Zustand per RPC ab (Pixel-Daten bzw. echtes DOM-Auslesen/Klick-Simulation), nicht
      // die Konsolen-Ausgabe. `validation.expected` bleibt fuer diese Typen bewusst leer (die
      // dom_*-Typen nutzen stattdessen `validation.text`), sonst wuerde validateOutput()s
      // Ausgabe-Fallback-Check faelschlich gegen die (meist leere) Konsolen-Ausgabe pruefen.
      let extraChecksOk = true;
      if (validation.type === 'canvas_not_blank') {
        extraChecksOk = await sandboxEls.value[idx].checkCanvasNotBlank();
      } else if (validation.type === 'canvas_changed') {
        extraChecksOk = await sandboxEls.value[idx].checkCanvasChanged(validation.ms || 400);
      } else if (validation.type === 'dom_text') {
        const text = await sandboxEls.value[idx].checkDomText(validation.target);
        extraChecksOk = typeof text === 'string' && text.trim() === validation.text;
      } else if (validation.type === 'dom_click_text') {
        const text = await sandboxEls.value[idx].checkDomClickText(validation.click, validation.target, validation.clicks);
        extraChecksOk = typeof text === 'string' && text.trim() === validation.text;
      }
      if (!isMounted.value) return;

      const valid = extraChecksOk && validateOutput(result.output, validation);

      if (valid) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
        if (skippedTasks.value.has(idx)) {
          const next = new Set(skippedTasks.value);
          next.delete(idx);
          skippedTasks.value = next;
        }
        finishCheck(idx);
      } else {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        if (taskAttempts.value[idx] < 2) {
          taskFeedback.value[idx] = { success: false, message: t('lesson.hintSoft') };
        } else {
          taskFeedback.value[idx] = {
            success: false,
            message: t('lesson.hintExpected').replace('{expected}', validation.expected || ''),
          };
        }
      }
      checking.value = false;
    };

    const finishCheck = (idx) => {
      const total = tasks.value.length;
      const done = doneCount.value;
      if (done === total) {
        markCompleted(props.lesson.id);
        taskFeedback.value[idx] = { success: true, message: t('lesson.allTasksDone') };
      } else {
        const remaining = total - done;
        taskFeedback.value[idx] = {
          success: true,
          message: t('lesson.taskDoneRemaining').replace('{n}', idx + 1).replace('{r}', remaining),
        };
      }
    };

    const goToNext = () => {
      emit('completed', props.lesson.id);
    };

    return {
      lang,
      t,
      lessonContent,
      setSandboxRef,
      checking,
      tasks,
      isExample,
      taskCodes,
      taskOutputs,
      taskFeedback,
      taskRan,
      runTask,
      checkTask,
      goToNext,
      allTasksComplete,
      lessonSummary,
      completedTasks,
      skippedTasks,
      skipTask,
      isTaskDone,
      taskAttempts,
      instructionWithGlossary,
    };
  },
};
</script>

<style scoped>
.lesson-view {
  max-width: 800px;
  margin: 0 auto;
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
  margin-top: 1em;
  margin-bottom: 0.5em;
}

.lesson-content :deep(code) {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}

.lesson-content :deep(.glossary-term) {
  border-bottom: 1px dotted var(--primary-purple, #4a2274);
  cursor: help;
}

.lesson-content :deep(pre) {
  background: #f8f9fa;
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}

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

.editor-hint-ran {
  color: var(--primary-purple, #4a2274);
}

.task-block {
  margin-bottom: 24px;
  padding-bottom: 24px;
  padding-left: 14px;
  border-bottom: 1px solid #dee2e6;
  border-left: 4px solid transparent;
}

.task-block.task-required {
  border-left-color: var(--accent-orange, #ff9800);
}

.task-block.task-example {
  border-left-color: #ced4da;
}

.task-block:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
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
  background: #f1f3f5;
  color: #868e96;
}

.badge-required {
  background: #fff3e0;
  color: var(--accent-orange, #fb8c00);
}

.task-instruction {
  display: block;
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
  margin: 0 0 8px 0;
  font-size: 0.95em;
  line-height: 1.4;
}

.task-done {
  color: #28a745;
  margin-right: 6px;
}

.task-pending {
  color: #adb5bd;
  margin-right: 6px;
}

.task-skipped {
  color: #d9822b;
  margin-right: 6px;
}

.task-status-label {
  font-weight: 400;
  color: #6c757d;
  font-size: 0.9em;
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
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
}

.btn-next:hover {
  background: #3d1b5c;
}

a.btn-next {
  display: inline-block;
  text-decoration: none;
  text-align: center;
}

.code-editor-wrapper {
  max-width: 500px;
  border-radius: 8px;
  transition: box-shadow 0.15s, border-color 0.15s;
}

/* Rahmen zeigt: dieser Code wurde schon mindestens einmal ausgefuehrt (siehe jsLesson.ranExplainer
   oben in der Lektion) - unabhaengig davon, ob die Aufgabe schon bestanden ist. */
.code-editor-wrapper.code-editor-ran :deep(.cm-host) {
  border-color: var(--accent-orange, #ff9800);
  box-shadow: 0 0 0 2px rgba(255, 152, 0, 0.2);
}

.code-ran-note {
  margin: -6px 0 12px 0;
  font-size: 0.82em;
  color: var(--accent-orange, #fb8c00);
  font-weight: 600;
}

.solution-reveal {
  max-width: 500px;
  margin: 0 0 12px 0;
  border: 1px dashed #d9c7ea;
  border-radius: 6px;
  background: #f7f1fb;
}

.solution-reveal summary {
  cursor: pointer;
  padding: 8px 12px;
  font-weight: 600;
  font-size: 0.85em;
  color: var(--primary-purple, #4a2274);
  user-select: none;
}

.solution-code {
  margin: 0;
  padding: 0 12px 12px 12px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 0.85em;
  white-space: pre-wrap;
  word-break: break-word;
  color: #333;
}

.editor-actions {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 12px;
}

.btn-run {
  background: #6c757d;
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}

.btn-run:hover:not(:disabled) {
  background: #5a6268;
}

.btn-run:disabled {
  background: #adb5bd;
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-check {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}

.btn-check:hover:not(:disabled) {
  background: #fb8c00;
}

.btn-check:disabled {
  background: #6c757d;
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-skip {
  background: transparent;
  color: #6c757d;
  border: 1px solid #dee2e6;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 15px;
}

.btn-skip:hover:not(:disabled) {
  background: #f8f9fa;
  border-color: #adb5bd;
}

.btn-skip:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.output-display {
  margin-top: 12px;
  padding: 12px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  margin-bottom: 12px;
}

.output-display strong {
  display: block;
  margin-bottom: 8px;
  font-size: 0.9em;
  color: #555;
}

.output-content {
  margin: 0;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  white-space: pre-wrap;
  word-break: break-word;
}

.feedback {
  padding: 12px 16px;
  border-radius: 6px;
  font-weight: 500;
}

.feedback-success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.feedback-error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
</style>
