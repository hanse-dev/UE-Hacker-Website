<template>
  <section class="week-tour">
    <p v-if="loading" class="tour-loading">{{ t('tour.loading') }}</p>

    <template v-else>
      <!-- Seite 1: Woche wählen -->
      <div v-if="phase === 'week'" class="tour-page">
        <p class="tour-intro">{{ t('tour.intro') }}</p>
        <div class="week-picker-header">
          <h2 class="section-label">{{ t('tour.pickWeek') }}</h2>
          <button class="certificates-link" @click="phase = 'certificates'">
            🎓 {{ t('tour.certificates.count').replace('{n}', countCertificates()) }} · {{ t('tour.certificates.viewAll') }}
          </button>
        </div>

        <div class="week-map" ref="weekMapRef">
          <svg class="week-map-path" :viewBox="mapViewBox" preserveAspectRatio="none">
            <path :d="pathD" />
          </svg>
          <div class="tile-grid week-tile-grid">
            <button
              v-for="(week, index) in weeks"
              :key="index"
              :ref="(el) => setTileRef(el, index)"
              class="tile week-tile"
              :class="{ active: selectedWeekIndex === index }"
              :style="tileGridStyle(index)"
              :data-week="index + 1"
              @click="selectWeek(index)"
            >
              <span class="week-tile-icon">
                {{ weekIcon(index + 1) }}
                <span v-if="isCertificateEarned(index + 1)" class="week-tile-badge" data-earned="true">🎓</span>
              </span>
              <strong>{{ t('week.label') }} {{ index + 1 }}</strong>
              <span>{{ weekTheme(week) }}</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Seite 2: Thema wählen -->
      <div v-else-if="phase === 'variant' && selectedWeek" class="tour-page">
        <button class="breadcrumb-back" @click="phase = 'week'">← {{ t('tour.pickWeek') }}</button>
        <h2 class="section-label">{{ t('week.label') }} {{ selectedWeekIndex + 1 }}: {{ weekTheme(selectedWeek) }}</h2>
        <p class="tour-intro">{{ t('tour.pickVariant') }}</p>
        <div class="tile-grid variant-tile-grid">
          <button
            v-for="v in availableVariants"
            :key="v.key"
            class="tile variant-tile"
            :class="{ active: selectedWeek.selectedVariant === v.key }"
            :data-variant="v.key"
            @click="selectVariant(v.key)"
          >
            {{ v.label }}
          </button>
        </div>

        <div class="week-zip-download">
          <a :href="`/wochen-zips/woche-${selectedWeekIndex + 1}${lang === 'en' ? '-en' : ''}.zip`" download class="btn-week-zip">
            {{ t('week.download.week').replace('{n}', selectedWeekIndex + 1) }}
          </a>
          <span class="week-zip-hint">{{ t('week.download.week.hint') }}</span>
        </div>
      </div>

      <!-- Seite 3: Meine Zertifikate -->
      <div v-else-if="phase === 'certificates'" class="tour-page">
        <button class="breadcrumb-back" @click="phase = 'week'">{{ t('tour.certificates.back') }}</button>
        <h2 class="section-label">{{ t('tour.certificates.title') }}</h2>
        <FortschrittWidget :weeks="weeks" :start-expanded="true" />
      </div>

      <!-- Seite 4+: Kursinhalt (geführte Tour) -->
      <WeekTourStepper
        v-else-if="phase === 'tour' && selectedWeek && selectedWeek.selectedVariant"
        :week="selectedWeek"
        :week-number="selectedWeekIndex + 1"
        :week-theme="weekTheme(selectedWeek)"
        :variant="selectedWeek.selectedVariant"
        :variant-label="selectedVariantLabel"
        :course-id="courseId"
        :initial-step="initialStep"
        :has-next-week="hasNextWeek"
        :lesson-content-path="lessonContentPath"
        :key="selectedWeekIndex"
        @change-week="phase = 'week'"
        @change-variant="phase = 'variant'"
        @go-next-week="goToNextWeek"
      />
    </template>
  </section>
</template>

<script>
import { ref, computed, onMounted, onUnmounted, nextTick, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import WeekTourStepper from './WeekTourStepper.vue';
import FortschrittWidget from './FortschrittWidget.vue';
import { loadWeeklyContent } from '../composables/useWeeklyContent.js';
import { useLanguage } from '../composables/useLanguage.js';
import { useZertifikate } from '../composables/useZertifikate.js';

const COURSE_ID = 'python-12-wochen-grundkurs';

const VARIANT_CONFIG = [
  { key: 'abenteuer', flagKey: 'hasAbenteuerVariant', labelKey: 'variant.adventure' },
  { key: 'pferde',    flagKey: 'hasPferdeVariant',    labelKey: 'variant.horses' },
  { key: 'scifi',     flagKey: 'hasScifiVariant',     labelKey: 'variant.scifi' },
];

// Technisches Wochenthema (variantenunabhängig, siehe INHALTE.md Abschnitt 3) als Icon für die
// Übersicht - vor der Themenwahl kennen wir noch keine Variante, daher ein neutrales Symbol.
const WEEK_ICONS = {
  1: '🚀', 2: '🔤', 3: '🔀', 4: '🔁', 5: '🧩', 6: '📋',
  7: '🧰', 8: '🗃️', 9: '💾', 10: '🏗️', 11: '🧬', 12: '🏆',
};

// Rückwärtskompatibel zum alten ?week=&tab=-Schema der früheren Akkordeon-Kursseite
// (WeekSection.vue, entfernt) - z.B. von PlacementCourse.vue und den Cäsar-Chiffre-Lektionen
// verlinkt. Nur relevant, falls ein Deep-Link zufällig schon eine Variante mitbringt (das reale
// alte Schema tat das nie, landet also ohnehin auf der Themen-Wahl-Seite mit Lektion als Standard).
const TAB_TO_STEP = {
  lektion: '1_lektion', lesson: '1_lektion',
  debug: '2_debug',
  missionen: '3_missionen', missions: '3_missionen',
  boss: '5_boss',
  check: '4_check',
  loesungen: '6_loesungen', solutions: '6_loesungen',
  glossar: '0_glossar', glossary: '0_glossar',
};

/**
 * Catmull-Rom-Spline durch alle Punkte, als kubische Bezier-Kurven ausgegeben - ergibt einen
 * weichen "Reiseweg" statt gerader Liniensegmente. Klassische Umrechnung mit Tension 1/6.
 */
function smoothPathD(points) {
  if (points.length < 2) return '';
  if (points.length === 2) {
    return `M ${points[0].x},${points[0].y} L ${points[1].x},${points[1].y}`;
  }
  let d = `M ${points[0].x},${points[0].y}`;
  for (let i = 0; i < points.length - 1; i++) {
    const p0 = points[i - 1] || points[i];
    const p1 = points[i];
    const p2 = points[i + 1];
    const p3 = points[i + 2] || p2;
    const cp1x = p1.x + (p2.x - p0.x) / 6;
    const cp1y = p1.y + (p2.y - p0.y) / 6;
    const cp2x = p2.x - (p3.x - p1.x) / 6;
    const cp2y = p2.y - (p3.y - p1.y) / 6;
    d += ` C ${cp1x},${cp1y} ${cp2x},${cp2y} ${p2.x},${p2.y}`;
  }
  return d;
}

export default {
  name: 'WeekTourView',
  components: { WeekTourStepper, FortschrittWidget },
  setup() {
    const { lang, t } = useLanguage();
    const route = useRoute();
    const router = useRouter();
    const { isCertificateEarned, countCertificates } = useZertifikate();

    const weeks = ref([]);
    const loading = ref(true);
    const selectedWeekIndex = ref(null);
    const initialStep = ref(null);
    const phase = ref('week'); // 'week' | 'variant' | 'certificates' | 'tour'

    const selectedWeek = computed(() =>
      selectedWeekIndex.value != null ? weeks.value[selectedWeekIndex.value] : null
    );

    const availableVariants = computed(() => {
      if (!selectedWeek.value) return [];
      return VARIANT_CONFIG
        .filter((v) => selectedWeek.value[v.flagKey])
        .map((v) => ({ key: v.key, label: t(v.labelKey) }));
    });

    const selectedVariantLabel = computed(() =>
      availableVariants.value.find((v) => v.key === selectedWeek.value?.selectedVariant)?.label ?? ''
    );

    // Wochen im Lektions-Format (Format wie der JS-Grundkurs): pro Woche/Thema/Sprache ein Ordner
    // content/python-woche{N}-{thema}[-en]/ mit lessons.json. Existiert er, ersetzt er die
    // Notebook-Schritte Lektion/Debug/Missionen/Boss dieser Woche (siehe WeekTourStepper.vue).
    const lessonFolders = new Set(
      Object.keys(import.meta.glob('../../content/python-woche*/lessons.json')).map((k) => k.split('/').slice(-2)[0])
    );
    const lessonContentPath = computed(() => {
      const variant = selectedWeek.value?.selectedVariant;
      if (selectedWeekIndex.value == null || !variant) return null;
      const name = `python-woche${selectedWeekIndex.value + 1}-${variant}${lang.value === 'en' ? '-en' : ''}`;
      return lessonFolders.has(name) ? name : null;
    });

    const hasNextWeek = computed(() =>
      selectedWeekIndex.value != null && selectedWeekIndex.value + 1 < weeks.value.length
    );

    const weekTheme = (week) => {
      const raw = week.title ?? '';
      if (!raw.includes(':')) return raw;
      return raw.split(':').slice(1).join(':').trim();
    };

    const weekIcon = (weekNumber) => WEEK_ICONS[weekNumber] ?? '📘';

    const selectWeek = (index) => {
      selectedWeekIndex.value = index;
      phase.value = 'variant';
    };

    const selectVariant = (variant) => {
      if (!selectedWeek.value) return;
      selectedWeek.value.selectedVariant = variant;
      initialStep.value = null;
      phase.value = 'tour';
      router.replace({ query: { week: selectedWeekIndex.value + 1, variant } });
    };

    /** "Nächste Woche" nach bestandenem Check: fällt auf die erste verfügbare Variante zurück,
     * falls die aktuelle in der nächsten Woche fehlt; ohne nächste Woche wird der Button gar
     * nicht erst angezeigt (siehe hasNextWeek). */
    const goToNextWeek = () => {
      if (selectedWeekIndex.value == null) return;
      const nextIndex = selectedWeekIndex.value + 1;
      if (nextIndex >= weeks.value.length) return;
      const nextWeek = weeks.value[nextIndex];
      const currentVariant = selectedWeek.value?.selectedVariant;
      const currentCfg = VARIANT_CONFIG.find((v) => v.key === currentVariant);
      const variant = currentCfg && nextWeek[currentCfg.flagKey]
        ? currentVariant
        : VARIANT_CONFIG.find((v) => nextWeek[v.flagKey])?.key;

      selectedWeekIndex.value = nextIndex;
      if (variant) {
        nextWeek.selectedVariant = variant;
        initialStep.value = null;
        phase.value = 'tour';
        router.replace({ query: { week: nextIndex + 1, variant } });
      } else {
        phase.value = 'variant';
      }
      // Vorher stand man am Ende des Check-Schritts weit unten - ohne Scroll-Reset würde die
      // neue Woche irgendwo mittendrin aufgehen. Zur Lektion selbst scrollen (Anfang von
      // .tour-stepper), nicht zum ganz obersten Seitenrand (Kursbeschreibung/Banner davor).
      nextTick(() => {
        document.querySelector('.tour-stepper')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    };

    const applyDeepLink = () => {
      const weekNum = Number(route.query.week);
      if (!weekNum || weekNum < 1 || weekNum > weeks.value.length) {
        phase.value = 'week';
        return;
      }
      selectedWeekIndex.value = weekNum - 1;
      const variant = String(route.query.variant || '');
      if (variant && weeks.value[weekNum - 1].notebooks[variant]) {
        weeks.value[weekNum - 1].selectedVariant = variant;
        const stepParam = String(route.query.step || '') || null;
        const tabParam = String(route.query.tab || '').toLowerCase();
        initialStep.value = stepParam || TAB_TO_STEP[tabParam] || null;
        phase.value = 'tour';
      } else {
        // Alte Links (z.B. ?week=N&tab=lektion, nie mit variant) landen hier auf der
        // Themen-Wahl-Seite - nach der Themenwahl startet die Tour ohnehin auf Lektion.
        phase.value = 'variant';
      }
    };

    // ── "Inseln"-Pfad zwischen den Wochen-Kacheln ────────────────────────────
    // Echte Schlangen-Anordnung (Zeile 2 läuft rückwärts usw.), damit der Pfad von einer Woche
    // zur nächsten immer ein kurzer Nachbar-Sprung ist statt einer langen Diagonale quer durchs
    // Raster. Die Spaltenzahl kommt direkt aus dem tatsächlich gerenderten CSS-Grid (auto-fill),
    // damit das bei jeder Fensterbreite korrekt bleibt, ohne die Spaltenzahl hart zu codieren.
    const weekMapRef = ref(null);
    const tileRefs = ref([]);
    const pathD = ref('');
    const mapViewBox = ref('0 0 0 0');
    const cols = ref(1);
    let resizeObserver = null;

    const setTileRef = (el, index) => {
      if (el) tileRefs.value[index] = el;
    };

    const tileGridStyle = (index) => {
      const c = cols.value || 1;
      const row = Math.floor(index / c);
      const colInRow = index % c;
      const displayCol = row % 2 === 0 ? colInRow : c - 1 - colInRow;
      return { gridColumn: String(displayCol + 1), gridRow: String(row + 1) };
    };

    const computeCols = () => {
      const grid = weekMapRef.value?.querySelector('.week-tile-grid');
      if (!grid) return;
      const n = getComputedStyle(grid).gridTemplateColumns.split(' ').filter(Boolean).length;
      if (n > 0 && n !== cols.value) cols.value = n;
    };

    const updatePath = () => {
      const container = weekMapRef.value;
      if (!container || !weeks.value.length) return;
      const containerRect = container.getBoundingClientRect();
      const points = weeks.value
        .map((_, i) => {
          const el = tileRefs.value[i];
          if (!el) return null;
          return {
            x: el.getBoundingClientRect().left + el.offsetWidth / 2 - containerRect.left,
            y: el.getBoundingClientRect().top + el.offsetHeight / 2 - containerRect.top,
          };
        })
        .filter(Boolean);
      pathD.value = smoothPathD(points);
      mapViewBox.value = `0 0 ${containerRect.width} ${containerRect.height}`;
    };

    const observeMap = () => {
      if (resizeObserver) resizeObserver.disconnect();
      if (!weekMapRef.value) return;
      resizeObserver = new ResizeObserver(() => {
        computeCols();
        nextTick(updatePath);
      });
      resizeObserver.observe(weekMapRef.value);
      computeCols();
      nextTick(updatePath);
    };

    watch(phase, (p) => {
      if (p === 'week') nextTick(observeMap);
    });

    onUnmounted(() => {
      if (resizeObserver) resizeObserver.disconnect();
    });

    const load = async () => {
      loading.value = true;
      weeks.value = await loadWeeklyContent(lang.value);
      applyDeepLink();
      loading.value = false;
      if (phase.value === 'week') nextTick(observeMap);
    };

    onMounted(load);
    watch(lang, load);

    return {
      t, lang, weeks, loading, phase, selectedWeekIndex, selectedWeek, availableVariants, initialStep,
      selectedVariantLabel, hasNextWeek, lessonContentPath, weekTheme, weekIcon, selectWeek, selectVariant,
      goToNextWeek, courseId: COURSE_ID, isCertificateEarned, countCertificates,
      weekMapRef, setTileRef, tileGridStyle, pathD, mapViewBox,
    };
  },
};
</script>

<style scoped>
.week-tour {
  padding: 20px;
}

.tour-page {
  animation: tour-page-in 0.18s ease;
}

@keyframes tour-page-in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.tour-intro {
  color: #555;
  margin-bottom: 24px;
}

.tour-loading {
  color: #9ca3af;
  font-style: italic;
}

.section-label {
  font-size: 1.3em;
  color: var(--primary-purple, #4a2274);
  margin: 0 0 10px;
  border-bottom: none;
}

.week-picker-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 14px;
}

.week-picker-header .section-label { margin: 0; }

.certificates-link {
  background: #fef9e7;
  border: 1px solid #ffd700;
  border-radius: 8px;
  padding: 7px 14px;
  font-size: 0.85em;
  font-weight: 600;
  color: #7c3aed;
  cursor: pointer;
}
.certificates-link:hover { background: #fdebd0; }

.breadcrumb-back {
  background: transparent;
  border: none;
  color: #7c5a94;
  font-size: 0.9em;
  cursor: pointer;
  padding: 0 0 14px;
}
.breadcrumb-back:hover { color: var(--primary-purple, #4a2274); text-decoration: underline; }

/* ── Wochen-Karte: Kacheln + verbindender Pfad ("Inseln") ───────────────── */
.week-map {
  position: relative;
}

.week-map-path {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.week-map-path path {
  fill: none;
  stroke: #d9c7ea;
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 2 12;
}

.tile-grid {
  display: grid;
  gap: 14px;
  position: relative;
  z-index: 1;
}

.week-tile-grid {
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
}

.variant-tile-grid {
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  max-width: 760px;
}

.tile {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 20px 18px;
  cursor: pointer;
  transition: all 0.15s ease;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.tile:hover {
  border-color: #d9c7ea;
  background: #f7f1fb;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(74, 34, 116, 0.12);
}

.tile.active {
  border-color: var(--primary-purple, #4a2274);
  background: #efe3f6;
}

.week-tile-icon {
  position: relative;
  display: inline-block;
  font-size: 1.6em;
  width: 1.3em;
}

.week-tile-badge {
  position: absolute;
  top: -8px;
  right: -10px;
  font-size: 0.55em;
}

.week-tile strong {
  font-size: 1.05em;
  color: var(--primary-purple, #4a2274);
}

.week-tile span:not(.week-tile-badge) {
  font-size: 0.85em;
  color: #6b7280;
}

.variant-tile {
  align-items: center;
  text-align: center;
  font-size: 1.15em;
  font-weight: 600;
  color: #374151;
  padding: 26px 18px;
}

.week-zip-download {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 18px 0 4px;
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
