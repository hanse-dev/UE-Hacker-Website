<template>
  <div class="ki-labor-tour">
    <template v-if="phase === 'week'">
      <p class="choose-week-title">{{ t('weekPicker.chooseWeekTitle') }}</p>
      <div class="week-grid">
        <button
          v-for="week in weeks"
          :key="week.number"
          class="week-tile"
          :class="{ locked: !week.available }"
          :disabled="!week.available"
          @click="selectWeek(week.number)"
        >
          <span class="week-tile-number">{{ t('week.label') }} {{ week.number }}</span>
          <span class="week-tile-title">{{ week.title }}</span>
          <span v-if="!week.available" class="week-tile-badge">{{ t('weekPicker.comingSoon') }}</span>
        </button>
      </div>
    </template>

    <JsCourseTour
      v-else-if="phase === 'tour'"
      engine="pyodide"
      :course-id="`ki-labor-woche${selectedWeekNumber}`"
      :content-path="`ki-labor-woche${selectedWeekNumber}`"
      :week-label="`${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`"
      :has-check="selectedWeekHasCheck"
      @change-week="phase = 'week'"
      @open-check="phase = 'check'"
    />

    <div v-else class="ki-labor-check">
      <div class="tour-breadcrumb">
        <button class="breadcrumb-back" @click="phase = 'tour'">{{ t('tour.backToTour') }}</button>
        <span class="breadcrumb-week">{{ t('week.label') }} {{ selectedWeekNumber }}: {{ selectedWeekTitle }}</span>
      </div>

      <WeekCheckPanel :week-number="selectedWeekNumber" course-key="ki-labor" />

      <div v-if="checkPassed" class="certificate-reveal">
        <div class="certificate-badge">🎓</div>
        <h3>{{ t('tour.certificate.title') }}</h3>
        <p>{{ t('tour.certificate.earned').replace('{week}', `${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`) }}</p>

        <div v-if="isLoggedIn" class="certificate-name-row">
          <label :for="`ki-labor-cert-name-${selectedWeekNumber}`">{{ t('progress.certificate.name.label') }}</label>
          <input
            :id="`ki-labor-cert-name-${selectedWeekNumber}`"
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

      <div class="after-check-choice">
        <button class="tile after-check-tile" @click="phase = 'week'">{{ t('tour.afterCheck.overview') }}</button>
        <button v-if="nextWeekAvailable" class="tile after-check-tile" @click="selectWeek(selectedWeekNumber + 1)">
          {{ t('tour.afterCheck.nextWeek') }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import JsCourseTour from './JsCourseTour.vue';
import WeekCheckPanel from './WeekCheckPanel.vue';
import { useLanguage } from '../composables/useLanguage';
import { useAuth } from '../composables/useAuth';
import { useWeekChecks } from '../composables/useWeekChecks';
import { downloadCertificatePdf } from '../composables/useCertificatePdf';
import { KI_LABOR_WEEKS as WEEK_DEFS, KI_LABOR_COURSE_TITLE as COURSE_TITLE } from '../data/kiLaborWeeks.js';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

// engine="pyodide" statt js-sandbox - gleiche Tour (JsCourseTour.vue), andere Ausfuehrung
// (LessonView.vue statt JsLessonView.vue). WEEK_DEFS/COURSE_TITLE in ../data/kiLaborWeeks.js,
// weil auch useCourseCertificates.js (Zertifikate im Profil) die Lernziele fürs PDF braucht.

// Gleiches Glob-Pattern wie in JsCourseTour.vue - hier nur zum Pruefen, welche Wochen ueberhaupt
// einen Content-Ordner haben (Verfuegbarkeit), nicht zum Laden der Lektionen selbst.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');
const weekCheckModules = import.meta.glob('../../content/ki-labor-checks/week-*.json');

export default {
  name: 'KiLaborTour',
  components: { JsCourseTour, WeekCheckPanel },
  setup() {
    const { t, lang } = useLanguage();
    const { isLoggedIn, user } = useAuth();
    const { isWeekCheckPassed } = useWeekChecks('ki-labor');
    const route = useRoute();
    const router = useRouter();
    const phase = ref('week');
    const selectedWeekNumber = ref(null);

    const weeks = computed(() =>
      WEEK_DEFS.map((w) => ({
        ...w,
        available: `../../content/ki-labor-woche${w.number}/lessons.json` in lessonJsonModules,
      }))
    );

    const selectedWeek = computed(() => WEEK_DEFS.find((w) => w.number === selectedWeekNumber.value));
    const selectedWeekTitle = computed(() => selectedWeek.value?.title || '');
    const selectedWeekHasCheck = computed(
      () => `../../content/ki-labor-checks/week-${selectedWeekNumber.value}.json` in weekCheckModules
    );
    const nextWeekAvailable = computed(() =>
      weeks.value.some((w) => w.number === selectedWeekNumber.value + 1 && w.available)
    );

    const selectWeek = (number) => {
      const week = weeks.value.find((w) => w.number === number);
      if (!week?.available) return;
      selectedWeekNumber.value = number;
      phase.value = 'tour';
      router.replace({ query: { week: number } });
    };

    onMounted(() => {
      const weekNum = Number(route.query.week);
      if (weekNum && weeks.value.some((w) => w.number === weekNum && w.available)) {
        selectedWeekNumber.value = weekNum;
        phase.value = 'tour';
      }
    });

    // ── Zertifikat-Reveal nach bestandenem Check (siehe WeekTourStepper.vue, hier ohne
    //    Notebook/Themen-Varianten-Komplexität) ──────────────────────────────────────────────
    const checkPassed = computed(() => isWeekCheckPassed(selectedWeekNumber.value));
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
          weekNumber: selectedWeekNumber.value,
          weekTitle: selectedWeekTitle.value,
          lernziele: selectedWeek.value?.lernziele || [],
          learnerName: certificateName.value || user.value?.username || '',
          lang: lang.value,
          courseTitle: COURSE_TITLE,
        });
      } finally {
        pdfBusy.value = false;
      }
    };

    return {
      t,
      phase,
      weeks,
      selectedWeekNumber,
      selectedWeekTitle,
      selectedWeekHasCheck,
      nextWeekAvailable,
      selectWeek,
      isLoggedIn,
      checkPassed,
      certificateName,
      setCertificateName,
      pdfBusy,
      onDownloadPdf,
    };
  },
};
</script>

<style scoped>
.ki-labor-tour {
  max-width: 1200px;
  margin: 0 auto;
}

.choose-week-title {
  text-align: center;
  margin-bottom: 24px;
  color: #555;
}

.week-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px;
  max-width: 900px;
  margin: 0 auto;
}

.week-tile {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: 16px 10px;
  background: white;
  border: 2px solid var(--primary-purple, #4a2274);
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
}

.week-tile:hover:not(:disabled) {
  background: #f7f1fb;
}

.week-tile.locked {
  border-color: #dee2e6;
  cursor: not-allowed;
  opacity: 0.7;
}

.week-tile-number {
  font-size: 0.8em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: var(--accent-orange, #ff9800);
}

.week-tile.locked .week-tile-number {
  color: #adb5bd;
}

.week-tile-title {
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.week-tile.locked .week-tile-title {
  color: #868e96;
}

.week-tile-badge {
  font-size: 0.75em;
  color: #868e96;
}

.ki-labor-check {
  max-width: 900px;
  margin: 0 auto;
}

.tour-breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.92em;
  color: #7c5a94;
  font-weight: 600;
  margin-bottom: 12px;
}

.breadcrumb-back {
  background: none;
  border: none;
  padding: 0;
  font: inherit;
  font-weight: 600;
  color: #7c5a94;
  cursor: pointer;
  text-decoration: underline;
}

.breadcrumb-back:hover {
  color: var(--primary-purple, #4a2274);
}

.breadcrumb-week {
  color: var(--primary-purple, #4a2274);
}

.certificate-reveal {
  margin-top: 20px;
  padding: 24px;
  background: #fff9e6;
  border: 2px solid #ffe69c;
  border-radius: 12px;
  text-align: center;
}

.certificate-badge {
  font-size: 2.5em;
}

.certificate-reveal h3 {
  margin: 8px 0 4px;
  color: var(--primary-purple, #4a2274);
}

.certificate-name-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  margin: 14px 0;
}

.certificate-name-row input {
  padding: 8px 12px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 1em;
  text-align: center;
}

.btn-certificate-pdf {
  background: var(--primary-purple, #4a2274);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.btn-certificate-pdf:disabled {
  opacity: 0.6;
  cursor: default;
}

.certificate-login-hint {
  color: #6c757d;
  font-size: 0.9em;
}

.tour-check-pending {
  margin-top: 16px;
  color: #6c757d;
  font-style: italic;
}

.after-check-choice {
  display: flex;
  gap: 12px;
  justify-content: center;
  margin-top: 20px;
  flex-wrap: wrap;
}

.after-check-tile {
  background: #fff;
  border: 2px solid #e6dcef;
  border-radius: 10px;
  padding: 10px 18px;
  cursor: pointer;
  font: inherit;
  font-weight: 600;
  color: var(--primary-purple, #4a2274);
}

.after-check-tile:hover {
  border-color: var(--primary-purple, #4a2274);
  background: #f7f1fb;
}
</style>
