<template>
  <div class="week-check-panel">
    <p v-if="loading" class="check-loading">{{ lang === 'en' ? 'Loading check…' : 'Check wird geladen…' }}</p>
    <p v-else-if="!questions.length" class="check-empty">
      {{ lang === 'en' ? 'No check questions for this week yet.' : 'Für diese Woche gibt es noch keinen Check.' }}
    </p>
    <template v-else>
      <div class="check-intro">
        <h3>{{ lang === 'en' ? 'Understanding check' : 'Verständnis-Check' }}</h3>
        <p>
          {{ lang === 'en'
            ? 'Short quiz for this week\'s topics. Pass with 80%+.'
            : 'Kurzer Test zu den Themen dieser Woche. Bestehen mit 80%+.' }}
        </p>
        <span v-if="alreadyPassed" class="check-badge">{{ lang === 'en' ? 'Already passed' : 'Bereits bestanden' }}</span>
      </div>
      <QuizStep
        :questions="questions"
        :pass-threshold="passThreshold"
        :lang="lang"
        @completed="onPassed"
        @failed="onFailed"
      />
    </template>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import QuizStep from './QuizStep.vue';
import { loadWeekChecks, getWeekQuestions, useWeekChecks } from '../composables/useWeekChecks';
import { useLanguage } from '../composables/useLanguage';

export default {
  name: 'WeekCheckPanel',
  components: { QuizStep },
  props: {
    weekNumber: { type: Number, required: true },
  },
  setup(props) {
    const { lang } = useLanguage();
    const { markWeekPassed, isWeekCheckPassed } = useWeekChecks();
    const data = ref(null);
    const loading = ref(true);
    const questions = ref([]);

    const passThreshold = computed(() => data.value?.passThreshold ?? 0.8);
    const alreadyPassed = computed(() => isWeekCheckPassed(props.weekNumber));

    const pickQuestions = () => {
      questions.value = data.value
        ? getWeekQuestions(data.value, props.weekNumber, lang.value)
        : [];
    };

    const load = async () => {
      loading.value = true;
      try {
        data.value = await loadWeekChecks();
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
      markWeekPassed(props.weekNumber, result);
    };

    const onFailed = () => {};

    return {
      lang,
      loading,
      questions,
      passThreshold,
      alreadyPassed,
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

.check-loading,
.check-empty {
  color: #6c757d;
  font-style: italic;
}
</style>
