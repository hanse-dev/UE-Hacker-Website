import { marked } from 'marked';
import { assetUrl } from '../utils/assetUrl';

function parseDate(dateString) {
  const datePart = dateString.split(', ')[1];
  if (!datePart) return null;
  const parts = datePart.split('.');
  if (parts.length !== 3) return null;
  return new Date(`20${parts[2]}`, parts[1] - 1, parts[0]);
}

function parseISO(isoString) {
  return isoString ? new Date(isoString) : null;
}

function isRecurringActive(termin, today) {
  if (!termin.recurring || !termin.validFrom) return false;
  const from = parseISO(termin.validFrom);
  if (!from || today < from) return false;
  if (!termin.validUntil) return true;
  const until = parseISO(termin.validUntil);
  return until && today <= until;
}

export async function loadCourseData(courseId, lang = 'de') {
  let course = null;
  let description = '';
  let courseTermine = [];

  try {
    const url = assetUrl('kurse.json');
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 10000);
    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeout);
    if (!response.ok) {
      throw new Error(`kurse.json: ${response.status} ${response.statusText} (${url})`);
    }
    const kurse = await response.json();
    course = kurse.find((k) => k.id === courseId);
    if (!course) {
      console.warn('loadCourseData: Kurs nicht gefunden:', courseId, 'Verfügbar:', kurse.map((k) => k.id));
    }
  } catch (e) {
    console.error('Could not load courses:', e);
  }

  if (course) {
    try {
      const enContentPath = `${course.contentPath}-en`;
      const hasEnDescription = ['python-12-wochen-grundkurs', 'python-grundlagen-interaktiv', 'python-einstufung'];
      const descPath = (lang === 'en' && hasEnDescription.includes(courseId))
        ? enContentPath
        : course.contentPath;
      const descModule = await import(`../../content/${descPath}/beschreibung.md?raw`);
      description = marked(descModule.default);
    } catch (e) {
      console.warn('Could not load beschreibung.md, falling back to kurse.json:', e.message);
      const fallback = lang === 'en' && course.description_en
        ? course.description_en
        : course.description;
      description = fallback
        ? `<p>${fallback}</p>`
        : '<p>Die Beschreibung für diesen Kurs konnte nicht geladen werden.</p>';
    }

    try {
      const response = await fetch(assetUrl('termine.json'));
      const allTermine = await response.json();
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const getSortDate = (termin) => {
        if (termin.recurring) return parseISO(termin.validFrom) || today;
        return parseDate(termin.date) || today;
      };

      courseTermine = allTermine
        .filter((termin) => {
          if (termin.cancelled || !termin.link.startsWith(`/kurs/${courseId}`)) return false;
          if (termin.recurring) return isRecurringActive(termin, today);
          const terminDate = parseDate(termin.date);
          return terminDate && terminDate >= today;
        })
        .sort((a, b) => {
          const aRec = a.recurring ? 0 : 1;
          const bRec = b.recurring ? 0 : 1;
          if (aRec !== bRec) return aRec - bRec;
          return getSortDate(a) - getSortDate(b);
        });
    } catch (e) {
      console.error('Could not load appointments:', e);
    }
  }

  return { course, description, courseTermine };
}
