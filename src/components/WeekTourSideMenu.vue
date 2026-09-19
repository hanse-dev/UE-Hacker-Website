<template>
  <nav class="tour-side-menu">
    <div class="side-menu-section">
      <h4>{{ t('tour.sideMenu.steps') }}</h4>
      <ul class="side-menu-list">
        <li v-for="step in steps" :key="step.key">
          <button
            class="side-menu-step"
            :class="{ active: !activeReference && step.key === currentStepKey, reached: !!visitedKeys[step.key] }"
            :data-step-key="step.key"
            @click="$emit('select-step', step.key)"
          >
            <span class="side-menu-icon">{{ visitedKeys[step.key] ? '✓' : step.icon }}</span>
            <span>{{ step.label }}</span>
          </button>
        </li>
      </ul>
    </div>

    <div class="side-menu-section" v-if="headings.length">
      <h4>{{ t('tour.sideMenu.sections') }}</h4>
      <ul class="side-menu-list side-menu-sub">
        <li v-for="heading in headings" :key="heading.cellIndex">
          <button
            class="side-menu-heading"
            :class="{ [`level-${heading.level}`]: true }"
            @click="$emit('select-heading', heading.cellIndex)"
          >
            {{ heading.text }}
          </button>
        </li>
      </ul>
    </div>

    <div class="side-menu-section" v-if="referenceItems.length || weekZipUrl">
      <h4>{{ t('tour.sideMenu.reference') }}</h4>
      <ul class="side-menu-list">
        <li v-for="ref_ in referenceItems" :key="ref_.key">
          <button
            class="side-menu-step side-menu-reference"
            :class="{ active: activeReference === ref_.key }"
            :data-reference-key="ref_.key"
            @click="$emit('select-reference', ref_.key)"
          >
            <span class="side-menu-icon">{{ ref_.icon }}</span>
            <span>{{ ref_.label }}</span>
          </button>
        </li>
        <li v-if="weekZipUrl">
          <a class="side-menu-step side-menu-download" :href="weekZipUrl" download data-week-zip>
            <span class="side-menu-icon">📦</span>
            <span>{{ t('tour.sideMenu.downloadWeek') }}</span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'WeekTourSideMenu',
  props: {
    steps: { type: Array, required: true },
    currentStepKey: { type: String, default: null },
    visitedKeys: { type: Object, default: () => ({}) },
    headings: { type: Array, default: () => [] },
    referenceItems: { type: Array, default: () => [] },
    weekZipUrl: { type: String, default: null },
    activeReference: { type: String, default: null },
  },
  emits: ['select-step', 'select-heading', 'select-reference'],
  setup() {
    const { t } = useLanguage();
    return { t };
  },
};
</script>

<style scoped>
.tour-side-menu {
  display: flex;
  flex-direction: column;
  gap: 18px;
  min-width: 200px;
  max-width: 240px;
}

.side-menu-section h4 {
  margin: 0 0 8px;
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: #8a7a99;
}

.side-menu-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.side-menu-step {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: none;
  border-radius: 6px;
  padding: 7px 10px;
  text-align: left;
  cursor: pointer;
  font-size: 0.88em;
  color: #4b5563;
  transition: background 0.15s, color 0.15s;
}

.side-menu-step:hover {
  background: #f3f0f7;
}

.side-menu-step.reached {
  color: var(--primary-purple, #4a2274);
}

.side-menu-step.active {
  background: var(--primary-purple, #4a2274);
  color: white;
  font-weight: 600;
}

.side-menu-icon {
  width: 1.2em;
  text-align: center;
  flex-shrink: 0;
}

.side-menu-sub {
  padding-left: 6px;
  border-left: 2px solid #efe3f6;
}

.side-menu-heading {
  width: 100%;
  background: transparent;
  border: none;
  padding: 5px 10px;
  text-align: left;
  cursor: pointer;
  font-size: 0.82em;
  color: #6b7280;
  border-radius: 4px;
}

.side-menu-heading:hover {
  background: #f3f0f7;
  color: #374151;
}

.side-menu-heading.level-2 {
  font-weight: 600;
}

.side-menu-reference {
  color: #7c5a94;
}

.side-menu-download {
  color: #7c5a94;
  text-decoration: none;
}
</style>
