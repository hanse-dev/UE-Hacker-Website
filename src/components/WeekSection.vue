<template>
  <div class="week-section" :id="`woche-${index + 1}`">
    <div class="week-section-inner">
      <div class="week-header" @click="$emit('toggle')">
        <h2>{{ week.title }}</h2>
        <button class="toggle-btn" :class="{ 'expanded': week.expanded }">
          <span class="toggle-icon">{{ week.expanded ? '−' : '+' }}</span>
        </button>
      </div>

      <div v-show="week.expanded" class="week-content">
        <!-- Compact week summary -->
        <div v-if="week.shortDesc || week.lernziele?.length" class="week-summary">
          <p v-if="week.shortDesc" class="week-summary-desc">{{ week.shortDesc }}</p>
          <div v-if="week.lernziele?.length" class="lernziele-chips">
            <span v-for="(ziel, i) in week.lernziele" :key="i" class="lernziel-chip">
              {{ ziel }}
            </span>
          </div>
        </div>

        <!-- Week ZIP download -->
        <div v-if="week.hasNotebook" class="week-zip-download">
          <a :href="`/wochen-zips/woche-${index + 1}.zip`" download class="btn-week-zip">
            {{ t('week.download.week').replace('{n}', index + 1) }}
          </a>
          <span class="week-zip-hint">{{ t('week.download.week.hint') }}</span>
        </div>

        <!-- Cheat Sheets -->
        <CheatSheetList
          v-if="week.hasNotebook && week.cheatSheets?.length > 0"
          :cheat-sheets="week.cheatSheets"
          :expanded-cheat-sheets="week.expandedCheatSheets"
          @toggle="$emit('toggle-cheat-sheet', $event)"
        />

        <!-- Other downloads -->
        <div v-if="!week.hasNotebook && week.downloads?.length > 0" class="downloads-section">
          <h4>{{ t('week.downloads') }}</h4>
          <ul>
            <li v-for="(file, fileIndex) in week.downloads" :key="fileIndex">
              <a :href="file.url" download :class="{ 'cheat-sheet-link': file.isCheatSheet }">
                <span class="download-icon">{{ file.isCheatSheet ? '📚' : '📥' }}</span>
                {{ file.name }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Notebook viewer with variant + tab navigation -->
        <div v-if="week.hasNotebook" class="notebook-area">

          <!-- Row 1: Varianten-Auswahl -->
          <VariantSelector :week="week" @set-variant="$emit('set-variant', $event)" />

          <!-- Row 2: Missionen & Belohnungen -->
          <MissionenPanel
            :week-number="index + 1"
            :variant="week.selectedVariant"
            :course-id="courseId"
          />

          <!-- Row 3: Notebook-Tabs -->
          <div class="notebook-tabs">
            <button
              v-for="tab in tabs"
              :key="tab.key"
              class="tab-btn"
              :class="{ active: selectedTab === tab.key, available: hasTab(tab.key) }"
              :disabled="!hasTab(tab.key)"
              :title="tab.description"
              @click="selectedTab = tab.key"
            >
              <span class="tab-icon">{{ tab.icon }}</span>
              <span class="tab-label">{{ tab.label }}</span>
            </button>
          </div>

          <!-- Check tab (quiz, not notebook) -->
          <WeekCheckPanel
            v-if="week.expanded && selectedTab === '4_check' && hasCheck"
            :week-number="index + 1"
          />

          <!-- Notebook -->
          <JupyterNotebook
            v-else-if="week.expanded && activeNotebookUrl"
            :notebook-path="activeNotebookUrl"
            :notebook-url="activeNotebookUrl"
            :week-number="index + 1"
            :variant="week.selectedVariant"
            :course-id="courseId"
            :key="`${index}-${week.selectedVariant}-${selectedTab}`"
          />
          <div v-else-if="selectedTab !== '4_check'" class="tab-empty">
            {{ t('week.noNotebook') }}
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import JupyterNotebook from './JupyterNotebook.vue';
import MissionenPanel from './MissionenPanel.vue';
import WeekCheckPanel from './WeekCheckPanel.vue';
import CheatSheetList from './CheatSheetList.vue';
import VariantSelector from './VariantSelector.vue';
import { useLanguage } from '../composables/useLanguage.js';
import { loadWeekChecks, hasWeekCheck } from '../composables/useWeekChecks.js';

const TABS_CONFIG = [
  { key: '1_lektion',   icon: '📚', labelKey: 'tab.lesson',    descKey: 'tab.lesson.desc' },
  { key: '2_debug',     icon: '🐛', labelKey: 'tab.debug',     descKey: 'tab.debug.desc' },
  { key: '3_missionen', icon: '⭐', labelKey: 'tab.missions',  descKey: 'tab.missions.desc' },
  { key: '4_check',     icon: '✅', labelKey: 'tab.check',     descKey: 'tab.check.desc' },
  { key: '5_boss',      icon: '🐉', labelKey: 'tab.boss',      descKey: 'tab.boss.desc' },
  { key: '6_loesungen', icon: '🔧', labelKey: 'tab.solutions', descKey: 'tab.solutions.desc' },
  { key: '0_glossar',   icon: '📖', labelKey: 'tab.glossary',  descKey: 'tab.glossary.desc' },
];

export default {
  name: 'WeekSection',
  components: { JupyterNotebook, MissionenPanel, WeekCheckPanel, CheatSheetList, VariantSelector },
  props: {
    week: { type: Object, required: true },
    index: { type: Number, required: true },
    courseId: { type: String, required: true },
  },
  emits: ['toggle', 'toggle-cheat-sheet', 'set-variant'],
  setup(props) {
    const { t } = useLanguage();
    const route = useRoute();
    const checksData = ref(null);

    const tabStorageKey = `ue-hacker-week-tab-${props.courseId}-${props.index}`;
    const selectedTab = ref(
      localStorage.getItem(tabStorageKey) ?? props.week.selectedTab ?? '1_lektion'
    );

    watch(selectedTab, (value) => {
      localStorage.setItem(tabStorageKey, value);
    });

    const weekNumber = computed(() => props.index + 1);
    const hasCheck = computed(() => hasWeekCheck(checksData.value, weekNumber.value));

    const tabs = computed(() => {
      const base = TABS_CONFIG.map(tab => ({
        ...tab,
        label: t(tab.labelKey),
        description: t(tab.descKey),
      }));
      // Hide check tab if no questions for this week
      return base.filter((tab) => tab.key !== '4_check' || hasCheck.value);
    });

    const hasTab = (key) => {
      if (key === '4_check') return hasCheck.value;
      return !!props.week.notebooks?.[props.week.selectedVariant]?.[key];
    };

    const activeNotebookUrl = computed(() => {
      if (selectedTab.value === '4_check') return null;
      return props.week.notebooks?.[props.week.selectedVariant]?.[selectedTab.value] ?? null;
    });

    const applyRouteTab = () => {
      const weekParam = Number(route.query.week);
      if (weekParam !== weekNumber.value) return;
      const tab = String(route.query.tab || '').toLowerCase();
      // Deep-link from placement / share URL: open the requested tab (default: lesson notebooks)
      if (tab === 'check' && hasCheck.value) {
        selectedTab.value = '4_check';
      } else if (!tab || tab === 'lektion' || tab === 'lesson') {
        selectedTab.value = '1_lektion';
      } else if (tab === 'debug') {
        selectedTab.value = '2_debug';
      } else if (tab === 'missionen' || tab === 'missions') {
        selectedTab.value = '3_missionen';
      } else if (tab === 'boss') {
        selectedTab.value = '5_boss';
      } else if (tab === 'loesungen' || tab === 'solutions') {
        selectedTab.value = '6_loesungen';
      } else if (tab === 'glossar' || tab === 'glossary') {
        selectedTab.value = '0_glossar';
      }
    };

    onMounted(async () => {
      try {
        checksData.value = await loadWeekChecks();
      } catch (e) {
        console.error(e);
      }
      applyRouteTab();
    });

    watch(() => [route.query.week, route.query.tab, hasCheck.value], applyRouteTab);

    return {
      tabs, t, selectedTab, hasTab, activeNotebookUrl,
      hasCheck,
    };
  },
};
</script>

<style scoped>
/* ── Notebook area ─────────────────────────────────────────────────────── */
.notebook-area {
  margin-top: 16px;
}

/* ── Variant selector: siehe VariantSelector.vue ─────────────────────────── */

/* ── Tabs ──────────────────────────────────────────────────────────────── */
.notebook-tabs {
  display: flex;
  gap: 0;
  border-bottom: 2px solid #dee2e6;
  margin-bottom: 0;
  overflow-x: auto;
  scrollbar-width: none;
}

.notebook-tabs::-webkit-scrollbar { display: none; }

.tab-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 10px 14px;
  border: none;
  border-bottom: 3px solid transparent;
  background: transparent;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 500;
  color: #666;
  white-space: nowrap;
  transition: all 0.18s ease;
  margin-bottom: -2px;
}

.tab-btn:hover:not(:disabled) {
  color: #333;
  background: #f8f9fa;
  border-bottom-color: #ccc;
}

.tab-btn.active {
  color: #ff4136;
  border-bottom-color: #ff4136;
  font-weight: 700;
  background: #fff8f8;
}

.tab-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.tab-icon {
  font-size: 1.1em;
}

.tab-label {
  font-size: 0.9em;
}

.tab-empty {
  padding: 30px;
  text-align: center;
  color: #999;
  background: #f8f9fa;
  border-radius: 0 0 8px 8px;
  border: 1px solid #dee2e6;
  border-top: none;
}

/* ── Shared / existing styles ──────────────────────────────────────────── */
.downloads-section h4 {
  margin-top: 20px;
  border-top: 1px solid #eee;
  padding-top: 15px;
}

.downloads-section ul {
  list-style-type: none;
  padding: 0;
}

.downloads-section li {
  margin-bottom: 10px;
}

.downloads-section li a {
  text-decoration: none;
  color: #ff4136;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.downloads-section li a:hover {
  background-color: #fff5f5;
  transform: translateX(5px);
}

.cheat-sheet-link {
  color: #28a745 !important;
  font-weight: bold;
  border: 2px solid #28a745;
  background-color: #f8fff9;
}

.cheat-sheet-link:hover {
  background-color: #e8f5e8 !important;
}

/* ── Cheat Sheets: siehe CheatSheetList.vue ──────────────────────────────── */

.week-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  padding: 15px 20px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  margin-bottom: 0;
  transition: all 0.3s ease;
}

.week-header:hover {
  background: #e9ecef;
  border-color: #ff4136;
}

.week-header h2 { margin: 0; color: #333; font-size: 1.2em; }

.toggle-btn {
  background: transparent;
  border: none;
  font-size: 1.5em;
  cursor: pointer;
  color: #666;
  padding: 5px 10px;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.toggle-btn:hover { background: #ff4136; color: white; }
.toggle-btn.expanded { background: #ff4136; color: white; transform: rotate(180deg); }
.toggle-icon { font-weight: bold; display: block; }

.week-content {
  padding: 20px;
  border: 1px solid #dee2e6;
  border-top: none;
  border-radius: 0 0 8px 8px;
  background: white;
}

.week-section { margin-bottom: 20px; }

.week-section-inner {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* ── Compact week summary ──────────────────────────────────────────────── */
.week-summary {
  padding: 14px 0 16px;
  margin-bottom: 4px;
}

.week-summary-desc {
  margin: 0 0 12px;
  color: #4b5563;
  font-size: 0.95em;
  line-height: 1.55;
}

.lernziele-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.lernziel-chip {
  display: inline-block;
  background: #fef9c3;
  border: 1px solid #fde047;
  color: #713f12;
  padding: 3px 10px;
  border-radius: 20px;
  font-size: 0.78em;
  font-weight: 500;
  white-space: nowrap;
}

.week-zip-download {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 0 4px;
  flex-wrap: wrap;
}

.btn-week-zip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 6px 14px;
  font-size: 0.9em;
  color: var(--primary-purple, #4a2274);
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.15s, border-color 0.15s;
}

.btn-week-zip:hover {
  background: #e9ecef;
  border-color: var(--primary-purple, #4a2274);
}

.week-zip-hint {
  font-size: 0.8em;
  color: #888;
}
</style>
