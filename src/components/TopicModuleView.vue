<template>
  <div class="topic-module-view">
    <div class="topic-header">
      <button type="button" class="btn-back" @click="$emit('back')">
        {{ lang === 'en' ? '← All topics' : '← Alle Themen' }}
      </button>
      <h2>{{ topicTitle }}</h2>
      <p class="topic-summary">{{ topicSummary }}</p>
    </div>

    <!-- Skip test -->
    <div v-if="showSkipTest" class="skip-test-section">
      <h3>{{ lang === 'en' ? 'Already know this?' : 'Kennst du das schon?' }}</h3>
      <p class="skip-intro">
        {{ lang === 'en'
          ? `Pass the quick test (${Math.round((topic.skipTest.passThreshold || 0.8) * 100)}%+) to skip this topic.`
          : `Bestehe den Kurztest (${Math.round((topic.skipTest.passThreshold || 0.8) * 100)}%+), um dieses Thema zu überspringen.` }}
      </p>
      <QuizStep
        :questions="topic.skipTest.questions"
        :pass-threshold="topic.skipTest.passThreshold || 0.8"
        :lang="lang"
        @completed="onSkipPassed"
      />
      <button type="button" class="btn-skip-dismiss" @click="dismissSkipTest">
        {{ lang === 'en' ? 'I want to learn this topic' : 'Ich möchte das Thema lernen' }}
      </button>
    </div>

    <!-- Main steps -->
    <div v-else class="topic-steps">
      <div
        v-for="(step, idx) in topic.steps"
        :key="step.id"
        class="step-block"
        :class="{ completed: isStepCompleted(step.id) }"
      >
        <div class="step-header">
          <span class="step-num">{{ idx + 1 }}</span>
          <span class="step-type">{{ stepTypeLabel(step) }}</span>
          <span v-if="isStepCompleted(step.id)" class="step-done">✓</span>
        </div>

        <QuizStep
          v-if="step.type === 'quiz' && activeStepIndex >= idx"
          :questions="step.questions"
          :title="stepTitle(step)"
          :pass-threshold="1"
          :lang="lang"
          @completed="() => onStepCompleted(step.id, idx)"
        />

        <CodeTaskStep
          v-else-if="step.type === 'code' && activeStepIndex >= idx"
          :instruction="step.instruction"
          :instruction-en="step.instruction_en"
          :code-template="step.codeTemplate"
          :validation="step.validation"
          :lang="lang"
          :completed="isStepCompleted(step.id)"
          @completed="() => onStepCompleted(step.id, idx)"
        />

        <div v-else-if="activeStepIndex < idx" class="step-locked">
          {{ lang === 'en' ? 'Complete the previous step first.' : 'Schließe zuerst den vorherigen Schritt ab.' }}
        </div>
      </div>

      <div v-if="allStepsComplete" class="topic-complete-box">
        <p>{{ lang === 'en' ? 'Topic completed! Great job!' : 'Thema abgeschlossen! Super gemacht!' }}</p>
        <button type="button" class="btn-next-topic" @click="$emit('completed', topic.id)">
          {{ lang === 'en' ? 'Back to dashboard' : 'Zurück zur Übersicht' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import QuizStep from './QuizStep.vue';
import CodeTaskStep from './CodeTaskStep.vue';
import { useLearnerProgress } from '../composables/useLearnerProgress';

export default {
  name: 'TopicModuleView',
  components: { QuizStep, CodeTaskStep },
  props: {
    topic: { type: Object, required: true },
    variant: { type: String, default: 'kinder' },
    lang: { type: String, default: 'de' },
  },
  emits: ['back', 'completed', 'skipped'],
  setup(props, { emit }) {
    const {
      getTopicStatus,
      markTopicInProgress,
      markStepCompleted,
      markTopicCompleted,
      markTopicSkipped,
      isStepCompleted: checkStepCompleted,
    } = useLearnerProgress(props.variant);

    const skipDismissed = ref(false);

    const topicTitle = computed(() =>
      props.lang === 'en' && props.topic.title_en ? props.topic.title_en : props.topic.title
    );

    const topicSummary = computed(() =>
      props.lang === 'en' && props.topic.summary_en ? props.topic.summary_en : props.topic.summary
    );

    const status = computed(() => getTopicStatus(props.topic.id));

    const showSkipTest = computed(() =>
      props.topic.skipTest?.questions?.length > 0
      && status.value === 'not_started'
      && !skipDismissed.value
    );

    const isStepCompleted = (stepId) => checkStepCompleted(props.topic.id, stepId);

    const activeStepIndex = computed(() => {
      const steps = props.topic.steps || [];
      for (let i = 0; i < steps.length; i++) {
        if (!isStepCompleted(steps[i].id)) return i;
      }
      return steps.length;
    });

    const allStepsComplete = computed(() => {
      const steps = props.topic.steps || [];
      return steps.length > 0 && steps.every((s) => isStepCompleted(s.id));
    });

    const stepTitle = (step) =>
      props.lang === 'en' && step.title_en ? step.title_en : (step.title || '');

    const stepTypeLabel = (step) => {
      if (step.type === 'quiz') return props.lang === 'en' ? 'Quiz' : 'Quiz';
      return props.lang === 'en' ? 'Code task' : 'Code-Aufgabe';
    };

    onMounted(() => {
      if (status.value !== 'skipped' && status.value !== 'completed') {
        markTopicInProgress(props.topic.id);
      }
    });

    watch(allStepsComplete, (done) => {
      if (done && status.value !== 'completed' && status.value !== 'skipped') {
        markTopicCompleted(props.topic.id);
      }
    });

    const onStepCompleted = (stepId, idx) => {
      markStepCompleted(props.topic.id, stepId);
    };

    const onSkipPassed = (scoreResult) => {
      markTopicSkipped(props.topic.id, scoreResult.score);
      emit('skipped', props.topic.id);
    };

    const dismissSkipTest = () => {
      skipDismissed.value = true;
      markTopicInProgress(props.topic.id);
    };

    return {
      topicTitle,
      topicSummary,
      showSkipTest,
      isStepCompleted,
      activeStepIndex,
      allStepsComplete,
      stepTitle,
      stepTypeLabel,
      onStepCompleted,
      onSkipPassed,
      dismissSkipTest,
    };
  },
};
</script>

<style scoped>
.topic-module-view {
  max-width: 800px;
}

.topic-header {
  margin-bottom: 24px;
}

.btn-back {
  background: transparent;
  border: 1px solid #dee2e6;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  margin-bottom: 12px;
  color: var(--primary-purple, #4a2274);
}

.topic-header h2 {
  margin: 0 0 8px 0;
}

.topic-summary {
  color: #555;
  margin: 0;
}

.skip-test-section {
  background: #f0f4ff;
  border: 2px solid #6c8ebf;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 24px;
}

.skip-test-section h3 {
  margin: 0 0 8px 0;
}

.skip-intro {
  color: #555;
  margin: 0 0 16px 0;
}

.btn-skip-dismiss {
  margin-top: 12px;
  background: transparent;
  border: 1px dashed #6c8ebf;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  color: #445;
}

.step-block {
  margin-bottom: 20px;
  border-left: 3px solid #dee2e6;
  padding-left: 16px;
}

.step-block.completed {
  border-left-color: #28a745;
}

.step-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.step-num {
  background: var(--primary-purple, #4a2274);
  color: white;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85em;
}

.step-type {
  font-weight: 600;
  color: #333;
}

.step-done {
  color: #28a745;
  font-weight: bold;
}

.step-locked {
  color: #adb5bd;
  font-style: italic;
  padding: 12px;
  background: #f8f9fa;
  border-radius: 6px;
}

.topic-complete-box {
  margin-top: 24px;
  padding: 20px;
  background: #d4edda;
  border: 1px solid #c3e6cb;
  border-radius: 8px;
  text-align: center;
}

.topic-complete-box p {
  margin: 0 0 16px 0;
  color: #155724;
  font-weight: 600;
}

.btn-next-topic {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}
</style>
