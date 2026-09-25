<template>
  <div class="week-check-panel">
    <p v-if="loading" class="check-loading">{{ t('check.loading') }}</p>
    <p v-else-if="!questions.length" class="check-empty">
      {{ t('check.empty') }}
    </p>
    <template v-else>
      <div class="check-intro">
        <h3>{{ t('check.title') }}</h3>
        <p>
          {{ t('check.intro') }}
        </p>
        <span v-if="alreadyPassed" class="check-badge">{{ t('check.alreadyPassed') }}</span>
      </div>
      <QuizStep
        :questions="questions"
        :pass-threshold="passThreshold"
        :lang="lang"
        @completed="onPassed"
        @failed="onFailed"
      />
      <CodeChallenge :week-number="weekNumber" :challenge-index="0" :label="t('check.challenge.easy')" :course-key="courseKey" />
      <CodeChallenge :week-number="weekNumber" :challenge-index="1" :label="t('check.challenge.harder')" :course-key="courseKey" />
      <p v-if="quizPassed && codingPassed" class="check-fully-done">
        {{ t('check.fullyDone') }}
      </p>
    </template>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import QuizStep from './QuizStep.vue';
import CodeChallenge from './CodeChallenge.vue';
import { loadWeekChecks, getWeekQuestions, useWeekChecks } from '../composables/useWeekChecks';
import { useLanguage } from '../composables/useLanguage';

export default {
  name: 'WeekCheckPanel',
  components: { QuizStep, CodeChallenge },
  props: {
    weekNumber: { type: Number, required: true },
    courseKey: { type: String, default: 'python' },
  },
  setup(props) {
    const { lang, t } = useLanguage();
    const { markQuizPassed, isWeekCheckPassed, isQuizPassedForWeek, isCodingPassedForWeek } = useWeekChecks(props.courseKey);
    const data = ref(null);
    const loading = ref(true);
    const questions = ref([]);

    const passThreshold = computed(() => data.value?.passThreshold ?? 0.8);
    const alreadyPassed = computed(() => isWeekCheckPassed(props.weekNumber));
    const quizPassed = computed(() => isQuizPassedForWeek(props.weekNumber));
    const codingPassed = computed(() => isCodingPassedForWeek(props.weekNumber));

    const pickQuestions = () => {
      questions.value = data.value
        ? getWeekQuestions(data.value, props.weekNumber, lang.value)
        : [];
    };

    const load = async () => {
      loading.value = true;
      try {
        data.value = await loadWeekChecks(props.courseKey);
        pickQuestions();
      } catch (e) {
        console.error(e);
        data.value = null;
        questions.value = [];
      } finally {
        loading.value = false;
      }
    };

    onMounted(load);
    watch(() => props.weekNumber, load);
    watch(lang, () => {
      if (data.value) pickQuestions();
    });

    const onPassed = (result) => {
      markQuizPassed(props.weekNumber, result);
    };

    const onFailed = () => {};

    return {
      lang,
      t,
      loading,
      questions,
      passThreshold,
      alreadyPassed,
      quizPassed,
      codingPassed,
      onPassed,
      onFailed,
    };
  },
};
</script>

<style scoped>
.week-check-panel {
  background: #fff;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  padding: 20px;
  margin-top: 8px;
}

.check-intro {
  margin-bottom: 16px;
}

.check-intro h3 {
  margin: 0 0 6px 0;
  color: var(--primary-purple, #4a2274);
}

.check-intro p {
  margin: 0;
  color: #555;
  font-size: 0.95em;
}

.check-badge {
  display: inline-block;
  margin-top: 10px;
  background: #d4edda;
  color: #155724;
  font-size: 0.8em;
  font-weight: 700;
  padding: 2px 10px;
  border-radius: 10px;
}

.check-fully-done {
  margin: 16px 0 0 0;
  padding: 12px 16px;
  background: #fff3cd;
  border: 1px solid #ffe69c;
  border-radius: 8px;
  font-weight: 600;
  color: #664d03;
}

.check-loading,
.check-empty {
  color: #6c757d;
  font-style: italic;
}
</style>
