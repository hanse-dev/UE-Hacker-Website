<template>
  <div class="code-challenge web-code-challenge" :data-challenge-index="challengeIndex" v-if="challenge">
    <div class="challenge-header">
      <h4>{{ title }}</h4>
      <span v-if="alreadyPassed" class="challenge-badge">{{ t('challenge.passed') }}</span>
    </div>
    <p class="challenge-instruction">{{ instruction }}</p>

    <JsCodeCell v-model="code" language="html" />
    <div class="challenge-actions">
      <button @click="runCode" :disabled="checking" class="btn-run">
        {{ t('editor.run') }}
      </button>
      <button @click="checkCode" :disabled="checking" class="btn-check">
        {{ checking ? t('editor.checking') : t('editor.check') }}
      </button>
      <button
        v-if="challenge.codeTemplate && code !== challenge.codeTemplate"
        @click="resetCode"
        :disabled="checking"
        class="btn-reset"
      >
        {{ t('editor.reset') }}
      </button>
    </div>
    <!-- Vorschau erst nach dem ersten Lauf (wie die Arbeitsflaeche in JsLessonView.vue) - ein
         gemountetes Frame startet eine dauerhaft laufende Heartbeat-Schleife. -->
    <JsSandboxFrame v-if="ran" ref="sandboxEl" :web-mode="true" />
    <div v-if="output" class="challenge-output">
      <strong>{{ t('editor.output') }}</strong>
      <pre>{{ output }}</pre>
    </div>
    <div v-if="feedback" :class="['challenge-feedback', feedback.success ? 'feedback-success' : 'feedback-error']">
      {{ feedback.message }}
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch, nextTick } from 'vue';
import JsCodeCell from './JsCodeCell.vue';
import JsSandboxFrame from './JsSandboxFrame.vue';
import { useWeekChecks, loadWeekChecks } from '../composables/useWeekChecks';
import { validateWebChecks } from '../composables/useTaskValidation';
import { DEV_SKIP_CHECKS } from '../composables/devSkipChecks.js';
import { useLanguage } from '../composables/useLanguage';

/**
 * Coding-Aufgabe im Check fuer die Web-Kurse (`WeekCheckPanel.vue` mit `engine="web"`): wie
 * CodeChallenge.vue, aber HTML statt Python - Editor mit lang-html, Vorschau als Web-Sandbox,
 * Pruefung ueber `validation.type: 'web'` (validateWebChecks). Fortschritt landet im selben
 * Wochen-Check-Speicher (`markCodingPassed`), damit Zertifikat und Profil ohne Sonderfall gelten.
 */
export default {
  name: 'WebCodeChallenge',
  components: { JsCodeCell, JsSandboxFrame },
  props: {
    weekNumber: { type: Number, required: true },
    challengeIndex: { type: Number, default: 0 },
    label: { type: String, default: '' },
    courseKey: { type: String, required: true },
  },
  setup(props) {
    const { lang, t } = useLanguage();
    const { markCodingPassed, isCodingChallengePassed } = useWeekChecks(props.courseKey);

    const challenge = ref(null);
    const code = ref('');
    const output = ref('');
    const feedback = ref(null);
    const checking = ref(false);
    const ran = ref(false);
    const sandboxEl = ref(null);
    const attempts = ref(0);

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
      } catch {
        challenge.value = null;
      }
    };
    onMounted(load);
    watch(() => [props.weekNumber, props.challengeIndex], () => {
      output.value = '';
      feedback.value = null;
      load();
    });

    const resetCode = () => {
      code.value = challenge.value?.codeTemplate ?? '';
      output.value = '';
      feedback.value = null;
    };

    const render = async () => {
      ran.value = true;
      await nextTick();
      const result = await sandboxEl.value.run(code.value);
      output.value = result.success
        ? (result.output || '').trim()
        : t('editor.errorPrefix') + (result.error || '');
      return result;
    };

    const runCode = async () => {
      checking.value = true;
      feedback.value = null;
      await render();
      checking.value = false;
    };

    const checkCode = async () => {
      checking.value = true;
      feedback.value = null;
      const validation = challenge.value?.validation || {};
      let ok;
      let hint = '';
      if (DEV_SKIP_CHECKS) {
        ok = validateWebChecks(validation, null).ok;
      } else {
        const result = await render();
        const facts = result.success ? await sandboxEl.value.checkWeb(validation.checks || []) : null;
        const webResult = validateWebChecks(validation, facts);
        ok = webResult.ok;
        hint = validation.checks?.[webResult.failedIndex]?.hint || '';
      }
      if (ok) {
        markCodingPassed(props.weekNumber, props.challengeIndex);
        feedback.value = { success: true, message: t('challenge.passedMessage') };
      } else {
        attempts.value += 1;
        // Wie in den Lektionen: erst ein sanfter Hinweis, ab dem zweiten Versuch der konkrete.
        feedback.value = {
          success: false,
          message: attempts.value >= 2 && hint ? hint : t('webChallenge.notYet'),
        };
      }
      checking.value = false;
    };

    return {
      t, challenge, instruction, title, alreadyPassed, code, output, feedback, checking, ran,
      sandboxEl, runCode, checkCode, resetCode,
    };
  },
};
</script>

<style scoped>
.code-challenge {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px dashed var(--border);
}

.challenge-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}

.challenge-header h4 {
  margin: 0;
  color: var(--brand-text);
}

.challenge-badge {
  background: var(--success-bg);
  color: var(--success-text);
  font-size: 0.75em;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 10px;
}

.challenge-instruction {
  margin: 0 0 12px 0;
  color: var(--text-muted);
  line-height: 1.5;
}

.challenge-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
}

.btn-run,
.btn-check,
.btn-reset {
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

.btn-check {
  background: var(--accent-orange, #ff9800);
  color: white;
}

.btn-reset {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.btn-run:disabled,
.btn-check:disabled {
  background: #adb5bd;
  cursor: not-allowed;
}

.challenge-output {
  margin-bottom: 10px;
  padding: 10px;
  background: var(--surface-muted);
  border: 1px solid var(--border);
  border-radius: 6px;
}

.challenge-output pre {
  margin: 6px 0 0 0;
  white-space: pre-wrap;
}

.challenge-feedback {
  padding: 10px 14px;
  border-radius: 6px;
  font-weight: 500;
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
</style>
