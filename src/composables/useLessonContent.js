import { ref } from 'vue';
import { marked } from 'marked';

// Wildcard-Glob statt fester Pro-Kurs-Liste — ein neuer LessonView.vue-Kurs (z.B. ein Projekt-Kurs)
// braucht dadurch keine Änderung hier mehr, nur einen neuen Content-Ordner unter `content/`.
const allLessonModules = import.meta.glob(
  '../../content/*/*.md',
  { query: '?raw', import: 'default' }
);

const allGlossaryModules = import.meta.glob('../../content/*/glossary.json');

function escapeHtml(s) {
  if (!s) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/**
 * Lädt Lektions-Markdown + Glossar für den interaktiven Kurs/Cäsar-Chiffre und versieht
 * Glossar-Begriffe (in Aufgabentexten wie im gerenderten Lektionstext) mit Tooltip-Spans.
 * `isMounted` wird vom aufrufenden Component verwaltet (auch von dessen Task-Run/Check-Logik
 * genutzt) und hier nur gelesen, um State-Updates nach dem Unmount zu vermeiden.
 */
export function useLessonContent(isMounted) {
  const lessonContent = ref('');
  let glossary = {};

  const loadGlossary = async (contentPath) => {
    try {
      const key = `../../content/${contentPath}/glossary.json`;
      const loader = allGlossaryModules[key];
      if (loader) {
        const mod = await loader();
        glossary = mod.default || {};
      }
    } catch {
      glossary = {};
    }
  };

  // Ein Begriff wie "Wert" kann selbst wieder in der Erklärung eines anderen Begriffs
  // (z.B. "Variable") vorkommen. Bei sequenziellem Ersetzen auf dem wachsenden Output würde
  // ein späterer Begriff dann *innerhalb* des schon eingefügten title-Attributs erneut treffen
  // und dort ungeschütztes HTML (<span ...>) einfügen, was das äußere title-Attribut aufbricht.
  // Deshalb immer nur ein einziger kombinierter Regex-Durchlauf über den Originaltext.
  const glossaryRegex = (terms) => new RegExp(
    `(?<![<>])(${terms.map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})(?![^<]*>)`,
    'g',
  );

  const instructionWithGlossary = (text) => {
    if (!text || !glossary || Object.keys(glossary).length === 0) return escapeHtml(text || '');
    const escaped = escapeHtml(text);
    const terms = Object.keys(glossary).sort((a, b) => b.length - a.length);
    return escaped.replace(glossaryRegex(terms), (match) => {
      const explanation = glossary[match].replace(/"/g, '&quot;');
      return `<span class="glossary-term" title="${explanation}">${match}</span>`;
    });
  };

  const applyGlossaryTooltips = (html) => {
    if (!glossary || Object.keys(glossary).length === 0) return html;
    const codeBlockRegex = /<pre><code>[\s\S]*?<\/code><\/pre>/gi;
    const codeBlocks = html.match(codeBlockRegex) || [];
    const textParts = html.split(codeBlockRegex);
    const terms = Object.keys(glossary).sort((a, b) => b.length - a.length);
    const result = textParts.map((part, i) => {
      const out = part.replace(glossaryRegex(terms), (match) => {
        const explanation = glossary[match].replace(/"/g, '&quot;');
        return `<span class="glossary-term" title="${explanation}">${match}</span>`;
      });
      return out + (codeBlocks[i] || '');
    }).join('');
    return result;
  };

  const loadContent = async (lesson, contentPath) => {
    if (!lesson?.file || !contentPath) return;
    const key = `../../content/${contentPath}/${lesson.file}`;
    const loader = allLessonModules[key];
    if (!loader) {
      lessonContent.value = '<p>Lektion konnte nicht geladen werden.</p>';
      return;
    }
    try {
      if (Object.keys(glossary).length === 0) await loadGlossary(contentPath);
      const text = await loader();
      if (!isMounted.value) return;
      let html = marked(text ?? '');
      html = applyGlossaryTooltips(html);
      lessonContent.value = html;
    } catch (e) {
      if (!isMounted.value) return;
      console.error('Could not load lesson content:', e);
      lessonContent.value = '<p>Lektion konnte nicht geladen werden.</p>';
    }
  };

  return { lessonContent, loadGlossary, loadContent, instructionWithGlossary };
}
