<template>
  <div v-if="passed" class="certificate-reveal">
    <div class="certificate-badge">🎓</div>
    <h3>{{ t('tour.certificate.title') }}</h3>
    <p>{{ t('tour.certificate.earned').replace('{week}', title) }}</p>

    <div v-if="isLoggedIn" class="certificate-name-row">
      <label :for="`final-cert-name-${courseKey}`">{{ t('progress.certificate.name.label') }}</label>
      <input
        :id="`final-cert-name-${courseKey}`"
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
  <p v-else class="final-check-pending">{{ t('check.finalPending') }}</p>
</template>

<script>
import { ref, computed } from 'vue';
import { useLanguage } from '../composables/useLanguage';
import { useAuth } from '../composables/useAuth';
import { useWeekChecks, loadWeekChecks } from '../composables/useWeekChecks';
import { downloadCertificatePdf } from '../composables/useCertificatePdf';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

/**
 * Zertifikat nach dem Abschluss-Check eines Einstiegskurses (ProjectCourse.vue `finalCheck`) - wie
 * der Reveal in KiLaborTour.vue, nur ohne Wochen: ein Zertifikat fuer den ganzen Kurs, PDF nur
 * mit Login, Lernziele aus `lernziele` im Check-Content.
 */
export default {
  name: 'FinalCertificate',
  props: {
    courseKey: { type: String, required: true },
    // { de, en } aus kurse.json - steht auf dem Zertifikat.
    courseTitle: { type: Object, required: true },
  },
  setup(props) {
    const { t, lang } = useLanguage();
    const { isLoggedIn, user } = useAuth();
    const { isWeekCheckPassed } = useWeekChecks(props.courseKey);

    const passed = computed(() => isWeekCheckPassed(1));
    const title = computed(() => props.courseTitle[lang.value] || props.courseTitle.de);
    const certificateName = ref(localStorage.getItem(CERTIFICATE_NAME_KEY) || user.value?.username || '');
    const setCertificateName = (value) => {
      certificateName.value = value;
      localStorage.setItem(CERTIFICATE_NAME_KEY, value);
    };

    const pdfBusy = ref(false);
    const onDownloadPdf = async () => {
      pdfBusy.value = true;
      try {
        const data = await loadWeekChecks(props.courseKey);
        await downloadCertificatePdf({
          weekNumber: 1,
          weekTitle: title.value,
          lernziele: data?.weeks?.['1']?.lernziele || [],
          learnerName: certificateName.value || user.value?.username || '',
          lang: lang.value,
          courseTitle: props.courseTitle,
          singleCheck: true,
        });
      } finally {
        pdfBusy.value = false;
      }
    };

    return { t, isLoggedIn, passed, title, certificateName, setCertificateName, pdfBusy, onDownloadPdf };
  },
};
</script>

<style scoped>
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

.final-check-pending {
  margin-top: 16px;
  color: #6c757d;
  font-style: italic;
}
</style>
