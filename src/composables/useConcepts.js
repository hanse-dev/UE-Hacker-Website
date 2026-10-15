import data from '../../content/begriffe.json';

// Begriffe in Projekt-Kursen (z.B. "Array", "Schleife") auf die Woche des Grundkurses verlinken,
// in der sie erklärt werden. Daten: content/begriffe.json, Sprache = `language` aus kurse.json.
// Die Links öffnen in einem neuen Tab, damit das Projekt (Code im Editor) offen bleibt.

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeAttr(s) {
  return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
}

export function conceptsFor(language) {
  const list = data[language];
  return Array.isArray(list) ? list : [];
}

export function conceptHref(concept) {
  return `/kurs/${concept.kurs}?week=${concept.woche}`;
}

export function courseName(concept) {
  return data.kurse?.[concept.kurs] || concept.kurs;
}

// Ein einziger Regex über alle Schreibweisen (längste zuerst, damit "Arrays" vor "Array" und
// "for-Schleife" vor "Schleife" greift). Nur ganze Wörter: kein Buchstabe, keine Ziffer, kein
// Unterstrich oder Bindestrich direkt davor/danach ("funktioniert", "Klassen-Umfrage" zählen nicht).
function buildMatcher(list) {
  const byForm = new Map();
  for (const c of list) for (const f of c.formen) byForm.set(f, c);
  const forms = [...byForm.keys()].sort((a, b) => b.length - a.length);
  if (forms.length === 0) return null;
  const regex = new RegExp(`(?<![\\p{L}\\p{N}_-])(${forms.map(escapeRegex).join('|')})(?![\\p{L}\\p{N}_-])`, 'gu');
  return { regex, byForm };
}

function sortByWeek(concepts) {
  return [...concepts].sort((a, b) => a.woche - b.woche || a.begriff.localeCompare(b.begriff));
}

/** Begriffe, die in einem Klartext (z.B. Aufgabenstellung) vorkommen. */
export function conceptsInText(text, language) {
  const m = buildMatcher(conceptsFor(language));
  if (!m || !text) return [];
  const found = new Set();
  for (const hit of String(text).matchAll(m.regex)) found.add(m.byForm.get(hit[1]));
  return sortByWeek(found);
}

// Bereiche, in denen nie verlinkt wird: Code-Blöcke, Inline-Code, schon vorhandene Links,
// Überschriften und die Tags selbst (Attribute!).
const SKIP = /(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>|<a\b[\s\S]*?<\/a>|<h[1-6][\s\S]*?<\/h[1-6]>|<[^>]+>)/gi;

/**
 * Verlinkt im gerenderten Lektions-HTML jeden Begriff beim ersten Vorkommen im Fließtext und
 * liefert alle in der Lektion vorkommenden Begriffe (auch aus Inline-Code wie `push`, nicht aus
 * Code-Blöcken) für den "Hier lernst du mehr"-Kasten.
 */
export function linkConcepts(html, language) {
  const m = buildMatcher(conceptsFor(language));
  if (!m || !html) return { html: html || '', found: [] };
  const linked = new Set();
  const parts = html.split(SKIP);
  const out = parts.map((part, i) => {
    if (i % 2 === 1) return part; // vom Split eingefangener Skip-Bereich
    return part.replace(m.regex, (match) => {
      const c = m.byForm.get(match);
      if (linked.has(c)) return match;
      linked.add(c);
      const title = `${c.erklaerung} – ${courseName(c)}, Woche ${c.woche}`;
      return `<a class="concept-link" href="${conceptHref(c)}" target="_blank" rel="noopener" title="${escapeAttr(title)}">${match}</a>`;
    });
  }).join('');

  const prose = html.replace(/<pre[\s\S]*?<\/pre>/gi, ' ').replace(/<[^>]+>/g, ' ');
  return { html: out, found: conceptsInText(prose, language) };
}

/**
 * Vereinigung mehrerer Begriffslisten, nach Kurswoche sortiert. Doppelte über Kurs + Begriff
 * erkennen, nicht über die Objekt-Identität - aus einem Vue-ref kommen reaktive Proxys zurück, die
 * nicht `===` zum Original aus begriffe.json sind.
 */
export function mergeConcepts(...lists) {
  const all = new Map();
  for (const l of lists) for (const c of l) all.set(`${c.kurs}|${c.begriff}`, c);
  return sortByWeek(all.values());
}
