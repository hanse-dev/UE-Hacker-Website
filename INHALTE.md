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
| `projekt-morsecode` | `content/morsecode/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-zahlendetektiv` | `content/zahlendetektiv/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON) |
| `projekt-js-spielewerkstatt` | `content/js-spielewerkstatt/` | *(keine EN-Version)* | Projekt-Kurs (Markdown + JSON, `engine: "js-sandbox"`) |
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

### Notebook-Typen (6 Ordner pro Woche/Variante)

| Kürzel | Inhalt |
|---|---|
| `0_glossar` | Begriffserklärungen für die Woche |
| `1_lektion` | Hauptlektion mit Erklärungen und Beispielen |
| `2_debug` | Fehlersuche-Aufgaben |
| `3_missionen` | Hauptaufgaben der Woche |
| `5_boss` | Boss-Quest (Abschlussaufgabe) |
| `6_loesungen` | Musterlösungen |

**Ausnahme:** Cheat-Sheets (`wissens_cheat_sheet.ipynb`) und `gesamtglossar.ipynb` sind NICHT Teil
dieser Umstellung — eigene, unabhängige Pipeline (`scripts/md_to_cheatsheet_notebook.py`), bleiben
echte `.ipynb`-Dateien.

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

### Woche 12 — Turtle Graphics
| Variante | DE Titel | EN Titel |
|---|---|---|
| Abenteuer | Die magische Leinwand | *(EN-Titel aus Notebook)* |
| Pferde | Das Turnier-Visualisierung | *(EN-Titel aus Notebook)* |
| Sci-Fi | Die Hologramm-Projektoren | *(EN-Titel aus Notebook)* |

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

### Wenn du ein Notebook inhaltlich änderst (12-Wochen-Kurs):
- [ ] DE: die einzelnen Zell-Dateien unter
      `content/python-12-wochen-grundkurs/woche-{N}/{variante}/woche{N}_{variante}_{typ}/NN_*.py`
- [ ] EN: `content/python-12-wochen-grundkurs-en/woche-{N}/{en_variante}/week{N}_{en_variante}_{typ}/NN_*.py`
- [ ] `_generated/`/`_bundle/` **nicht** von Hand anfassen — werden bei `npm run dev`/`npm run build`
      automatisch aus den `NN_*.py`-Dateien neu erzeugt (`scripts/build_cell_notebooks.py`)

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

### Wenn du einen Projekt-Kurs hinzufügst (wie Cäsar-Chiffre, Morsecode, Zahlen-Detektiv):
- [ ] Neuer Ordner `content/{contentPath}/`: `beschreibung.md`, `lektion-01.md`…`lektion-NN.md`,
      `lessons.json` (Schema wie beim interaktiven Kurs: `id`/`title`/`file`/`lessonSummary`/
      `tasks[{instruction, codeTemplate, isBonus?, validation}]`) — kein `glossary.json` nötig,
      ist optional.
- [ ] Neuer Eintrag in `public/kurse.json` mit **Pflichtfeldern**: `id` (Präfix `projekt-`),
      `type: "projekt"`, `contentPath`, `title`/`title_en`, `description`/`description_en`, sowie
      den Filter-Metadaten `language` (`"python"`/`"javascript"`, Slug — steuert nur die Anzeige,
      keine Übersetzung nötig), `level` (`"einsteiger"`/`"fortgeschritten"`) und `tags` (Array aus
      einem festen Vokabular, aktuell: `kryptografie`, `knobelaufgabe`, `kommunikation`,
      `logikraetsel`, `mathematik`). Ein neuer Tag braucht neue `projectTag.<slug>`-Keys in
      **beiden** `src/locales/de.js`/`en.js` — sonst zeigt die Filter-Chip/Karte nur den rohen Slug.
      Kein manuelles Dauer-/Lektionsanzahl-Feld nötig, `ProjekteView.vue` berechnet das live aus der
      Länge von `lessons.json`.
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
- [ ] Jede Aufgabe braucht eine echte `validation` — es gibt bewusst **keinen** Selbsteinschätzungs-
      Button ("Ich hab's ausprobiert") mehr, jede Aufgabe (auch Demo-Beispiele mit bereits fertigem
      `codeTemplate`) wird über Ausführen + Prüfen automatisch geprüft. Ein Demo-Beispiel bekommt
      dafür eine `validation`, die zum unveränderten `codeTemplate` passt (z.B. `canvas_not_blank`
      bei einem bereits zeichnenden Beispiel) — die Prüfung besteht dann sofort beim ersten Klick.
- [ ] Jede Aufgabe muss eigenständig lauffähig sein — jeder Lauf (Ausführen/Prüfen) baut das
      iframe komplett neu auf, es gibt **keinen** geteilten Namespace zwischen Aufgaben (anders
      als beim Pyodide-Kernel, der über eine ganze Lektion hinweg erhalten bleibt).

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
