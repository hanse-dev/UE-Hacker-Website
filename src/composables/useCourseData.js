import { marked } from 'marked';
import { assetUrl } from '../utils/assetUrl';
import { upcomingTermine } from '../utils/terminDate.js';

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
      const response = await fetch('/api/termine');
      const allTermine = await response.json();
      courseTermine = upcomingTermine(
        allTermine.filter((termin) => termin.link.startsWith(`/kurs/${courseId}`)),
      );
    } catch (e) {
      console.error('Could not load appointments:', e);
    }
  }

  return { course, description, courseTermine };
}
