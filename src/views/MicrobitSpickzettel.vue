<template>
  <div class="spickzettel">
    <GuideLessonView
      :lesson="lesson"
      content-path="microbit-spickzettel"
      variant="microbit-spickzettel"
      course-id="microbit-spickzettel"
    />
  </div>
</template>

<script>
import GuideLessonView from '../components/GuideLessonView.vue';

// Nachschlage-Seite für die micro:bit-Kurse: immer offen, ohne Abhakpunkte und ohne Fortschritt.
// Die Begriffs-Links der Kurse springen per #anker zu den Überschriften (content/begriffe.json).
const LESSON = { id: 'spickzettel', file: 'spickzettel.md', tasks: [] };

export default {
  name: 'MicrobitSpickzettel',
  components: { GuideLessonView },
  setup() {
    return { lesson: LESSON };
  },
};
</script>

<style scoped>
.spickzettel {
  padding: 24px 16px 40px;
}
</style>
