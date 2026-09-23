<template>
  <div>
    <section id="hero">
      <h2>{{ t('home.hero.title') }}</h2>
      <p>{{ t('home.hero.subtitle') }}</p>
      <div class="hero-buttons">
        <a href="#kurse-uebersicht" class="cta-button">{{ t('home.cta.courses') }}</a>
        <router-link to="/projekte" class="cta-button cta-button-secondary">{{ t('home.cta.projects') }}</router-link>
      </div>
    </section>

    <section id="termine" v-if="termine.length > 0">
      <h2>{{ t('home.appointments.title') }}</h2>
      <div class="termine-list">
        <router-link v-for="termin in termine" :key="termin.id" :to="termin.link" class="termin-link">
          <div class="termin-card" :class="{ 'cancelled': termin.cancelled }">
            <h3 v-if="termin.cancelled" class="cancelled-text">{{ t('home.appt.cancelled') }}</h3>
            <h3>{{ termin.date }}</h3>
            <h4 class="termin-topic">{{ termin.topic }}</h4>
            <p><strong>{{ t('home.appt.time') }}</strong> {{ termin.time }}</p>
            <p><strong>{{ t('home.appt.location') }}</strong> {{ termin.location }}</p>
          </div>
        </router-link>
      </div>
    </section>

    <section id="kurse-uebersicht">
      <h2>{{ t('home.courses.title') }}</h2>
      <p class="placement-hint">
        {{ t('home.cta.placementHint') }}
        <router-link to="/kurs/python-einstufung" class="placement-hint-link">{{ t('home.cta.placement') }} →</router-link>
      </p>
      <div class="course-list">
        <router-link v-for="kurs in kurse" :key="kurs.id" :to="`/kurs/${kurs.id}`" class="course-card">
          <span v-if="kurs.format" class="course-format-badge">{{ t(`courseFormat.${kurs.format}`) }}</span>
          <h3>{{ lang === 'en' && kurs.title_en ? kurs.title_en : kurs.title }}</h3>
          <p>{{ lang === 'en' && kurs.description_en ? kurs.description_en : kurs.description }}</p>
          <span class="course-link">{{ t('home.course.moreInfo') }}</span>
        </router-link>
      </div>
    </section>

    <section id="projekte-teaser">
      <div class="projekte-teaser-card">
        <div class="projekte-teaser-text">
          <h3>{{ t('home.projects.title') }}</h3>
          <p>{{ t('home.projects.desc') }}</p>
        </div>
        <router-link to="/projekte" class="projekte-teaser-link">{{ t('home.projects.link') }}</router-link>
      </div>
    </section>

    <section id="unterstuetzer">
      <h2>{{ t('home.supporters.title') }}</h2>
      <div class="unterstuetzer-list">
        <div class="unterstuetzer-card">
          <div class="unterstuetzer-content">
            <img src="@/assets/itscouts-logo.jpeg" alt="ITScouts Logo" class="unterstuetzer-logo">
            <div class="unterstuetzer-text">
              <h3>ITScouts</h3>
              <p>{{ t('home.itscouts.desc') }}</p>
              <a href="https://www.faw.de/luebeck/projekte/it-scout" target="_blank" rel="noopener noreferrer" class="mehr-infos-link">{{ t('home.moreInfo') }}</a>
            </div>
          </div>
        </div>

        <div class="unterstuetzer-card">
          <div class="unterstuetzer-content">
            <img src="@/assets/logo_dlc_beta.svg" alt="DLC Logo" class="unterstuetzer-logo">
            <div class="unterstuetzer-text">
              <h3>DLC - Digital Learning Center</h3>
              <p>{{ t('home.dlc.desc') }}</p>
              <a href="https://dlc.sh" target="_blank" rel="noopener noreferrer" class="mehr-infos-link">{{ t('home.moreInfo') }}</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { assetUrl } from '../utils/assetUrl';
import { useLanguage } from '../composables/useLanguage.js';

export default {
  name: 'Home',
  setup() {
    const termine = ref([]);
    const kurse = ref([]);

    // Helper to parse date strings like "Dienstag, 16.09.25"
    const parseDate = (dateString) => {
      const datePart = dateString.split(', ')[1];
      if (!datePart) return null;
      const parts = datePart.split('.');
      if (parts.length !== 3) return null;
      // new Date(year, monthIndex, day)
      return new Date(`20${parts[2]}`, parts[1] - 1, parts[0]);
    };

    // Helper for recurring terms: Laufzeit aktiv wenn heute zwischen validFrom und validUntil
    const parseISO = (isoString) => (isoString ? new Date(isoString) : null);
    const isRecurringActive = (termin, today) => {
      if (!termin.recurring || !termin.validFrom) return false;
      const from = parseISO(termin.validFrom);
      if (!from || today < from) return false;
      if (!termin.validUntil) return true;
      const until = parseISO(termin.validUntil);
      return until && today <= until;
    };

    const fetchTermine = async () => {
      try {
        const response = await fetch(assetUrl('termine.json'));
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const allTermine = await response.json();

        const today = new Date();
        today.setHours(0, 0, 0, 0);

        const getSortDate = (termin) => {
          if (termin.recurring) return parseISO(termin.validFrom) || today;
          return parseDate(termin.date) || today;
        };

        termine.value = allTermine
          .filter(termin => {
            if (termin.cancelled) return false;
            if (termin.recurring) return isRecurringActive(termin, today);
            const terminDate = parseDate(termin.date);
            return terminDate && terminDate >= today;
          })
          .sort((a, b) => {
            // Wiederkehrende Termine zuerst, dann nach Datum
            const aRec = a.recurring ? 0 : 1;
            const bRec = b.recurring ? 0 : 1;
            if (aRec !== bRec) return aRec - bRec;
            return getSortDate(a) - getSortDate(b);
          });

      } catch (error) {
        console.error('Could not load or filter termine:', error);
      }
    };

    const fetchKurse = async () => {
      try {
        const response = await fetch(assetUrl('kurse.json'));
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        kurse.value = await response.json();
      } catch (error) {
        console.error('Could not load kurse:', error);
      }
    };

    const { lang, t } = useLanguage();

    onMounted(async () => {
      await fetchTermine();
      await fetchKurse();

      // Filter courses — Projekt-Kurse haben eine eigene Übersicht unter /projekte
      const ALWAYS_VISIBLE_KURSE = ['python-12-wochen-grundkurs', 'python-grundlagen-interaktiv', 'js-grundkurs'];
      kurse.value = kurse.value.filter(kurs => {
        if (kurs.type === 'projekt') {
          return false;
        }
        if (ALWAYS_VISIBLE_KURSE.includes(kurs.id)) {
          return true;
        }
        return termine.value.some(termin => termin.link.startsWith(`/kurs/${kurs.id}`));
      });

      // Sort courses by their earliest appointment date
      kurse.value.sort((kursA, kursB) => {
        const getEarliestDate = (kursId) => {
          const kursTermine = termine.value
            .filter(termin => termin.link.startsWith(`/kurs/${kursId}`))
            .map(termin => parseDate(termin.date));
          
          if (kursTermine.length === 0) return null;
          
          // Return the earliest date
          return new Date(Math.min.apply(null, kursTermine));
        };

        const dateA = getEarliestDate(kursA.id);
        const dateB = getEarliestDate(kursB.id);

        if (dateA && !dateB) return -1; // A has a date, B doesn't -> A comes first
        if (!dateA && dateB) return 1;  // B has a date, A doesn't -> B comes first
        if (!dateA && !dateB) return 0; // Neither has a date -> keep original order

        return dateA - dateB; // Both have dates -> sort chronologically
      });
    });

    return {
      termine,
      kurse,
      lang,
      t,
    };
  },
};
</script>

<style scoped>
.course-list .course-card {
  display: block;
  color: inherit;
  text-decoration: none;
}

.placement-hint {
  margin: -14px 0 24px;
  color: #666;
  font-size: 0.95em;
}

.placement-hint-link {
  display: inline-block;
  margin-left: 6px;
  color: var(--primary-purple, #4a2274);
  font-weight: 700;
  text-decoration: underline;
  transition: color 0.2s;
}

.placement-hint-link:hover {
  color: #3d1b5c;
}

.course-format-badge {
  display: inline-block;
  margin-bottom: 10px;
  padding: 3px 10px;
  border-radius: 20px;
  background: #f3eef8;
  color: var(--primary-purple, #4a2274);
  font-size: 0.75em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.projekte-teaser-card {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 24px;
  background: #fafafa;
  border: 1px solid var(--border-color, #e0e0e0);
  border-left: 6px solid var(--accent-orange, #ff9800);
  border-radius: 12px;
}

.projekte-teaser-text h3 {
  margin: 0 0 4px;
  color: var(--primary-purple, #4a2274);
}

.projekte-teaser-text p {
  margin: 0;
  color: #444;
}

.projekte-teaser-link {
  background: var(--primary-purple, #4a2274);
  color: white;
  text-decoration: none;
  padding: 10px 18px;
  border-radius: 8px;
  font-weight: 600;
  white-space: nowrap;
  transition: background 0.2s;
}

.projekte-teaser-link:hover {
  background: #3d1b5c;
}

.termin-topic {
  font-weight: bold;
  color: #333;
  margin-top: -10px;
  margin-bottom: 15px;
}

.unterstuetzer-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 25px;
}

.unterstuetzer-card {
  background: #fafafa;
  border-radius: 12px;
  padding: 25px;
  border: 1px solid var(--border-color, #e0e0e0);
}

.unterstuetzer-content {
  display: flex;
  align-items: center;
}

.unterstuetzer-link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease;
}

.unterstuetzer-link:hover {
  transform: translateY(-2px);
}

.mehr-infos-link {
  display: inline-block;
  margin-top: 1rem;
  color: #007bff;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.mehr-infos-link:hover {
  color: #0056b3;
  text-decoration: underline;
}

.unterstuetzer-logo {
  width: 120px;
  height: auto;
  margin-right: 2rem;
  border-radius: 4px;
}

.unterstuetzer-text h3 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
}

.unterstuetzer-text p {
  margin: 0;
  color: #666;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .unterstuetzer-content {
    flex-direction: column;
    text-align: center;
  }
  
  .unterstuetzer-logo {
    margin-right: 0;
    margin-bottom: 1rem;
  }
}
</style>
