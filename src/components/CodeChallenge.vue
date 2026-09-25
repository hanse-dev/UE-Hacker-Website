<template>
  <div class="code-challenge" :data-challenge-index="challengeIndex" v-if="challenge">
    <div class="challenge-header">
      <h4>{{ title }}</h4>
      <span v-if="alreadyPassed" class="challenge-badge">{{ t('challenge.passed') }}</span>
    </div>
    <p class="challenge-instruction">{{ instruction }}</p>

    <div class="challenge-editor-header">
      <button @click="initializeKernel" :disabled="kernelReady" class="btn-kernel">
        {{ kernelReady ? t('jupyter.ready') : t('editor.initPython') }}
      </button>
    </div>
    <textarea
      v-model="code"
      class="code-editor"
      spellcheck="false"
      rows="4"
      :placeholder="t('challenge.codePlaceholder')"
    ></textarea>
    <div class="challenge-actions">
      <button @click="runCode" :disabled="!kernelReady || checking" class="btn-run">
        {{ t('editor.run') }}
      </button>
      <button @click="checkCode" :disabled="!kernelReady || checking" class="btn-check">
        {{ checking ? t('editor.checking') : t('editor.check') }}
      </button>
    </div>
    <div v-if="output !== null" class="challenge-output">
      <strong>{{ t('editor.output') }}</strong>
      <pre>{{ output }}</pre>
    </div>
    <div v-if="feedback" :class="['challenge-feedback', feedback.success ? 'feedback-success' : 'feedback-error']">
      {{ feedback.message }}
    </div>
    <p v-if="kernelStatus" class="kernel-status">{{ kernelStatus }}</p>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import { usePyodide } from '../composables/usePyodide';
import { useWeekChecks, loadWeekChecks } from '../composables/useWeekChecks';
import { validateOutput } from '../composables/useTaskValidation';
import { useLanguage } from '../composables/useLanguage';

// Skalare (str/int/float/bool) kommen von Pyodide schon als JS-Wert. Komplexere Werte (z.B. ein
// dict oder ein Funktions-Rueckgabewert) sind ein PyProxy - fuer den Vergleich in ein einfaches
// JS-Objekt umwandeln (dict_converter: Object.fromEntries statt der Standard-Map).
function toPlainJs(raw) {
  return (raw && typeof raw.toJs === 'function')
    ? raw.toJs({ dict_converter: Object.fromEntries })
    : raw;
}

export default {
  name: 'CodeChallenge',
  props: {
    weekNumber: { type: Number, required: true },
    challengeIndex: { type: Number, default: 0 },
    label: { type: String, default: '' },
    courseKey: { type: String, default: 'python' },
  },
  setup(props) {
    const { lang, t } = useLanguage();
    const { kernelReady, kernelStatus, initializeKernel, runPython, pyodideRef } = usePyodide();
    const { markCodingPassed, isCodingChallengePassed } = useWeekChecks(props.courseKey);

    const challenge = ref(null);
    const code = ref('');
    const output = ref(null);
    const feedback = ref(null);
    const checking = ref(false);

    const instruction = computed(() =>
      lang.value === 'en' && challenge.value?.instruction_en
        ? challenge.value.instruction_en
        : challenge.value?.instruction
    );

    const title = computed(() => {
      const base = t('challenge.title');
      return props.label ? `${base}: ${props.label}` : base;
    });

    const alreadyPassed = computed(() => isCodingChallengePassed(props.weekNumber, props.challengeIndex));

    const load = async () => {
      try {
        const data = await loadWeekChecks(props.courseKey);
        const challenges = data?.weeks?.[String(props.weekNumber)]?.codingChallenges || [];
        challenge.value = challenges[props.challengeIndex] || null;
        code.value = challenge.value?.codeTemplate ?? '';
      } catch (e) {
        challenge.value = null;
      }
    };

    onMounted(load);
    watch(() => [props.weekNumber, props.challengeIndex], () => {
      output.value = null;
      feedback.value = null;
      load();
    });

    const runCode = async () => {
      if (!kernelReady.value) return;
      checking.value = true;
      feedback.value = null;
      const result = await runPython(code.value);
      output.value = result.success
        ? (result.output || t('jupyter.noOutput'))
        : t('editor.errorPrefix') + (result.error || '');
      checking.value = false;
    };

    const checkCode = async () => {
      if (!kernelReady.value) return;
      checking.value = true;
      feedback.value = null;

      // Variablen/Funktionen aus einem frueheren Lauf (gleicher, geteilter Pyodide-Namespace)
      // vor dem Ausfuehren entfernen - sonst koennte ein alter Wert/eine alte Definition eine
      // Pruefung faelschlich bestehen lassen, obwohl der aktuelle Code sie gar nicht (mehr) setzt.
      const requiredVars = Object.keys(challenge.value?.validation?.variables || {});
      const functionCalls = challenge.value?.validation?.functionCalls || [];
      const requiredFns = [...new Set(functionCalls.map((c) => c.name))];
      [...requiredVars, ...requiredFns].forEach((name) => {
        // .delete() wirft, wenn der Name noch nie gesetzt wurde (erster Versuch) - das ist
        // hier der Normalfall, nicht abfangen wuerde checkCode() vorzeitig abbrechen.
        try { pyodideRef.value?.globals.delete(name); } catch { /* existierte noch nicht */ }
      });

      const result = await runPython(code.value);

      if (!result.success) {
        output.value = t('editor.errorPrefix') + (result.error || '');
        feedback.value = { success: false, message: output.value };
        checking.value = false;
        return;
      }
      output.value = result.output || t('jupyter.noOutput');

      const actualVars = {};
      requiredVars.forEach((name) => {
        actualVars[name] = toPlainJs(pyodideRef.value?.globals.get(name));
      });

      const functionResults = functionCalls.map(({ name, args, expected }) => {
        const fn = pyodideRef.value?.globals.get(name);
        if (typeof fn !== 'function') return { expected, error: true };
        try {
          // Defensiv: der AST-Loop-Guard (usePyodide.js) injiziert Deadline-Checks in jede
          // Schleife der eingereichten Zelle, auch in Funktionskoerpern. Die Deadline-Variable
          // wird nach dem urspruenglichen Lauf wieder geloescht - ohne diese Zeile wuerde der
          // Aufruf einer Funktion mit eigener Schleife hier mit NameError abstuerzen.
          pyodideRef.value.globals.set('__cell_deadline__', Date.now() / 1000 + 5);
          const actual = toPlainJs(fn(...args));
          return { expected, actual };
        } catch {
          return { expected, error: true };
        } finally {
          try { pyodideRef.value?.globals.delete('__cell_deadline__'); } catch { /* ignore */ }
        }
      });

      const valid = validateOutput(result.output, challenge.value?.validation, actualVars, functionResults);
      if (valid) {
        markCodingPassed(props.weekNumber, props.challengeIndex);
        feedback.value = {
          success: true,
          message: t('challenge.passedMessage'),
        };
      } else {
        feedback.value = {
          success: false,
          message: t('challenge.notYetMessage'),
        };
      }
      checking.value = false;
    };

    return {
      lang,
      t,
      kernelReady,
      kernelStatus,
      initializeKernel,
      challenge,
      instruction,
      title,
      alreadyPassed,
      code,
      output,
      feedback,
      checking,
      runCode,
      checkCode,
    };
  },
};
</script>

<style scoped>
.code-challenge {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px dashed #dee2e6;
}

.challenge-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.challenge-header h4 {
  margin: 0;
  color: var(--primary-purple, #4a2274);
}

.challenge-badge {
  background: #d4edda;
  color: #155724;
  font-size: 0.75em;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 10px;
}

.challenge-instruction {
  margin: 0 0 12px 0;
  color: #444;
  line-height: 1.5;
}

.challenge-editor-header {
  margin-bottom: 10px;
}

.btn-kernel {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 500;
}

.btn-kernel:disabled {
  background: #28a745;
  cursor: default;
}

.code-editor {
  width: 100%;
  max-width: 500px;
  min-height: 70px;
  padding: 12px;
  box-sizing: border-box;
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 14px;
  line-height: 1.5;
  resize: vertical;
  margin-bottom: 10px;
  display: block;
}

.challenge-actions {
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}

.btn-run,
.btn-check {
  border: none;
  padding: 8px 18px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9em;
  font-weight: 600;
}

.btn-run {
  background: #6c757d;
  color: white;
}

.btn-run:disabled,
.btn-check:disabled {
  background: #adb5bd;
  cursor: not-allowed;
}

.btn-check {
  background: var(--accent-orange, #ff9800);
  color: white;
}

.challenge-output {
  margin-bottom: 10px;
  padding: 10px 12px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
}

.challenge-output strong {
  display: block;
  margin-bottom: 6px;
  font-size: 0.85em;
  color: #555;
}

.challenge-output pre {
  margin: 0;
  font-family: 'Courier New', Consolas, Monaco, monospace;
  font-size: 0.9em;
  white-space: pre-wrap;
  word-break: break-word;
}

.challenge-feedback {
  padding: 10px 14px;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.9em;
}

.feedback-success {
  background: #d4edda;
  color: #155724;
}

.feedback-error {
  background: #f8d7da;
  color: #721c24;
}

.kernel-status {
  margin-top: 8px;
  font-size: 0.85em;
  color: #6c757d;
}
</style>
