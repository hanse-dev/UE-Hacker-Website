<template>
  <div class="code-task-step">
    <p class="task-instruction">
      <span v-if="completed" class="task-done">✓</span>
      <span v-else class="task-pending">○</span>
      {{ instructionText }}
    </p>
    <textarea
      v-model="code"
      class="code-editor"
      spellcheck="false"
      rows="5"
      :placeholder="lang === 'en' ? 'Your code...' : 'Dein Code...'"
    ></textarea>
    <div class="editor-actions">
      <button
        type="button"
        @click="runCode"
        :disabled="!kernelReady || checking"
        class="btn-run"
      >
        {{ lang === 'en' ? 'Run' : 'Ausführen' }}
      </button>
      <button
        type="button"
        @click="checkCode"
        :disabled="!kernelReady || checking"
        class="btn-check"
      >
        {{ checking ? (lang === 'en' ? 'Checking...' : 'Wird geprüft...') : (lang === 'en' ? 'Check' : 'Prüfen') }}
      </button>
    </div>
    <div v-if="output !== null" class="output-display">
      <strong>{{ lang === 'en' ? 'Output:' : 'Ausgabe:' }}</strong>
      <pre class="output-content">{{ output }}</pre>
    </div>
    <div v-if="feedback" :class="['feedback', feedback.success ? 'feedback-success' : 'feedback-error']">
      {{ feedback.message }}
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import { usePyodide } from '../composables/usePyodide';
import { validateOutput } from '../composables/useTaskValidation';

export default {
  name: 'CodeTaskStep',
  props: {
    instruction: { type: String, required: true },
    instructionEn: { type: String, default: '' },
    codeTemplate: { type: String, default: '' },
    validation: { type: Object, default: null },
    lang: { type: String, default: 'de' },
    completed: { type: Boolean, default: false },
  },
  emits: ['completed'],
  setup(props, { emit }) {
    const { kernelReady, initializeKernel, runPython } = usePyodide();
    const code = ref(props.codeTemplate || '');
    const output = ref(null);
    const feedback = ref(null);
    const checking = ref(false);

    const instructionText = computed(() =>
      props.lang === 'en' && props.instructionEn ? props.instructionEn : props.instruction
    );

    watch(() => props.codeTemplate, (v) => {
      if (!props.completed) code.value = v || '';
    });

    onMounted(() => initializeKernel());

    const runCode = async () => {
      if (!kernelReady.value) return;
      checking.value = true;
      output.value = null;
      feedback.value = null;
      const result = await runPython(code.value);
      if (result.success) {
        output.value = result.output || (props.lang === 'en' ? '(no output)' : '(keine Ausgabe)');
      } else {
        output.value = (props.lang === 'en' ? 'Error: ' : 'Fehler: ') + (result.error || '');
      }
      checking.value = false;
    };

    const checkCode = async () => {
      if (!kernelReady.value) return;
      checking.value = true;
      feedback.value = null;
      const result = await runPython(code.value);
      if (!result.success) {
        const errMsg = (props.lang === 'en' ? 'Error: ' : 'Fehler: ') + (result.error || '');
        output.value = errMsg;
        feedback.value = { success: false, message: errMsg };
        checking.value = false;
        return;
      }
      output.value = result.output || (props.lang === 'en' ? '(no output)' : '(keine Ausgabe)');
      const valid = validateOutput(result.output, props.validation);
      if (valid) {
        feedback.value = {
          success: true,
          message: props.lang === 'en' ? 'Correct!' : 'Richtig!',
        };
        emit('completed');
      } else {
        feedback.value = {
          success: false,
          message: props.lang === 'en'
            ? `Output doesn't match yet. Expected something containing: "${props.validation?.expected || ''}"`
            : `Die Ausgabe stimmt noch nicht. Erwartet: "${props.validation?.expected || ''}"`,
        };
      }
      checking.value = false;
    };

    return {
      code,
      output,
      feedback,
      checking,
      kernelReady,
      instructionText,
      runCode,
      checkCode,
    };
  },
};
</script>

<style scoped>
.code-task-step {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
}

.task-instruction {
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
  margin: 0 0 12px 0;
  line-height: 1.4;
}

.task-done { color: #28a745; margin-right: 6px; }
.task-pending { color: #adb5bd; margin-right: 6px; }

.code-editor {
  width: 100%;
  max-width: 100%;
  min-height: 100px;
  padding: 12px;
  box-sizing: border-box;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  line-height: 1.5;
  resize: vertical;
  margin-bottom: 10px;
}

.code-editor:focus {
  outline: 2px solid var(--primary-purple, #4a2274);
  outline-offset: -2px;
}

.editor-actions {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}

.btn-run {
  background: #6c757d;
  color: white;
  border: none;
  padding: 8px 18px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

.btn-run:hover:not(:disabled) { background: #5a6268; }
.btn-run:disabled { opacity: 0.6; cursor: not-allowed; }

.btn-check {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 8px 18px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

.btn-check:hover:not(:disabled) { background: #fb8c00; }
.btn-check:disabled { opacity: 0.6; cursor: not-allowed; }

.output-display {
  padding: 10px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  margin-bottom: 10px;
}

.output-display strong {
  display: block;
  margin-bottom: 6px;
  font-size: 0.85em;
  color: #555;
}

.output-content {
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  white-space: pre-wrap;
}

.feedback {
  padding: 10px 14px;
  border-radius: 6px;
  font-weight: 500;
}

.feedback-success {
  background: #d4edda;
  color: #155724;
}

.feedback-error {
  background: #f8d7da;
  color: #721c24;
}
</style>
