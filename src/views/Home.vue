<template>
  <div>
    <section id="hero">
      <h2>Willkommen bei den Übergangshackern!</h2>
      <p>Deine Reise in die Welt des Programmierens beginnt hier. Lerne Python auf eine Weise, die Spass macht.</p>
      <router-link to="/kurs/python-12-wochen-grundkurs" class="cta-button">Zum 12-Wochen-Kurs</router-link>
    </section>

    <section id="termine" v-if="termine.length > 0">
      <h2>Nächste Termine</h2>
      <div class="termine-list">
        <router-link v-for="termin in termine" :key="termin.id" :to="termin.link" class="termin-link">
          <div class="termin-card" :class="{ 'cancelled': termin.cancelled }">
            <h3 v-if="termin.cancelled" class="cancelled-text">Termin abgesagt</h3>
            <h3>{{ termin.date }}</h3>
            <h4 class="termin-topic">{{ termin.topic }}</h4>
            <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
            <p><strong>Ort:</strong> {{ termin.location }}</p>
          </div>
        </router-link>
      </div>
    </section>

    <section id="kurse-uebersicht">
      <h2>Kursübersicht</h2>
      <div class="course-list">
        <div v-for="kurs in kurse" :key="kurs.id" class="course-card">
          <h3>{{ kurs.title }}</h3>
          <p>{{ kurs.description }}</p>
          <router-link :to="`/kurs/${kurs.id}`" class="course-link">Mehr erfahren</router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

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

    const fetchTermine = async () => {
      try {
        const response = await fetch('/termine.json');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const allTermine = await response.json();

        const today = new Date();
        today.setHours(0, 0, 0, 0);

        termine.value = allTermine
          .filter(termin => {
            const terminDate = parseDate(termin.date);
            return terminDate && terminDate >= today;
          })
          .sort((a, b) => parseDate(a.date) - parseDate(b.date)); // Sort appointments by date

      } catch (error) {
        console.error('Could not load or filter termine:', error);
      }
    };

    const fetchKurse = async () => {
      try {
        const response = await fetch('/kurse.json');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        kurse.value = await response.json();
      } catch (error) {
        console.error('Could not load kurse:', error);
      }
    };

    onMounted(async () => {
      await fetchTermine();
      await fetchKurse();

      // Filter courses
      kurse.value = kurse.value.filter(kurs => {
        if (kurs.id === 'python-12-wochen-grundkurs') {
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
    };
  },
};
</script>

<style scoped>
.termin-topic {
  font-weight: bold;
  color: #333;
  margin-top: -10px;
  margin-bottom: 15px;
}
</style>
