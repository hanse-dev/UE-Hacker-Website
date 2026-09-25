<template>
  <div class="profil-view">
    <h1>{{ t('profil.title') }}</h1>

    <div v-if="!isLoggedIn" class="profil-login-required">
      <p>{{ t('profil.loginRequired') }}</p>
    </div>

    <template v-else>
      <p class="profil-greeting">{{ t('profil.greeting').replace('{name}', user?.username || '') }}</p>

      <section class="profil-badges">
        <h2>{{ t('profil.badges.title') }}</h2>
        <p class="profil-badges-hint">{{ t('profil.badges.hint') }}</p>

        <p v-if="loading" class="profil-loading">{{ t('profil.loading') }}</p>
        <div v-else class="badge-grid">
          <router-link
            v-for="badge in badges"
            :key="badge.id"
            :to="`/kurs/${badge.id}`"
            class="badge-card"
            :class="{ earned: badge.earned }"
          >
            <span class="badge-icon">{{ badge.earned ? '🏅' : '🔒' }}</span>
            <span class="badge-title">{{ lang === 'en' && badge.title_en ? badge.title_en : badge.title }}</span>
            <span class="badge-status">
              {{ badge.earned ? t('profil.badges.earned') : `${badge.completedCount}/${badge.totalLessons}` }}
            </span>
          </router-link>
        </div>
      </section>

      <section class="profil-certificates">
        <h2>{{ t('profil.certificates.title') }}</h2>
        <p class="profil-certificates-hint">{{ t('profil.certificates.hint') }}</p>

        <p v-if="certLoading" class="profil-loading">{{ t('profil.loading') }}</p>
        <template v-else>
          <div v-if="certCourses.some((c) => c.earnedCount > 0)" class="certificate-name-field">
            <label for="profil-certificate-name">{{ t('progress.certificate.name.label') }}</label>
            <input
              id="profil-certificate-name"
              type="text"
              :value="certificateName"
              @input="setCertificateName($event.target.value)"
            />
          </div>

          <div v-for="course in certCourses" :key="course.courseKey" class="cert-course-block">
            <h3 class="cert-course-title">
              {{ lang === 'en' && course.title_en ? course.title_en : course.title }}
              <span class="cert-course-count">{{ course.earnedCount }}/{{ course.weeks.length }} 🎓</span>
            </h3>
            <div class="badge-grid">
              <div
                v-for="week in course.weeks"
                :key="week.weekNumber"
                class="badge-card"
                :class="{ earned: week.earned }"
              >
                <router-link :to="`/kurs/${course.courseId}?week=${week.weekNumber}`" class="badge-card-link">
                  <span class="badge-icon">{{ week.earned ? '🎓' : '🔒' }}</span>
                  <span class="badge-title">{{ t('week.label') }} {{ week.weekNumber }}</span>
                  <span class="badge-status">
                    {{ lang === 'en' && week.title_en ? week.title_en : week.title }}
                  </span>
                </router-link>
                <button
                  v-if="week.earned"
                  class="btn-certificate-pdf"
                  :disabled="pdfBusyKey === certKey(course.courseKey, week.weekNumber)"
                  @click="onDownloadCertificate(course, week)"
                >
                  {{ pdfBusyKey === certKey(course.courseKey, week.weekNumber) ? t('progress.certificate.generating') : t('progress.certificate.download') }}
                </button>
              </div>
            </div>
          </div>
        </template>
      </section>
    </template>
  </div>
</template>

<script>
import { onMounted, ref, watch } from 'vue';
import { useAuth } from '../composables/useAuth.js';
import { useLanguage } from '../composables/useLanguage.js';
import { useProjectBadges } from '../composables/useProjectBadges.js';
import { useCourseCertificates } from '../composables/useCourseCertificates.js';
import { downloadCertificatePdf } from '../composables/useCertificatePdf.js';

const CERTIFICATE_NAME_KEY = 'ue-hacker-certificate-name';

export default {
  name: 'ProfilView',
  setup() {
    const { t, lang } = useLanguage();
    const { user, isLoggedIn } = useAuth();
    const { badges, loading, load } = useProjectBadges();
    const { courses: certCourses, loading: certLoading, load: loadCertificates } = useCourseCertificates();

    const loadAll = () => {
      load();
      loadCertificates(lang.value);
    };

    onMounted(() => {
      if (isLoggedIn.value) loadAll();
    });
    // Direkter Login-/Logout-Wechsel auf dieser Seite (ohne Neuladen) soll die Abzeichen sofort
    // laden bzw. den Login-Hinweis zeigen, nicht den Stand vom Seitenaufruf behalten.
    watch(isLoggedIn, (now) => {
      if (now) loadAll();
    });
    // Die Lernziele/Titel der Python-Zertifikate stecken in der Sprachversion des Notebook-
    // Frontmatters (loadWeekLernziele) - ein Sprachwechsel muss sie neu laden, sonst zeigt die
    // PDF nach dem Umschalten weiter die alte Sprache.
    watch(lang, () => {
      if (isLoggedIn.value) loadCertificates(lang.value);
    });

    // Gleicher Storage-Key wie FortschrittWidget.vue/KiLaborTour.vue - ein Name für alle
    // Zertifikate, egal aus welchem Kurs.
    const certificateName = ref(localStorage.getItem(CERTIFICATE_NAME_KEY) || user.value?.username || '');
    const setCertificateName = (value) => {
      certificateName.value = value;
      localStorage.setItem(CERTIFICATE_NAME_KEY, value);
    };

    const certKey = (courseKey, weekNumber) => `${courseKey}-${weekNumber}`;
    const pdfBusyKey = ref(null);
    const onDownloadCertificate = async (course, week) => {
      const key = certKey(course.courseKey, week.weekNumber);
      pdfBusyKey.value = key;
      try {
        await downloadCertificatePdf({
          weekNumber: week.weekNumber,
          weekTitle: lang.value === 'en' && week.title_en ? week.title_en : week.title,
          lernziele: week.lernziele || [],
          learnerName: certificateName.value || user.value?.username || '',
          lang: lang.value,
          courseTitle: { de: course.title, en: course.title_en },
        });
      } finally {
        pdfBusyKey.value = null;
      }
    };

    return {
      t, lang, user, isLoggedIn, badges, loading, certCourses, certLoading,
      certificateName, setCertificateName, certKey, pdfBusyKey, onDownloadCertificate,
    };
  },
};
</script>

<style scoped>
.profil-view {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.profil-login-required {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 20px;
  color: #555;
}

.profil-greeting {
  font-size: 1.1em;
  color: #333;
  margin-bottom: 32px;
}

.profil-badges h2 {
  margin-bottom: 4px;
}

.profil-badges-hint {
  color: #666;
  font-size: 0.9em;
  margin: 0 0 20px 0;
}

.profil-loading {
  color: #666;
}

.badge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 14px;
}

.badge-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 10px;
  padding: 18px 12px;
  text-align: center;
  transition: border-color 0.15s, transform 0.15s;
}

.badge-card-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  width: 100%;
  text-decoration: none;
}

.badge-card:hover {
  border-color: var(--primary-purple, #4a2274);
  transform: translateY(-2px);
}

.badge-card.earned {
  border-color: #ffd700;
  background: linear-gradient(135deg, #fef9e7 0%, #fdebd0 100%);
}

.badge-icon {
  font-size: 2.2em;
}

.badge-title {
  font-weight: 600;
  color: #333;
  font-size: 0.95em;
}

.badge-status {
  font-size: 0.8em;
  color: #666;
}

.badge-card.earned .badge-status {
  color: #8a6d00;
  font-weight: 600;
}

.profil-certificates {
  margin-top: 40px;
}

.profil-certificates h2 {
  margin-bottom: 4px;
}

.profil-certificates-hint {
  color: #666;
  font-size: 0.9em;
  margin: 0 0 20px 0;
}

.cert-course-block {
  margin-bottom: 28px;
}

.cert-course-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1em;
  color: #333;
  margin: 0 0 12px 0;
}

.cert-course-count {
  font-size: 0.8em;
  font-weight: 600;
  color: #7c3aed;
  background: #f3ecfe;
  border-radius: 999px;
  padding: 2px 10px;
}

.certificate-name-field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  margin: 0 0 20px 0;
}

.certificate-name-field label {
  font-size: 0.9em;
  color: #555;
  font-weight: 600;
}

.certificate-name-field input {
  flex: 1;
  min-width: 180px;
  max-width: 320px;
  padding: 8px 10px;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 0.9em;
}

.btn-certificate-pdf {
  margin-top: 2px;
  background: #7c3aed;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 0.75em;
  cursor: pointer;
}

.btn-certificate-pdf:hover:not(:disabled) {
  background: #6d28d9;
}

.btn-certificate-pdf:disabled {
  opacity: 0.6;
  cursor: default;
}
</style>
