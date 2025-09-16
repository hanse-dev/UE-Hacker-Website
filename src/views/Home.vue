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
          <div class="termin-card">
            <h3>{{ termin.date }}</h3>
            <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
            <p><strong>Ort:</strong> {{ termin.location }}</p>
            <p><strong>Thema:</strong> {{ termin.topic }}</p>
          </div>
        </router-link>
      </div>
    </section>

    <section id="kurse-uebersicht">
      <h2>Kursübersicht</h2>
      <div class="course-list">
        <div class="course-card">
          <h3>12-Wochen Python Grundkurs</h3>
          <p>Alles, was du für den Einstieg in Python brauchst. Von den Grundlagen bis zu deinem ersten eigenen Projekt.</p>
          <router-link to="/kurs/python-12-wochen-grundkurs" class="course-link">Mehr erfahren</router-link>
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

    onMounted(async () => {
      try {
        const response = await fetch('/termine.json');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        termine.value = await response.json();
      } catch (error) {
        console.error('Could not load termine:', error);
      }
    });

    return {
      termine,
    };
  },
};
</script>
