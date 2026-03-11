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
        <div v-if="week.content" v-html="week.content" class="week-description"></div>

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

        <div v-if="week.hasNotebook" class="notebook-variants">
          <h4>📚 Notebook-Varianten</h4>
          <div class="variant-selector">
            <button
              v-if="week.hasAbenteuerVariant"
              @click="$emit('set-variant', 'abenteuer')"
              :class="{ active: week.selectedVariant === 'abenteuer' }"
              class="variant-btn"
            >
              🗺️ Abenteuer
            </button>
            <button
              v-if="week.hasPferdeVariant"
              @click="$emit('set-variant', 'pferde')"
              :class="{ active: week.selectedVariant === 'pferde' }"
              class="variant-btn"
            >
              🐴 Pferde
            </button>
            <button
              v-if="week.hasScifiVariant"
              @click="$emit('set-variant', 'scifi')"
              :class="{ active: week.selectedVariant === 'scifi' }"
              class="variant-btn"
            >
              🚀 Sci-Fi
            </button>
          </div>
          <JupyterNotebook
            :notebook-path="getNotebookPath()"
            :notebook-url="getNotebookUrl()"
            :week-number="index + 1"
            :variant="week.selectedVariant"
            :course-id="courseId"
            :key="`${index}-${week.selectedVariant}`"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import JupyterNotebook from './JupyterNotebook.vue';

export default {
  name: 'WeekSection',
  components: { JupyterNotebook },
  props: {
    week: { type: Object, required: true },
    index: { type: Number, required: true },
    courseId: { type: String, required: true },
  },
  emits: ['toggle', 'toggle-cheat-sheet', 'set-variant'],
  setup(props) {
    const isCheatSheetExpanded = (csIndex) => props.week.expandedCheatSheets?.[csIndex] ?? false;

    const getNotebookPath = () => {
      const w = props.week;
      if (w.selectedVariant === 'abenteuer') return w.abenteuerNotebookPath;
      if (w.selectedVariant === 'pferde') return w.pferdeNotebookPath;
      if (w.selectedVariant === 'scifi') return w.scifiNotebookPath;
      return null;
    };

    const getNotebookUrl = () => {
      const w = props.week;
      if (w.selectedVariant === 'abenteuer') return w.abenteuerNotebookUrl;
      if (w.selectedVariant === 'pferde') return w.pferdeNotebookUrl;
      if (w.selectedVariant === 'scifi') return w.scifiNotebookUrl;
      return null;
    };

    return { isCheatSheetExpanded, getNotebookPath, getNotebookUrl };
  },
};
</script>

<style scoped>
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

.download-icon {
  font-size: 1.2em;
}

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

.cheat-sheet-header:hover {
  background: #218838;
}

.cheat-sheet-header h4 {
  margin: 0;
  font-size: 1.1em;
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

.cheat-sheet-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

.cheat-sheet-toggle-btn.expanded {
  transform: rotate(180deg);
}

.cheat-sheet-content {
  padding: 20px;
  background: white;
}

.cheat-sheet-actions {
  margin-bottom: 20px;
  text-align: center;
}

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

.cheat-sheet-markdown :deep(h3) {
  color: #555;
  margin-top: 1.5em;
}

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

.cheat-sheet-markdown :deep(pre code) {
  background: none;
  padding: 0;
  border: none;
}

.cheat-sheet-markdown :deep(ul),
.cheat-sheet-markdown :deep(ol) {
  padding-left: 25px;
}

.cheat-sheet-markdown :deep(li) {
  margin-bottom: 5px;
}

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

.cheat-sheet-markdown :deep(th) {
  background: #f8f9fa;
  font-weight: bold;
}

.cheat-sheet-markdown :deep(blockquote) {
  border-left: 4px solid #28a745;
  padding-left: 20px;
  margin-left: 0;
  color: #666;
  font-style: italic;
}

.notebook-variants {
  margin-bottom: 20px;
}

.notebook-variants h4 {
  margin-bottom: 15px;
  color: #333;
  font-size: 1.1em;
}

.variant-selector {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.variant-btn {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.variant-btn:hover {
  background: #e9ecef;
  border-color: #ff4136;
}

.variant-btn.active {
  background: #ff4136;
  color: white;
  border-color: #ff4136;
  font-weight: bold;
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

.week-header h2 {
  margin: 0;
  color: #333;
  font-size: 1.2em;
}

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

.toggle-btn:hover {
  background: #ff4136;
  color: white;
}

.toggle-btn.expanded {
  background: #ff4136;
  color: white;
  transform: rotate(180deg);
}

.toggle-icon {
  font-weight: bold;
  display: block;
}

.week-content {
  padding: 20px;
  border: 1px solid #dee2e6;
  border-top: none;
  border-radius: 0 0 8px 8px;
  background: white;
}

.week-section {
  margin-bottom: 20px;
}

.week-section-inner {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.week-description {
  background: #f9f9f9;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
  border-left: 4px solid #ffd700;
}

.week-description :deep(h2),
.week-description :deep(h3),
.week-description :deep(h4) {
  color: #333;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

.week-description :deep(h1) {
  font-size: 1.4em;
  color: #333;
  margin-top: 0;
  margin-bottom: 0.5em;
}

.week-description :deep(h2) {
  font-size: 1.2em;
}

.week-description :deep(h3) {
  font-size: 1.1em;
}

.week-description :deep(h4) {
  font-size: 1em;
}

.week-description :deep(p) {
  line-height: 1.6;
  margin-bottom: 1em;
}

.week-description :deep(ul),
.week-description :deep(ol) {
  margin-bottom: 1em;
  padding-left: 25px;
}

.week-description :deep(code) {
  background: #fff;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}
</style>
