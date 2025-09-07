<template>
  <div>
    <section id="hero">
      <h2>Willkommen bei den Uebergangshackern!</h2>
      <p>Deine Reise in die Welt des Programmierens beginnt hier. Lerne Python auf eine Weise, die Spass macht.</p>
      <router-link to="/kurs/python-12-wochen-grundkurs" class="cta-button">Zum 12-Wochen-Kurs</router-link>
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
export default {
  name: 'Home',
};
</script>
