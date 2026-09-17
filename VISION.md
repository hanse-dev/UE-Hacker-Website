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
| **Python** | `python-grundlagen-interaktiv` ✅ | `python-12-wochen-grundkurs` ✅ | `projekt-caesar-chiffre` ✅ · weitere geplant (`kurs-python-projekte` 📋) | 💡 Spieleprogrammierung mit Pygame Zero (alternativer/früherer Einstieg, siehe `KURSPLAN.md` Kurs 1) · 💡 RPG/OOP-Advanced (`KURSPLAN.md` Kurs 3 Track A, baut auf Wochen 10–11 auf) |
| **JavaScript** | 💡 noch keiner (Idee: leichter interaktiver Einstieg analog Python) | 💡 evtl. langfristig, im bewährten Storytelling-/Wochenformat wie Python — nicht dringend, nicht entschieden | `projekt-js-spielewerkstatt` 🚧 nächstes konkretes Thema | 💡 Browser-Spiel Advanced (`KURSPLAN.md` Kurs 3 Track B) — Voraussetzung ist der JS-Projekt-Kurs, **nicht** der Python-Grundkurs |
| **KI/ML** | – | 💡 `kurs-ki-labor` (`KURSPLAN.md` Kurs 4) — **einzige legitime Cross-Track-Voraussetzung: Python-Grundkurs** | – | – |
| **Datenbanken** | – | 💡 noch nicht ausgearbeitet — andockbar an Python- oder JS-Backend-Inhalte, da SQL sprachneutral ist | – | – |
| **Web** (HTML/CSS + JS) | – | 💡 eher als Erweiterung des JS-Tracks als eigenständiger Track | – | – |

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

- Braucht JavaScript langfristig einen eigenen 12-Wochen-Grundkurs, oder reicht eine wachsende
  Kette aus Projekt-Kursen (wie die Spielewerkstatt)? Tendenz: falls ja, im bewährten
  Storytelling-/Wochenformat wie der Python-Kurs, da sich die Grundlagen dort gut vermitteln
  lassen — aber nicht dringend.
- Datenbanken- und Web-Track sind noch nicht ausgearbeitet, nur als Themenfelder vorgemerkt.
- Reihenfolge/Priorität zwischen KI-Track und weiteren Python-Projekt-Kursen ist offen (siehe
  `todo.md` "Nächste Themen").
