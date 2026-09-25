// Statische Titel/Lernziele-Liste fürs KI-Labor, analog zu JsGrundkursTour.vue (lohnt sich nur
// bei Themen-Varianten/Cheat-Sheets, die es hier bewusst nicht gibt) - Titel 1:1 aus KURSPLAN.md
// "KI-Track: KI-Grundlagen". Eigene Datei statt lokale Konstante in KiLaborTour.vue, weil auch
// useCourseCertificates.js (Zertifikate im Profil) die Lernziele fürs PDF braucht.
export const KI_LABOR_WEEKS = [
  {
    number: 1,
    title: 'Was ist KI?',
    lernziele: [
      'Den Unterschied zwischen Regeln schreiben und aus Beispielen lernen erklären können',
      'Die Begriffe Trainingsdaten, Label, Modell und Vorhersage kennen und anwenden können',
      'Grenzen von KI benennen können (wenige/einseitige Trainingsdaten, kein echtes Verständnis)',
    ],
  },
  {
    number: 2,
    title: 'Daten sind alles',
    lernziele: [
      'Einen Datensatz als Liste von Beispielen mit mehreren Merkmalen aufbauen können',
      'Muster in Daten von Auge erkennen (z.B. mit einer List Comprehension filtern)',
      'Mit fehlenden Werten (.get() mit Standardwert) sicher umgehen können',
      'Merkmale und Label eines Datensatzes trennen können',
    ],
  },
  {
    number: 3,
    title: 'Nächste Nachbarn (k-NN)',
    lernziele: [
      'Den Abstand zwischen zwei Beispielen mit mehreren Merkmalen berechnen können (euklidische Distanz)',
      'Den nächsten Nachbarn (1-NN) in einem Trainingsdatensatz finden können',
      'Die k nächsten Nachbarn holen und mit einem Mehrheitsentscheid klassifizieren können (k-NN)',
      'Einen kompletten k-NN-Klassifikator komplett selbst in Python schreiben können',
    ],
  },
  {
    number: 4,
    title: 'Training & Test',
    lernziele: [
      'Einen Datensatz mit Slicing in Trainings- und Testdaten aufteilen können',
      'Die Genauigkeit eines Klassifikators (Anteil richtiger Vorhersagen) selbst berechnen können',
      'Vorhersagen für einen kompletten Testdatensatz sammeln und mit den erwarteten Werten vergleichen können',
      'Overfitting an einem absichtlich zu kleinen/unrepräsentativen Trainingsdatensatz erkennen können',
    ],
  },
  { number: 5, title: 'Entscheidungsbäume', lernziele: [] },
  { number: 6, title: 'Neuronale Netze I', lernziele: [] },
  { number: 7, title: 'Neuronale Netze II', lernziele: [] },
  { number: 8, title: 'Grenzen & Ethik', lernziele: [] },
];

export const KI_LABOR_COURSE_TITLE = { de: 'KI-Labor', en: 'AI Lab' };
