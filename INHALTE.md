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

Kurs-Metadaten (Titel, Beschreibung) → `public/kurse.json` (enthält `title`, `title_en`, `description`, `description_en`)

---

## 2. 12-Wochen-Kurs: Dateinamen-Schema

### Ordnerstruktur

```
content/python-12-wochen-grundkurs/          ← Deutsch
  woche-{1–12}/
    woche{N}.md                              ← Wochenbeschreibung (Lernziele etc.)
    abenteuer/
      woche{N}_abenteuer_{typ}.ipynb
    pferde/
      woche{N}_pferde_{typ}.ipynb
    scifi/
      woche{N}_scifi_{typ}.ipynb

content/python-12-wochen-grundkurs-en/       ← Englisch (gleiche Struktur)
  woche-{1–12}/
    woche{N}.md
    adventure/
      week{N}_adventure_{typ}.ipynb
    horses/
      week{N}_horses_{typ}.ipynb
    scifi/
      week{N}_scifi_{typ}.ipynb
```

### Varianten-Mapping DE → EN

| DE Ordner | EN Ordner | DE Dateiname | EN Dateiname |
|---|---|---|---|
| `abenteuer/` | `adventure/` | `woche{N}_abenteuer_{typ}.ipynb` | `week{N}_adventure_{typ}.ipynb` |
| `pferde/` | `horses/` | `woche{N}_pferde_{typ}.ipynb` | `week{N}_horses_{typ}.ipynb` |
| `scifi/` | `scifi/` | `woche{N}_scifi_{typ}.ipynb` | `week{N}_scifi_{typ}.ipynb` |

### Notebook-Typen (6 Dateien pro Woche/Variante)

| Kürzel | Inhalt |
|---|---|
| `0_glossar` | Begriffserklärungen für die Woche |
| `1_lektion` | Hauptlektion mit Erklärungen und Beispielen |
| `2_debug` | Fehlersuche-Aufgaben |
| `3_missionen` | Hauptaufgaben der Woche |
| `5_boss` | Boss-Quest (Abschlussaufgabe) |
| `6_loesungen` | Musterlösungen |

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

## 4. Belohnungen / Rewards

Die Missionen und ihre Punkte sind in zwei parallelen JSON-Dateien definiert:

| Sprache | Datei |
|---|---|
| Deutsch | `public/rewards-manifest.json` |
| Englisch | `public/rewards-manifest-en.json` |

Struktur: `{ "python-12-wochen-grundkurs": { "abenteuer"|"pferde"|"scifi": { "1"–"12": { missions, bossQuests } } } }`

**Bei Änderungen an Missionen / Punkten immer beide Dateien synchron halten.**

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
- [ ] DE: `content/python-12-wochen-grundkurs/woche-{N}/{variante}/woche{N}_{variante}_{typ}.ipynb`
- [ ] EN: `content/python-12-wochen-grundkurs-en/woche-{N}/{en_variante}/week{N}_{en_variante}_{typ}.ipynb`

### Wenn du Missionen/Punkte änderst:
- [ ] `public/rewards-manifest.json`
- [ ] `public/rewards-manifest-en.json`

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
- [ ] Ggf. Download-ZIP neu generieren (`npm run pack:notebooks`)

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
| Fortschritts-Widget (12-Wochen) | `src/components/FortschrittWidget.vue` |
| Missionen-Panel | `src/components/MissionenPanel.vue` |
