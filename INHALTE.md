# Inhalts-Übersicht: Dateistruktur und Zusammenhänge

Dieses Dokument beschreibt, welche Dateien zusammengehören und was bei Änderungen gleichzeitig angepasst werden muss.

---

## 1. Kurse im Überblick

| Kurs-ID | Inhaltspfad (DE) | Inhaltspfad (EN) | Typ |
|---|---|---|---|
| `python-12-wochen-grundkurs` | `content/python-12-wochen-grundkurs/` | `content/python-12-wochen-grundkurs-en/` | Notebooks |
| `python-grundlagen-interaktiv` | `content/python-grundlagen-interaktiv/` | *(keine EN-Version)* | Markdown + JSON |
| *(Variante)* | `content/python-grundlagen-interaktiv-kinder/` | *(keine EN-Version)* | Markdown + JSON |
| *(Variante)* | `content/python-grundlagen-interaktiv-jugendliche/` | *(keine EN-Version)* | Markdown + JSON |
| `projekt-caesar-chiffre` | `content/caesar-chiffre/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-haeufigkeitsanalyse` | `content/haeufigkeitsanalyse/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-morsecode` | `content/morsecode/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-zahlendetektiv` | `content/zahlendetektiv/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-js-spielewerkstatt` | `content/js-spielewerkstatt/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "js-sandbox"`) |
| `projekt-js-memory` | `content/js-memory/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "js-sandbox"`, `sandboxMode: "dom"` — DOM statt Canvas) |
| `projekt-js-quiz` | `content/js-quiz/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "js-sandbox"`, `sandboxMode: "dom"` – DOM-Übungsfläche statt Canvas) |
| `projekt-microbit-auto` | `content/microbit-auto/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "anleitung"`, Hardware-Kurs zum Abhaken) |
| `web-erste-website` | Einfach: `content/web-erste-website/` + `content/web-erste-website-checks/`; Intensiv: `content/web-grundkurs-woche{1-9}/` + `content/web-grundkurs-checks/` | *(keine EN-Version)* | Stufenwahl (`WebsiteCourse.vue`): Einfach = Lektionsliste mit Abschluss-Check (`type: "lektionen"`, `finalCheck: true`), Intensiv = 9 Wochen mit Wochen-Checks (`WeeklyCourseTour.vue`, Titel/Lernziele in `src/data/webGrundkursWeeks.js`) |
| `projekt-microbit-ampel` | `content/microbit-ampel/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "anleitung"`, LEDs auf dem Breadboard, Steckpläne als SVG) |
| `projekt-microbit-sterne` | `content/microbit-sterne/` | *(keine EN-Version)* | Projekt-Kurs „Fang den Stern“ (Markdown + JSON, `engine: "anleitung"`, Spiel auf der 5×5-Anzeige, ohne Zusatzteile, Bilder als SVG) |
| `projekt-microbit-einfuehrung` | `content/microbit-einfuehrung/` | *(keine EN-Version)* | Einführung „Erste Schritte“ (`engine: "anleitung"`, `unlisted`): jede Startseite eines micro:bit-Kurses (`language: "microbit"`) verweist Neue per Kasten hierher (`CourseDetail.vue`), die letzte Lektion verlinkt alle micro:bit-Kurse zurück |
| *(kein Kurs)* micro:bit-Spickzettel | `content/microbit-spickzettel/spickzettel.md` | *(keine EN-Version)* | Nachschlageseite `/microbit/spickzettel` (`MicrobitSpickzettel.vue`, rendert über `GuideLessonView`, keine Aufgaben, speichert nichts): ein `##`-Abschnitt je Begriff, jeder mit `:::bloecke`/`:::python`/`:::javascript`; Ziel der Begriffs-Links aller micro:bit-Kurse |
| *(kein Kurs)* micro:bit-Spickzettel | `content/microbit-spickzettel/spickzettel.md` | *(keine EN-Version)* | Nachschlageseite `/microbit/spickzettel` (`MicrobitSpickzettel.vue`, rendert über `GuideLessonView`, keine Aufgaben, speichert nichts): ein `##`-Abschnitt je Begriff, jeder mit `:::bloecke`/`:::python`/`:::javascript`; Ziel der Begriffs-Links aller micro:bit-Kurse |
| *(Lektions-Format)* Woche 1–12 (alle) | `content/python-woche{N}-{abenteuer\|pferde\|scifi}/` | `content/python-woche{N}-{thema}-en/` | Markdown + JSON, Pyodide; ersetzt die Notebook-Schritte Lektion/Debug/Missionen/Boss jeder Woche/Variante/Sprache (siehe HANDOFF.md 3.47–3.54). Die alten `1_lektion`/`2_debug`/`3_missionen`/`5_boss`-Zellenordner gibt es nicht mehr — nur `0_glossar` und `6_loesungen` bleiben als Notebooks (Nachschlagewerke, siehe unten). |
| `js-grundkurs` | `content/js-grundkurs/` (Beschreibung) + `content/js-grundkurs-woche{1-9}/` (Wochen) | *(keine EN-Version)* | Grundkurs (Markdown + JSON, `engine: "js-sandbox"`, eigene Mehrwochen-Struktur) |

Alle Projekt-Kurse (`type: "projekt"` in `kurse.json`) sind gesammelt und filterbar unter
**`/projekte`** (`src/views/ProjekteView.vue`) zu finden — nach Sprache, Level, Thema/Tags und
Dauer. Sie erscheinen bewusst *nicht* mehr in der normalen Kursliste auf der Startseite.

`projekt-js-spielewerkstatt` ist der erste Projekt-Kurs mit `engine: "js-sandbox"` statt Pyodide —
`ProjectCourse.vue` rendert je nach diesem Feld `LessonView.vue` (Python/Pyodide, Default) oder
`JsLessonView.vue` (JavaScript, eigene iframe-Sandbox). Details siehe Abschnitt 6.

`js-grundkurs` ist ein **Grundkurs** (nicht Projekt-Kurs, siehe `VISION.md`s Format-Definitionen),
9 Wochen, dieselbe `js-sandbox`-Engine wie `js-spielewerkstatt`, aber eine eigene Content-Struktur:
`content/js-grundkurs/beschreibung.md` liefert nur die Kursbeschreibung auf der Detailseite,
die eigentlichen Lektionen liegen in 9 unabhängigen Ordnern `content/js-grundkurs-woche{N}/`
(je ein eigenes `lessons.json`, Schema wie bei Projekt-Kursen). `CourseDetail.vue` hat dafür einen
eigenen, hart codierten Dispatch-Zweig (`isJsGrundkurs`, analog zu `isWeeklyCourse`/
`isPlacementCourse` — kein generisches `type`-Feld wie bei Projekt-Kursen, da es bisher nur diesen
einen Kurs seiner Art gibt), der `JsGrundkursTour.vue`/`JsCourseTour.vue`
(`src/components/`) rendert. Wochen sind frei wählbar (keine Freischaltung nach Abschluss der
Vorwoche), nur Lektionen innerhalb einer Woche sind sequenziell gesperrt. Details siehe
`KURSPLAN.md` "JavaScript-Track: Grundkurs" und `HANDOFF.md` 3.43.

Kurs-Metadaten (Titel, Beschreibung) → `public/kurse.json` (enthält `title`, `title_en`, `description`, `description_en`)

---

## 2. 12-Wochen-Kurs: Dateinamen-Schema

### Ordnerstruktur

Seit der Umstellung auf das **Zellen-Format** (Branch `12-wochen-kurs-zellen-format`) ist jedes
Notebook kein einzelnes `.ipynb` mehr, sondern ein gleichnamiger **Ordner** mit einer Datei pro
Zelle: `NN_markdown.py` (Markdown-Text als alleinstehendes String-Literal) bzw. `NN_code.py`
(Code unverändert), numeriert in Notebook-Reihenfolge.

```
content/python-12-wochen-grundkurs/          ← Deutsch
  woche-{1–12}/
    woche{N}.md                              ← Wochenbeschreibung (Lernziele etc.)
    abenteuer/
      woche{N}_abenteuer_{typ}/
        01_markdown.py, 02_code.py, …
        _generated/woche{N}_abenteuer_{typ}.ipynb.json   ← generiert, nicht committed
        _bundle/woche{N}_abenteuer_{typ}.py              ← generiert, nicht committed
    pferde/
      woche{N}_pferde_{typ}/…
    scifi/
      woche{N}_scifi_{typ}/…

content/python-12-wochen-grundkurs-en/       ← Englisch (gleiche Struktur)
  woche-{1–12}/
    woche{N}.md
    adventure/
      week{N}_adventure_{typ}/…
    horses/
      week{N}_horses_{typ}/…
    scifi/
      week{N}_scifi_{typ}/…
```

`_generated/` (notebook-förmige JSON fürs Browser-Rendering) und `_bundle/` (eine `.py`-Datei pro
Notebook, direkt mit `python3 datei.py` lauffähig — kein Jupyter/Pyodide nötig, ersetzt den alten
`.ipynb`-Download) werden bei jedem `npm run dev`/`npm run build` frisch aus den Zellen-Dateien
erzeugt (`scripts/build_cell_notebooks.py`) und sind gitignored — **nur die numerierten
`NN_*.py`-Dateien sind committete Quelle.**

### Varianten-Mapping DE → EN

| DE Ordner | EN Ordner | DE Notebook-Ordner | EN Notebook-Ordner |
|---|---|---|---|
| `abenteuer/` | `adventure/` | `woche{N}_abenteuer_{typ}/` | `week{N}_adventure_{typ}/` |
| `pferde/` | `horses/` | `woche{N}_pferde_{typ}/` | `week{N}_horses_{typ}/` |
| `scifi/` | `scifi/` | `woche{N}_scifi_{typ}/` | `week{N}_scifi_{typ}/` |

### Notebook-Typen (2 Ordner pro Woche/Variante — nur noch Nachschlagewerke)

Seit alle Wochen im Lektions-Format sind (HANDOFF.md 3.47–3.54), sind Lektion/Debug/Missionen/Boss
kein Notebook-Schritt mehr (siehe Abschnitt 1) — nur diese zwei Typen bleiben als Zellenordner:

| Kürzel | Inhalt |
|---|---|
| `0_glossar` | Begriffserklärungen für die Woche |
| `6_loesungen` | Musterlösungen zu den Aufgaben der Lektionen (eine Zelle je Aufgabe) |

**Ausnahme:** Cheat-Sheets (`wissens_cheat_sheet.ipynb`) und `gesamtglossar.ipynb` sind NICHT Teil
dieser Umstellung — eigene, unabhängige Pipeline (`scripts/md_to_cheatsheet_notebook.py`), bleiben
echte `.ipynb`-Dateien.

### Offline-Downloads (`public/wochen-zips/`, `projekt-zips/`, `ki-labor-zips/`)

Online läuft alles auf der Website (Pyodide). Offline gibt es für den 12-Wochen-Kurs, die
Python-Projekt-Kurse und das KI-Labor **drei Formate, je ein eigener Button**
(`src/components/OfflineDownloads.vue`, im 12-Wochen-Kurs zusätzlich im Seitenmenü):

| Format | ZIP-Endung | Inhalt | Generator |
|---|---|---|---|
| Jupyter-Notebooks | `-notebooks.zip` | Aufgaben- und Lösungs-Notebook getrennt (`_aufgaben`/`_loesungen`, EN `_tasks`/`_solutions`) | `build_lesson_notebook.py`, `build_project_notebook.py`, `build_kilabor_notebook.py` |
| Eine Python-Datei | `-komplett.zip` | eine mit `python3` lauffähige `.py` (12 Wochen: je Thema eine), Lösungen als Code | `build_lesson_bundle.py` (`build_bundle`), `build_offline_py.py` |
| Einzeldateien | `-einzeln.zip` | eine `.py` pro Lektion/Debug/Mission/Extra-Herausforderung (12 Wochen: plus `00_glossar.py`, ein Ordner je Thema) | `build_lesson_bundle.py` (`build_lesson_files`), `build_offline_py.py` |

Pfade: `wochen-zips/woche-{N}[-en]-{format}.zip` (Cheat-Sheets der Woche liegen in allen drei),
`projekt-zips/{contentPath}-{format}.zip` (nur Python-Projekte; neue Python-Projekte in
`PROJECT_COURSES` in `build_project_notebook.py` eintragen — ein Test prüft das gegen `kurse.json`),
`ki-labor-zips/woche-{N}-{format}.zip`; dazu das Gesamtpaket `python-12-wochen-notebooks.zip`.
Lösungsquellen: 12 Wochen aus den `*_6_loesungen`-Zellenordnern, Projekt-Kurse aus `task.solution`
(zeigt in der App auch den „Lösung anzeigen“-Button), KI-Labor aus `task.referenceSolution` — bewusst
ein anderer Feldname, damit im KI-Labor kein Lösungs-Button erscheint. Neue KI-Labor-Aufgabe ⇒
`referenceSolution` mitpflegen; `scripts/check_kilabor_solutions.py` (Test in
`lesson-notebook-generator.spec.js`) prüft, dass jede davon läuft und die erwartete Ausgabe liefert.
`scripts/pack_notebooks.py` packt alles und schreibt die Liste nach `public/offline-downloads.json`.
Nichts davon wird committed; es entsteht bei `npm run dev`/`npm run build` und vor jedem
Playwright-Lauf (`scripts/ensure-test-prereqs.mjs`) neu, wenn Quellen neuer sind.

---

## 3. Woche-für-Woche: Themen und Geschichten

> Wenn du eine Geschichte in einer Variante änderst, muss die **parallele Variante** der anderen Sprache ebenfalls angepasst werden.

### Woche 1 — Einführung und erstes Programm
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Reise beginnt | The journey begins! |
| Pferde | Der Reitbeginn | The riding begins! |
| Sci-Fi | Startsequenz | Launch sequence! |

### Woche 2 — Datentypen und Variablen
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die vier magischen Elemente | The Four Magic Elements |
| Pferde | Die vier Hufschlag-Typen | The Four Hoof-Beat Types |
| Sci-Fi | Die vier Quanten-Typen | The Four Quantum Types |

### Woche 3 — Bedingungen (if-else)
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Wege der Entscheidung | The Paths of Decision |
| Pferde | Die Weichen des Reitwegs | The Crossroads of the Riding Path |
| Sci-Fi | Die Pfade der Entscheidung | The Paths of Decision |

### Woche 4 — Schleifen (for, while)
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Der Kreislauf der Macht | The Cycle of Power |
| Pferde | Der Rhythmus des Reitens | The Rhythm of Riding |
| Sci-Fi | Der Zyklus der Zeit | The Cycle of Time |

### Woche 5 — Funktionen
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Zauberformeln der Macht | The Spell Formulas of Power |
| Pferde | Die Trainingsroutinen | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Systemprotokolle | *(EN-Titel aus Notebook)* |

### Woche 6 — Listen
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Schatzkammer der Sammlungen | *(EN-Titel aus Notebook)* |
| Pferde | Die Trainings-Sammlungen | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Daten-Bänke der Raumstation | *(EN-Titel aus Notebook)* |

### Woche 7 — Module und Bibliotheken
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die magischen Werkzeugkästen | *(EN-Titel aus Notebook)* |
| Pferde | Die Werkzeugkisten des Reiterhofs | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Modul-Banken der Raumstation | *(EN-Titel aus Notebook)* |

### Woche 8 — Dictionaries und Tupel
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Steckbriefe und Artefakte | *(EN-Titel aus Notebook)* |
| Pferde | Die Stall-Archive des Reiterhofs | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Daten-Archive der Raumstation | *(EN-Titel aus Notebook)* |

### Woche 9 — JSON-Dateien und I/O
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Schriftrollen der Daten | *(EN-Titel aus Notebook)* |
| Pferde | Die Stall-Archive des Reiterhofs | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Daten-Pipelines der Raumstation | *(EN-Titel aus Notebook)* |

### Woche 10 — OOP Grundlagen
| Variante | DE/EN Titel |
|---|---|
| Alle | Die magischen Blaupausen / The magical blueprints |

### Woche 11 — OOP Fortgeschritten
| Variante | DE/EN Titel |
|---|---|
| Alle | Die magische Evolution / The magical evolution |

### Woche 12 — Abschlussprojekt Text-Adventure
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die Drachenhöhle von Pyralia | *(EN-Titel aus Notebook)* |
| Pferde | Der Reiterhof bei Nacht | *(EN-Titel aus Notebook)* |
| Sci-Fi | Notfall auf Nebula-7 | *(EN-Titel aus Notebook)* |

---

## 4. Missionen & Zertifikate

Die Missionen (nur IDs, keine Punkte/Items) sind in zwei parallelen JSON-Dateien definiert:

| Sprache | Datei |
|---|---|
| Deutsch | `public/rewards-manifest.json` |
| Englisch | `public/rewards-manifest-en.json` |

Struktur: `{ "python-12-wochen-grundkurs": { "abenteuer"|"pferde"|"scifi": { "1"–"12": { missions: [id, ...], bossQuests: [id, ...] } } } }`

Ein **Zertifikat** für eine Woche/Variante wird verliehen, wenn (a) alle Missionen + Boss-Quests dieser Woche als erledigt markiert sind UND (b) der Wochen-Check (Quiz + Coding-Aufgabe im Check-Tab) bestanden ist. Es gibt kein Punkte-/Sammel-System mehr – Logik dazu in `src/composables/useFortschritt.js`, `useWeekChecks.js`, `useZertifikate.js`.

**Bei Änderungen an Missionen immer beide Dateien synchron halten.**

---

## 5. Interaktiver Einführungskurs: Varianten

```
content/python-grundlagen-interaktiv/              ← Original (nicht mehr direkt genutzt)
content/python-grundlagen-interaktiv-kinder/       ← DE, 8–12 Jahre
content/python-grundlagen-interaktiv-jugendliche/  ← DE, 13–17 Jahre
content/python-grundlagen-interaktiv-kinder-en/    ← EN, 8–12 Jahre
content/python-grundlagen-interaktiv-jugendliche-en/ ← EN, 13–17 Jahre
```

Jeder Ordner enthält dieselben Dateien:

| Datei | Inhalt |
|---|---|
| `lessons.json` | Reihenfolge, Aufgaben, Validierung, Code-Templates |
| `lektion-01.md` … `lektion-10.md` | Erklärungstext pro Lektion |
| `lektion-datentypen.md` | Sonderlektion Datentypen |
| `glossary.json` | Begriffe mit Erklärungen (Tooltip) |
| `beschreibung.md` | Kursübersichtstext |

**Unterschiede zwischen den Varianten:**

| Merkmal | Kinder | Jugendliche |
|---|---|---|
| Beispiele | Tiere, Spiele, Fantasie | Apps, Daten, Alltag |
| Code-Templates | `print("___")` (ausgefüllt) | leer |
| Aufgaben pro Lektion | 2 | 3 (letzte = Bonus) |
| Zusammenfassungen | begeistert, mit Emojis | sachlich |

**Lektionsreihenfolge** (in allen 3 Ordnern identisch):
`lektion-01` → `lektion-02` → `lektion-03` → `lektion-datentypen` → `lektion-04` → `lektion-05` → `lektion-06` → `lektion-07` → `lektion-08` → `lektion-09` → `lektion-10`

---

## 6. Was muss gleichzeitig geändert werden?

### Wenn du ein Notebook inhaltlich änderst (12-Wochen-Kurs, nur noch Glossar/Lösungen — `typ` ∈ `{0_glossar, 6_loesungen}`):
- [ ] DE: die einzelnen Zell-Dateien unter
      `content/python-12-wochen-grundkurs/woche-{N}/{variante}/woche{N}_{variante}_{typ}/NN_*.py`
- [ ] EN: `content/python-12-wochen-grundkurs-en/woche-{N}/{en_variante}/week{N}_{en_variante}_{typ}/NN_*.py`
- [ ] `_generated/`/`_bundle/` **nicht** von Hand anfassen — werden bei `npm run dev`/`npm run build`
      automatisch aus den `NN_*.py`-Dateien neu erzeugt (`scripts/build_cell_notebooks.py`)
- [ ] Änderst du `6_loesungen`, muss die Anzahl/Reihenfolge der Lösungs-Code-Zellen weiter zu den
      nicht-Beispiel-Aufgaben der zugehörigen `lessons.json` passen (`python-lektionen-format.spec.js`
      prüft das) — sonst weicht auch der ZIP-Download (`scripts/build_lesson_bundle.py`) ab.

### Wenn du eine Lektion/Mission/Boss-Etappe im Lektions-Format änderst (12-Wochen-Kurs, Woche 1–12):
- [ ] Vor dem Merge: `npm run testkind -- --geaendert` (KI-Test-Kind, nur die geänderten Lektionen; Stellen „hoch“ beheben, „mittel“ ansehen, danach erneut laufen lassen). Dazu `npm run check:verstaendlichkeit -- --wochen N --nur nie-gezeigt`.
- [ ] `content/python-woche{N}-{thema}[-en]/lessons.json` (Aufgaben/`codeTemplate`/`validation`) und
      die zugehörige `lektion-XX.md`/`debug-XX.md`/`mission-XX.md`/`boss-XX.md` (Erzähltext)
- [ ] Passende Referenzlösung in `..._6_loesungen` (siehe oben) nachziehen; neue Lösung als Zell-Paar mit
      der höchsten Nummer anlegen und `python3 scripts/sync_loesungen.py` laufen lassen (sortiert in
      Aufgaben-Reihenfolge, `--check` prüft nur)
- [ ] DE **und** EN (eigener `-en`-Ordner, kein gemeinsamer Content wie beim interaktiven Kurs)
- [ ] Kein Build-Schritt nötig — der ZIP-Download liest `lessons.json` und die Markdown-Dateien
      direkt (`scripts/build_lesson_bundle.py`, läuft bei `npm run dev`/`npm run build`)

### Wenn du einen neuen Kurs anlegst, in einem Grundkurs Wochen umbaust oder neue Begriffe einführst:
- [ ] `content/begriffe.json`: Projekt-Kurse, JS-Grundkurs, Python-12-Wochen-Kurs und KI-Labor
      verlinken Begriffe wie „Array“ oder „Schleife“ auf die Grundkurs-Woche, die sie erklärt
      (`useConcepts.js`, HANDOFF 3.108/3.110; in den Grundkursen selbst nur frühere Wochen). Verschiebt sich ein Thema in
      eine andere Woche (JS-Grundkurs, Python 12 Wochen), dort `woche`/`lektion` nachziehen. Neuer
      Begriff = neuer Eintrag mit allen Schreibweisen unter `formen` (Groß-/Kleinschreibung zählt).
- [ ] **Jeder neue Kurs bekommt Begriffs-Links oder eine bewusste Ausnahme** —
      `tests/begriffe.spec.js` schlägt sonst fehl. Projekt-Kurse: automatisch über `language`
      (`javascript`/`python`) in `kurse.json`. Kurs mit eigener Wochen-Tour: `concept-language`,
      `concept-course`, `concept-week` an `JsCourseTour.vue` geben (Vorlage `JsGrundkursTour.vue`)
      und die ID in `LINKED_COURSES` des Tests eintragen. Sonst die ID mit Grund in `WITHOUT_LINKS`.
- [ ] Neuer Grundkurs als Link-Ziel: Begriffe mit `kurs`/`woche` in `begriffe.json`, Kursname unter
      `kurse`, Wochen-Ordner in `WEEK_FOLDER` des Tests (prüft, dass `lektion` dort wirklich vorkommt).
- [ ] **micro:bit** (`language: "microbit"`, HANDOFF 3.131): Ein neuer micro:bit-Kurs bekommt die
      Links automatisch. Führt eine Lektion ein Konzept ein, das im Spickzettel fehlt: Abschnitt
      `## Name` mit allen drei Ansichten in `content/microbit-spickzettel/spickzettel.md`, Eintrag in
      der „Inhalt:“-Zeile und unter `microbit` in `begriffe.json` mit `anker` = Slug der Überschrift
      (`src/utils/slug.js`: ä → ae, Leerzeichen → `-`). Block-Namen, die auch normale Wörter sind
      („oder“, „wenn“), nur unter `fett` eintragen – die verlinken nur als ganzer Fettdruck. Danach
      im Kurs prüfen, ob ein Wort falsch verlinkt (in Ampel Stufe 3 wurde „Rot **und** Gelb“ zu „Und, oder“).
- [ ] **micro:bit** (`language: "microbit"`, HANDOFF 3.131): Ein neuer micro:bit-Kurs bekommt die
      Links automatisch. Führt eine Lektion ein Konzept ein, das im Spickzettel fehlt: Abschnitt
      `## Name` mit allen drei Ansichten in `content/microbit-spickzettel/spickzettel.md`, Eintrag in
      der „Inhalt:“-Zeile und unter `microbit` in `begriffe.json` mit `anker` = Slug der Überschrift
      (`src/utils/slug.js`: ä → ae, Leerzeichen → `-`). Block-Namen, die auch normale Wörter sind
      („oder“, „wenn“), nur unter `fett` eintragen – die verlinken nur als ganzer Fettdruck. Danach
      im Kurs prüfen, ob ein Wort falsch verlinkt (in Ampel Stufe 3 wurde „Rot **und** Gelb“ zu „Und, oder“).

### Wenn du einen Web-Kurs (HTML/CSS, `sandboxMode: "web"`) änderst oder anlegst:
- [ ] Aufgaben prüfen nur über `validation: { "type": "web", "checks": [...] }` (Felder siehe
      `validateWebChecks()` in `useTaskValidation.js`); jede Pflichtaufgabe braucht `solution` und
      jede Prüfung einen `hint` (Kinder sehen ihn ab dem zweiten Fehlversuch). Frei wählbare Werte
      (Farbe, Schrift) mit `notValue` gegen die Vorlage prüfen; Browser-Standard = `"initial"`.
- [ ] `tests/web-erste-website.spec.js` spielt jede Aufgabe durch: Vorlage muss durchfallen,
      Musterlösung bestehen. Bilder nur aus `public/web-bilder/` (Liste in `lektion-03.md` muss zu
      den Dateien passen, prüft derselbe Test).
- [ ] „Meine Seite“ (Stufe Einfach): Aufgaben mit `"meineSeite": true` starten mit der eigenen,
      gespeicherten Seite (`ue-hacker-meine-seite-<contentPath>`, nur lokal, verfällt nicht) statt mit
      `codeTemplate`. Lektion 1 legt sie an, Lektion 2–7 haben je eine letzte Aufgabe „Deine Seite“,
      Lektion 8 macht sie fertig. `codeTemplate` ist dann nur der Ersatz für Kinder ohne gespeicherte
      Seite (allgemeine Seite auf dem Stand der Vorlektion) und muss trotzdem durchfallen.
- [ ] Stufe Intensiv: je Woche `content/web-grundkurs-woche{N}/` (Abschnitte `lektion`/`debug`/`mission`) und
      `content/web-grundkurs-checks/week-N.json`; Lernziele fürs PDF stehen in `src/data/webGrundkursWeeks.js`
      (nur Stoff dieser Woche). `tests/web-grundkurs.spec.js` prüft jede vorhandene Woche automatisch.
      HTML-Begriffe in `content/begriffe.json` (`html`, Ziel über `pfade`) zeigen auf die Intensiv-Woche.
- [ ] Abschluss-Check: `content/<contentPath>-checks/` (`config.json`, `week-1.json` mit
      `questions`, 2 `codingChallenges` mit `solution`, `lernziele` fürs Zertifikat-PDF). Kurs in
      `COURSE_INFO` (`useCourseCertificates.js`, `singleCheck: true`), `"finalCheck": true` in
      `kurse.json`. Neue Frage = neue `id` (Fortschritts-Vertrag).

### Wenn du Missionen änderst:
- [ ] `public/rewards-manifest.json`
- [ ] `public/rewards-manifest-en.json`

### Wenn du die Wochen-Check-Fragen oder die Coding-Aufgabe änderst:
- [ ] `content/python-checks/week-{N}.json` (Feld `questions` bzw. `codingChallenges` je Woche, DE+EN
      in denselben Einträgen). Allgemeine Config (`passThreshold`, `placementPerWeek`, `projects`, …)
      steht separat in `content/python-checks/config.json`. Seit dem `weeks-json-splitten`-Refactor
      **eine Datei pro Woche** statt einer gemeinsamen `weeks.json` — beim Zusammenführen zur Laufzeit
      siehe `useWeekChecks.js` (Browser/Vite) bzw. `content/python-checks/index.mjs` (Tests/Node).
      `codingChallenges[].validation` kann neben `type`/`expected` (Ausgabe-Prüfung) optional ein
      `variables`-Feld haben (`{name: erwarteterWert}`) — prüft zusätzlich echte Variablenwerte im
      Python-Namespace nach der Ausführung, damit eine Aufgabe nicht durch bloßes Ausgeben des
      erwarteten Texts ohne die geforderten Variablen umgangen werden kann. Nur für Aufgaben nötig,
      bei denen das Anlegen bestimmter Variablen selbst Teil der Aufgabe ist. `variables` unterstützt
      auch verschachtelte Werte (z.B. `{"person": {"name": "Alex"}}"` für ein Dictionary).
      Für Funktionsaufgaben gibt es analog ein optionales `functionCalls`-Feld
      (`[{name, args, expected}, …]`) — ruft die geforderte Funktion nach der Ausführung mit einem
      in der Aufgabenstellung nie genannten Eingabewert erneut auf und prüft das Ergebnis. Deckt
      auch auf, wenn eine Funktion nur zufällig für das eine vorgerechnete Beispiel stimmt.

### Wenn du Kurs-Metadaten (Titel, Beschreibung) änderst:
- [ ] `public/kurse.json` (Felder `title`, `title_en`, `description`, `description_en`)
- [ ] `content/{kurs-id}/beschreibung.md`
- [ ] `content/{kurs-id}-en/beschreibung.md` (falls EN-Version existiert)

### Wenn ein Kurs im Unterricht erprobt ist (Beta entfernen) oder neu dazukommt:
- [ ] `"beta": true` in `public/kurse.json` entfernen bzw. bei neuen Kursen setzen; die Liste
      `NICHT_BETA` in `tests/kurse-beta.spec.js` mitziehen. Beta zeigt `BetaBadge.vue` auf Startseite,
      Projekte-Karte und Kursseite (dort mit Erklärung). Welche Kurse unverlinkt oder Beta sind,
      zeigt das Admin-Menü im Reiter „Kurse“.

### Wenn du eine Lektion im interaktiven Kurs änderst:
- [ ] `lektion-XX.md` in **allen fünf** Ordnern anpassen (oder bewusst nur bestimmte Varianten)
- [ ] `lessons.json` im jeweiligen Ordner (Aufgaben, Validierung, Templates)

Ordner-Mapping (immer paarweise anpassen):
| DE | EN |
|---|---|
| `python-grundlagen-interaktiv-kinder/` | `python-grundlagen-interaktiv-kinder-en/` |
| `python-grundlagen-interaktiv-jugendliche/` | `python-grundlagen-interaktiv-jugendliche-en/` |

### Wenn du eine neue Woche hinzufügst (12-Wochen-Kurs):
- [ ] 18 DE-Notebooks (3 Varianten × 6 Typen)
- [ ] 18 EN-Notebooks
- [ ] `woche{N}.md` (DE) + `woche{N}.md` (EN)
- [ ] Einträge in `rewards-manifest.json` + `rewards-manifest-en.json`
- [ ] Ggf. Download-ZIP neu generieren (`npm run build:cells && npm run pack:notebooks`)

### Python-Lektions-Format (`content/python-woche{N}-{thema}[-en]/lessons.json`): Prüf-Felder
- [ ] `validation.expected` — Teilstring der Ausgabe (Pflicht, `output_contains`). Fordert die Aufgabe
      mehrere Zeilen (Überschrift + Ergebnis, zwei Werte), eine **Liste**: jeder Eintrag muss vorkommen,
      der Hinweis ab dem zweiten Fehlversuch nennt den ersten fehlenden. Frei wählbare Teile nur mit
      ihrem festen Anfang aufnehmen (`"Autor: "`).
- [ ] `validation.varies: true` (Zufalls-Aufgaben) — Prüfen führt den Code bis zu 6-mal aus; mindestens
      eine Ausgabe muss sich unterscheiden, jede muss `expected` erfüllen. Die Aufgabe muss deshalb den
      gezogenen Wert mit ausgeben („Gib zum Schluss die Liste wuerfe aus.“); die Wahrscheinlichkeit, dass
      eine richtige Lösung 6-mal dasselbe zieht, klein halten (nicht nur eine Münze werfen).
- [ ] `validation.codeContains` (optional, Array) — wird in Lektionen **nicht** ausgewertet (Lektionen
      prüfen nur die Ausgabe, Test „for-Aufgabe … auch hart codiert“); steht nur noch als Beschreibung der
      erwarteten Bausteine da. Nie bei Beispielen, und nie ein Baustein, der schon im `codeTemplate` steht
      (Test in `python-lektionen-format.spec.js`).
- [ ] `validation.stdin` (optional, Array aus Texten) — Antworten für `input()` beim **Prüfen** (kein
      Eingabefenster, Ausgabe deterministisch); **Ausführen** öffnet weiter das Eingabefenster. In der
      Aufgabe nennen, was automatisch eingegeben wird, und `expected` darauf stützen.

### Wenn du einen Projekt-Kurs hinzufügst (wie Cäsar-Chiffre, Morsecode, Zahlen-Detektiv, Häufigkeitsanalyse):
- [ ] Neuer Ordner `content/{contentPath}/`: `beschreibung.md`, `lektion-01.md`…`lektion-NN.md`,
      `lessons.json` (Schema wie beim interaktiven Kurs: `id`/`title`/`file`/`lessonSummary`/
      `tasks[{instruction, codeTemplate, isBonus?, validation}]`) — kein `glossary.json` nötig,
      ist optional.
- [ ] Neuer Eintrag in `public/kurse.json` mit **Pflichtfeldern**: `id` (Präfix `projekt-`),
      `type: "projekt"`, `contentPath`, `title`/`title_en`, `description`/`description_en`, sowie
      den Filter-Metadaten `language` (`"python"`/`"javascript"`, Slug — steuert den Sprach-Filter
      und schaltet die Begriffs-Links auf den passenden Grundkurs ein, keine Übersetzung nötig), `level` (`"einsteiger"`/`"fortgeschritten"`) und `tags` (Array aus
      einem festen Vokabular, aktuell: `kryptografie`, `knobelaufgabe`, `kommunikation`,
      `logikraetsel`, `mathematik`, `spiele`, `robotik`). Ein neuer Tag braucht neue `projectTag.<slug>`-Keys in
      **beiden** `src/locales/de.js`/`en.js` — sonst zeigt die Filter-Chip/Karte nur den rohen Slug.
      Kein manuelles Dauer-/Lektionsanzahl-Feld nötig, `ProjekteView.vue` berechnet das live aus der
      Länge von `lessons.json`.
- [ ] **Python-Projekt:** Ordner in `PROJECT_COURSES` (`scripts/build_project_notebook.py`) eintragen
      (Offline-Downloads) und den Zähler „N Projekt-Kurse“ in `tests/lesson-notebook-generator.spec.js`
      erhöhen. Jede Aufgabe braucht ein `solution`-Feld (Lösungs-Button + Offline-Lösungen).
- [ ] Begriffs-Links prüfen: Erscheinen im Lektionstext Links und am Ende der Kasten „Neu oder
      unklar?“? Fehlt ein Begriff, der im Projekt wichtig ist und in einem Grundkurs erklärt wird,
      in `content/begriffe.json` ergänzen (siehe oben).
- [ ] Tests/Tooling: Kartenzahlen und Filter-Erwartungen in `tests/projekte.spec.js`, Regel in
      `scripts/test-changed.mjs`, Ordner in den `lint:spelling`-Globs (`package.json`),
      `npm run contract:update`.
- [ ] **Kein** Eintrag in `rewards-manifest*.json` nötig — Projekt-Kurse sind vom Zertifikats-/
      Punktesystem ausgenommen (wie der 12-Wochen-Kurs es hat, siehe Abschnitt 4).
- [ ] **Kein** manueller Eintrag für das Abschluss-Abzeichen im Profil (`/profil`) nötig —
      `useProjectBadges.js` nutzt dasselbe Wildcard-Glob wie `ProjekteView.vue` und erkennt jeden
      Kurs mit `type: "projekt"` automatisch. Das Abzeichen gilt als verdient, sobald alle
      Lektionen laut `useInteractiveProgress` abgeschlossen sind — kein separater Mechanismus.
- [ ] DE-first ist ok (kein `-en`-Content-Ordner nötig) — `useCourseData.js`s `hasEnDescription`
      muss dann NICHT erweitert werden, die Beschreibung fällt automatisch auf Deutsch zurück.
- [ ] `src/router/index.js`, `src/composables/useLessonContent.js` (Wildcard-Glob) und
      `src/views/Home.vue` (Projekt-Kurse werden dort generisch über `type === 'projekt'`
      ausgefiltert) brauchen **keine** Änderung mehr für einen weiteren Projekt-Kurs — nur
      Content-Ordner + `kurse.json`-Eintrag.

**Für einen JavaScript-Projekt-Kurs (wie `js-spielewerkstatt`) statt Python/Pyodide:**
- [ ] `kurse.json`-Eintrag bekommt zusätzlich `"engine": "js-sandbox"` (fehlt das Feld, ist
      `"pyodide"` der Default — bestehende Python-Projekte brauchen keine Änderung).
      `ProjectCourse.vue` rendert dann `JsLessonView.vue`/`JsSandboxFrame.vue` statt
      `LessonView.vue`. Kein `.btn-kernel`-Init-Schritt nötig — jeder Lauf startet ein frisches,
      isoliertes iframe (`sandbox="allow-scripts"`, keine `allow-same-origin`), Reset ist der
      Normalfall (siehe `src/composables/useJsSandbox.js`).
- [ ] `lessons.json`-Aufgaben können zusätzlich zu `variables`/`functionCalls`
      (siehe unten) zwei JS-spezifische `validation.type`-Werte nutzen: `canvas_not_blank`
      (irgendein gezeichneter Pixel auf dem festen Spielfeld-Canvas, ID `spielfeld`) und
      `canvas_changed` (Pixel unterscheiden sich vor/nach `ms` Millisekunden — beweist eine
      wirklich laufende `requestAnimationFrame`-Schleife, nicht nur ein einzelnes Standbild).
      Fehlt `validation.expected`, wird die Ausgabe-Prüfung übersprungen (für reine Canvas-/
      Funktions-Aufgaben ohne geforderte `console.log`-Ausgabe).
- [ ] Projekt ohne Canvas (wie `js-memory`): zusätzlich `"sandboxMode": "dom"` in `kurse.json`.
      Die Sandbox zeigt dann die DOM-Übungsfläche aus `js-grundkurs` Woche 7 (`#dom-uebung` mit
      `#ueberschrift`, `#text`, `#knopf`, `#anzeige`); eigene Elemente hängt der Code per
      `createElement`/`appendChild` an. Prüfung über `dom_text` (`target`, `text`) und
      `dom_click_text` (`click`, `target`, `text`, optional `clicks`). `click` ist eine ID oder
      eine Liste von IDs, die der Reihe nach angeklickt werden. Gelesen wird sofort nach dem
      letzten Klick — ein `setTimeout` im Aufgaben-Code ist dann noch nicht gelaufen.
- [ ] Jede Aufgabe braucht eine echte `validation` — es gibt bewusst **keinen** Selbsteinschätzungs-
      Button ("Ich hab's ausprobiert") mehr, jede Aufgabe (auch Demo-Beispiele mit bereits fertigem
      `codeTemplate`) wird über Ausführen + Prüfen automatisch geprüft. Ein Demo-Beispiel bekommt
      dafür eine `validation`, die zum unveränderten `codeTemplate` passt (z.B. `canvas_not_blank`
      bei einem bereits zeichnenden Beispiel) — die Prüfung besteht dann sofort beim ersten Klick.
- [ ] Jede Aufgabe muss eigenständig lauffähig sein — jeder Lauf (Ausführen/Prüfen) baut das
      iframe komplett neu auf, es gibt **keinen** geteilten Namespace zwischen Aufgaben (anders
      als beim Pyodide-Kernel, der über eine ganze Lektion hinweg erhalten bleibt).
- [ ] **DOM- statt Canvas-Projekt (wie `js-quiz`):** `kurse.json`-Eintrag bekommt zusätzlich
      `"sandboxMode": "dom"`. `CourseDetail.vue` → `ProjectCourse.vue` (`domMode`) → `JsLessonView.vue`
      zeigen dann die feste Übungsfläche aus dem JS-Grundkurs Woche 7 (`#dom-uebung` mit
      `#ueberschrift`, `#text`, `#knopf`, `#anzeige`) statt des Canvas. Geprüft wird mit `dom_text`
      (`target`, `text`) und `dom_click_text` (`click`, `target`, `text`, optional `clicks`).
      Weitere Elemente erzeugt der Code der Lernenden selbst (`createElement`) — sie brauchen eine
      feste ID aus der Aufgabenstellung, sonst kann die Prüfung sie nicht finden. Reine
      `console.log`-Aufgaben bekommen `"showCanvas": false`. Test: `tests/js-quiz.spec.js`.

**Für einen Hardware-Kurs zum Abhaken (wie `microbit-auto` und `microbit-ampel`):**
- [ ] Vor dem Merge: `npm run testkind -- --geaendert` (prüft geänderte Stufen mit Blöcken; einmal auch `--kurs <ordner> --variante python`). Neue MakeCode-Bedienhinweise im echten Editor nachklicken.
- [ ] `kurse.json`-Eintrag bekommt `"engine": "anleitung"`. `ProjectCourse.vue` rendert dann
      `GuideLessonView.vue`: kein Kernel, kein Editor. Der Code läuft auf dem echten Gerät, die
      Plattform kann ihn nicht prüfen.
- [ ] Optional `"unlisted": true` in `kurse.json` (geht bei jedem Projekt-Kurs): Der Kurs ist live und
      über `/kurs/<id>` erreichbar, fehlt aber in `/projekte` und bei den Profil-Abzeichen (dort erst
      sichtbar, sobald man ihn begonnen hat). Zum Veröffentlichen das Feld entfernen und die
      Karten-Anzahl in `tests/projekte.spec.js` sowie die Tests in `tests/microbit-auto.spec.js` und
      `tests/auth-ui.spec.js` (Profil-Abzeichen, läuft nur mit `npm run test:auth`) anpassen.
- [ ] `lessons.json`-Aufgaben haben nur `instruction` (und optional `isBonus`) — **bewusste Ausnahme**
      von „jede Aufgabe braucht ein `expected`“: Das Team hakt selbst ab. Sind alle Pflichtaufgaben
      abgehakt, gilt die Lektion als abgeschlossen (`useInteractiveProgress`, wie bei allen
      Projekt-Kursen). Einzelne Haken werden im selben Fortschritts-Eintrag gespeichert (`partialChecks`); ohne Account verfallen sie nach einem Tag. Jede Lektion braucht mindestens eine
      Pflichtaufgabe.
- [ ] Markdown: Abschnitte, die nur für einen Weg gelten, stehen zwischen `:::bloecke` bzw.
      `:::python` und `:::` (jede Markierung als eigener Absatz mit Leerzeile davor und danach).
      Jeder Code steht in so einem Abschnitt, und jede Lektion hat gleich viele Blöcke- wie
      Python-Abschnitte. Optional `:::javascript` (MakeCode-JavaScript, bisher nur die Ampelanlage):
      Hat ein Kurs das, braucht jede Lektion ebenso viele JavaScript-Abschnitte; der Umschalter zeigt
      nur die Ansichten, die eine Lektion hat. Diese und die folgenden Regeln prüft `expectGuideContent()` aus
      `tests/helpers/guide-content.js`; jeder neue Anleitungs-Kurs ruft sie in seinem Spec auf.
- [ ] Jede Bonusaufgabe (`isBonus`) hat am Ende der Lektion einen Abschnitt `## Bonus: <Titel>` mit
      klarer Aufgabenstellung. Tipps stehen darunter eingeklappt in `<details><summary>Tipps
      anzeigen</summary>` … `</details>` (Leerzeile nach `<summary>`-Zeile und vor `</details>`,
      sonst wird das Markdown darin nicht gerendert). Tipps nennen neue Bausteine und Denkschritte,
      zeigen aber nie die fertige Lösung.
- [ ] Vorgegebener Code darf die Aufgabe nicht komplett lösen, wenn das Team selbst etwas
      herausfinden soll: nur das Gerüst zeigen (z.B. den ersten Fall), das fertige Programm
      eingeklappt in `<details><summary>Lösung anzeigen</summary>` darunter (Beispiel: Stufe 9,
      `lektion-10.md`). Eine letzte Stufe mit frei wählbaren Aufträgen braucht keine Bonusaufgabe.
- [ ] Kurse mit `engine: "anleitung"` zeigen in der Seitenleiste die `PartnerBox`: Eine zweite Person
      kann sich mit ihrem Account eintragen, dann landet der Stand des Kurses (abgeschlossene
      Stufen und einzelne Haken) in beiden Accounts und beide bekommen das Abzeichen. Tests dazu
      laufen nur mit `npm run test:auth`.
- [ ] Haken sind umkehrbar: Wird in einer abgeschlossenen Stufe ein Pflicht-Haken entfernt, gilt
      sie nicht mehr als abgeschlossen und die nächste ist wieder gesperrt.
- [ ] MakeCode-Blöcke als Text: Codeblock mit Sprache `bloecke`, pro Zeile `[kategorie] Beschriftung`,
      zwei Leerzeichen Einrückung je Ebene. Kategorien (= Farben, siehe `GuideLessonView.vue`):
      `grundlagen`, `eingabe`, `schleifen`, `logik`, `variablen`, `mathematik`, `funktionen`, `musik`,
      `minicar`, `pins`, `funk`, `led`. Neue Kategorie → dort eine `.mc-<name>`-Farbe ergänzen. Deutsche
      Block-Beschriftungen stehen in den offiziellen Übersetzungen:
      `https://makecode.microbit.org/api/translations?lang=de&filename=microbit%2Fcore-strings.json&approved=true`
      (für Funk `radio-strings.json`), Schlüssel mit `|block`.
- [ ] Bilder als `<img src="/microbit/..." alt="...">` aus `public/microbit/` (passen sich der Spaltenbreite
      an). Die Steckpläne der Ampel erzeugt `python3 scripts/build_ampel_steckplaene.py` nach
      `public/microbit/ampel/`, die Bilder von Einführung und „Fang den Stern“
      `python3 scripts/build_microbit_bilder.py` nach `public/microbit/einfuehrung/` (auch die Hilfe
      beim Verbinden, die jeder Kurs zeigen darf) und `public/microbit/sterne/`; dort ändern und neu
      erzeugen, nie die SVGs von Hand bearbeiten.
      Pinbelegung der Ampel (HANDOFF 3.119): Auto Rot/Gelb/Grün = P16/P15/P14, Fußgänger Rot/Grün =
      P13/P12, Taster P20.
- [ ] Python-Beispiele einmal mit `python3` auf Syntax prüfen (`compile()`); ausführen lassen sie
      sich nur auf dem micro:bit. Die Bibliothek für das Auto liegt unter
      `public/microbit/keyes_MiniCar.py` (Keyestudio-Original mit einer Zeile Korrektur, siehe Dateikopf).
- [ ] Neuer micro:bit-Kurs: in die Link-Liste am Ende von `content/microbit-einfuehrung/lektion-03.md`
      aufnehmen (`tests/microbit-einfuehrung.spec.js` prüft das); der Einführungs-Kasten erscheint von selbst.
- [ ] Neuer Ordner → Rechtschreib-Globs in `package.json` (`lint:spelling`) und Regel in
      `scripts/test-changed.mjs` ergänzen.

---

## 7. Wo stehen welche Dinge im Code?

| Was | Datei |
|---|---|
| Sprache umschalten (DE/EN) | `src/composables/useLanguage.js` |
| UI-Texte DE | `src/locales/de.js` |
| UI-Texte EN | `src/locales/en.js` |
| Wochendaten laden | `src/composables/useWeeklyContent.js` |
| Kursmetadaten laden | `src/composables/useCourseData.js` |
| Interaktiver Kurs – Fortschritt | `src/composables/useInteractiveProgress.js` |
| Interaktiver Kurs – UI + Variantenwahl | `src/components/InteractiveCourse.vue` |
| Interaktiver Kurs – Lektion anzeigen | `src/components/LessonView.vue` |
| Kursdetailseite | `src/views/CourseDetail.vue` |
| Projekt-Kurs – UI + Lektions-Fortschritt | `src/components/ProjectCourse.vue` |
| Projekte-Übersicht + Filter (Sprache/Level/Tags/Dauer) | `src/views/ProjekteView.vue` |
| JS-Projekt-Kurs – Lektion anzeigen (Pendant zu `LessonView.vue`) | `src/components/JsLessonView.vue` |
| JS-Sandbox – iframe + RPC-Protokoll (Ausführen/Prüfen/Canvas) | `src/composables/useJsSandbox.js`, `src/components/JsSandboxFrame.vue` |
| JS-Code-Editor mit IntelliSense/Tab (CodeMirror) | `src/components/JsCodeCell.vue` |
| JS-Grundkurs – Wochenauswahl + Wochen-Stepper | `src/components/JsGrundkursTour.vue`, `src/components/JsCourseTour.vue` |
| Fortschritts-Widget (12-Wochen) | `src/components/FortschrittWidget.vue` |
| Missionen-Panel | `src/components/MissionenPanel.vue` |
| Profilseite (Login-gated) + Projekt-Abschluss-Abzeichen | `src/views/ProfilView.vue`, `src/composables/useProjectBadges.js` |
