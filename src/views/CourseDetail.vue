<template>
  <section class="course-detail" v-if="course">
    <h1>{{ course.title }}</h1>
    <div v-if="description" v-html="description" class="course-description"></div>

    <!-- Fortschritts-Widget (nur für Python 12-Wochen-Kurs) – ein-/ausklappbar -->
    <div v-if="isWeeklyCourse && fortschrittReady" class="fortschritt-widget">
      <div class="fortschritt-widget-header" @click="fortschrittExpanded = !fortschrittExpanded">
        <h3>🏆 Deine gesammelten Belohnungen</h3>
        <span class="fortschritt-toggle">{{ fortschrittExpanded ? '−' : '+' }}</span>
      </div>
      <div v-show="fortschrittExpanded" class="fortschritt-widget-content">
        <!-- Import/Export für lokale Nutzer -->
        <div class="fortschritt-import-export">
          <button @click="exportFortschritt" class="fortschritt-io-btn" title="Fortschritt als JSON herunterladen">
            📤 Exportieren
          </button>
          <label class="fortschritt-io-btn">
            📥 Importieren
            <input
              type="file"
              accept=".json,application/json"
              class="fortschritt-file-input"
              @change="onImportFile"
            />
          </label>
        </div>
        <div class="fortschritt-skript-erklaerung">
          <div class="fortschritt-skript-header" @click="skriptErklaerungExpanded = !skriptErklaerungExpanded">
            <h4>💻 Lokal arbeiten? So funktioniert das Fortschritt-Skript</h4>
            <span class="fortschritt-toggle">{{ skriptErklaerungExpanded ? '−' : '+' }}</span>
          </div>
          <div v-show="skriptErklaerungExpanded" class="fortschritt-skript-content">
            <p>Wenn du die Notebooks <strong>lokal</strong> in Jupyter oder VS Code ausführst, kannst du trotzdem Punkte sammeln:</p>
            <ol>
              <li><strong>Skript ausführen</strong>, wenn du eine Mission gemeistert hast:
                <pre><code>python fortschritt.py</code></pre>
                Das Skript fragt dich interaktiv: Questreihe (Abenteuer/Pferde/Sci-Fi), Woche (1–12), was du beendet hast (Mission 1–3 oder Boss-Quest 1–3). Es erstellt <code>mein-fortschritt.json</code> im aktuellen Verzeichnis.
              </li>
              <li><strong>Hier importieren</strong>: Klicke oben auf „📥 Importieren“ und wähle deine <code>mein-fortschritt.json</code> – die Missionen werden zusammengeführt.</li>
            </ol>
            <p class="fortschritt-skript-details">Das Skript liegt im Projekt unter <code>scripts/fortschritt.py</code>. Mit dem Notebook-Pack unten kannst du alle Dateien herunterladen. Direkt: <code>python fortschritt.py add abenteuer w10-m1</code> oder <code>python fortschritt.py show</code> für den aktuellen Stand.</p>
          </div>
        </div>

        <!-- Questreihen-Auswahl -->
        <div class="fortschritt-variant-selector">
          <span class="fortschritt-variant-label">Questreihe:</span>
          <div class="fortschritt-variant-buttons">
            <button
              @click="selectedFortschrittVariant = 'alle'"
              :class="{ active: selectedFortschrittVariant === 'alle' }"
              class="fortschritt-variant-btn"
            >
              Alle
            </button>
            <button
              v-for="v in variantKeys"
              :key="v"
              @click="selectedFortschrittVariant = v"
              :class="{ active: selectedFortschrittVariant === v }"
              class="fortschritt-variant-btn"
            >
              {{ variantLabels[v] }}
            </button>
          </div>
        </div>

        <div class="fortschritt-variants">
          <div class="fortschritt-variant" v-for="v in displayedVariantKeys" :key="v">
            <span class="variant-label">{{ variantLabels[v] }}</span>
            <span class="variant-points">{{ getVariantProgress(v).totalPoints }} {{ variantUnits[v] }}</span>
            <span class="variant-items" v-if="getVariantProgress(v).claims.length > 0">
              ({{ getVariantProgress(v).claims.length }} Missionen)
            </span>
          </div>
        </div>

        <!-- Verlauf nach Woche -->
        <div class="fortschritt-weekly-section">
          <h4>📅 Verlauf nach Woche</h4>
          <p class="fortschritt-weekly-hint">Pro Woche gibt es 6 Missionen (3 Haupt + 3 Boss). Zeigt wie viel % du bereits eingelöst hast.</p>
          <div class="fortschritt-by-week" v-for="v in displayedVariantKeys" :key="`week-${v}`">
            <h5>{{ variantLabels[v] }}</h5>
            <div class="week-progress-grid">
              <div
                v-for="w in getWeeklyProgress(v)"
                :key="`${v}-w${w.week}`"
                class="week-progress-card"
                :class="{ 'has-claims': w.claimedCount > 0, 'complete': w.percentOpen === 0 }"
              >
                <div class="week-progress-header" @click="toggleWeekProgress(v, w.week)">
                  <span class="week-number">Woche {{ w.week }}</span>
                  <span class="week-stats">{{ w.claimedCount }}/6 ✓ {{ w.percentDone }}%</span>
                  <span class="week-open" v-if="w.percentOpen > 0">{{ w.percentOpen }}% offen</span>
                  <span class="week-open complete" v-else>✓ Vollständig</span>
                  <span class="week-toggle">{{ isWeekProgressExpanded(v, w.week) ? '−' : '+' }}</span>
                </div>
                <div v-show="isWeekProgressExpanded(v, w.week)" class="week-progress-detail">
                  <ul v-if="w.claims.length > 0" class="fortschritt-claims-list">
                    <li v-for="(c, i) in w.claims" :key="`${v}-w${w.week}-${c.missionId}-${i}`">
                      <span class="claim-label">{{ formatClaimLabel(c) }}:</span>
                      <span class="claim-reward">{{ c.points }} {{ variantUnits[v] }} + {{ c.item }}</span>
                    </li>
                  </ul>
                  <p v-else class="week-no-claims">Noch nichts in dieser Woche eingelöst.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="fortschritt-details" v-for="v in displayedVariantKeys" :key="`details-${v}`">
          <div v-if="getVariantProgress(v).claims.length > 0" class="fortschritt-variant-detail">
            <h4>{{ variantLabels[v] }} – alle eingelösten Belohnungen</h4>
            <ul class="fortschritt-claims-list">
              <li v-for="(c, i) in getVariantProgress(v).claims" :key="`${v}-${c.missionId}-${i}`">
                <span class="claim-label">{{ formatClaimLabel(c) }} (Woche {{ getWeekFromMissionId(c.missionId) }}):</span>
                <span class="claim-reward">{{ c.points }} {{ variantUnits[v] }} + {{ c.item }}</span>
              </li>
            </ul>
            <h4 class="items-header">📦 Gesammelte Items</h4>
            <ul class="fortschritt-items-list">
              <li v-for="(item, i) in getVariantProgress(v).items" :key="`${v}-item-${i}`">{{ item }}</li>
            </ul>
          </div>
        </div>
        <p class="fortschritt-hint" v-if="getTotalClaims() === 0">Klicke „Punkte einlösen“ bei jeder Mission, die du gemeistert hast!</p>
      </div>
    </div>

    <!-- Upcoming Appointments Section -->
    <div class="appointments-section">
      <h3>Nächste Termine für diesen Kurs</h3>
      <div v-if="courseTermine.length > 0" class="termine-list-local">
        <div v-for="termin in courseTermine" :key="termin.id" class="termin-card-local">
          <h4>{{ termin.date }}</h4>
          <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
          <p><strong>Ort:</strong> {{ termin.location }}</p>
          <p v-if="termin.topic"><strong>Thema:</strong> {{ termin.topic }}</p>
        </div>
      </div>
      <p v-else class="termine-empty">Aktuell keine Termine für diesen Kurs.</p>
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

          <!-- Show cheat sheets for weeks with notebooks -->
          <div v-if="week.hasNotebook && week.cheatSheets?.length > 0" class="downloads-section">
            <div v-for="(cheatSheet, csIndex) in week.cheatSheets" :key="csIndex" class="cheat-sheet-container">
              <div class="cheat-sheet-header" @click="toggleCheatSheet(week, csIndex)">
                <h4>{{ cheatSheet.name }}</h4>
                <button class="cheat-sheet-toggle-btn" :class="{ 'expanded': isCheatSheetExpanded(week, csIndex) }">
                  <span class="toggle-icon">{{ isCheatSheetExpanded(week, csIndex) ? '−' : '+' }}</span>
                </button>
              </div>
              
              <div v-show="isCheatSheetExpanded(week, csIndex)" class="cheat-sheet-content">
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
              :variant="week.selectedVariant"
              :course-id="id"
              :key="`${index}-${week.selectedVariant}`"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Notebook-Pack Download (nur für Python 12-Wochen-Kurs) – ganz unten -->
    <div v-if="isWeeklyCourse" class="notebook-pack-download">
      <a href="/python-12-wochen-notebooks.zip" download class="notebook-pack-btn">
        📦 Alle Notebooks als Pack herunterladen
      </a>
      <p class="notebook-pack-hint">Zip mit allen 12 Wochen (Abenteuer, Pferde, Sci-Fi) + Cheat Sheets – zum Arbeiten in Jupyter oder VS Code.</p>
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
import { useFortschritt } from '../composables/useFortschritt';

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
    const fortschrittReady = ref(false);

    const fortschrittExpanded = ref(true);
    const skriptErklaerungExpanded = ref(false);
    const selectedFortschrittVariant = ref('alle');
    const displayedVariantKeys = computed(() =>
      selectedFortschrittVariant.value === 'alle' ? variantKeys : [selectedFortschrittVariant.value]
    );
    const { getVariantProgress, exportProgress, importProgress } = useFortschritt();

    const exportFortschritt = () => {
      const json = exportProgress();
      const blob = new Blob([json], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'mein-fortschritt.json';
      a.click();
      URL.revokeObjectURL(a.href);
    };

    const onImportFile = (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        const result = importProgress(reader.result);
        if (result.ok) {
          alert('Fortschritt wurde importiert und mit deinem bestehenden Stand zusammengeführt.');
        } else {
          alert('Import fehlgeschlagen: ' + (result.error || 'Unbekannter Fehler'));
        }
      };
      reader.readAsText(file, 'UTF-8');
      e.target.value = '';
    };
    const variantKeys = ['abenteuer', 'pferde', 'scifi'];
    const variantLabels = { abenteuer: '🗺️ Abenteuer', pferde: '🐴 Pferde', scifi: '🚀 Sci-Fi' };
    const variantUnits = { abenteuer: 'XP', pferde: 'Huf-Punkte', scifi: 'Cyber Credits' };

    const formatClaimLabel = (c) => c.missionLabel || (c.missionId ? deriveMissionLabel(c.missionId) : '–');
    const deriveMissionLabel = (id) => {
      const m = id.match(/w(\d+)-(m|boss)(\d+)/);
      if (!m) return id;
      return m[2] === 'm' ? `Mission ${m[3]}` : `Boss-Quest ${m[3]}`;
    };
    const getTotalClaims = () => variantKeys.reduce((n, v) => n + getVariantProgress(v).claims.length, 0);

    const getWeekFromMissionId = (missionId) => {
      const m = missionId && missionId.match(/w(\d+)-/);
      return m ? parseInt(m[1], 10) : '?';
    };

    const WEEKLY_TOTAL = 6;
    const getWeeklyProgress = (variant) => {
      const claims = getVariantProgress(variant).claims;
      const byWeek = {};
      for (let w = 1; w <= 12; w++) byWeek[w] = { week: w, claims: [], claimedCount: 0, percentDone: 0, percentOpen: 100 };
      for (const c of claims) {
        const w = getWeekFromMissionId(c.missionId);
        if (typeof w === 'number' && byWeek[w]) {
          byWeek[w].claims.push(c);
          byWeek[w].claimedCount = byWeek[w].claims.length;
          byWeek[w].percentDone = Math.round((byWeek[w].claimedCount / WEEKLY_TOTAL) * 100);
          byWeek[w].percentOpen = 100 - byWeek[w].percentDone;
        }
      }
      return Object.values(byWeek);
    };

    const weekProgressExpanded = ref({});
    const isWeekProgressExpanded = (variant, week) => weekProgressExpanded.value[`${variant}-${week}`] ?? false;
    const toggleWeekProgress = (variant, week) => {
      const key = `${variant}-${week}`;
      weekProgressExpanded.value = { ...weekProgressExpanded.value, [key]: !weekProgressExpanded.value[key] };
    };

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

    const toggleCheatSheet = (week, csIndex) => {
      if (!week.expandedCheatSheets) week.expandedCheatSheets = {};
      week.expandedCheatSheets[csIndex] = !week.expandedCheatSheets[csIndex];
    };

    const isCheatSheetExpanded = (week, csIndex) => {
      return week.expandedCheatSheets?.[csIndex] ?? false;
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
                            cheatSheets: [],
                            wissensCheatSheetNotebookUrl: null,
                            expandedCheatSheets: {},
                            selectedVariant: null,
                            expanded: weekNum === 1, // Nur erste Woche standardmäßig geöffnet
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
                    } else if (path.includes('wissens_cheat_sheet')) {
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
                                cheatSheets: [],
                                wissensCheatSheetNotebookUrl: null,
                                expandedCheatSheets: {},
                                selectedVariant: null,
                                expanded: weekNum === 1,
                            });
                        }
                        weeklyContent[weekNum].wissensCheatSheetNotebookUrl = notebookUrl;
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
                            const url = path.replace('../../content', '/content').replace('.md', '') + '.md';
                            const filename = path.split('/').pop() || '';

                            let name = 'Cheat Sheet';
                            if (filename.includes('wissens')) name = '📚 Wissens-Cheat-Sheet';
                            else if (filename.includes('turtle')) name = '🐢 Turtle Cheat Sheet';

                            try {
                                const contentLoader = await loader();
                                const parsed = fm(contentLoader.default);
                                if (!weeklyContent[weekNum].cheatSheets) weeklyContent[weekNum].cheatSheets = [];
                                const notebookUrl = weeklyContent[weekNum].wissensCheatSheetNotebookUrl || null;
                                weeklyContent[weekNum].cheatSheets.push({
                                    name,
                                    content: marked(parsed.body),
                                    url,
                                    notebookUrl: filename.includes('wissens') ? notebookUrl : null
                                });
                            } catch (e) {
                                console.error('Could not load cheat sheet content:', e);
                            }
                        }
                    }
                }
            });
            await Promise.all(cheatSheetPromises);

            // Sort cheat sheets: Wissens-Cheat-Sheet first, then Turtle
            Object.values(weeklyContent).forEach(week => {
                if (week.cheatSheets?.length > 1) {
                    week.cheatSheets.sort((a, b) => (a.name.includes('Wissens') ? 0 : 1) - (b.name.includes('Wissens') ? 0 : 1));
                }
            });

            weeks.value = Object.values(weeklyContent).sort((a, b) => {
                const weekA = parseInt(a.title.match(/\d+/) || 0, 10);
                const weekB = parseInt(b.title.match(/\d+/) || 0, 10);
                return weekA - weekB;
            });
        }
        fortschrittReady.value = true;
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
      id: props.id,
      course,
      description,
      weeks,
      isWeeklyCourse,
      courseTermine,
      fortschrittReady,
      fortschrittExpanded,
      skriptErklaerungExpanded,
      selectedFortschrittVariant,
      displayedVariantKeys,
      variantKeys,
      variantLabels,
      variantUnits,
      getVariantProgress,
      formatClaimLabel,
      getTotalClaims,
      exportFortschritt,
      onImportFile,
      getWeekFromMissionId,
      getWeeklyProgress,
      isWeekProgressExpanded,
      toggleWeekProgress,
      setVariant,
      toggleWeek,
      toggleCheatSheet,
      isCheatSheetExpanded,
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

.fortschritt-widget {
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
  border: 2px solid #ffd700;
  border-radius: 8px;
  margin-bottom: 40px;
  overflow: hidden;
}

.fortschritt-widget-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  cursor: pointer;
  user-select: none;
}

.fortschritt-widget-header:hover {
  background: rgba(255, 255, 255, 0.3);
}

.fortschritt-widget-header h3 {
  margin: 0;
  color: #333;
  border: none;
  padding: 0;
}

.fortschritt-toggle {
  font-size: 1.5em;
  font-weight: bold;
  color: #666;
}

.fortschritt-widget-content {
  padding: 0 20px 20px 20px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-import-export {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-io-btn {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid #dee2e6;
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 0.9em;
  cursor: pointer;
  transition: all 0.2s;
  margin: 0;
}

.fortschritt-io-btn:hover {
  border-color: #ffd700;
  background: white;
}

.fortschritt-file-input {
  display: none;
}

.fortschritt-io-hint {
  margin: 0;
  font-size: 0.85em;
  color: #666;
  flex: 1 1 100%;
}

.fortschritt-skript-erklaerung {
  margin-top: 12px;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  overflow: hidden;
  background: #f8f9fa;
}

.fortschritt-skript-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  cursor: pointer;
  user-select: none;
}

.fortschritt-skript-header:hover {
  background: #e9ecef;
}

.fortschritt-skript-header h4 {
  margin: 0;
  font-size: 0.95em;
  color: #333;
}

.fortschritt-skript-content {
  padding: 0 16px 16px 16px;
  border-top: 1px solid #dee2e6;
}

.fortschritt-skript-content p {
  margin: 12px 0 0 0;
  font-size: 0.9em;
  line-height: 1.6;
  color: #444;
}

.fortschritt-skript-content ol {
  margin: 8px 0 0 0;
  padding-left: 20px;
}

.fortschritt-skript-content li {
  margin-bottom: 10px;
  font-size: 0.9em;
  line-height: 1.6;
}

.fortschritt-skript-content pre {
  margin: 6px 0 0 0;
  padding: 8px 12px;
  background: #e9ecef;
  border-radius: 4px;
  font-size: 0.85em;
  overflow-x: auto;
}

.fortschritt-skript-content code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.9em;
}

.fortschritt-skript-details {
  font-size: 0.85em;
  color: #666;
  margin-top: 12px;
}

.fortschritt-variant-selector {
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-variant-label {
  display: block;
  font-size: 0.9em;
  font-weight: 600;
  color: #555;
  margin-bottom: 10px;
}

.fortschritt-variant-buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.fortschritt-variant-btn {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid #dee2e6;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s;
}

.fortschritt-variant-btn:hover {
  border-color: #ffd700;
  background: rgba(255, 255, 255, 1);
}

.fortschritt-variant-btn.active {
  background: #ffd700;
  border-color: #ffd700;
  font-weight: 600;
  color: #333;
}

.fortschritt-variants {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  margin: 15px 0;
}

.fortschritt-variant {
  background: rgba(255, 255, 255, 0.8);
  padding: 10px 16px;
  border-radius: 8px;
  border: 1px solid #eee;
  font-weight: 600;
}

.variant-label {
  margin-right: 8px;
}

.variant-points {
  color: #ff4136;
}

.variant-items {
  font-size: 0.9em;
  color: #666;
  margin-left: 4px;
}

.fortschritt-weekly-section {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 215, 0, 0.5);
}

.fortschritt-weekly-section h4 {
  margin: 0 0 6px 0;
  font-size: 1em;
  color: #333;
}

.fortschritt-weekly-hint {
  margin: 0 0 16px 0;
  font-size: 0.85em;
  color: #666;
}

.fortschritt-by-week h5 {
  margin: 12px 0 8px 0;
  font-size: 0.95em;
  color: #555;
}

.week-progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 10px;
}

.week-progress-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
}

.week-progress-card.has-claims {
  border-color: #c8e6c9;
  background: rgba(232, 245, 233, 0.6);
}

.week-progress-card.complete {
  border-color: #2e7d32;
  background: rgba(200, 230, 201, 0.8);
}

.week-progress-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  padding: 10px 12px;
  cursor: pointer;
  font-size: 0.9em;
}

.week-progress-header:hover {
  background: rgba(255, 255, 255, 0.7);
}

.week-number {
  font-weight: 600;
  color: #333;
  min-width: 65px;
}

.week-stats {
  color: #2e7d32;
  font-weight: 600;
}

.week-open {
  font-size: 0.85em;
  color: #666;
}

.week-open.complete {
  color: #2e7d32;
}

.week-toggle {
  margin-left: auto;
  font-weight: bold;
  color: #999;
}

.week-progress-detail {
  padding: 0 12px 12px 12px;
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.week-progress-detail ul {
  margin: 8px 0 0 0;
  padding-left: 18px;
}

.week-no-claims {
  margin: 8px 0 0 0;
  font-size: 0.9em;
  color: #999;
  font-style: italic;
}

.fortschritt-details {
  margin-top: 16px;
}

.fortschritt-variant-detail {
  background: rgba(255, 255, 255, 0.9);
  padding: 16px;
  border-radius: 8px;
  border: 1px solid #eee;
  margin-bottom: 12px;
}

.fortschritt-variant-detail h4 {
  margin: 0 0 10px 0;
  font-size: 1em;
  color: #555;
}

.fortschritt-variant-detail .items-header {
  margin-top: 16px;
  margin-bottom: 8px;
}

.fortschritt-claims-list,
.fortschritt-items-list {
  margin: 0 0 0 4px;
  padding-left: 20px;
}

.fortschritt-claims-list li,
.fortschritt-items-list li {
  margin-bottom: 6px;
}

.claim-label {
  font-weight: 600;
  color: #333;
  margin-right: 6px;
}

.claim-reward {
  color: #666;
}

.fortschritt-hint {
  margin: 15px 0 0 0;
  font-size: 0.9em;
  color: #666;
}

.notebook-pack-download {
  background: linear-gradient(135deg, #e8f4f8 0%, #d4ebf2 100%);
  border: 2px solid #0ea5e9;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 40px;
}

.notebook-pack-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: #0ea5e9;
  color: white;
  padding: 14px 24px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05em;
  transition: all 0.2s;
}

.notebook-pack-btn:hover {
  background: #0284c7;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4);
}

.notebook-pack-hint {
  margin: 12px 0 0 0;
  font-size: 0.9em;
  color: #555;
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

.termine-empty {
  color: #666;
  font-style: italic;
  margin: 0;
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