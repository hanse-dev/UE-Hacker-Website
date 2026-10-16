// Stufe „Intensiv“ von „Meine erste Website“ (WebsiteCourse.vue): 9 Wochen HTML & CSS, Wochen-Check +
// Zertifikat je Woche. Titel aus KURSPLAN.md "Web-Track", Lernziele gehen aufs Zertifikat-PDF
// (useCourseCertificates.js) - nur Stoff, der in genau dieser Woche gelehrt wird.
export const WEB_GRUNDKURS_WEEKS = [
  {
    number: 1,
    title: 'Das Grundgerüst',
    lernziele: [
      'Das Grundgerüst einer HTML-Seite (DOCTYPE, html, head, body) aufschreiben und erklären können',
      'Elemente aus Anfangs-Tag, Inhalt und End-Tag aufbauen und richtig verschachteln können',
      'Attribute wie lang, title und id einsetzen können',
      'Überschriften, Absätze, Zeilenumbrüche und Kommentare verwenden können',
    ],
  },
  {
    number: 2,
    title: 'Struktur mit Bedeutung',
    lernziele: [
      'Eine Seite mit header, nav, main, section, article und footer gliedern können',
      'Überschriften-Ebenen sinnvoll hierarchisch einsetzen können',
      'Aufzählungen, nummerierte und verschachtelte Listen bauen können',
      'Text mit strong, em und mark auszeichnen können',
    ],
  },
  {
    number: 3,
    title: 'Bilder, Links und Tabellen',
    lernziele: [
      'Bilder mit src, alt und Größenangabe einbinden können',
      'Links zu anderen Seiten und Sprungmarken innerhalb der Seite setzen können',
      'Tabellen mit Kopfzeile (thead, th) und Datenzeilen (tbody, td) aufbauen können',
      'Bilder mit figure und figcaption beschriften können',
    ],
  },
  {
    number: 4,
    title: 'Formulare',
    lernziele: [
      'Eingabefelder mit input und passendem type (text, email, number, checkbox) anlegen können',
      'Jedes Feld mit label beschriften und über for/id verknüpfen können',
      'Auswahllisten (select/option), Textbereiche (textarea) und Knöpfe einsetzen können',
      'Pflichtfelder mit required und Hilfetexte mit placeholder festlegen können',
    ],
  },
  {
    number: 5,
    title: 'CSS-Grundlagen',
    lernziele: [
      'CSS-Regeln mit Tag-, Klassen-, id- und Nachfahren-Selektoren schreiben können',
      'Erklären können, welche Regel gewinnt (Reihenfolge und Spezifität)',
      'Farben als Name, Hex-Wert und rgb() angeben können',
      'Schriften gestalten und Werte mit CSS-Variablen wiederverwenden können',
    ],
  },
  {
    number: 6,
    title: 'Das Box-Modell',
    lernziele: [
      'Inhalt, padding, border und margin einer Box unterscheiden können',
      'Breite und Höhe festlegen und box-sizing: border-box einsetzen können',
      'Blöcke mit margin: auto zentrieren können',
      'Elemente mit position: relative und absolute verschieben können',
    ],
  },
  {
    number: 7,
    title: 'Flexbox',
    lernziele: [
      'Elemente mit display: flex in eine Reihe oder Spalte stellen können',
      'Elemente mit justify-content und align-items ausrichten können',
      'Abstände mit gap setzen und Umbrüche mit flex-wrap erlauben können',
      'Mit flex: 1 Platz auf mehrere Elemente verteilen können',
    ],
  },
  {
    number: 8,
    title: 'Grid und Handy-Ansicht',
    lernziele: [
      'Ein Raster mit display: grid und grid-template-columns bauen können',
      'Spaltenbreiten mit fr und repeat() angeben können',
      'Mit Media Queries eine Seite für schmale Bildschirme anpassen können',
      'Bilder mit max-width: 100% an die Breite anpassen können',
    ],
  },
  {
    number: 9,
    title: 'Abschlussprojekt',
    lernziele: [
      'Eine vollständige, gegliederte Website zu einem eigenen Thema planen und bauen können',
      'Navigation, Inhalte, Galerie und Formular zu einer Seite zusammenfügen können',
      'Mit :hover und transition auf Maus-Bewegungen reagieren können',
      'Mit einer Zeile JavaScript einen Knopf zum Leben erwecken können',
    ],
  },
];

export const WEB_GRUNDKURS_COURSE_TITLE = { de: 'Meine erste Website – Intensiv', en: 'My First Website – Intensive' };
