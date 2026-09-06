<template>
  <div class="downloads-section">
    <div v-for="(cheatSheet, csIndex) in cheatSheets" :key="csIndex" class="cheat-sheet-container">
      <div class="cheat-sheet-header" @click="$emit('toggle', csIndex)">
        <h4>{{ cheatSheet.name }}</h4>
        <button class="cheat-sheet-toggle-btn" :class="{ 'expanded': isExpanded(csIndex) }">
          <span class="toggle-icon">{{ isExpanded(csIndex) ? '−' : '+' }}</span>
        </button>
      </div>
      <div v-show="isExpanded(csIndex)" class="cheat-sheet-content">
        <div class="cheat-sheet-actions">
          <a :href="cheatSheet.url" download class="download-btn">
            <span class="download-icon">📥</span>
            {{ t('week.download.md') }}
          </a>
          <a v-if="cheatSheet.notebookUrl" :href="cheatSheet.notebookUrl" download class="download-btn">
            <span class="download-icon">📓</span>
            {{ t('week.download.nb') }}
          </a>
        </div>
        <div class="cheat-sheet-preview" v-if="cheatSheet.content">
          <div v-html="cheatSheet.content" class="cheat-sheet-markdown"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'CheatSheetList',
  props: {
    cheatSheets: { type: Array, required: true },
    expandedCheatSheets: { type: Object, default: () => ({}) },
  },
  emits: ['toggle'],
  setup(props) {
    const { t } = useLanguage();
    const isExpanded = (csIndex) => props.expandedCheatSheets?.[csIndex] ?? false;
    return { t, isExpanded };
  },
};
</script>

<style scoped>
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

/* border-top/padding-top hier explizit, weil sie vor dem WeekSection-Split aus der generischen
   .downloads-section h4-Regel "durchsickerten" (siehe Refactoring-HANDOFF-Notiz) — Computed Style
   vor der Aufteilung geprüft und hier 1:1 übernommen, damit sich am Rendering nichts ändert. */
.cheat-sheet-header h4 {
  margin: 0;
  font-size: 1.1em;
  border-top: 1px solid #eee;
  padding-top: 15px;
}

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
</style>
