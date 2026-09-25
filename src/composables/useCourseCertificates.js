import { ref } from 'vue';
import { loadWeekChecks, listCertificateCourseKeys, useWeekChecks } from './useWeekChecks';
import { loadWeekLernziele } from './useWeeklyContent';
import { KI_LABOR_WEEKS } from '../data/kiLaborWeeks.js';

// Kleines, statisches Mapping courseKey -> Kurs-Route/Titel, analog zu den COURSE_TITLE-
// Konstanten in useCertificatePdf.js/KiLaborTour.vue. Bewusst kein generischer Registry-Mechanismus
// (bisher nur 2 Kurse mit Wochen-Zertifikaten: der 12-Wochen-Grundkurs und das KI-Labor) - ein
// courseKey ohne Eintrag hier wird beim Laden einfach übersprungen statt einen Fehler zu werfen.
const COURSE_INFO = {
  python: {
    courseId: 'python-12-wochen-grundkurs',
    title: 'Python 12-Wochen-Grundkurs',
    title_en: 'Python 12-Week Basics Course',
  },
  'ki-labor': {
    courseId: 'ki-labor',
    title: 'KI-Labor',
    title_en: 'AI Lab',
  },
};

// Lernziele je Kurs für die Zertifikat-PDF (siehe useCertificatePdf.js) - pro courseKey anders
// beschafft: Python hat sie in den Wochen-Notebooks als Markdown-Frontmatter (loadWeekLernziele,
// sprachabhängig), das KI-Labor in einer statischen Liste (kiLaborWeeks.js, bisher nur Deutsch).
async function loadLernzieleByWeek(courseKey, lang) {
  if (courseKey === 'python') {
    const byWeek = await loadWeekLernziele(lang);
    const result = {};
    for (const [weekNumber, week] of Object.entries(byWeek)) {
      result[weekNumber] = week.lernzieleFull || [];
    }
    return result;
  }
  if (courseKey === 'ki-labor') {
    const result = {};
    for (const week of KI_LABOR_WEEKS) {
      result[week.number] = week.lernziele || [];
    }
    return result;
  }
  return {};
}

/**
 * Zertifikate für alle Kurse mit Wochen-Check (aktuell Python-Grundkurs + KI-Labor) - fürs
 * Profil (ProfilView.vue). Nur Wochen, für die tatsächlich Check-Content existiert, tauchen auf
 * (keine "Woche 3 kommt noch"-Kacheln für ein Kurs-Thema, das inhaltlich noch nicht fertig ist).
 */
export function useCourseCertificates() {
  const courses = ref([]);
  const loading = ref(true);

  const load = async (lang = 'de') => {
    loading.value = true;
    try {
      const courseKeys = listCertificateCourseKeys().filter((key) => COURSE_INFO[key]);
      courses.value = await Promise.all(
        courseKeys.map(async (courseKey) => {
          const info = COURSE_INFO[courseKey];
          const [data, lernzieleByWeek] = await Promise.all([
            loadWeekChecks(courseKey),
            loadLernzieleByWeek(courseKey, lang),
          ]);
          const { isWeekCheckPassed } = useWeekChecks(courseKey);
          const weekNumbers = Object.keys(data.weeks || {})
            .map(Number)
            .sort((a, b) => a - b);
          const weeks = weekNumbers.map((weekNumber) => {
            const week = data.weeks[String(weekNumber)];
            const totalChallenges = week.codingChallenges?.length ?? 2;
            return {
              weekNumber,
              title: week.title,
              title_en: week.title_en,
              earned: isWeekCheckPassed(weekNumber, totalChallenges),
              lernziele: lernzieleByWeek[weekNumber] || [],
            };
          });
          return {
            courseKey,
            ...info,
            weeks,
            earnedCount: weeks.filter((w) => w.earned).length,
          };
        })
      );
    } catch (e) {
      console.error('Could not load course certificates:', e);
      courses.value = [];
    } finally {
      loading.value = false;
    }
  };

  return { courses, loading, load };
}
