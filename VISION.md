# VISION.md — Mission & langfristiger Kursplan

Dieses Dokument hält die Gesamt-Vision fest: warum es diese Plattform gibt, wie Kurse
grundsätzlich aufgebaut sind, und welche Themen langfristig dazukommen sollen. Es ändert sich
selten — für die konkreten Lehrpläne einzelner Kurse siehe `KURSPLAN.md`, für die kurzfristige
Umsetzung (nächster Branch, offene Punkte) siehe `todo.md`.

---

## Mission

Kinder und Jugendliche lernen echtes Programmieren — nicht nur Syntax, sondern das Gefühl,
etwas Eigenes gebaut zu haben (ein Spiel, eine verschlüsselte Nachricht, eine eigene Website).
Themen-Varianten (Abenteuer/Pferde/Sci-Fi) und Projekt-Kurse sorgen dafür, dass dranbleiben
Spaß macht statt Pflicht zu sein.

---

## Kurs-Formate

Jedes Thema/jede Sprache kann eines oder mehrere dieser Formate bekommen — nicht jedes Format
ist für jedes Thema nötig.

| Format | Umfang | Merkmale | Beispiel |
|---|---|---|---|
| **Einstieg** | wenige Lektionen | niedrigschwellig, kein Vorwissen im eigenen Track nötig | `python-grundlagen-interaktiv` |
| **Grundkurs** | mehrwöchig | Themen-Varianten, Quiz + Coding-Check, Wochen-Zertifikate | `python-12-wochen-grundkurs` |
| **Projekt-Kurs** | 5–8 Lektionen | ein greifbares Ergebnis, kein Zertifikat, niedrige Einstiegshürde — hält zwischen den großen Kursen bei der Stange | `projekt-caesar-chiffre` |
| **Vertiefung/Advanced** | mehrwöchig | Voraussetzung: Grundkurs/Projekt-Kurse **derselben** Sprache | (noch keiner umgesetzt) |

---

## Wichtigstes Prinzip: modulare Abhängigkeiten

**Eine Voraussetzung gilt nur innerhalb ihrer eigenen Sprache/ihres eigenen Themas.** Ein Kurs
verlangt eine andere Sprache nur, wenn er sie inhaltlich tatsächlich braucht — nie nur, weil er
"fortgeschritten" ist. Legitime Cross-Track-Abhängigkeit: der KI-Track braucht den Python-Track,
weil die gängigen ML-Bibliotheken (pandas, scikit-learn) Python sind. Nicht legitim: ein
JS-Browserspiel-Kurs, der den Python-Grundkurs voraussetzt, obwohl er kein Python enthält (dieser
Fehler stand bis zu diesem Dokument in `KURSPLAN.md` und wurde hier korrigiert).

**Spiele sind kein eigener Track**, sondern Projekt-/Vertiefungs-Content *innerhalb* der
jeweiligen Sprache: Pygame-Zero-Spiele im Python-Track, Canvas-Spiele im JavaScript-Track. Jede
Variante braucht nur ihre eigene Sprache als Vorwissen.

---

## Tracks

| Track | Einstieg | Grundkurs | Projekt-Kurse | Vertiefung |
|---|---|---|---|---|
| **Python** | `python-grundlagen-interaktiv` ✅ | `python-12-wochen-grundkurs` ✅ | Cäsar, Vigenère, Häufigkeitsanalyse, Morsecode, Zahlen-Detektiv, Text-Adventure ✅ · weitere Ideen in `PROJEKTIDEEN.md` | 💡 noch keine — Pygame-Ideen aus `KURSPLAN.md` laufen nicht in Pyodide (siehe `todo.md`, `kurs-python-spiele` verworfen) |
| **JavaScript** | 💡 noch keiner (Idee: leichter interaktiver Einstieg analog Python) | `js-grundkurs` ✅ — 9 Wochen, leichtes Format ohne Themen-Varianten (siehe `KURSPLAN.md`), Woche 4 (Funktionen) ist empfohlenes Vorwissen für `projekt-js-spielewerkstatt` | `projekt-js-spielewerkstatt` ✅ · `projekt-js-snake` ✅ (Canvas-Spiele) · `projekt-js-memory` ✅ · `projekt-js-quiz` ✅ — die ersten DOM-Projekte, schließen an Woche 7 des Grundkurses an · weitere DOM-Ideen in `PROJEKTIDEEN.md` | 💡 Browser-Spiel Advanced (`KURSPLAN.md` Kurs 3 Track B) — Voraussetzung ist der JS-Projekt-Kurs, **nicht** der Python-Grundkurs |
| **KI/ML** | – | `ki-labor` ✅ — 8 Wochen, ohne Themen-Varianten (siehe `KURSPLAN.md`), Algorithmen (k-NN, Entscheidungsbaum, kleines neuronales Netz) komplett in reinem Python selbst gebaut statt mit scikit-learn — **einzige legitime Cross-Track-Voraussetzung: Python-Grundkurs** | 💡 noch keine (Ideen in `PROJEKTIDEEN.md`) | – |
| **Hardware** (micro:bit) | – | – | `projekt-microbit-auto` ✅ · `projekt-microbit-ampel` ✅ (noch unverlinkt; beide nur DE, an echter Hardware noch nicht erprobt, siehe `todo.md`) | – |
| **Datenbanken** | – | 💡 noch nicht ausgearbeitet — andockbar an Python- oder JS-Backend-Inhalte, da SQL sprachneutral ist | – | – |
| **Web** (HTML/CSS + JS) | 🚧 „Meine erste Website“ (ca. 10–12, 8 Lektionen + Abschluss-Zertifikat) | 🚧 Web-Grundkurs HTML & CSS (ab 13, 9 Wochen, Wochen-Checks + Zertifikate) — Plan in `KURSPLAN.md`, beginnt mit Branch `web-sandbox` | – | – |

Status-Legende: ✅ vorhanden · 🚧 nächstes konkretes Thema (Branch/Plan existiert) · 📋 geplant
(in `todo.md` benannt, noch kein Plan) · 💡 Idee/Backlog, nicht committed.

---

## Verhältnis der Dokumente

- **`VISION.md`** (dieses Dokument) — Mission, Format-Definitionen, Track-Modell,
  Abhängigkeitsprinzip. Ändert sich selten, nur wenn sich das Gesamtbild wirklich verschiebt.
- **`KURSPLAN.md`** — konkrete Lehrpläne pro Kurs (Wochenthemen, Lernziele, Zielgruppen). Bleibt
  granular und wird inhaltlich am Track-Modell hier ausgerichtet.
- **`todo.md`** — kurzfristige Umsetzung: welcher Branch als nächstes, was ist offen.
- **`INHALTE.md`** — Dateistruktur/Kopplungen für bestehenden Content.
- **`HANDOFF.md`** — technischer Stand, Session-Übergabe.

---

## Offene Fragen (bewusst nicht entschieden)

- Datenbanken-Track ist noch nicht ausgearbeitet, nur als Themenfeld vorgemerkt (Web-Track: siehe `KURSPLAN.md`).
- Reihenfolge/Priorität zwischen KI-Track und weiteren Python-Projekt-Kursen ist offen (siehe
  `todo.md` "Nächste Themen").
