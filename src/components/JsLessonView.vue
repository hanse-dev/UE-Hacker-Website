<template>
  <div class="lesson-view js-lesson-view">
    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ t('lesson.loading') }}</p>
      <div v-else v-html="lessonContent"></div>
    </div>

    <div class="lesson-editor-section">
      <p class="editor-hint">{{ t('jsLesson.editorHint') }}</p>

      <JsSandboxFrame ref="sandboxEl" />

      <template v-for="(task, idx) in tasks" :key="idx">
        <div class="task-block">
          <p class="task-instruction">
            <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
            <span v-else class="task-pending">○</span>
            <span v-html="instructionWithGlossary(task.instruction || t('lesson.taskPrefix') + (idx + 1))"></span>
            <span v-if="completedTasks.has(idx)" class="task-status-label">{{ t('lesson.taskDone') }}</span>
            <span v-else-if="!completedTasks.has(idx) && completedTasks.size > 0" class="task-status-label">{{ t('lesson.taskPending') }}</span>
          </p>
          <textarea
            v-model="taskCodes[idx]"
            class="code-editor"
            spellcheck="false"
            rows="6"
            :placeholder="t('lesson.taskPrefix') + (idx + 1) + '...'"
          ></textarea>
          <div class="editor-actions">
            <button @click="runTask(idx)" :disabled="checking" class="btn-run">
              {{ t('editor.run') }}
            </button>
            <button
              v-if="task.check !== 'self'"
              @click="checkTask(idx)"
              :disabled="checking"
              class="btn-check"
            >
              {{ checking ? t('editor.checking') : t('editor.check') }}
            </button>
            <button
              v-else-if="!completedTasks.has(idx)"
              @click="markSelfChecked(idx)"
              class="btn-selfcheck"
            >
              {{ t('jsLesson.selfCheckBtn') }}
            </button>
            <span v-else class="task-status-label">{{ t('jsLesson.selfCheckDone') }}</span>
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
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onBeforeUnmount, computed } from 'vue';
import JsSandboxFrame from './JsSandboxFrame.vue';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { validateOutput } from '../composables/useTaskValidation';
import { useLessonContent } from '../composables/useLessonContent';

export default {
  name: 'JsLessonView',
  components: { JsSandboxFrame },
  props: {
    lesson: { type: Object, required: true },
    contentPath: { type: String, required: true },
    variant: { type: String, default: 'kinder' },
    courseId: { type: String, default: 'python-grundlagen-interaktiv' },
  },
  emits: ['completed', 'next'],
  setup(props, { emit }) {
    const { lang, t } = useLanguage();
    const { markCompleted } = useInteractiveProgress(props.variant, props.courseId);

    const sandboxEl = ref(null);
    const checking = ref(false);
    const isMounted = ref(true);
    const { lessonContent, loadGlossary, loadContent, instructionWithGlossary } = useLessonContent(isMounted);

    const tasks = computed(() => {
      const list = props.lesson?.tasks;
      return Array.isArray(list) ? list : [];
    });

    const allTasksComplete = computed(() => {
      const list = tasks.value;
      return list.length > 0 && completedTasks.value.size === list.length;
    });

    const lessonSummary = computed(() => props.lesson?.lessonSummary || t('lesson.defaultSummary'));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const taskAttempts = ref([]);
    const completedTasks = ref(new Set());

    const initTaskState = () => {
      const list = tasks.value;
      taskCodes.value = list.map((x) => x.codeTemplate ?? '');
      taskOutputs.value = list.map(() => null);
      taskFeedback.value = list.map(() => null);
      taskAttempts.value = list.map(() => 0);
      completedTasks.value = new Set();
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

    const runTask = async (idx) => {
      if (checking.value) return;
      checking.value = true;
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;
      sandboxEl.value.scrollIntoView();

      const result = await sandboxEl.value.run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      taskOutputs.value[idx] = result.success
        ? (result.output || t('jsLesson.noOutput'))
        : t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
      checking.value = false;
    };

    const checkTask = async (idx) => {
      if (checking.value) return;
      checking.value = true;
      taskFeedback.value[idx] = null;
      sandboxEl.value.scrollIntoView();

      const validation = tasks.value[idx]?.validation || {};
      const result = await sandboxEl.value.run(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (!result.success) {
        taskAttempts.value[idx] = (taskAttempts.value[idx] || 0) + 1;
        const errMsg = t('editor.errorPrefix') + (result.error || t('jsLesson.unknownError'));
        taskOutputs.value[idx] = errMsg;
        taskFeedback.value[idx] = { success: false, message: errMsg };
        checking.value = false;
        return;
      }
      taskOutputs.value[idx] = result.output || t('jsLesson.noOutput');

      let canvasOk = true;
      if (validation.type === 'canvas_not_blank') {
        canvasOk = await sandboxEl.value.checkCanvasNotBlank();
      } else if (validation.type === 'canvas_changed') {
        canvasOk = await sandboxEl.value.checkCanvasChanged(validation.ms || 400);
      }
      if (!isMounted.value) return;

      const actualVars = {};
      for (const name of Object.keys(validation.variables || {})) {
        actualVars[name] = await sandboxEl.value.getVariable(name);
      }

      const functionResults = [];
      for (const fc of validation.functionCalls || []) {
        const r = await sandboxEl.value.callFunction(fc.name, fc.args);
        functionResults.push({ expected: fc.expected, actual: r.ok ? r.value : undefined, error: !r.ok });
      }
      if (!isMounted.value) return;

      const valid = canvasOk && validateOutput(result.output, validation, actualVars, functionResults);

      if (valid) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
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
      const done = completedTasks.value.size;
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

    const markSelfChecked = (idx) => {
      if (completedTasks.value.has(idx)) return;
      completedTasks.value = new Set([...completedTasks.value, idx]);
      taskFeedback.value[idx] = null;
      const total = tasks.value.length;
      if (completedTasks.value.size === total) markCompleted(props.lesson.id);
    };

    const goToNext = () => {
      emit('completed', props.lesson.id);
    };

    return {
      lang,
      t,
      lessonContent,
      sandboxEl,
      checking,
      tasks,
      taskCodes,
      taskOutputs,
      taskFeedback,
      runTask,
      checkTask,
      markSelfChecked,
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
  min-height: 110px;
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

.btn-selfcheck {
  background: var(--accent-yellow, #fdd835);
  color: #4a3800;
  border: none;
  padding: 10px 24px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
}

.btn-selfcheck:hover {
  filter: brightness(0.95);
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
