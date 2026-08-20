<template>
  <div class="placement-course">
    <div v-if="loading" class="loading">{{ lang === 'en' ? 'Loading…' : 'Lade…' }}</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <template v-else-if="!showResults">
      <div class="placement-intro">
        <h2>{{ lang === 'en' ? 'Where should I start?' : 'Wo soll ich starten?' }}</h2>
        <p>
          {{ lang === 'en'
            ? 'Answer a few questions from different weeks. We recommend which week to open next — you can jump there directly.'
            : 'Beantworte ein paar Fragen aus verschiedenen Wochen. Wir empfehlen dir, welche Woche als Nächstes sinnvoll ist — und du kannst direkt hinspringen.' }}
        </p>
      </div>
      <QuizStep
        v-if="questions.length"
        :questions="questions"
        :pass-threshold="0"
        :lang="lang"
        @completed="onSubmit"
        @failed="onSubmit"
      />
    </template>

    <div v-else class="placement-results">
      <h2>{{ lang === 'en' ? 'Your result' : 'Dein Ergebnis' }}</h2>
      <p class="results-intro">
        {{ lang === 'en'
          ? 'Green = looks good. Orange = worth reviewing that week.'
          : 'Grün = sieht gut aus. Orange = diese Woche lohnt sich zum Wiederholen.' }}
      </p>

      <ul class="week-results">
        <li
          v-for="row in weekResults"
          :key="row.weekNumber"
          :class="['week-result', row.ok ? 'ok' : 'review']"
        >
          <div class="week-result-text">
            <strong>{{ row.title }}</strong>
            <span>{{ row.correct }}/{{ row.total }}
              ({{ Math.round(row.score * 100) }}%)</span>
          </div>
          <router-link
            class="week-jump"
            :to="{
              path: '/kurs/python-12-wochen-grundkurs',
              query: { week: String(row.weekNumber), tab: 'lektion' },
              hash: `#woche-${row.weekNumber}`,
            }"
          >
            {{ lang === 'en' ? 'Open week →' : 'Woche öffnen →' }}
          </router-link>
        </li>
      </ul>

      <div v-if="allPassed" class="projects-block">
        <h3>
          {{ lang === 'en'
            ? 'Everything looks strong — try a project!'
            : 'Alles sitzt — Zeit für ein eigenes Projekt!' }}
        </h3>
        <p class="projects-intro">
          {{ lang === 'en'
            ? 'Here are three ideas that use what you learned in the 12-week course:'
            : 'Hier sind drei Ideen, die das aus dem 12-Wochen-Kurs nutzen:' }}
        </p>
        <ul class="project-list">
          <li v-for="p in projects" :key="p.id" class="project-card">
            <strong>{{ p.title }}</strong>
            <p>{{ p.description }}</p>
            <p v-if="p.skills?.length" class="project-skills">
              {{ lang === 'en' ? 'Uses:' : 'Nutzt:' }}
              {{ p.skills.join(' · ') }}
            </p>
          </li>
        </ul>
      </div>

      <p v-else-if="recommendedWeek" class="recommend">
        {{ lang === 'en' ? 'Suggested start:' : 'Empfohlener Start:' }}
        <router-link
          :to="{
            path: '/kurs/python-12-wochen-grundkurs',
            query: { week: String(recommendedWeek.weekNumber), tab: 'lektion' },
            hash: `#woche-${recommendedWeek.weekNumber}`,
          }"
        >
          {{ recommendedWeek.title }}
        </router-link>
      </p>

      <button type="button" class="btn-retry" @click="reset">
        {{ lang === 'en' ? 'Retake placement' : 'Einstufung wiederholen' }}
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue';
import QuizStep from './QuizStep.vue';
import {
  loadWeekChecks,
  getPlacementQuestions,
  getProjectIdeas,
  useWeekChecks,
  scoreQuizAnswers,
  isQuizPassed,
} from '../composables/useWeekChecks';
import { useLanguage } from '../composables/useLanguage';

export default {
  name: 'PlacementCourse',
  components: { QuizStep },
  setup() {
    const { lang } = useLanguage();
    const { savePlacementResult, placementResult } = useWeekChecks();
    const data = ref(null);
    const loading = ref(true);
    const error = ref(null);
    const weekResults = ref([]);
    const showResults = ref(false);
    const questions = ref([]);

    const threshold = computed(() => data.value?.passThreshold ?? 0.8);
    const projects = computed(() =>
      data.value ? getProjectIdeas(data.value, lang.value) : []
    );

    const allPassed = computed(
      () => weekResults.value.length > 0 && weekResults.value.every((r) => r.ok)
    );

    const recommendedWeek = computed(() => {
      if (allPassed.value) return null;
      const weak = weekResults.value.filter((r) => !r.ok);
      if (weak.length) return weak.sort((a, b) => a.weekNumber - b.weekNumber)[0];
      return null;
    });

    const pickQuestions = () => {
      questions.value = data.value
        ? getPlacementQuestions(data.value, lang.value)
        : [];
    };

    const restoreResults = () => {
      if (!placementResult.value?.completed || !placementResult.value.weekScores) {
        return false;
      }
      weekResults.value = Object.entries(placementResult.value.weekScores).map(
        ([weekNumber, s]) => ({
          weekNumber: Number(weekNumber),
          title: s.title,
          score: s.score,
          correct: s.correct,
          total: s.total,
          ok: isQuizPassed(s.score, threshold.value),
        })
      ).sort((a, b) => a.weekNumber - b.weekNumber);
      showResults.value = weekResults.value.length > 0;
      return showResults.value;
    };

    const load = async () => {
      loading.value = true;
      error.value = null;
      try {
        data.value = await loadWeekChecks();
        if (!restoreResults()) {
          pickQuestions();
        }
      } catch (e) {
        console.error(e);
        error.value = lang.value === 'en'
          ? 'Could not load placement.'
          : 'Einstufung konnte nicht geladen werden.';
      } finally {
        loading.value = false;
      }
    };

    const onSubmit = (payload) => {
      const qs = questions.value;
      const answers = payload?.answers || [];
      const byWeek = {};

      qs.forEach((q, i) => {
        const w = q.weekNumber;
        if (!byWeek[w]) byWeek[w] = { questions: [], answers: [], title: q.weekTitle };
        byWeek[w].questions.push(q);
        byWeek[w].answers.push(answers[i]);
      });

      const scores = {};
      const rows = [];
      for (const [weekNumber, group] of Object.entries(byWeek)) {
        const result = scoreQuizAnswers(group.questions, group.answers);
        scores[weekNumber] = {
          ...result,
          title: group.title,
        };
        rows.push({
          weekNumber: Number(weekNumber),
          title: group.title,
          score: result.score,
          correct: result.correct,
          total: result.total,
          ok: isQuizPassed(result.score, threshold.value),
        });
      }

      rows.sort((a, b) => a.weekNumber - b.weekNumber);
      weekResults.value = rows;
      savePlacementResult(scores);
      showResults.value = true;
    };

    const reset = () => {
      showResults.value = false;
      weekResults.value = [];
      savePlacementResult(null);
      pickQuestions();
    };

    onMounted(load);
    watch(lang, () => {
      if (!showResults.value) pickQuestions();
    });

    return {
      lang,
      loading,
      error,
      questions,
      showResults,
      weekResults,
      recommendedWeek,
      allPassed,
      projects,
      onSubmit,
      reset,
    };
  },
};
</script>

<style scoped>
.placement-course {
  max-width: 800px;
  margin: 0 auto;
  padding: 12px 0 40px;
}

.loading, .error {
  padding: 40px;
  text-align: center;
}

.error {
  color: #dc3545;
  background: #f8d7da;
  border-radius: 8px;
}

.placement-intro h2 {
  margin: 0 0 8px 0;
}

.placement-intro p {
  color: #555;
  margin: 0 0 20px 0;
  line-height: 1.5;
}

.placement-results h2 {
  margin: 0 0 8px 0;
}

.results-intro {
  color: #555;
  margin: 0 0 20px 0;
}

.week-results {
  list-style: none;
  padding: 0;
  margin: 0 0 24px 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.week-result {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 10px;
  border: 2px solid #dee2e6;
  background: #fff;
}

.week-result.ok {
  border-color: #28a745;
  background: #f8fff9;
}

.week-result.review {
  border-color: #ff9800;
  background: #fff8f0;
}

.week-result-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.week-result-text span {
  font-size: 0.9em;
  color: #555;
}

.week-jump {
  background: var(--primary-purple, #4a2274);
  color: white;
  text-decoration: none;
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9em;
}

.recommend {
  margin: 0 0 20px 0;
  font-weight: 600;
}

.recommend a {
  color: var(--primary-purple, #4a2274);
}

.projects-block {
  margin: 0 0 24px 0;
  padding: 18px;
  border-radius: 12px;
  background: #f3eef8;
  border: 2px solid #c4a8e0;
}

.projects-block h3 {
  margin: 0 0 8px 0;
  color: var(--primary-purple, #4a2274);
}

.projects-intro {
  margin: 0 0 14px 0;
  color: #555;
  line-height: 1.45;
}

.project-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.project-card {
  background: #fff;
  border-radius: 10px;
  padding: 14px 16px;
  border: 1px solid #e0d4ef;
}

.project-card strong {
  display: block;
  margin-bottom: 6px;
  color: #2d1b4e;
}

.project-card p {
  margin: 0;
  color: #444;
  line-height: 1.45;
  font-size: 0.95em;
}

.project-skills {
  margin-top: 8px !important;
  font-size: 0.85em !important;
  color: #6c5a7a !important;
}

.btn-retry {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
}
</style>
