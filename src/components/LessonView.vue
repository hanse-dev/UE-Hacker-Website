<template>
  <div class="lesson-view">
    <div class="lesson-content">
      <p v-if="!lessonContent" class="lesson-loading">{{ lang === 'en' ? 'Loading lesson...' : 'Lektion wird geladen...' }}</p>
      <div v-else v-html="lessonContent"></div>
    </div>

    <div class="lesson-editor-section">
      <p class="editor-hint">{{ lang === 'en' ? 'Python loads automatically when you open the page (~30 sec). Write your code and click "Check" once "Python ready" appears.' : 'Python wird beim Öffnen automatisch geladen (~30 Sek.). Schreibe deinen Code und klicke auf „Prüfen", sobald „Python bereit" angezeigt wird.' }}</p>
      <div class="editor-header">
        <span class="editor-label">{{ lang === 'en' ? 'Your Code' : 'Dein Code' }}</span>
        <button
          @click="initializeKernel"
          :disabled="kernelReady"
          class="btn-kernel"
        >
          {{ kernelReady ? (lang === 'en' ? '✓ Python ready' : '✓ Python bereit') : (lang === 'en' ? 'Initialize Python' : 'Python initialisieren') }}
        </button>
      </div>

      <template v-for="(task, idx) in tasks" :key="idx">
        <div class="task-block">
          <p class="task-instruction">
            <span v-if="completedTasks.has(idx)" class="task-done">✓</span>
            <span v-else class="task-pending">○</span>
            <span v-if="task.isBonus" class="task-bonus-badge">Bonus</span>
            <span v-html="instructionWithGlossary(task.instruction || (lang === 'en' ? 'Task ' : 'Aufgabe ') + (idx + 1))"></span>
            <span v-if="completedTasks.has(idx)" class="task-status-label">{{ lang === 'en' ? '(done)' : '(erledigt)' }}</span>
            <span v-else-if="!completedTasks.has(idx) && completedTasks.size > 0" class="task-status-label">{{ lang === 'en' ? '(pending)' : '(noch offen)' }}</span>
          </p>
          <textarea
            v-model="taskCodes[idx]"
            class="code-editor"
            spellcheck="false"
            rows="4"
            :placeholder="(lang === 'en' ? 'Task ' : 'Aufgabe ') + (idx + 1) + '...'"
          ></textarea>
          <div class="editor-actions">
            <button
              @click="runTask(idx)"
              :disabled="!kernelReady || checking"
              class="btn-run"
            >
              {{ lang === 'en' ? 'Run' : 'Ausführen' }}
            </button>
            <button
              @click="checkTask(idx)"
              :disabled="!kernelReady || checking"
              class="btn-check"
            >
              {{ checking ? (lang === 'en' ? 'Checking...' : 'Wird geprüft...') : (lang === 'en' ? 'Check' : 'Prüfen') }}
            </button>
          </div>
          <div v-if="taskOutputs[idx] !== null" class="output-display">
            <strong>{{ lang === 'en' ? 'Output:' : 'Ausgabe:' }}</strong>
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
          {{ lang === 'en' ? 'Go to the 12-Week Python Course' : 'Zum 12-Wochen Python Grundkurs' }}
        </router-link>
        <button v-else @click="goToNext" class="btn-next">{{ lang === 'en' ? 'Next lesson' : 'Weiter zur nächsten Lektion' }}</button>
      </div>

      <div v-if="kernelStatus" class="kernel-status">
        {{ kernelStatus }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch, onMounted, onBeforeUnmount, computed } from 'vue';
import { marked } from 'marked';
import { usePyodide } from '../composables/usePyodide';
import { useInteractiveProgress } from '../composables/useInteractiveProgress';
import { useLanguage } from '../composables/useLanguage';
import { validateOutput } from '../composables/useTaskValidation';

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
  },
  emits: ['completed', 'next'],
  setup(props, { emit }) {
    const { lang } = useLanguage();
    const { kernelReady, kernelStatus, initializeKernel, runPython } = usePyodide();
    const { markCompleted, isLessonUnlocked } = useInteractiveProgress(props.variant);

    const lessonContent = ref('');
    const checking = ref(false);
    const isMounted = ref(true);

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

    const lessonSummary = computed(() => props.lesson?.lessonSummary || (lang.value === 'en' ? 'Great, you completed this lesson!' : 'Super, du hast diese Lektion abgeschlossen!'));

    const taskCodes = ref([]);
    const taskOutputs = ref([]);
    const taskFeedback = ref([]);
    const completedTasks = ref(new Set());

    const initTaskState = () => {
      const t = tasks.value;
      taskCodes.value = t.map((x) => x.codeTemplate ?? '');
      taskOutputs.value = t.map(() => null);
      taskFeedback.value = t.map(() => null);
      completedTasks.value = new Set();
    };

    onMounted(() => {
      initializeKernel();
      loadGlossary();
    });

    onBeforeUnmount(() => {
      isMounted.value = false;
    });

    const allLessonModules = import.meta.glob(
      [
        '../../content/python-grundlagen-interaktiv-kinder/*.md',
        '../../content/python-grundlagen-interaktiv-jugendliche/*.md',
        '../../content/python-grundlagen-interaktiv-kinder-en/*.md',
        '../../content/python-grundlagen-interaktiv-jugendliche-en/*.md',
      ],
      { query: '?raw', import: 'default' }
    );

    const allGlossaryModules = import.meta.glob(
      [
        '../../content/python-grundlagen-interaktiv-kinder/glossary.json',
        '../../content/python-grundlagen-interaktiv-jugendliche/glossary.json',
        '../../content/python-grundlagen-interaktiv-kinder-en/glossary.json',
        '../../content/python-grundlagen-interaktiv-jugendliche-en/glossary.json',
      ],
    );

    let glossary = {};
    const loadGlossary = async () => {
      try {
        const key = `../../content/${props.contentPath}/glossary.json`;
        const loader = allGlossaryModules[key];
        if (loader) {
          const mod = await loader();
          glossary = mod.default || {};
        }
      } catch {
        glossary = {};
      }
    };

    const instructionWithGlossary = (text) => {
      if (!text || !glossary || Object.keys(glossary).length === 0) return escapeHtml(text || '');
      const escaped = escapeHtml(text);
      const terms = Object.keys(glossary).sort((a, b) => b.length - a.length);
      let out = escaped;
      for (const term of terms) {
        const regex = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'g');
        const explanation = glossary[term].replace(/"/g, '&quot;');
        out = out.replace(regex, `<span class="glossary-term" title="${explanation}">$1</span>`);
      }
      return out;
    };

    const escapeHtml = (s) => {
      if (!s) return '';
      return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    };

    const applyGlossaryTooltips = (html) => {
      if (!glossary || Object.keys(glossary).length === 0) return html;
      const codeBlockRegex = /<pre><code>[\s\S]*?<\/code><\/pre>/gi;
      const codeBlocks = html.match(codeBlockRegex) || [];
      const textParts = html.split(codeBlockRegex);
      const terms = Object.keys(glossary).sort((a, b) => b.length - a.length);
      const result = textParts.map((part, i) => {
        let out = part;
        for (const term of terms) {
          const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
          const regex = new RegExp(`(?<![<>])(${escaped})(?![^<]*>)`, 'g');
          const explanation = glossary[term].replace(/"/g, '&quot;');
          out = out.replace(regex, `<span class="glossary-term" title="${explanation}">$1</span>`);
        }
        return out + (codeBlocks[i] || '');
      }).join('');
      return result;
    };

    const loadContent = async () => {
      if (!props.lesson?.file || !props.contentPath) return;
      const key = `../../content/${props.contentPath}/${props.lesson.file}`;
      const loader = allLessonModules[key];
      if (!loader) {
        lessonContent.value = '<p>Lektion konnte nicht geladen werden.</p>';
        return;
      }
      try {
        if (Object.keys(glossary).length === 0) await loadGlossary();
        const text = await loader();
        if (!isMounted.value) return;
        let html = marked(text ?? '');
        html = applyGlossaryTooltips(html);
        lessonContent.value = html;
      } catch (e) {
        if (!isMounted.value) return;
        console.error('Could not load lesson content:', e);
        lessonContent.value = '<p>Lektion konnte nicht geladen werden.</p>';
      }
    };

    watch(
      () => props.lesson,
      (newLesson) => {
        initTaskState();
        loadContent();
      },
      { immediate: true }
    );

    const runTask = async (idx) => {
      if (!kernelReady.value) return;
      checking.value = true;
      taskOutputs.value[idx] = null;
      taskFeedback.value[idx] = null;

      const result = await runPython(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (result.success) {
        taskOutputs.value[idx] = result.output || (lang.value === 'en' ? '(no output)' : '(keine Ausgabe)');
      } else {
        taskOutputs.value[idx] = (lang.value === 'en' ? 'Error: ' : 'Fehler: ') + (result.error || (lang.value === 'en' ? 'Unknown error' : 'Unbekannter Fehler'));
      }
      checking.value = false;
    };

    const checkTask = async (idx) => {
      if (!kernelReady.value) return;
      checking.value = true;
      taskFeedback.value[idx] = null;

      const result = await runPython(taskCodes.value[idx]);
      if (!isMounted.value) return;

      if (result.success) {
        taskOutputs.value[idx] = result.output || (lang.value === 'en' ? '(no output)' : '(keine Ausgabe)');
      } else {
        const errMsg = (lang.value === 'en' ? 'Error: ' : 'Fehler: ') + (result.error || (lang.value === 'en' ? 'Unknown error' : 'Unbekannter Fehler'));
        taskOutputs.value[idx] = errMsg;
        taskFeedback.value[idx] = { success: false, message: errMsg };
        checking.value = false;
        return;
      }

      const validation = tasks.value[idx]?.validation;
      const valid = validateOutput(result.output, validation);

      if (valid) {
        completedTasks.value = new Set([...completedTasks.value, idx]);
        const total = tasks.value.length;
        const done = completedTasks.value.size;
        if (done === total) {
          markCompleted(props.lesson.id);
          taskFeedback.value[idx] = {
            success: true,
            message: lang.value === 'en' ? 'Correct! You completed all tasks.' : 'Richtig! Du hast alle Aufgaben abgeschlossen.',
          };
        } else {
          const remaining = total - done;
          taskFeedback.value[idx] = {
            success: true,
            message: lang.value === 'en'
              ? `Correct! Task ${idx + 1} done. ${remaining} task(s) remaining.`
              : `Richtig! Aufgabe ${idx + 1} erledigt. Noch ${remaining} Aufgabe(n) zu lösen.`,
          };
        }
      } else {
        taskFeedback.value[idx] = {
          success: false,
          message: lang.value === 'en'
            ? `Output doesn't match yet. Expected something containing: "${validation?.expected || ''}"`
            : `Die Ausgabe stimmt noch nicht. Erwartet wurde etwas mit: "${validation?.expected || ''}"`,
        };
      }

      checking.value = false;
    };

    const goToNext = () => {
      emit('completed', props.lesson.id);
    };

    return {
      lang,
      lessonContent,
      checking,
      tasks,
      taskCodes,
      taskOutputs,
      taskFeedback,
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
</style>
