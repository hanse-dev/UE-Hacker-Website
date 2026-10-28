import lehrplan from '../../content/python-12-wochen-grundkurs/lehrplan.md?raw';
import {
  formatTerminDate,
  formatTerminTime,
  nextWednesdayIso,
  parseTerminDate,
  parseTerminTime,
  recurringLabel,
  toIso,
} from '../utils/terminDate.js';

export const WOCHEN_KURS = 'python-12-wochen-grundkurs';
export const WERKSTATT = '__werkstatt';
export const EIGENER_LINK = '__link';
export const NEUER_ORT = '__neu';

export const WERKSTATT_TERMIN = {
  topic: 'Offene Werkstatt: Weiterarbeiten am eigenen Kurs oder Projekt',
  link: '/projekte',
};

export const DEFAULT_START = '17:00';
export const DEFAULT_END = '18:00';

export const WOCHEN = [...lehrplan.matchAll(/^## Woche (\d+) – (.+)$/gm)]
  .map((m) => ({ nr: Number(m[1]), title: m[2].trim() }));

export function wochenTopic(nr) {
  const woche = WOCHEN.find((w) => w.nr === nr);
  return woche ? `Woche ${nr}: ${woche.title}` : `Woche ${nr}`;
}

// Auswahl im Formular: Kurse und Projekte aus kurse.json, ohne versteckte (unlisted).
export function terminKursOptionen(kurse) {
  const listed = kurse.filter((k) => !k.unlisted);
  return {
    kurse: listed.filter((k) => k.type !== 'projekt'),
    projekte: listed.filter((k) => k.type === 'projekt'),
  };
}

function wocheAusLink(link) {
  const m = /#woche-(\d+)$/.exec(link || '');
  return m ? Number(m[1]) : null;
}

// Ohne festes Thema: der 12-Wochen-Kurs läuft mit der Woche nach dem letzten Termin weiter,
// sonst eine offene Werkstatt.
export function terminVorschlag(termine) {
  const neuester = [...termine].sort((a, b) => b.id - a.id)
    .find((termin) => !termin.cancelled && !termin.recurring);
  const woche = neuester && neuester.link.startsWith(`/kurs/${WOCHEN_KURS}`) ? wocheAusLink(neuester.link) : null;
  if (woche && woche < 12) return { auswahl: WOCHEN_KURS, woche: woche + 1 };
  return { auswahl: WERKSTATT, woche: null };
}

function zuletztGenutzterOrt(termine) {
  const neuester = [...termine].sort((a, b) => b.id - a.id)[0];
  return neuester?.location || '';
}

export function linkFuer(form) {
  if (form.auswahl === WERKSTATT) return WERKSTATT_TERMIN.link;
  if (form.auswahl === EIGENER_LINK) return form.link;
  if (form.auswahl === WOCHEN_KURS && form.woche) return `/kurs/${WOCHEN_KURS}#woche-${form.woche}`;
  return `/kurs/${form.auswahl}`;
}

export function topicFuer(form, kurse) {
  if (form.auswahl === WERKSTATT) return WERKSTATT_TERMIN.topic;
  if (form.auswahl === EIGENER_LINK) return form.topic;
  if (form.auswahl === WOCHEN_KURS && form.woche) return wochenTopic(form.woche);
  return kurse.find((k) => k.id === form.auswahl)?.title || form.topic;
}

export function neuesTerminForm(termine, now = new Date()) {
  const vorschlag = terminVorschlag(termine);
  const dateIso = nextWednesdayIso(now);
  return {
    auswahl: vorschlag.auswahl,
    woche: vorschlag.woche,
    vorgeschlagen: true,
    topic: '',
    link: '',
    dateIso,
    start: DEFAULT_START,
    end: DEFAULT_END,
    ort: zuletztGenutzterOrt(termine),
    neuerOrt: '',
    cancelled: false,
    recurring: false,
    validFrom: dateIso,
    validUntil: '',
  };
}

export function terminFormAus(termin, kurse) {
  const date = parseTerminDate(termin.date);
  const time = parseTerminTime(termin.time) || { start: DEFAULT_START, end: DEFAULT_END };
  const m = /^\/kurs\/([^#/?]+)/.exec(termin.link || '');
  let auswahl = EIGENER_LINK;
  if (termin.link === WERKSTATT_TERMIN.link) auswahl = WERKSTATT;
  else if (m && kurse.some((k) => k.id === m[1])) auswahl = m[1];
  return {
    auswahl,
    woche: auswahl === WOCHEN_KURS ? wocheAusLink(termin.link) : null,
    vorgeschlagen: false,
    topic: termin.topic,
    link: termin.link,
    dateIso: date ? toIso(date) : (termin.validFrom || ''),
    start: time.start,
    end: time.end,
    ort: termin.location,
    neuerOrt: '',
    cancelled: termin.cancelled,
    recurring: termin.recurring,
    validFrom: termin.validFrom || '',
    validUntil: termin.validUntil || '',
  };
}

export function terminPayload(form) {
  const validFrom = form.validFrom || form.dateIso;
  return {
    date: form.recurring ? recurringLabel(validFrom) : formatTerminDate(form.dateIso),
    time: formatTerminTime(form.start, form.end),
    location: (form.ort === NEUER_ORT ? form.neuerOrt : form.ort).trim(),
    topic: form.topic.trim(),
    link: form.link.trim(),
    cancelled: form.cancelled,
    recurring: form.recurring,
    validFrom: form.recurring ? (validFrom || null) : null,
    validUntil: form.recurring ? (form.validUntil || null) : null,
  };
}
