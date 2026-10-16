<template>
  <WeeklyCourseTour
    class="ki-labor-tour"
    :weeks="KI_LABOR_WEEKS"
    week-prefix="ki-labor-woche"
    course-key="ki-labor"
    :course-title="KI_LABOR_COURSE_TITLE"
    engine="pyodide"
    concept-language="python"
    downloads-base="/ki-labor-zips/woche-"
  />
</template>

<script>
import WeeklyCourseTour from './WeeklyCourseTour.vue';
import { KI_LABOR_WEEKS, KI_LABOR_COURSE_TITLE } from '../data/kiLaborWeeks.js';

// KI-Labor: 8 Wochen Python (Pyodide), Wochen-Check + Zertifikat je Woche - die ganze Logik steckt
// in WeeklyCourseTour.vue, Titel/Lernziele in ../data/kiLaborWeeks.js.
export default {
  name: 'KiLaborTour',
  components: { WeeklyCourseTour },
  setup() {
    return { KI_LABOR_WEEKS, KI_LABOR_COURSE_TITLE };
  },
};
</script>
