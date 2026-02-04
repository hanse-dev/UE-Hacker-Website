<template>
  <section class="course-detail" v-if="course">
    <h1>{{ course.title }}</h1>
    <div v-if="description" v-html="description" class="course-description"></div>

    <!-- Upcoming Appointments Section -->
    <div class="appointments-section" v-if="courseTermine.length > 0">
      <h3>Nächste Termine für diesen Kurs</h3>
      <div class="termine-list-local">
        <div v-for="termin in courseTermine" :key="termin.id" class="termin-card-local">
          <h4>{{ termin.date }}</h4>
          <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
          <p><strong>Ort:</strong> {{ termin.location }}</p>
          <p v-if="termin.topic"><strong>Thema:</strong> {{ termin.topic }}</p>
        </div>
      </div>
    </div>

    <div class="table-of-contents" v-if="weeks.length > 0">
      <h3>Inhaltsverzeichnis</h3>
      <ol>
        <li v-for="(week, index) in weeks" :key="`toc-${index}`">
          <a :href="`#woche-${index + 1}`">{{ week.title }}</a>
        </li>
      </ol>
    </div>

    <div v-for="(week, index) in weeks" :key="index" class="week-section" :id="`woche-${index + 1}`">
      <div class="week-section-inner">
        <div class="week-header" @click="toggleWeek(index)">
          <h2>{{ week.title }}</h2>
          <button class="toggle-btn" :class="{ 'expanded': week.expanded }">
            <span class="toggle-icon">{{ week.expanded ? '−' : '+' }}</span>
          </button>
        </div>

        <div v-show="week.expanded" class="week-content">
          <!-- Show markdown description if available -->
          <div v-if="week.content" v-html="week.content" class="week-description"></div>

          <!-- Show downloads for weeks with notebooks (only cheat sheets) -->
          <div v-if="week.hasNotebook && week.downloads.some(d => d.isCheatSheet)" class="downloads-section">
            <div class="cheat-sheet-container">
              <div class="cheat-sheet-header" @click="toggleCheatSheet(week)">
                <h4>🐢 Turtle Cheat Sheet</h4>
                <button class="cheat-sheet-toggle-btn" :class="{ 'expanded': week.showCheatSheet }">
                  <span class="toggle-icon">{{ week.showCheatSheet ? '−' : '+' }}</span>
                </button>
              </div>
              
              <div v-show="week.showCheatSheet" class="cheat-sheet-content">
                <div class="cheat-sheet-actions">
                  <a :href="week.downloads.find(d => d.isCheatSheet).url" download class="download-btn">
                    <span class="download-icon">📥</span>
                    Als Markdown herunterladen
                  </a>
                </div>
                
                <div class="cheat-sheet-preview" v-if="week.cheatSheetContent">
                  <div v-html="week.cheatSheetContent" class="cheat-sheet-markdown"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Show downloads for non-notebook weeks -->
          <div v-if="!week.hasNotebook && week.downloads.length > 0" class="downloads-section">
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

          <!-- Show interactive notebook if available -->
          <div v-if="week.hasNotebook" class="notebook-variants">
            <h4>📚 Notebook-Varianten</h4>
            <div class="variant-selector">
              <button 
                v-if="week.hasAbenteuerVariant"
                @click="setVariant(week, 'abenteuer')"
                :class="{ active: week.selectedVariant === 'abenteuer' }"
                class="variant-btn"
              >
                🗺️ Abenteuer
              </button>
              <button 
                v-if="week.hasPferdeVariant"
                @click="setVariant(week, 'pferde')"
                :class="{ active: week.selectedVariant === 'pferde' }"
                class="variant-btn"
              >
                🐴 Pferde
              </button>
              <button 
                v-if="week.hasScifiVariant"
                @click="setVariant(week, 'scifi')"
                :class="{ active: week.selectedVariant === 'scifi' }"
                class="variant-btn"
              >
                🚀 Sci-Fi
              </button>
            </div>
            
            <JupyterNotebook
              :notebook-path="getNotebookPath(week)"
              :notebook-url="getNotebookUrl(week)"
              :week-number="index + 1"
              :key="week.selectedVariant"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
  <div v-else>
      <p>Kurs wird geladen...</p>
  </div>
</template>

<script>
import { ref, onMounted, computed, reactive } from 'vue';
import fm from 'front-matter';
import { marked } from 'marked';
import JupyterNotebook from '../components/JupyterNotebook.vue';

export default {
  name: 'CourseDetail',
  components: {
    JupyterNotebook,
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const course = ref(null);
    const description = ref('');
    const weeks = ref([]);
    const courseTermine = ref([]);

    const isWeeklyCourse = computed(() => {
        return props.id === 'python-12-wochen-grundkurs';
    });

    const parseDate = (dateString) => {
      const datePart = dateString.split(', ')[1];
      if (!datePart) return null;
      const parts = datePart.split('.');
      if (parts.length !== 3) return null;
      return new Date(`20${parts[2]}`, parts[1] - 1, parts[0]);
    };

    const parseISO = (isoString) => (isoString ? new Date(isoString) : null);
    const isRecurringActive = (termin, today) => {
      if (!termin.recurring || !termin.validFrom) return false;
      const from = parseISO(termin.validFrom);
      if (!from || today < from) return false;
      if (!termin.validUntil) return true;
      const until = parseISO(termin.validUntil);
      return until && today <= until;
    };

    const setVariant = (week, variant) => {
      week.selectedVariant = variant;
    };

    const toggleWeek = (index) => {
      weeks.value[index].expanded = !weeks.value[index].expanded;
    };

    const toggleCheatSheet = (week) => {
      week.showCheatSheet = !week.showCheatSheet;
    };

    onMounted(async () => {
      // Load course data from JSON
      try {
        const response = await fetch('/kurse.json');
        const kurse = await response.json();
        course.value = kurse.find(k => k.id === props.id);
      } catch (e) {
        console.error('Could not load courses:', e);
      }

      if (course.value) {
        // Load description
        try {
          const descModule = await import(`../../content/${course.value.contentPath}/beschreibung.md?raw`);
          description.value = marked(descModule.default);
        } catch (e) {
          console.error('Could not load course description:', e);
          description.value = '<p>Die Beschreibung für diesen Kurs konnte nicht geladen werden.</p>';
        }

        // Load appointments for this course
        try {
            const response = await fetch('/termine.json');
            const allTermine = await response.json();
            const today = new Date();
            today.setHours(0, 0, 0, 0);

            const getSortDate = (termin) => {
                if (termin.recurring) return parseISO(termin.validFrom) || today;
                return parseDate(termin.date) || today;
            };

            courseTermine.value = allTermine
                .filter(termin => {
                    if (termin.cancelled || !termin.link.startsWith(`/kurs/${props.id}`)) return false;
                    if (termin.recurring) return isRecurringActive(termin, today);
                    const terminDate = parseDate(termin.date);
                    return terminDate && terminDate >= today;
                })
                .sort((a, b) => {
                    const aRec = a.recurring ? 0 : 1;
                    const bRec = b.recurring ? 0 : 1;
                    if (aRec !== bRec) return aRec - bRec;
                    return getSortDate(a) - getSortDate(b);
                });
        } catch (e) {
            console.error('Could not load appointments:', e);
        }

        // Load weekly content only for the 12-week course
        if (isWeeklyCourse.value) {
            const weekModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.md', { query: '?raw' });
            const notebookModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.ipynb', { query: '?url', import: 'default' });
            const downloadModules = import.meta.glob('../../content/python-12-wochen-grundkurs/woche-*/*.*', { query: '?url', import: 'default' });
            const weeklyContent = {};

            // First, check for notebooks
            const notebookPromises = Object.entries(notebookModules).map(async ([path, loader]) => {
                const weekMatch = path.match(/woche-(\d+)/);
                if (weekMatch) {
                    const weekNum = parseInt(weekMatch[1], 10);
                    const notebookUrl = await loader();
                    
                    // Detect variant type from filename
                    const isAbenteuer = path.includes('_abenteuer.ipynb');
                    const isPferde = path.includes('_pferde.ipynb');
                    const isScifi = path.includes('_scifi.ipynb');
                    
                    if (!weeklyContent[weekNum]) {
                        weeklyContent[weekNum] = reactive({
                            title: `Woche ${weekNum}`,
                            hasNotebook: true,
                            hasAbenteuerVariant: false,
                            hasPferdeVariant: false,
                            hasScifiVariant: false,
                            abenteuerNotebookPath: null,
                            abenteuerNotebookUrl: null,
                            pferdeNotebookPath: null,
                            pferdeNotebookUrl: null,
                            scifiNotebookPath: null,
                            scifiNotebookUrl: null,
                            downloads: [],
                            selectedVariant: null,
                            expanded: weekNum === 1, // Nur erste Woche standardmäßig geöffnet
                            showCheatSheet: false, // Cheat Sheet standardmäßig geschlossen
                        });
                    }
                    
                    if (isAbenteuer) {
                        weeklyContent[weekNum].hasAbenteuerVariant = true;
                        weeklyContent[weekNum].abenteuerNotebookPath = notebookUrl;
                        weeklyContent[weekNum].abenteuerNotebookUrl = notebookUrl;
                        if (!weeklyContent[weekNum].selectedVariant) {
                            weeklyContent[weekNum].selectedVariant = 'abenteuer';
                        }
                    } else if (isPferde) {
                        weeklyContent[weekNum].hasPferdeVariant = true;
                        weeklyContent[weekNum].pferdeNotebookPath = notebookUrl;
                        weeklyContent[weekNum].pferdeNotebookUrl = notebookUrl;
                        if (!weeklyContent[weekNum].selectedVariant) {
                            weeklyContent[weekNum].selectedVariant = 'pferde';
                        }
                    } else if (isScifi) {
                        weeklyContent[weekNum].hasScifiVariant = true;
                        weeklyContent[weekNum].scifiNotebookPath = notebookUrl;
                        weeklyContent[weekNum].scifiNotebookUrl = notebookUrl;
                        if (!weeklyContent[weekNum].selectedVariant) {
                            weeklyContent[weekNum].selectedVariant = 'scifi';
                        }
                    }
                }
            });
            await Promise.all(notebookPromises);

            // Then load markdown for all weeks
            const markdownPromises = Object.entries(weekModules).map(async ([path, loader]) => {
                const weekMatch = path.match(/woche-(\d+)/);
                if (weekMatch) {
                    const weekNum = parseInt(weekMatch[1], 10);
                    // Skip cheat sheet files - they are handled separately
                    if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) {
                        return;
                    }
                    const rawContent = (await loader()).default;
                    const parsed = fm(rawContent);

                    if (weeklyContent[weekNum]) {
                        // Week already has a notebook, add markdown content to it
                        weeklyContent[weekNum].content = marked(parsed.body);
                        if (parsed.attributes.title) {
                            weeklyContent[weekNum].title = parsed.attributes.title;
                        }
                    } else {
                        // Week has no notebook, create entry with markdown
                        weeklyContent[weekNum] = reactive({
                            title: parsed.attributes.title || `Woche ${weekNum}`,
                            content: marked(parsed.body),
                            hasNotebook: false,
                            downloads: [],
                            selectedVariant: null,
                            expanded: weekNum === 1, // Nur erste Woche standardmäßig geöffnet
                        });
                    }
                }
            });
            await Promise.all(markdownPromises);

            // Load other downloads (excluding notebooks and markdown files)
            const downloadPromises = Object.entries(downloadModules).map(async ([path, loader]) => {
                if (path.endsWith('.md') || path.endsWith('.ipynb')) return;
                const weekMatch = path.match(/woche-(\d+)/);
                if (weekMatch) {
                    const weekNum = parseInt(weekMatch[1], 10);
                    if (weeklyContent[weekNum]) {
                        const url = await loader();
                        weeklyContent[weekNum].downloads.push({
                            name: path.split('/').pop(),
                            url: url,
                        });
                    }
                }
            });
            await Promise.all(downloadPromises);

            // Load cheat sheets (special markdown files)
            const cheatSheetPromises = Object.entries(weekModules).map(async ([path, loader]) => {
                if (path.includes('cheat_sheet') || path.includes('cheat-sheet')) {
                    const weekMatch = path.match(/woche-(\d+)/);
                    if (weekMatch) {
                        const weekNum = parseInt(weekMatch[1], 10);
                        if (weeklyContent[weekNum]) {
                            const url = path.replace('../../content', '/content').replace('.md', '');
                            
                            // Fetch and render the cheat sheet content
                            try {
                                const contentLoader = await loader();
                                const parsed = fm(contentLoader.default);
                                weeklyContent[weekNum].cheatSheetContent = marked(parsed.body);
                            } catch (e) {
                                console.error('Could not load cheat sheet content:', e);
                            }
                            
                            weeklyContent[weekNum].downloads.push({
                                name: '🐢 Turtle Cheat Sheet',
                                url: url + '.md',
                                isCheatSheet: true
                            });
                        }
                    }
                }
            });
            await Promise.all(cheatSheetPromises);

            weeks.value = Object.values(weeklyContent).sort((a, b) => {
                const weekA = parseInt(a.title.match(/\d+/) || 0, 10);
                const weekB = parseInt(b.title.match(/\d+/) || 0, 10);
                return weekA - weekB;
            });
        }
      }
    });

    const getNotebookPath = (week) => {
      if (week.selectedVariant === 'abenteuer') return week.abenteuerNotebookPath;
      if (week.selectedVariant === 'pferde') return week.pferdeNotebookPath;
      if (week.selectedVariant === 'scifi') return week.scifiNotebookPath;
      return null;
    };

    const getNotebookUrl = (week) => {
      if (week.selectedVariant === 'abenteuer') return week.abenteuerNotebookUrl;
      if (week.selectedVariant === 'pferde') return week.pferdeNotebookUrl;
      if (week.selectedVariant === 'scifi') return week.scifiNotebookUrl;
      return null;
    };

    return {
      course,
      description,
      weeks,
      isWeeklyCourse,
      courseTermine,
      setVariant,
      toggleWeek,
      toggleCheatSheet,
      getNotebookPath,
      getNotebookUrl,
    };
  },
};
</script>

<style scoped>
.course-detail {
  padding: 20px;
}
.course-description {
  margin-bottom: 40px;
  font-size: 1.1em;
}
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

.cheat-sheet-iframe {
  width: 100%;
  height: 600px;
  border: none;
  background: white;
}

.cheat-sheet-markdown {
  padding: 20px;
  font-size: 0.95em;
  line-height: 1.6;
}

.cheat-sheet-markdown h1 {
  color: #28a745;
  border-bottom: 2px solid #28a745;
  padding-bottom: 10px;
  margin-top: 0;
}

.cheat-sheet-markdown h2 {
  color: #333;
  border-bottom: 1px solid #eee;
  padding-bottom: 5px;
  margin-top: 2em;
}

.cheat-sheet-markdown h3 {
  color: #555;
  margin-top: 1.5em;
}

.cheat-sheet-markdown code {
  background: #f8f9fa;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  border: 1px solid #e9ecef;
}

.cheat-sheet-markdown pre {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 6px;
  overflow-x: auto;
  border: 1px solid #e9ecef;
}

.cheat-sheet-markdown pre code {
  background: none;
  padding: 0;
  border: none;
}

.cheat-sheet-markdown ul,
.cheat-sheet-markdown ol {
  padding-left: 25px;
}

.cheat-sheet-markdown li {
  margin-bottom: 5px;
}

.cheat-sheet-markdown table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.cheat-sheet-markdown th,
.cheat-sheet-markdown td {
  border: 1px solid #ddd;
  padding: 8px 12px;
  text-align: left;
}

.cheat-sheet-markdown th {
  background: #f8f9fa;
  font-weight: bold;
}

.cheat-sheet-markdown blockquote {
  border-left: 4px solid #28a745;
  padding-left: 20px;
  margin-left: 0;
  color: #666;
  font-style: italic;
}

.table-of-contents {
  background-color: #fdfdfd;
  border: 1px solid #eee;
  padding: 20px;
  margin-bottom: 40px;
  border-radius: 8px;
}

.table-of-contents h3 {
  margin-top: 0;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 10px;
}

.table-of-contents ol {
  padding-left: 20px;
  margin: 0;
}

.table-of-contents li {
  margin-bottom: 10px;
}

.table-of-contents a {
  text-decoration: none;
  color: #333;
}

.table-of-contents a:hover {
  color: #ff4136;
}

.appointments-section {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  padding: 20px;
  margin-bottom: 40px;
  border-radius: 8px;
}

.appointments-section h3 {
  margin-top: 0;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 10px;
}

.termin-card-local {
  background: #fff;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
}

.termin-card-local h4 {
    margin-top: 0;
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
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

</style>