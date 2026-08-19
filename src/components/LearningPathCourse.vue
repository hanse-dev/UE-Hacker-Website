<template>
  <div class="learning-path-course">
    <!-- Variant selector -->
    <div v-if="!variant" class="variant-selector">
      <h2>{{ lang === 'en' ? 'Who is this path for?' : 'Für wen ist der Lernpfad?' }}</h2>
      <p class="variant-intro">
        {{ lang === 'en' ? 'Choose your version – you can switch later.' : 'Wähle deine Version – du kannst später wechseln.' }}
      </p>
      <div class="variant-cards">
        <button class="variant-card" @click="selectVariant('kinder')">
          <span class="variant-icon">🌟</span>
          <strong>{{ lang === 'en' ? 'For Kids' : 'Für Kinder' }}</strong>
          <span class="variant-age">{{ lang === 'en' ? '8–12 years' : '8–12 Jahre' }}</span>
        </button>
        <button class="variant-card" @click="selectVariant('jugendliche')">
          <span class="variant-icon">🚀</span>
          <strong>{{ lang === 'en' ? 'For Teenagers' : 'Für Jugendliche' }}</strong>
          <span class="variant-age">{{ lang === 'en' ? '13–17 years' : '13–17 Jahre' }}</span>
        </button>
      </div>
    </div>

    <template v-else>
      <div v-if="loading" class="loading">{{ lang === 'en' ? 'Loading...' : 'Lade...' }}</div>
      <div v-else-if="error" class="error">{{ error }}</div>

      <!-- Placement test -->
      <div v-else-if="showPlacement" class="placement-section">
        <h2>{{ placementTitle }}</h2>
        <p class="placement-intro">{{ placementIntro }}</p>
        <QuizStep
          :questions="placementQuestions"
          :pass-threshold="0"
          :lang="lang"
          @completed="onPlacementSubmit"
          @failed="onPlacementSubmit"
        />
        <button type="button" class="btn-skip-placement" @click="skipPlacement">
          {{ lang === 'en' ? 'Skip placement – show all topics' : 'Einstufung überspringen – alle Themen zeigen' }}
        </button>
      </div>

      <!-- Topic detail -->
      <TopicModuleView
        v-else-if="activeTopic"
        :topic="activeTopic"
        :variant="variant"
        :lang="lang"
        @back="activeTopicId = null"
        @completed="onTopicFinished"
        @skipped="onTopicFinished"
      />

      <!-- Dashboard -->
      <div v-else class="dashboard">
        <div class="dashboard-header">
          <div>
            <h2>{{ lang === 'en' ? 'Your Learning Path' : 'Dein Lernpfad' }}</h2>
            <p class="progress-text">
              {{ completedCount }} / {{ topics.length }}
              {{ lang === 'en' ? 'topics done' : 'Themen geschafft' }}
            </p>
          </div>
          <button type="button" class="btn-switch" @click="switchVariant">
            {{ lang === 'en' ? 'Switch version' : 'Version wechseln' }}
          </button>
        </div>

        <div class="progress-track-wrap">
          <div class="progress-track">
            <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
          </div>
        </div>

        <section v-if="recommendedTopics.length" class="topic-section recommended-section">
          <h3>{{ lang === 'en' ? 'Recommended for you' : 'Empfohlen für dich' }}</h3>
          <div class="topic-cards">
            <button
              v-for="topic in recommendedTopics"
              :key="'rec-' + topic.id"
              type="button"
              class="topic-card recommended"
              @click="openTopic(topic.id)"
            >
              <span class="topic-card-title">{{ topicLabel(topic) }}</span>
              <span class="topic-card-summary">{{ topicSummary(topic) }}</span>
              <span class="topic-badge badge-recommended">{{ lang === 'en' ? 'Recommended' : 'Empfohlen' }}</span>
            </button>
          </div>
        </section>

        <section class="topic-section">
          <h3>{{ lang === 'en' ? 'All topics' : 'Alle Themen' }}</h3>
          <div class="topic-cards">
            <button
              v-for="topic in topics"
              :key="topic.id"
              type="button"
              class="topic-card"
              :class="statusClass(topic.id)"
              @click="openTopic(topic.id)"
            >
              <span class="topic-card-title">{{ topicLabel(topic) }}</span>
              <span class="topic-card-summary">{{ topicSummary(topic) }}</span>
              <span class="topic-badge" :class="'badge-' + getTopicStatus(topic.id)">
                {{ statusLabel(topic.id) }}
              </span>
            </button>
          </div>
        </section>

        <div class="dashboard-actions">
          <button type="button" @click="exportProgress" class="btn-export">
            {{ lang === 'en' ? 'Export progress' : 'Fortschritt exportieren' }}
          </button>
          <label class="btn-import">
            {{ lang === 'en' ? 'Import' : 'Importieren' }}
            <input type="file" accept=".json" class="file-input" @change="onImportFile" />
          </label>
          <button type="button" @click="retakePlacement" class="btn-retake">
            {{ lang === 'en' ? 'Retake placement' : 'Einstufung wiederholen' }}
          </button>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import TopicModuleView from './TopicModuleView.vue';
import QuizStep from './QuizStep.vue';
import { useLearnerProgress } from '../composables/useLearnerProgress';
import { scoreQuizAnswers, isQuizPassed } from '../composables/useTaskValidation';
import { useLanguage } from '../composables/useLanguage';

const VARIANT_STORAGE_KEY = 'ue-hacker-lernpfad-variant';

const topicModules = import.meta.glob([
  '../../content/python-lernpfad/topics-kinder.json',
  '../../content/python-lernpfad/topics-jugendliche.json',
]);

const placementModules = import.meta.glob([
  '../../content/python-lernpfad/placement-kinder.json',
  '../../content/python-lernpfad/placement-jugendliche.json',
]);

export default {
  name: 'LearningPathCourse',
  components: { TopicModuleView, QuizStep },
  setup() {
    const { lang } = useLanguage();
    const route = useRoute();
    const variant = ref(localStorage.getItem(VARIANT_STORAGE_KEY) || null);
    const topics = ref([]);
    const placementData = ref(null);
    const loading = ref(false);
    const error = ref(null);
    const activeTopicId = ref(null);

    const progressKinder = useLearnerProgress('kinder');
    const progressJugendliche = useLearnerProgress('jugendliche');

    const progress = computed(() =>
      variant.value === 'jugendliche' ? progressJugendliche : progressKinder
    );

    const completedCount = computed(() => progress.value.completedCount.value);

    const recommendedTopics = computed(() =>
      progress.value.getRecommendedTopics(topics.value, 2)
    );

    const showPlacement = computed(() =>
      variant.value
      && placementData.value
      && !progress.value.state.value.placementCompleted
    );

    const activeTopic = computed(() =>
      topics.value.find((t) => t.id === activeTopicId.value) || null
    );

    const progressPercent = computed(() => {
      if (!topics.value.length) return 0;
      return Math.round((completedCount.value / topics.value.length) * 100);
    });

    const placementTitle = computed(() => {
      if (!placementData.value) return '';
      return lang.value === 'en' && placementData.value.title_en
        ? placementData.value.title_en
        : placementData.value.title;
    });

    const placementIntro = computed(() => {
      if (!placementData.value) return '';
      return lang.value === 'en' && placementData.value.intro_en
        ? placementData.value.intro_en
        : placementData.value.intro;
    });

    const placementQuestions = computed(() => placementData.value?.questions || []);

    const loadContent = async () => {
      if (!variant.value) return;
      loading.value = true;
      error.value = null;
      try {
        const topicsKey = `../../content/python-lernpfad/topics-${variant.value}.json`;
        const placementKey = `../../content/python-lernpfad/placement-${variant.value}.json`;
        const topicsLoader = topicModules[topicsKey];
        const placementLoader = placementModules[placementKey];
        if (!topicsLoader) throw new Error('topics.json not found');
        const topicsMod = await topicsLoader();
        topics.value = topicsMod.default || [];
        if (placementLoader) {
          const placementMod = await placementLoader();
          placementData.value = placementMod.default || null;
        }
        applyTopicFromRoute();
      } catch (e) {
        console.error(e);
        error.value = lang.value === 'en' ? 'Could not load learning path.' : 'Lernpfad konnte nicht geladen werden.';
      } finally {
        loading.value = false;
      }
    };

    const applyTopicFromRoute = () => {
      const topicId = route.query.topic;
      if (topicId && topics.value.some((t) => t.id === topicId)) {
        if (progress.value.state.value.placementCompleted || !placementData.value) {
          activeTopicId.value = topicId;
        }
      }
    };

    const selectVariant = (v) => {
      variant.value = v;
      localStorage.setItem(VARIANT_STORAGE_KEY, v);
      activeTopicId.value = null;
      loadContent();
    };

    const switchVariant = () => {
      variant.value = null;
      localStorage.removeItem(VARIANT_STORAGE_KEY);
      topics.value = [];
      activeTopicId.value = null;
    };

    const topicLabel = (topic) =>
      lang.value === 'en' && topic.title_en ? topic.title_en : topic.title;

    const topicSummary = (topic) =>
      lang.value === 'en' && topic.summary_en ? topic.summary_en : topic.summary;

    const getTopicStatus = (id) => progress.value.getTopicStatus(id);

    const statusClass = (id) => `status-${getTopicStatus(id)}`;

    const statusLabel = (id) => {
      const s = getTopicStatus(id);
      const labels = lang.value === 'en'
        ? { not_started: 'Open', in_progress: 'In progress', completed: 'Done', skipped: 'Skipped' }
        : { not_started: 'Offen', in_progress: 'In Arbeit', completed: 'Geschafft', skipped: 'Übersprungen' };
      return labels[s] || s;
    };

    const openTopic = (id) => {
      activeTopicId.value = id;
    };

    const onTopicFinished = () => {
      activeTopicId.value = null;
    };

    const onPlacementSubmit = (payload) => {
      const questions = placementData.value?.questions || [];
      const threshold = placementData.value?.passThreshold || 0.8;
      const answers = payload?.answers || [];

      const topicScores = {};
      const byTopic = {};

      questions.forEach((q, i) => {
        if (!q.topicId) return;
        if (!byTopic[q.topicId]) byTopic[q.topicId] = { questions: [], answerIndices: [] };
        byTopic[q.topicId].questions.push(q);
        byTopic[q.topicId].answerIndices.push(answers[i]);
      });

      for (const [topicId, group] of Object.entries(byTopic)) {
        const result = scoreQuizAnswers(group.questions, group.answerIndices);
        topicScores[topicId] = result.score;
        if (isQuizPassed(result.score, threshold)) {
          progress.value.markTopicSkipped(topicId, result.score);
        }
      }

      progress.value.markPlacementCompleted(topicScores);
    };

    const skipPlacement = () => {
      progress.value.markPlacementCompleted({});
    };

    const retakePlacement = () => {
      progress.value.state.value = {
        ...progress.value.state.value,
        placementCompleted: false,
        placementTopicScores: {},
      };
    };

    const exportProgress = () => {
      const json = progress.value.exportProgress();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `lernpfad-fortschritt-${variant.value}.json`;
      a.click();
      URL.revokeObjectURL(a.href);
    };

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = progress.value.importProgress(reader.result);
        if (result.ok) alert(lang.value === 'en' ? 'Progress imported.' : 'Fortschritt importiert.');
        else alert((lang.value === 'en' ? 'Import failed: ' : 'Import fehlgeschlagen: ') + result.error);
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };

    onMounted(loadContent);
    watch(variant, loadContent);
    watch(() => route.query.topic, applyTopicFromRoute);

    return {
      lang,
      variant,
      topics,
      placementData,
      loading,
      error,
      activeTopicId,
      activeTopic,
      showPlacement,
      completedCount,
      recommendedTopics,
      progressPercent,
      placementTitle,
      placementIntro,
      placementQuestions,
      selectVariant,
      switchVariant,
      topicLabel,
      topicSummary,
      getTopicStatus,
      statusClass,
      statusLabel,
      openTopic,
      onTopicFinished,
      onPlacementSubmit,
      skipPlacement,
      retakePlacement,
      exportProgress,
      onImportFile,
    };
  },
};
</script>

<style scoped>
.learning-path-course {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px 0;
}

.variant-selector {
  text-align: center;
  padding: 40px 20px;
}

.variant-selector h2 {
  margin-bottom: 8px;
}

.variant-intro {
  color: #666;
  margin-bottom: 32px;
}

.variant-cards {
  display: flex;
  gap: 24px;
  justify-content: center;
  flex-wrap: wrap;
}

.variant-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 200px;
  padding: 28px 20px;
  border: 2px solid #dee2e6;
  border-radius: 12px;
  background: #fff;
  cursor: pointer;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.variant-card:hover {
  border-color: var(--primary-purple, #4a2274);
  box-shadow: 0 4px 16px rgba(74, 34, 116, 0.12);
}

.variant-icon { font-size: 2.4em; }
.variant-age { font-size: 0.85em; color: #888; }

.loading, .error {
  padding: 40px;
  text-align: center;
}

.error {
  color: #dc3545;
  background: #f8d7da;
  border-radius: 8px;
}

.placement-section {
  max-width: 800px;
  margin: 0 auto;
  background: #fff;
  border: 2px solid var(--primary-purple, #4a2274);
  border-radius: 12px;
  padding: 24px;
}

.placement-intro {
  color: #555;
  margin-bottom: 20px;
}

.btn-skip-placement {
  margin-top: 16px;
  background: transparent;
  border: 1px dashed #adb5bd;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  color: #666;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 12px;
}

.dashboard-header h2 {
  margin: 0 0 4px 0;
}

.progress-text {
  color: #28a745;
  font-weight: 600;
  margin: 0;
}

.btn-switch {
  border: 1px solid var(--primary-purple, #4a2274);
  background: transparent;
  color: var(--primary-purple, #4a2274);
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
}

.progress-track-wrap {
  margin-bottom: 28px;
}

.progress-track {
  height: 10px;
  background: #e9ecef;
  border-radius: 5px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--primary-purple, #4a2274), var(--accent-orange, #ff9800));
  transition: width 0.3s;
}

.topic-section {
  margin-bottom: 28px;
}

.topic-section h3 {
  margin: 0 0 12px 0;
  font-size: 1.1em;
}

.recommended-section {
  background: #f0f4ff;
  border-radius: 10px;
  padding: 16px;
}

.topic-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 12px;
}

.topic-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  text-align: left;
  padding: 16px;
  border: 2px solid #dee2e6;
  border-radius: 10px;
  background: #fff;
  cursor: pointer;
  transition: border-color 0.15s;
}

.topic-card:hover {
  border-color: var(--primary-purple, #4a2274);
}

.topic-card.recommended {
  border-color: #6c8ebf;
}

.topic-card.status-completed,
.topic-card.status-skipped {
  border-color: #28a745;
  background: #f8fff9;
}

.topic-card.status-in_progress {
  border-color: var(--accent-orange, #ff9800);
}

.topic-card-title {
  font-weight: 700;
  color: #222;
}

.topic-card-summary {
  font-size: 0.88em;
  color: #666;
  line-height: 1.3;
}

.topic-badge {
  font-size: 0.75em;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 10px;
  margin-top: 4px;
}

.badge-not_started { background: #e9ecef; color: #555; }
.badge-in_progress { background: #fff3cd; color: #856404; }
.badge-completed { background: #d4edda; color: #155724; }
.badge-skipped { background: #cce5ff; color: #004085; }
.badge-recommended { background: #6c8ebf; color: white; }

.dashboard-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
}

.btn-export,
.btn-import,
.btn-retake {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9em;
}

.file-input { display: none; }

@media (max-width: 768px) {
  .variant-cards { flex-direction: column; align-items: center; }
}
</style>
