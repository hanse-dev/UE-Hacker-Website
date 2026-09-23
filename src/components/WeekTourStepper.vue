<template>
  <div class="tour-stepper">
    <div class="tour-header">
      <div class="tour-breadcrumb">
        <button class="breadcrumb-link" @click="$emit('change-week')">{{ t('week.label') }} {{ weekNumber }}: {{ weekTheme }}</button>
        <span class="breadcrumb-sep">›</span>
        <button class="breadcrumb-link" @click="$emit('change-variant')">{{ variantLabel }}</button>
      </div>
      <button class="side-menu-toggle" @click="sideMenuOpen = !sideMenuOpen">
        {{ sideMenuOpen ? '✕ ' + t('tour.sideMenu.hide') : '☰ ' + t('tour.sideMenu.show') }}
      </button>
    </div>

    <!-- Im Lektions-Format ersetzt die Leiste der eingebetteten Tour (inkl. Check-Punkt) diese hier -->
    <div v-if="!lessonContentPath" class="progress-stepper">
      <template v-for="(step, i) in steps" :key="step.key">
        <button
          class="stepper-step"
          :class="{ done: !!visitedKeys[step.key], current: !activeReference && !choosingNext && viewingStepKey === step.key }"
          :data-step-key="step.key"
          @click="viewStep(step.key)"
        >
          <span class="stepper-dot">{{ visitedKeys[step.key] ? '✓' : i + 1 }}</span>
          <span class="stepper-label">{{ step.label }}</span>
        </button>
        <span v-if="i < steps.length - 1" class="stepper-line" :class="{ done: !!visitedKeys[step.key] }"></span>
      </template>
    </div>

    <div class="tour-body">
      <div class="tour-content">
        <div v-if="activeReference" class="tour-reference-banner">
          <span>{{ referenceLabel }}</span>
          <button class="tour-back-btn" @click="activeReference = null">{{ t('tour.backToTour') }}</button>
        </div>

        <div v-if="activeCheatSheet" class="cheat-sheet-reference">
          <div class="cheat-sheet-actions">
            <a :href="activeCheatSheet.url" download class="download-btn">
              <span class="download-icon">📥</span>{{ t('week.download.md') }}
            </a>
            <a v-if="activeCheatSheet.notebookUrl" :href="activeCheatSheet.notebookUrl" download class="download-btn">
              <span class="download-icon">📓</span>{{ t('week.download.nb') }}
            </a>
          </div>
          <div class="cheat-sheet-markdown" v-html="activeCheatSheet.content"></div>
        </div>
        <div v-else-if="!activeReference && choosingNext" class="branch-choice-page">
          <h3>{{ t('tour.branch.title') }}</h3>
          <p>{{ t('tour.branch.intro') }}</p>
          <div class="branch-tile-grid">
            <button class="tile branch-tile" data-branch="5_boss" @click="chooseBranch('5_boss')">
              <span class="branch-tile-icon">🔥</span>
              <strong>{{ t('tour.deepen') }}</strong>
              <span class="branch-tile-desc">{{ t('tour.branch.deepenDesc') }}</span>
            </button>
            <button class="tile branch-tile" data-branch="4_check" @click="chooseBranch('4_check')">
              <span class="branch-tile-icon">✅</span>
              <strong>{{ t('tab.check') }}</strong>
              <span class="branch-tile-desc">{{ t('tour.branch.checkDesc') }}</span>
            </button>
          </div>
        </div>
        <WeekCheckPanel
          v-else-if="!activeReference && viewingStepKey === '4_check'"
          :week-number="weekNumber"
        />
        <LessonTour
          v-else-if="!activeReference && lessonContentPath && viewingStepKey === 'lessons'"
          :course-id="courseId"
          :content-path="lessonContentPath"
          engine="pyodide"
          embedded
          free-navigation
          :has-check="hasCheck"
          @open-check="viewStep('4_check')"
          :key="`lessons-${lessonContentPath}`"
        />
        <JupyterNotebook
          v-else-if="activeContentUrl"
          :notebook-path="activeContentUrl"
          :notebook-url="activeContentDownloadUrl"
          :download-name="activeContentDownloadName"
          :week-number="weekNumber"
          :variant="variant"
          :course-id="courseId"
          :key="`${weekNumber}-${variant}-${activeContentKey}`"
        />

        <!-- Im Lektions-Format (Schritt "lessons") navigiert die eingebetteten Tour sich selbst
             und meldet "open-check" erst, wenn die Lektionen wirklich durch sind - hier keinen
             zusätzlichen "Weiter zu Check"-Sprung anbieten, der die Lektionen überspringen würde. -->
        <div
          v-if="!activeReference && !choosingNext && !(lessonContentPath && viewingStepKey === 'lessons')"
          class="tour-tail"
        >
          <button
            v-if="viewingStepKey !== '4_check' && nextStep"
            class="tour-next-btn"
            @click="goNext"
          >{{ nextButtonLabel }} →</button>

          <template v-else-if="viewingStepKey === '4_check'">
            <div v-if="checkPassed" class="certificate-reveal">
              <div class="certificate-badge">🎓</div>
              <h3>{{ t('tour.certificate.title') }}</h3>
              <p>{{ t('tour.certificate.earned').replace('{week}', `${t('week.label')} ${weekNumber}: ${weekTheme}`) }}</p>

              <div v-if="isLoggedIn" class="certificate-name-row">
                <label :for="`cert-name-${weekNumber}`">{{ t('progress.certificate.name.label') }}</label>
                <input
                  :id="`cert-name-${weekNumber}`"
                  type="text"
                  :value="certificateName"
                  @input="setCertificateName($event.target.value)"
                />
              </div>
              <button v-if="isLoggedIn" class="btn-certificate-pdf" :disabled="pdfBusy" @click="onDownloadPdf">
                {{ pdfBusy ? t('progress.certificate.generating') : t('progress.certificate.download') }}
              </button>
              <p v-else class="certificate-login-hint">{{ t('progress.certificate.loginRequired') }}</p>
            </div>
            <p v-else class="tour-check-pending">{{ t('tour.certificate.pending') }}</p>

            <!-- Weiter geht's auch ohne bestandenen Check - niemand soll hier feststecken. -->
            <div class="after-check-choice">
              <button class="tile after-check-tile" data-after-check="overview" @click="$emit('change-week')">
                {{ t('tour.afterCheck.overview') }}
              </button>
              <button
                v-if="hasNextWeek"
                class="tile after-check-tile"
                data-after-check="next-week"
                @click="$emit('go-next-week')"
              >{{ t('tour.afterCheck.nextWeek') }}</button>
            </div>
          </template>

          <p v-else class="tour-done-msg">{{ t('tour.done') }}</p>
        </div>
      </div>

      <WeekTourSideMenu
        v-if="sideMenuOpen"
        :steps="steps"
        :current-step-key="!choosingNext ? viewingStepKey : null"
        :visited-keys="visitedKeys"
        :headings="headings"
        :reference-items="referenceItems"
        :week-zip-url="`/wochen-zips/woche-${weekNumber}${lang === 'en' ? '-en' : ''}.zip`"
        :active-reference="activeReference"
        @select-step="viewStep"
        @select-heading="scrollToCell"
        @select-reference="viewReference"
      />
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue';
import JupyterNotebook from './JupyterNotebook.vue';
import LessonTour from './JsCourseTour.vue';
import WeekCheckPanel from './WeekCheckPanel.vue';
import WeekTourSideMenu from './WeekTourSideMenu.vue';
import { useLanguage } from '../composables/useLanguage.js';
import { useAuth } from '../composables/useAuth.js';
import { useNotebookHeadings } from '../composables/useNotebookHeadings.js';
import { loadWeekChecks, hasWeekCheck, useWeekChecks } from '../composables/useWeekChecks.js';
import { downloadCertificatePdf } from '../composables/useCertificatePdf.js';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

const TOUR_STEPS_CONFIG = [
  { key: '1_lektion',   icon: '📚', labelKey: 'tab.lesson' },
  { key: '2_debug',     icon: '🐛', labelKey: 'tab.debug' },
  { key: '3_missionen', icon: '⭐', labelKey: 'tab.missions' },
  { key: '5_boss',      icon: '🔥', labelKey: 'tour.deepen' },
  { key: '4_check',     icon: '✅', labelKey: 'tab.check' },
];

const REFERENCE_CONFIG = [
  { key: '0_glossar',   icon: '📖', labelKey: 'tab.glossary' },
  { key: '6_loesungen', icon: '🔧', labelKey: 'tab.solutions' },
];

export default {
  name: 'WeekTourStepper',
  components: { JupyterNotebook, LessonTour, WeekCheckPanel, WeekTourSideMenu },
  props: {
    week: { type: Object, required: true },
    weekNumber: { type: Number, required: true },
    weekTheme: { type: String, default: '' },
    variant: { type: String, required: true },
    variantLabel: { type: String, default: '' },
    courseId: { type: String, required: true },
    initialStep: { type: String, default: null },
    hasNextWeek: { type: Boolean, default: false },
    // Optional: Inhaltsordner im Lektions-Format (lessons.json). Ersetzt dann die Notebook-Schritte
    // Lektion/Debug/Missionen/Extra-Herausforderung durch EINE Lektions-Tour (siehe JsCourseTour.vue).
    lessonContentPath: { type: String, default: null },
  },
  emits: ['change-week', 'change-variant', 'go-next-week'],
  setup(props) {
    const { t, lang } = useLanguage();
    const { isLoggedIn, user } = useAuth();
    const checksData = ref(null);
    const hasCheck = computed(() => hasWeekCheck(checksData.value, props.weekNumber));
    const sideMenuOpen = ref(true);
    const { isWeekCheckPassed } = useWeekChecks();

    const notebooksForVariant = computed(() => props.week.notebooks?.[props.variant] ?? {});

    const steps = computed(() => props.lessonContentPath
      ? [
          { key: 'lessons', icon: '📚', label: t('tour.lessons') },
          ...(hasCheck.value ? [{ ...TOUR_STEPS_CONFIG.find((s) => s.key === '4_check'), label: t('tab.check') }] : []),
        ]
      : TOUR_STEPS_CONFIG
        .filter((step) => step.key === '4_check' ? hasCheck.value : !!notebooksForVariant.value[step.key]?.renderUrl)
        .map((step) => ({ ...step, label: t(step.labelKey) }))
    );

    const referenceItems = computed(() => {
      const notebookRefs = REFERENCE_CONFIG
        .filter((ref_) => !!notebooksForVariant.value[ref_.key]?.renderUrl)
        .map((ref_) => ({ ...ref_, label: t(ref_.labelKey) }));
      // Cheat-Sheets sind kein Notebook (fertig gerendertes Markdown-HTML aus
      // useWeeklyContent.js) - eigene Referenz-Einträge, Name kommt bereits mit Emoji-Präfix
      // ("📚 Wissens-Cheat-Sheet"), hier nur in icon/label getrennt fürs Seitenmenü.
      const cheatSheetRefs = (props.week.cheatSheets || []).map((cs, i) => {
        const [icon, ...rest] = cs.name.split(' ');
        return { key: `cheat-${i}`, icon, label: rest.join(' ') || cs.name };
      });
      return [...notebookRefs, ...cheatSheetRefs];
    });

    const viewingStepKey = ref(null);
    const visitedKeys = ref({});
    const activeReference = ref(null);
    const choosingNext = ref(false);
    let usedInitialStep = false;

    const resetForWeekVariant = () => {
      activeReference.value = null;
      choosingNext.value = false;
      const initialIdx = !usedInitialStep && props.initialStep
        ? steps.value.findIndex((s) => s.key === props.initialStep)
        : -1;
      usedInitialStep = true;
      if (initialIdx >= 0) {
        viewingStepKey.value = props.initialStep;
        const visited = {};
        steps.value.slice(0, initialIdx + 1).forEach((s) => { visited[s.key] = true; });
        visitedKeys.value = visited;
      } else {
        viewingStepKey.value = steps.value[0]?.key ?? null;
        visitedKeys.value = viewingStepKey.value ? { [viewingStepKey.value]: true } : {};
      }
    };

    const load = async () => {
      try { checksData.value = await loadWeekChecks(); } catch { checksData.value = null; }
    };

    watch(() => [props.weekNumber, props.variant], resetForWeekVariant);
    watch(steps, () => {
      if (!viewingStepKey.value && steps.value.length) viewingStepKey.value = steps.value[0].key;
    });

    load().then(resetForWeekVariant);

    const viewStep = (key) => {
      activeReference.value = null;
      choosingNext.value = false;
      viewingStepKey.value = key;
      visitedKeys.value = { ...visitedKeys.value, [key]: true };
    };

    const viewReference = (key) => {
      activeReference.value = activeReference.value === key ? null : key;
    };

    const currentStepIndex = computed(() => steps.value.findIndex((s) => s.key === viewingStepKey.value));
    const nextStep = computed(() => steps.value[currentStepIndex.value + 1] ?? null);

    /**
     * Nach den Missionen wird nicht automatisch weitergeschaltet, sondern eine Wahl zwischen
     * Extra-Herausforderung (optional) und Check angeboten - beide führen letztlich zum Check.
     */
    const goNext = () => {
      if (viewingStepKey.value === '3_missionen') {
        const hasBoss = steps.value.some((s) => s.key === '5_boss');
        const hasCheckStep = steps.value.some((s) => s.key === '4_check');
        if (hasBoss && hasCheckStep) { choosingNext.value = true; return; }
        if (hasBoss) { viewStep('5_boss'); return; }
        if (hasCheckStep) { viewStep('4_check'); return; }
        return;
      }
      if (nextStep.value) viewStep(nextStep.value.key);
    };

    const chooseBranch = (key) => {
      choosingNext.value = false;
      viewStep(key);
    };

    const nextButtonLabel = computed(() => {
      if (viewingStepKey.value === '3_missionen') {
        const hasBoss = steps.value.some((s) => s.key === '5_boss');
        const hasCheckStep = steps.value.some((s) => s.key === '4_check');
        if (hasBoss && hasCheckStep) return t('tour.nextGeneric');
      }
      return nextStep.value ? t('tour.next').replace('{step}', nextStep.value.label) : '';
    });

    const activeCheatSheet = computed(() => {
      if (!activeReference.value?.startsWith('cheat-')) return null;
      const idx = Number(activeReference.value.slice(6));
      return props.week.cheatSheets?.[idx] ?? null;
    });

    const activeContentKey = computed(() => activeReference.value ?? viewingStepKey.value);
    const activeContentUrl = computed(() => {
      if (choosingNext.value && !activeReference.value) return null;
      if (activeContentKey.value === '4_check') return null;
      return notebooksForVariant.value[activeContentKey.value]?.renderUrl ?? null;
    });
    const activeContentDownloadUrl = computed(() => notebooksForVariant.value[activeContentKey.value]?.downloadUrl ?? null);
    const activeContentDownloadName = computed(() => notebooksForVariant.value[activeContentKey.value]?.downloadName ?? null);

    const { headings } = useNotebookHeadings(activeContentUrl);

    const scrollToCell = (cellIndex) => {
      const el = document.getElementById(`cell-${cellIndex}`);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const referenceLabel = computed(() => {
      const item = referenceItems.value.find((r) => r.key === activeReference.value);
      return item ? `${item.icon} ${item.label}` : '';
    });

    // ── Zertifikat-Reveal nach bestandenem Check ─────────────────────────────
    const checkPassed = computed(() => isWeekCheckPassed(props.weekNumber));
    const certificateName = ref(localStorage.getItem(CERTIFICATE_NAME_KEY) || user.value?.username || '');
    const setCertificateName = (value) => {
      certificateName.value = value;
      localStorage.setItem(CERTIFICATE_NAME_KEY, value);
    };
    const pdfBusy = ref(false);
    const onDownloadPdf = async () => {
      pdfBusy.value = true;
      try {
        await downloadCertificatePdf({
          weekNumber: props.weekNumber,
          weekTitle: props.week.title || `${t('week.label')} ${props.weekNumber}`,
          lernziele: props.week.lernzieleFull || [],
          learnerName: certificateName.value || user.value?.username || '',
          lang: lang.value,
        });
      } finally {
        pdfBusy.value = false;
      }
    };

    return {
      t, lang, steps, hasCheck, referenceItems, viewingStepKey, visitedKeys, activeReference, choosingNext, sideMenuOpen,
      viewStep, viewReference, chooseBranch, nextStep, nextButtonLabel, goNext,
      activeContentKey, activeContentUrl, activeContentDownloadUrl, activeContentDownloadName,
      activeCheatSheet, headings, scrollToCell, referenceLabel,
      checkPassed, isLoggedIn, certificateName, setCertificateName, pdfBusy, onDownloadPdf,
    };
  },
};
</script>

<style scoped>
.tour-stepper {
  margin-top: 8px;
}

.tour-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.tour-breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.92em;
}

.breadcrumb-link {
  background: transparent;
  border: none;
  color: #7c5a94;
  font-weight: 600;
  cursor: pointer;
  padding: 2px 4px;
}
.breadcrumb-link:hover { color: var(--primary-purple, #4a2274); text-decoration: underline; }
.breadcrumb-sep { color: #c4b5d0; }

.side-menu-toggle {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  padding: 6px 12px;
  font-size: 0.82em;
  cursor: pointer;
  color: #555;
  white-space: nowrap;
}
.side-menu-toggle:hover { background: #efe3f6; border-color: #d9c7ea; }

/* ── Fortschritts-Leiste (Kullern + Linien) ─────────────────────────────── */
.progress-stepper {
  display: flex;
  align-items: flex-start;
  margin: 18px 0 8px;
  overflow-x: auto;
  scrollbar-width: none;
}
.progress-stepper::-webkit-scrollbar { display: none; }

.stepper-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0 4px;
  min-width: 64px;
}

.stepper-dot {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #d1d5db;
  background: white;
  color: #9ca3af;
  font-weight: 700;
  font-size: 0.9em;
  transition: all 0.15s ease;
}

.stepper-step.done .stepper-dot {
  background: var(--primary-purple, #4a2274);
  border-color: var(--primary-purple, #4a2274);
  color: white;
}

.stepper-step.current .stepper-dot {
  background: var(--accent-orange, #ff9800);
  border-color: var(--accent-orange, #ff9800);
  color: white;
  box-shadow: 0 0 0 4px #fff3e0;
}

.stepper-label {
  font-size: 0.78em;
  color: #6b7280;
  text-align: center;
  white-space: nowrap;
}

.stepper-step.done .stepper-label { color: var(--primary-purple, #4a2274); }
.stepper-step.current .stepper-label { color: var(--accent-orange, #ff9800); font-weight: 700; }

.stepper-line {
  flex: 1;
  height: 3px;
  background: #e5e7eb;
  margin-top: 17px;
  min-width: 20px;
}
.stepper-line.done { background: var(--primary-purple, #4a2274); }

/* ── Inhalt ──────────────────────────────────────────────────────────────── */
.tour-body {
  display: flex;
  gap: 24px;
  margin-top: 16px;
  align-items: flex-start;
}

.tour-content {
  flex: 1;
  min-width: 0;
}

.tour-reference-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  background: #f3eef8;
  border: 1px solid #c4a8e0;
  border-radius: 8px 8px 0 0;
  padding: 10px 16px;
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.tour-back-btn {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85em;
  font-weight: 600;
}
.tour-back-btn:hover { background: #3d1b5c; }

/* ── Cheat-Sheet-Referenz ────────────────────────────────────────────────── */
.cheat-sheet-reference {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 20px;
}

.cheat-sheet-actions { margin-bottom: 16px; text-align: center; }

.download-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 4px 8px;
  padding: 10px 20px;
  background: #28a745;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: bold;
  transition: all 0.2s ease;
}
.download-btn:hover { background: #218838; transform: translateY(-2px); }
.download-icon { font-size: 1.1em; }

.cheat-sheet-markdown { font-size: 0.95em; line-height: 1.6; }

.cheat-sheet-markdown :deep(h1) {
  color: #28a745; border-bottom: 2px solid #28a745; padding-bottom: 10px; margin-top: 0;
}
.cheat-sheet-markdown :deep(h2) { color: #333; border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 2em; }
.cheat-sheet-markdown :deep(h3) { color: #555; margin-top: 1.5em; }
.cheat-sheet-markdown :deep(code) {
  background: #f8f9fa; padding: 2px 6px; border-radius: 3px;
  font-family: 'Courier New', monospace; font-size: 0.9em; border: 1px solid #e9ecef;
}
.cheat-sheet-markdown :deep(pre) {
  background: #f8f9fa; padding: 15px; border-radius: 6px; overflow-x: auto; border: 1px solid #e9ecef;
}
.cheat-sheet-markdown :deep(pre code) { background: none; padding: 0; border: none; }
.cheat-sheet-markdown :deep(ul), .cheat-sheet-markdown :deep(ol) { padding-left: 25px; }
.cheat-sheet-markdown :deep(li) { margin-bottom: 5px; }
.cheat-sheet-markdown :deep(table) { width: 100%; border-collapse: collapse; margin: 20px 0; }
.cheat-sheet-markdown :deep(th), .cheat-sheet-markdown :deep(td) {
  border: 1px solid #ddd; padding: 8px 12px; text-align: left;
}
.cheat-sheet-markdown :deep(th) { background: #f8f9fa; font-weight: bold; }
.cheat-sheet-markdown :deep(blockquote) {
  border-left: 4px solid #28a745; padding-left: 20px; margin-left: 0; color: #666; font-style: italic;
}

/* ── Verzweigung: Extra-Herausforderung oder Check ──────────────────────── */
.branch-choice-page {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 24px 20px;
}

.branch-choice-page h3 {
  margin: 0 0 6px;
  color: var(--primary-purple, #4a2274);
}

.branch-choice-page > p {
  margin: 0 0 18px;
  color: #555;
}

.branch-tile-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
  max-width: 640px;
}

.tile {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 18px 16px;
  cursor: pointer;
  transition: all 0.15s ease;
}
.tile:hover { border-color: #d9c7ea; background: #f7f1fb; transform: translateY(-2px); }

.branch-tile-icon { font-size: 1.6em; }
.branch-tile strong { color: var(--primary-purple, #4a2274); font-size: 1.05em; }
.branch-tile-desc { font-size: 0.82em; color: #6b7280; }

/* ── Ergebnis-Bereich (Weiter / Zertifikat) ─────────────────────────────── */
.tour-tail {
  padding: 18px 4px 4px;
}

.tour-next-btn {
  background: var(--accent-orange, #ff9800);
  color: white;
  border: none;
  padding: 12px 22px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1em;
  font-weight: 700;
}
.tour-next-btn:hover { background: #fb8c00; }

.tour-done-msg,
.tour-check-pending {
  background: #fff3cd;
  border: 1px solid #ffe69c;
  border-radius: 8px;
  padding: 14px 18px;
  font-weight: 600;
  color: #664d03;
}

/* ── Zertifikat-Reveal ───────────────────────────────────────────────────── */
.certificate-reveal {
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
  border: 2px solid #ffd700;
  border-radius: 12px;
  padding: 28px 24px;
  text-align: center;
  animation: certificate-pop 0.3s ease;
}

@keyframes certificate-pop {
  from { opacity: 0; transform: scale(0.92); }
  to { opacity: 1; transform: scale(1); }
}

.certificate-badge {
  font-size: 3em;
  line-height: 1;
  margin-bottom: 6px;
}

.certificate-reveal h3 {
  margin: 0 0 6px;
  color: #7c3aed;
}

.certificate-reveal > p {
  margin: 0 0 16px;
  color: #444;
}

.certificate-name-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 12px;
}

.certificate-name-row label {
  font-size: 0.85em;
  color: #555;
  font-weight: 600;
}

.certificate-name-row input {
  padding: 7px 10px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 0.9em;
  min-width: 200px;
}

.btn-certificate-pdf {
  background: #7c3aed;
  color: white;
  border: none;
  padding: 9px 18px;
  border-radius: 8px;
  font-size: 0.9em;
  font-weight: 600;
  cursor: pointer;
}
.btn-certificate-pdf:hover:not(:disabled) { background: #6d28d9; }
.btn-certificate-pdf:disabled { opacity: 0.6; cursor: default; }

.certificate-login-hint {
  font-size: 0.82em;
  color: #888;
  font-style: italic;
  margin: 0;
}

.after-check-choice {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 22px;
}

.after-check-tile {
  align-items: center;
  text-align: center;
  font-weight: 700;
  color: var(--primary-purple, #4a2274);
  min-width: 180px;
  background: white;
}

@media (max-width: 900px) {
  .tour-body { flex-direction: column; }
}
</style>
