<template>
  <div class="lesson-view">
    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
      <div v-else v-html="lessonContent"></div>
    </div>

    <div class="lesson-editor-section">
      <p class="editor-hint">{{ t('lesson.editorHint') }}</p>
      <p class="editor-hint editor-hint-ran">{{ t('jsLesson.ranExplainer') }}</p>
      <div class="editor-header">
        <span class="editor-label">{{ t('lesson.yourCode') }}</span>
        <button
          @click="initializeKernel"
          :disabled="kernelReady"
          class="btn-kernel"
        >
          {{ kernelReady ? t('jupyter.ready') : t('editor.initPython') }}
        </button>
      </div>

      <template v-for="(task, idx) in tasks" :key="idx">
        <div class="task-block" :class="{ 'task-example': task.example }">
          <span v-if="task.example" class="task-badge">{{ t('jsLesson.badgeExample') }}</span>
          <p class="task-instruction">
            <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
            <span v-else class="task-pending">○</span>
            <span v-if="task.isBonus" class="task-bonus-badge">Bonus</span>
            <span v-html="instructionWithGlossary(task.instruction || t('lesson.taskPrefix') + (idx + 1))"></span>
            <span v-if="completedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskDone') }}</span>
            <span v-else-if="!completedTasks.has(idx) && completedTasks.size > 0" class="task-status-label">{{ t('lesson.taskPending') }}</span>
          </p>
          <textarea
            v-model="taskCodes[idx]"
            @keydown.tab.exact.prevent="insertIndent($event, idx)"
            class="code-editor"
            :class="{ 'code-editor-ran': taskRan[idx] }"
            spellcheck="false"
            rows="4"
            :placeholder="t('lesson.taskPrefix') + (idx + 1) + '...'"
          ></textarea>
          <p v-if="taskRan[idx]" class="code-ran-note">▶ {{ t('jsLesson.alreadyRan') }}</p>
          <div class="editor-actions">
            <button
              @click="runTask(idx)"
              :disabled="!kernelReady || checking"
              class="btn-run"
            >
              {{ t('editor.run') }}
            </button>
            <button
              v-if="!task.example"
              @click="checkTask(idx)"
              :disabled="!kernelReady || checking"
              class="btn-check"
            >
              {{ checking ? t('editor.checking') : t('editor.check') }}
            </button>
          </div>
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
        <router-link
          v-if="lesson.nextCourseId"
          :to="'/kurs/' + lesson.nextCourseId"
          class="btn-next"
        >
          {{ t('lesson.goToWeeklyCourse') }}
        </router-link>
        <button v-else @click="goToNext" class="btn-next">{{ t('lesson.nextLesson') }}</button>
      </div>

      <div v-if="kernelStatus" class="kernel-status">
        {{ kernelStatus }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onBeforeUnmount, computed, nextTick } from 'vue';
import { usePyodide } from '../composables/usePyodide';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { validateOutput, missingCodeParts } from '../composables/useTaskValidation';
import { useLessonContent } from '../composables/useLessonContent';
import { loadSavedCode, saveLessonCode } from '../composables/useSavedCode';

export default {
  name: 'LessonView',
  props: {
    lesson: {
      type: Object,
      required: true,
    },
    contentPath: {
      type: String,
      required: true,
    },
    variant: {
      type: String,
      default: 'kinder',
    },
    courseId: {
      type: String,
      default: 'python-grundlagen-interaktiv',
    },
  },
  emits: ['completed', 'next'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const { kernelReady, kernelStatus, initializeKernel, runPython } = usePyodide();
    const { markCompleted, isLessonUnlocked } = useInteractiveProgress(props.variant, props.courseId);

    const checking = ref(false);
    const isMounted = ref(true);
    const { lessonContent, loadGlossary, loadContent, instructionWithGlossary } = useLessonContent(isMounted);

    const tasks = computed(() => {
      const t = props.lesson?.tasks;
      if (Array.isArray(t) && t.length > 0) return t;
      const single = props.lesson?.codeTemplate != null;
      if (single)
        return [
          {
            codeTemplate: props.lesson.codeTemplate,
            validation: props.lesson.validation,
          },
        ];
      return [];
    });

    const allTasksComplete = computed(() => {
      const t = tasks.value;
      return t.length > 0 && completedTasks.value.size === t.length;
    });

    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const taskAttempts = ref([]);
    const taskRan = ref([]);
    const completedTasks = ref(new Set());

    const initTaskState = () => {
      const t = tasks.value;
      const templates = t.map((x) => x.codeTemplate ?? '');
      // Zwischengespeicherten Code (max. 5 Tage alt, nur lokal) wiederherstellen
      const saved = loadSavedCode(props.contentPath)[props.lesson?.id];
      taskCodes.value = saved && saved.codes.length === templates.length ? [...saved.codes] : templates;
      taskOutputs.value = t.map(() => null);
      taskFeedback.value = t.map(() => null);
      taskAttempts.value = t.map(() => 0);
      taskRan.value = t.map(() => false);
      completedTasks.value = new Set();
    };

    watch(taskCodes, (codes) => {
      if (!props.lesson?.id || !codes.length) return;
      saveLessonCode(props.contentPath, props.lesson.id, codes, tasks.value.map((x) => x.codeTemplate ?? ''));
    }, { deep: true });

    onMounted(() => {
      initializeKernel();
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

    const runTask = async (idx) => {
      if (!kernelReady.value) return;
      checking.value = true;
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;
      taskRan.value[idx] = true;

      const result = await runPython(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (result.success) {
        taskOutputs.value[idx] = result.output || t('jupyter.noOutput');
        // Beispiel-Aufgaben (`"example": true`) haben keinen Pruefen-Button: ein erfolgreicher
        // Lauf zaehlt als erledigt.
        if (tasks.value[idx]?.example) markExampleDone(idx);
      } else {
        taskOutputs.value[idx] = t('editor.errorPrefix') + (result.error || t('jupyter.unknownError'));
      }
      checking.value = false;
    };

    // Tab rueckt ein (4 Leerzeichen, wie in Python ueblich) statt den Fokus aus dem Feld zu springen.
    const insertIndent = (event, idx) => {
      const el = event.target;
      const { selectionStart: start, selectionEnd: end } = el;
      const code = taskCodes.value[idx] ?? '';
      taskCodes.value[idx] = code.slice(0, start) + '    ' + code.slice(end);
      nextTick(() => { el.selectionStart = el.selectionEnd = start + 4; });
    };

    const markExampleDone = (idx) => {
      if (completedTasks.value.has(idx)) return;
      completedTasks.value = new Set([...completedTasks.value, idx]);
      if (completedTasks.value.size === tasks.value.length) markCompleted(props.lesson.id);
    };

    const checkTask = async (idx) => {
      if (!kernelReady.value) return;
      checking.value = true;
      taskFeedback.value[idx] = null;
      taskRan.value[idx] = true;

      // `validation.stdin`: vorgegebene Eingaben fuer input() - das Pruefen oeffnet dann kein Eingabefenster
      // und die Ausgabe ist deterministisch pruefbar (usePyodide.js: browser_input).
      const stdin = tasks.value[idx]?.validation?.stdin;
      window.ueStdinQueue = Array.isArray(stdin) ? stdin.map(String) : undefined;
      let result;
      try {
        result = await runPython(taskCodes.value[idx]);
      } finally {
        window.ueStdinQueue = undefined;
      }
      if (!isMounted.value) return;

      if (result.success) {
        taskOutputs.value[idx] = result.output || t('jupyter.noOutput');
      } else {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        const errMsg = t('editor.errorPrefix') + (result.error || t('jupyter.unknownError'));
        taskOutputs.value[idx] = errMsg;
        taskFeedback.value[idx] = { success: false, message: errMsg };
        checking.value = false;
        return;
      }

      const validation = tasks.value[idx]?.validation;
      const valid = validateOutput(result.output, validation, undefined, undefined, taskCodes.value[idx]);

      if (valid) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
        const total = tasks.value.length;
        const done = completedTasks.value.size;
        if (done === total) {
          markCompleted(props.lesson.id);
          taskFeedback.value[idx] = {
            success: true,
            message: t('lesson.allTasksDone'),
          };
        } else {
          const remaining = total - done;
          taskFeedback.value[idx] = {
            success: true,
            message: t('lesson.taskDoneRemaining').replace('{n}', idx + 1).replace('{r}', remaining),
          };
        }
      } else {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        // Ausgabe stimmt, aber ein geforderter Baustein (def/class/try ...) fehlt im Code
        const missing = missingCodeParts(taskCodes.value[idx], validation);
        if (missing.length > 0 && validateOutput(result.output, { ...validation, codeContains: undefined })) {
          taskFeedback.value[idx] = {
            success: false,
            message: t('lesson.hintStructure').replace('{items}', missing.map((m) => `\`${m}\``).join(', ')),
          };
          checking.value = false;
          return;
        }
        // Erster Fehlversuch: nur ein sanfter Hinweis, kein Lösungsverrat.
        // Ab dem zweiten Fehlversuch: die erwartete Teilzeichenkette zeigen, damit niemand
        // dauerhaft feststeckt.
        if (taskAttempts.value[idx] < 2) {
          taskFeedback.value[idx] = {
            success: false,
            message: t('lesson.hintSoft'),
          };
        } else {
          taskFeedback.value[idx] = {
            success: false,
            message: t('lesson.hintExpected').replace('{expected}', validation?.expected || ''),
          };
        }
      }

      checking.value = false;
    };

    const goToNext = () => {
      emit('completed', props.lesson.id);
    };

    return {
      lang,
      t,
      lessonContent,
      checking,
      tasks,
      taskCodes,
      taskOutputs,
      taskFeedback,
      taskRan,
      insertIndent,
      kernelReady,
      kernelStatus,
      initializeKernel,
      runTask,
      checkTask,
      goToNext,
      allTasksComplete,
      lessonSummary,
      completedTasks,
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

.editor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.editor-label {
  font-weight: 600;
  color: #333;
}

.btn-kernel {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
}

.btn-kernel:hover:not(:disabled) {
  background: #3d1b5c;
}

.btn-kernel:disabled {
  background: #28a745;
  cursor: default;
}

.task-block {
  margin-bottom: 24px;
  padding-bottom: 24px;
  border-bottom: 1px solid #dee2e6;
}

.task-block:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
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

.task-status-label {
  font-weight: 400;
  color: #6c757d;
  font-size: 0.9em;
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

.code-editor {
  width: 100%;
  max-width: 500px;
  min-height: 80px;
  padding: 15px;
  box-sizing: border-box;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  line-height: 1.6;
  resize: vertical;
  margin-bottom: 12px;
}

.code-editor:focus {
  outline: 2px solid var(--primary-purple, #4a2274);
  outline-offset: -2px;
}

.editor-actions {
  display: flex;
  gap: 10px;
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

.kernel-status {
  margin-top: 12px;
  font-size: 0.9em;
  color: #6c757d;
}

.task-block.task-example {
  border-left: 4px solid #ced4da;
  padding-left: 12px;
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
  background: #f1f3f5;
  color: #868e96;
}

/* Rahmen zeigt: dieser Code wurde schon mindestens einmal ausgefuehrt. */
.code-editor.code-editor-ran {
  border-color: var(--accent-orange, #ff9800);
  box-shadow: 0 0 0 2px rgba(255, 152, 0, 0.2);
}

.code-ran-note {
  margin: 0 0 8px 0;
  font-size: 0.82em;
  color: var(--accent-orange, #fb8c00);
  font-weight: 600;
}

.editor-hint-ran {
  margin-top: -6px;
}
</style>
