<template>
  <div class="appointments-section">
    <h3>Nächste Termine für diesen Kurs</h3>
    <div v-if="termine.length > 0" class="termine-list-local">
      <div v-for="termin in termine" :key="termin.id" class="termin-card-local">
        <h4>{{ termin.date }}</h4>
        <p><strong>Uhrzeit:</strong> {{ termin.time }}</p>
        <p><strong>Ort:</strong> {{ termin.location }}</p>
        <p v-if="termin.topic"><strong>Thema:</strong> {{ termin.topic }}</p>
      </div>
    </div>
    <p v-else class="termine-empty">Aktuell keine Termine für diesen Kurs.</p>
  </div>
</template>

<script>
export default {
  name: 'CourseAppointments',
  props: {
    termine: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style scoped>
.appointments-section {
  background-color: #f9f9f9;
  border: 1px solid #eee;
  padding: 20px;
  margin-bottom: 40px;
  border-radius: 8px;
}

.appointments-section h3 {
  margin-top: 0;
  border-bottom: 2px solid #ffd700;
  padding-bottom: 10px;
}

.termin-card-local {
  background: #fff;
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
}

.termin-card-local h4 {
  margin-top: 0;
}

.termine-empty {
  color: #666;
  font-style: italic;
  margin: 0;
}
</style>
