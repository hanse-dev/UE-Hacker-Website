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

        <!-- Cheat Sheets -->
        <div v-if="week.hasNotebook && week.cheatSheets?.length > 0" class="downloads-section">
          <div v-for="(cheatSheet, csIndex) in week.cheatSheets" :key="csIndex" class="cheat-sheet-container">
            <div class="cheat-sheet-header" @click="$emit('toggle-cheat-sheet', csIndex)">
              <h4>{{ cheatSheet.name }}</h4>
              <button class="cheat-sheet-toggle-btn" :class="{ 'expanded': isCheatSheetExpanded(csIndex) }">
                <span class="toggle-icon">{{ isCheatSheetExpanded(csIndex) ? '−' : '+' }}</span>
              </button>
            </div>
            <div v-show="isCheatSheetExpanded(csIndex)" class="cheat-sheet-content">
              <div class="cheat-sheet-actions">
                <a :href="cheatSheet.url" download class="download-btn">
                  <span class="download-icon">📥</span>
                  Als Markdown herunterladen
                </a>
                <a v-if="cheatSheet.notebookUrl" :href="cheatSheet.notebookUrl" download class="download-btn">
                  <span class="download-icon">📓</span>
                  Als Jupyter Notebook herunterladen
                </a>
              </div>
              <div class="cheat-sheet-preview" v-if="cheatSheet.content">
                <div v-html="cheatSheet.content" class="cheat-sheet-markdown"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Other downloads -->
        <div v-if="!week.hasNotebook && week.downloads?.length > 0" class="downloads-section">
          <h4>Downloads</h4>
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
          <div class="variant-selector">

            <button
              v-if="week.hasAbenteuerVariant"
              @click="$emit('set-variant', 'abenteuer')"
              :class="{ active: week.selectedVariant === 'abenteuer' }"
              class="variant-btn"
            >🗺️ Abenteuer</button>
            <button
              v-if="week.hasPferdeVariant"
              @click="$emit('set-variant', 'pferde')"
              :class="{ active: week.selectedVariant === 'pferde' }"
              class="variant-btn"
            >🐴 Pferde</button>
            <button
              v-if="week.hasScifiVariant"
              @click="$emit('set-variant', 'scifi')"
              :class="{ active: week.selectedVariant === 'scifi' }"
              class="variant-btn"
            >🚀 Sci-Fi</button>
          </div>

          <!-- Row 2: Missionen & Belohnungen -->
          <MissionenPanel
            :week-number="index + 1"
            :variant="week.selectedVariant"
            :course-id="courseId"
          />

          <!-- Row 3: Tab-Guide + Notebook-Tabs -->
          <details class="tab-guide">
            <summary class="tab-guide-summary">ℹ️ Wie ist die Woche aufgebaut?</summary>
            <div class="tab-guide-content">
              <p class="tab-guide-order">Empfohlene Reihenfolge: 📚 Lektion → 🐛 Debug → ⭐ Missionen → 🐉 Boss-Quest</p>
              <ul class="tab-guide-list">
                <li v-for="tab in TABS" :key="tab.key">
                  <span class="tab-guide-icon">{{ tab.icon }}</span>
                  <strong>{{ tab.label }}</strong> – {{ tab.description }}
                </li>
              </ul>
            </div>
          </details>

          <div class="notebook-tabs">
            <button
              v-for="tab in TABS"
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

          <!-- Notebook -->
          <JupyterNotebook
            v-if="activeNotebookUrl"
            :notebook-path="activeNotebookUrl"
            :notebook-url="activeNotebookUrl"
            :week-number="index + 1"
            :variant="week.selectedVariant"
            :course-id="courseId"
            :key="`${index}-${week.selectedVariant}-${selectedTab}`"
          />
          <div v-else class="tab-empty">
            Kein Notebook für diesen Bereich verfügbar.
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import JupyterNotebook from './JupyterNotebook.vue';
import MissionenPanel from './MissionenPanel.vue';

const TABS = [
  { key: '1_lektion',   label: 'Lektion',    icon: '📚', description: 'Neuer Stoff: lies und verstehe das Thema der Woche' },
  { key: '2_debug',     label: 'Debug',      icon: '🐛', description: 'Finde und fixe absichtliche Bugs im Code' },
  { key: '3_missionen', label: 'Missionen',  icon: '⭐', description: 'Kleine Aufgaben zum Üben des neuen Stoffs' },
  { key: '5_boss',      label: 'Boss-Quest', icon: '🐉', description: 'Die große Abschluss-Challenge – alles zusammen!' },
  { key: '6_loesungen', label: 'Lösungen',   icon: '🔧', description: 'Musterlösungen zu Missionen und Boss-Quest' },
  { key: '0_glossar',   label: 'Glossar',    icon: '📖', description: 'Alle Begriffe der Woche zum Nachschlagen – immer verfügbar' },
];

export default {
  name: 'WeekSection',
  components: { JupyterNotebook, MissionenPanel },
  props: {
    week: { type: Object, required: true },
    index: { type: Number, required: true },
    courseId: { type: String, required: true },
  },
  emits: ['toggle', 'toggle-cheat-sheet', 'set-variant'],
  setup(props) {
    const selectedTab = ref(props.week.selectedTab ?? '1_lektion');

    const isCheatSheetExpanded = (csIndex) =>
      props.week.expandedCheatSheets?.[csIndex] ?? false;

    const hasTab = (key) =>
      !!props.week.notebooks?.[props.week.selectedVariant]?.[key];

    const activeNotebookUrl = computed(() =>
      props.week.notebooks?.[props.week.selectedVariant]?.[selectedTab.value] ?? null
    );

    return { TABS, selectedTab, isCheatSheetExpanded, hasTab, activeNotebookUrl };
  },
};
</script>

<style scoped>
/* ── Notebook area ─────────────────────────────────────────────────────── */
.notebook-area {
  margin-top: 10px;
}

/* ── Variant selector ──────────────────────────────────────────────────── */
.variant-selector {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.variant-btn {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  padding: 8px 18px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 500;
}

.variant-btn:hover {
  background: #e9ecef;
  border-color: #ff4136;
}

.variant-btn.active {
  background: #ff4136;
  color: white;
  border-color: #ff4136;
  font-weight: 700;
}

/* ── Tab guide ─────────────────────────────────────────────────────────── */
.tab-guide {
  margin-bottom: 10px;
}

.tab-guide-summary {
  cursor: pointer;
  font-size: 0.82em;
  color: #888;
  user-select: none;
  padding: 4px 0;
  list-style: none;
}

.tab-guide-summary::-webkit-details-marker { display: none; }
.tab-guide-summary::marker { display: none; }

.tab-guide-summary:hover { color: #555; }

.tab-guide-content {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 12px 16px;
  margin-top: 6px;
}

.tab-guide-order {
  margin: 0 0 10px;
  font-size: 0.82em;
  color: #555;
  font-weight: 500;
}

.tab-guide-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.tab-guide-list li {
  font-size: 0.82em;
  color: #444;
  display: flex;
  gap: 6px;
  align-items: baseline;
}

.tab-guide-icon {
  flex-shrink: 0;
  width: 1.4em;
  text-align: center;
}

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

.download-icon { font-size: 1.2em; }

.cheat-sheet-container {
  margin-bottom: 20px;
  border: 2px solid #28a745;
  border-radius: 8px;
  overflow: hidden;
  background: #f8fff9;
}

.cheat-sheet-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  padding: 15px 20px;
  background: #28a745;
  color: white;
  transition: all 0.3s ease;
}

.cheat-sheet-header:hover { background: #218838; }

.cheat-sheet-header h4 { margin: 0; font-size: 1.1em; }

.cheat-sheet-toggle-btn {
  background: transparent;
  border: none;
  font-size: 1.5em;
  cursor: pointer;
  color: white;
  padding: 5px 10px;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.cheat-sheet-toggle-btn:hover { background: rgba(255, 255, 255, 0.2); }
.cheat-sheet-toggle-btn.expanded { transform: rotate(180deg); }

.cheat-sheet-content { padding: 20px; background: white; }

.cheat-sheet-actions { margin-bottom: 20px; text-align: center; }

.download-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 8px;
  padding: 12px 24px;
  background: #28a745;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  transition: all 0.3s ease;
}

.download-btn:hover {
  background: #218838;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
}

.cheat-sheet-preview {
  border: 1px solid #ddd;
  border-radius: 6px;
  overflow: hidden;
  background: white;
  max-height: 600px;
  overflow-y: auto;
}

.cheat-sheet-markdown {
  padding: 20px;
  font-size: 0.95em;
  line-height: 1.6;
}

.cheat-sheet-markdown :deep(h1) {
  color: #28a745;
  border-bottom: 2px solid #28a745;
  padding-bottom: 10px;
  margin-top: 0;
}

.cheat-sheet-markdown :deep(h2) {
  color: #333;
  border-bottom: 1px solid #eee;
  padding-bottom: 5px;
  margin-top: 2em;
}

.cheat-sheet-markdown :deep(h3) { color: #555; margin-top: 1.5em; }

.cheat-sheet-markdown :deep(code) {
  background: #f8f9fa;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  border: 1px solid #e9ecef;
}

.cheat-sheet-markdown :deep(pre) {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 6px;
  overflow-x: auto;
  border: 1px solid #e9ecef;
}

.cheat-sheet-markdown :deep(pre code) { background: none; padding: 0; border: none; }

.cheat-sheet-markdown :deep(ul),
.cheat-sheet-markdown :deep(ol) { padding-left: 25px; }

.cheat-sheet-markdown :deep(li) { margin-bottom: 5px; }

.cheat-sheet-markdown :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.cheat-sheet-markdown :deep(th),
.cheat-sheet-markdown :deep(td) {
  border: 1px solid #ddd;
  padding: 8px 12px;
  text-align: left;
}

.cheat-sheet-markdown :deep(th) { background: #f8f9fa; font-weight: bold; }

.cheat-sheet-markdown :deep(blockquote) {
  border-left: 4px solid #28a745;
  padding-left: 20px;
  margin-left: 0;
  color: #666;
  font-style: italic;
}

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
</style>
