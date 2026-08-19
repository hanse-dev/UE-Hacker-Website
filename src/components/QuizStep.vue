<template>
  <div class="quiz-step">
    <h4 v-if="title" class="quiz-step-title">{{ title }}</h4>

    <div
      v-for="(q, qIdx) in questions"
      :key="q.id || qIdx"
      class="quiz-question"
      :class="{ answered: answers[qIdx] !== null && answers[qIdx] !== undefined, correct: feedback[qIdx]?.correct, incorrect: feedback[qIdx] && !feedback[qIdx].correct }"
    >
      <p class="question-text">
        <span class="question-num">{{ qIdx + 1 }}.</span>
        {{ questionText(q) }}
      </p>

      <div v-if="q.type === 'true_false'" class="options tf-options">
        <button
          type="button"
          class="option-btn"
          :class="{ selected: answers[qIdx] === true, correct: showResults && q.correct === true, wrong: showResults && answers[qIdx] === true && q.correct !== true }"
          :disabled="submitted"
          @click="selectAnswer(qIdx, true)"
        >
          {{ lang === 'en' ? 'True' : 'Wahr' }}
        </button>
        <button
          type="button"
          class="option-btn"
          :class="{ selected: answers[qIdx] === false, correct: showResults && q.correct === false, wrong: showResults && answers[qIdx] === false && q.correct !== false }"
          :disabled="submitted"
          @click="selectAnswer(qIdx, false)"
        >
          {{ lang === 'en' ? 'False' : 'Falsch' }}
        </button>
      </div>

      <div v-else class="options mc-options">
        <button
          v-for="(opt, oIdx) in q.options"
          :key="oIdx"
          type="button"
          class="option-btn option-block"
          :class="{ selected: answers[qIdx] === oIdx, correct: showResults && q.correctIndex === oIdx, wrong: showResults && answers[qIdx] === oIdx && q.correctIndex !== oIdx }"
          :disabled="submitted"
          @click="selectAnswer(qIdx, oIdx)"
        >
          {{ opt }}
        </button>
      </div>

      <p v-if="feedback[qIdx]" :class="['question-feedback', feedback[qIdx].correct ? 'feedback-ok' : 'feedback-no']">
        {{ feedback[qIdx].message }}
      </p>
    </div>

    <div class="quiz-actions">
      <button
        v-if="!submitted"
        type="button"
        class="btn-check-quiz"
        :disabled="!allAnswered"
        @click="submitQuiz"
      >
        {{ lang === 'en' ? 'Check answers' : 'Antworten prüfen' }}
      </button>
      <div v-else-if="passed" class="quiz-result quiz-pass">
        {{ lang === 'en' ? `Correct! ${scoreResult.correct}/${scoreResult.total}` : `Richtig! ${scoreResult.correct}/${scoreResult.total}` }}
      </div>
      <div v-else class="quiz-result quiz-fail">
        {{ lang === 'en' ? `Not quite: ${scoreResult.correct}/${scoreResult.total}. Try again!` : `Noch nicht: ${scoreResult.correct}/${scoreResult.total}. Versuch es nochmal!` }}
        <button type="button" class="btn-retry" @click="retry">{{ lang === 'en' ? 'Retry' : 'Nochmal' }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import { scoreQuizAnswers, isQuizPassed } from '../composables/useTaskValidation';

export default {
  name: 'QuizStep',
  props: {
    questions: { type: Array, required: true },
    title: { type: String, default: '' },
    passThreshold: { type: Number, default: 1 },
    lang: { type: String, default: 'de' },
  },
  emits: ['completed', 'failed'],
  setup(props, { emit }) {
    const answers = ref([]);
    const feedback = ref([]);
    const submitted = ref(false);
    const scoreResult = ref({ score: 0, correct: 0, total: 0 });

    const initAnswers = () => {
      answers.value = props.questions.map(() => null);
      feedback.value = props.questions.map(() => null);
      submitted.value = false;
      scoreResult.value = { score: 0, correct: 0, total: 0 };
    };

    watch(() => props.questions, initAnswers, { immediate: true });

    const allAnswered = computed(() =>
      answers.value.every((a) => a !== null && a !== undefined)
    );

    const passed = computed(() =>
      submitted.value && isQuizPassed(scoreResult.value.score, props.passThreshold)
    );

    const showResults = computed(() => submitted.value);

    const questionText = (q) => {
      if (props.lang === 'en' && q.question_en) return q.question_en;
      return q.question;
    };

    const selectAnswer = (qIdx, value) => {
      if (submitted.value) return;
      const next = [...answers.value];
      next[qIdx] = value;
      answers.value = next;
    };

    const buildFeedback = () => {
      feedback.value = props.questions.map((q, i) => {
        const a = answers.value[i];
        let correct = false;
        if (q.type === 'true_false') correct = a === q.correct;
        else correct = a === q.correctIndex;
        const expl = props.lang === 'en' && q.explanation_en ? q.explanation_en : q.explanation;
        return {
          correct,
          message: correct
            ? (expl || (props.lang === 'en' ? 'Correct!' : 'Richtig!'))
            : (expl || (props.lang === 'en' ? 'Not quite – check again.' : 'Noch nicht ganz – schau nochmal hin.')),
        };
      });
    };

    const submitQuiz = () => {
      if (!allAnswered.value) return;
      scoreResult.value = scoreQuizAnswers(props.questions, answers.value);
      buildFeedback();
      submitted.value = true;
      const payload = { ...scoreResult.value, answers: [...answers.value] };
      if (isQuizPassed(scoreResult.value.score, props.passThreshold)) {
        emit('completed', payload);
      } else {
        emit('failed', payload);
      }
    };

    const retry = () => initAnswers();

    return {
      answers,
      feedback,
      submitted,
      scoreResult,
      allAnswered,
      passed,
      showResults,
      questionText,
      selectAnswer,
      submitQuiz,
      retry,
    };
  },
};
</script>

<style scoped>
.quiz-step {
  margin-bottom: 20px;
}

.quiz-step-title {
  margin: 0 0 16px 0;
  color: var(--primary-purple, #4a2274);
  font-size: 1.05em;
}

.quiz-question {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 12px;
}

.quiz-question.correct {
  border-color: #28a745;
  background: #f8fff9;
}

.quiz-question.incorrect {
  border-color: #dc3545;
  background: #fff8f8;
}

.question-text {
  margin: 0 0 12px 0;
  font-weight: 600;
  line-height: 1.4;
}

.question-num {
  color: var(--primary-purple, #4a2274);
  margin-right: 4px;
}

.options {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.mc-options {
  flex-direction: column;
}

.option-btn {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 6px;
  padding: 10px 16px;
  cursor: pointer;
  font-size: 0.95em;
  text-align: left;
  transition: border-color 0.15s, background 0.15s;
}

.option-btn:hover:not(:disabled) {
  border-color: var(--primary-purple, #4a2274);
}

.option-btn.selected {
  border-color: var(--primary-purple, #4a2274);
  background: rgba(74, 34, 116, 0.08);
}

.option-btn.correct {
  border-color: #28a745;
  background: #d4edda;
}

.option-btn.wrong {
  border-color: #dc3545;
  background: #f8d7da;
}

.option-btn:disabled {
  cursor: default;
}

.option-block {
  width: 100%;
}

.question-feedback {
  margin: 10px 0 0 0;
  font-size: 0.9em;
  padding: 8px 10px;
  border-radius: 4px;
}

.feedback-ok {
  background: #d4edda;
  color: #155724;
}

.feedback-no {
  background: #fff3cd;
  color: #856404;
}

.quiz-actions {
  margin-top: 8px;
}

.btn-check-quiz {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
}

.btn-check-quiz:disabled {
  background: #adb5bd;
  cursor: not-allowed;
}

.quiz-result {
  padding: 12px 16px;
  border-radius: 6px;
  font-weight: 600;
}

.quiz-pass {
  background: #d4edda;
  color: #155724;
}

.quiz-fail {
  background: #fff3cd;
  color: #856404;
}

.btn-retry {
  margin-left: 12px;
  background: transparent;
  border: 1px solid #856404;
  color: #856404;
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
}
</style>
