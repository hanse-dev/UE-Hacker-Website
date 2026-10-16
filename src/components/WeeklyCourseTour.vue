<template>
  <div class="weekly-course-tour">
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

    <template v-else-if="phase === 'tour'">
      <JsCourseTour
        :engine="engine"
        :web-mode="webMode"
        :show-canvas="webMode"
        :course-id="`${weekPrefix}${selectedWeekNumber}`"
        :content-path="`${weekPrefix}${selectedWeekNumber}`"
        :week-label="`${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`"
        :has-check="selectedWeekHasCheck"
        :concept-language="conceptLanguage"
        :concept-course="conceptCourse"
        :concept-week="conceptCourse ? selectedWeekNumber : 0"
        @change-week="phase = 'week'"
        @open-check="phase = 'check'"
      />
      <OfflineDownloads v-if="downloadsBase" :base="`${downloadsBase}${selectedWeekNumber}`" />
    </template>

    <div v-else class="weekly-course-check">
      <div class="tour-breadcrumb">
        <button class="breadcrumb-back" @click="phase = 'tour'">{{ t('tour.backToTour') }}</button>
        <span class="breadcrumb-week">{{ t('week.label') }} {{ selectedWeekNumber }}: {{ selectedWeekTitle }}</span>
      </div>

      <WeekCheckPanel :week-number="selectedWeekNumber" :course-key="courseKey" :engine="webMode ? 'web' : engine" />

      <div v-if="checkPassed" class="certificate-reveal">
        <div class="certificate-badge">🎓</div>
        <h3>{{ t('tour.certificate.title') }}</h3>
        <p>{{ t('tour.certificate.earned').replace('{week}', `${t('week.label')} ${selectedWeekNumber}: ${selectedWeekTitle}`) }}</p>

        <div v-if="isLoggedIn" class="certificate-name-row">
          <label :for="`${courseKey}-cert-name-${selectedWeekNumber}`">{{ t('progress.certificate.name.label') }}</label>
          <input
            :id="`${courseKey}-cert-name-${selectedWeekNumber}`"
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
import OfflineDownloads from './OfflineDownloads.vue';
import { useLanguage } from '../composables/useLanguage';
import { useAuth } from '../composables/useAuth';
import { useWeekChecks } from '../composables/useWeekChecks';
import { downloadCertificatePdf } from '../composables/useCertificatePdf';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

// Mehrwochen-Kurs mit Wochen-Check und Zertifikat je Woche: Wochenauswahl → Tour (JsCourseTour.vue)
// → Check (WeekCheckPanel.vue) mit Zertifikat-Reveal. Erst fuers KI-Labor gebaut (KiLaborTour.vue ist
// jetzt nur noch ein Wrapper), dann fuer die Stufe „Intensiv“ von „Meine erste Website“
// (WebsiteCourse.vue, engine js-sandbox + webMode). Wochen-Titel/Lernziele kommen als Prop, weil auch
// useCourseCertificates.js (Zertifikate im Profil) sie fuers PDF braucht.

// Gleiches Glob-Pattern wie in JsCourseTour.vue - hier nur zum Pruefen, welche Wochen ueberhaupt
// einen Content-Ordner bzw. einen Check haben (Verfuegbarkeit), nicht zum Laden selbst.
const lessonJsonModules = import.meta.glob('../../content/*/lessons.json');
const weekCheckModules = import.meta.glob('../../content/*-checks/week-*.json');

export default {
  name: 'WeeklyCourseTour',
  components: { JsCourseTour, WeekCheckPanel, OfflineDownloads },
  props: {
    // [{ number, title, lernziele }] - Titel fuer die Kacheln, Lernziele fuers Zertifikat-PDF.
    weeks: { type: Array, required: true },
    // Content-Ordner einer Woche = weekPrefix + Nummer (z.B. 'ki-labor-woche' → ki-labor-woche3).
    weekPrefix: { type: String, required: true },
    // Wochen-Checks in content/<courseKey>-checks/week-N.json, Fortschritt unter diesem Schluessel.
    courseKey: { type: String, required: true },
    // { de, en } - steht auf dem Zertifikat.
    courseTitle: { type: Object, required: true },
    engine: { type: String, default: 'pyodide' },
    // Web-Kurse: HTML/CSS-Sandbox in den Lektionen und Web-Aufgaben im Check.
    webMode: { type: Boolean, default: false },
    conceptLanguage: { type: String, default: '' },
    // Kurs-Schluessel in begriffe.json, wenn der Kurs selbst Link-Ziel ist - dann verlinken
    // Begriffe nur auf fruehere Wochen (useConcepts.js).
    conceptCourse: { type: String, default: '' },
    // Offline-Downloads je Woche (Pfad-Praefix + Nummer); leer = keine.
    downloadsBase: { type: String, default: '' },
  },
  setup(props) {
    const { t, lang } = useLanguage();
    const { isLoggedIn, user } = useAuth();
    const { isWeekCheckPassed } = useWeekChecks(props.courseKey);
    const route = useRoute();
    const router = useRouter();
    const phase = ref('week');
    const selectedWeekNumber = ref(null);

    const weeks = computed(() =>
      props.weeks.map((w) => ({
        ...w,
        available: `../../content/${props.weekPrefix}${w.number}/lessons.json` in lessonJsonModules,
      }))
    );

    const selectedWeek = computed(() => props.weeks.find((w) => w.number === selectedWeekNumber.value));
    const selectedWeekTitle = computed(() => selectedWeek.value?.title || '');
    const selectedWeekHasCheck = computed(
      () => `../../content/${props.courseKey}-checks/week-${selectedWeekNumber.value}.json` in weekCheckModules
    );
    const nextWeekAvailable = computed(() =>
      weeks.value.some((w) => w.number === selectedWeekNumber.value + 1 && w.available)
    );

    const selectWeek = (number) => {
      const week = weeks.value.find((w) => w.number === number);
      if (!week?.available) return;
      selectedWeekNumber.value = number;
      phase.value = 'tour';
      // Weitere Query-Parameter (z.B. ?stufe= bei „Meine erste Website“) bleiben erhalten.
      router.replace({ query: { ...route.query, week: number } });
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
          courseTitle: props.courseTitle,
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
.weekly-course-tour {
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

.weekly-course-check {
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
