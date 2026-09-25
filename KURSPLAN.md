# Kursplan – Lehrpläne der einzelnen Kurse

Detaillierte Wochenpläne/Lerninhalte für die Kurse, die in `VISION.md`s Track-Modell aufgeführt
sind. **Das Gesamtbild (welche Tracks es gibt, welches Format wofür, welche Voraussetzungen
gelten) steht in `VISION.md` — hier stehen nur die konkreten Lehrpläne.**

Wichtig, seit `VISION.md` eingeführt wurde: Kurse aus unterschiedlichen Sprachen/Tracks bauen
**nicht** automatisch aufeinander auf. Eine Voraussetzung gilt nur innerhalb ihres eigenen
Tracks — Ausnahme ist der KI-Track, der legitim auf dem Python-Track aufbaut (ML-Bibliotheken
sind Python). Die Kurse hier sind nach Track gruppiert, nicht mehr nach Alter/Nummer in einer
einzigen Kette.

---

## Python-Track: Spieleprogrammierung Grundkurs
**Zielgruppe:** ab 10 Jahre | **Dauer:** 8 Wochen | **Voraussetzungen:** keine (alternativer/
früherer Einstieg in den Python-Track, siehe `VISION.md`)

Erstes echtes Spiel programmieren. Sofortiger visueller Erfolg durch Pygame Zero.
Kein komplexes Setup – Pyodide im Browser oder lokales Python.

### Themen-Varianten
Alle bauen dasselbe Spiel, nur mit anderem Look:
- 🗺️ **Abenteuer:** Held weicht Hindernissen aus, sammelt Münzen
- 🐴 **Pferde:** Pferd springt über Zäune auf dem Reitparcours
- 🚀 **Sci-Fi:** Raumschiff weicht Asteroiden aus, sammelt Energie

### Wochenplan

| Woche | Thema | Lerninhalt |
|-------|-------|------------|
| 1 | Hallo Spielwelt | Pygame Zero kennenlernen, Fenster öffnen, Hintergrundbild |
| 2 | Die Spielfigur | Figur einladen, Position, Figur zeichnen |
| 3 | Bewegung | Tastatur-Steuerung, Figur bewegen, Grenzen setzen |
| 4 | Hindernisse | Objekte spawnen, zufällige Positionen (`random`) |
| 5 | Kollision | Treffer erkennen, Leben verlieren, Reaktion zeigen |
| 6 | Punkte & Score | Punkte zählen, Anzeige auf dem Bildschirm, Highscore |
| 7 | Spielzustände | Start-Screen, Game-Over-Screen, Neustart |
| 8 | Eigenes Spiel | Freie Woche: eigenes Spiel erweitern und präsentieren |

### Lernziele
- Einfache 2D-Spiele mit Pygame Zero bauen
- Spielfiguren steuern und animieren
- Kollisionserkennung und Spiellogik
- Zustandsmaschinen (Start / Spiel / Game Over)
- Zufall und Variablen in Spielen einsetzen

### Technisch
- **Tool:** Pygame Zero (pgzrun)
- **Konzepte:** Variablen, Funktionen, if-else, while, Klassen (leicht)
- **Kein Vorwissen** nötig – alle Python-Grundlagen werden direkt im Spielkontext eingeführt

---

## Python-Track: 12-Wochen-Grundkurs
**Zielgruppe:** ab 12 Jahre | **Dauer:** 12 Wochen | **Voraussetzungen:** keine

✅ **Bereits vollständig vorhanden.** Siehe `content/python-12-wochen-grundkurs/`.

Kurzbeschreibung: Systematischer Python-Einstieg mit Gamification. Drei parallele Themen-Varianten
(Abenteuer, Pferde, SciFi). 7 Notebooks pro Woche (Glossar, Lektion, Debug, Missionen, Reflexion, Lösungen, Boss-Quest).

Abgedeckte Themen: print/Variablen → Strings → Bedingungen → Schleifen → Funktionen →
Listen → Module → Dictionaries → Dateien → OOP → Vererbung → Abschlussprojekt (Text-Adventure)

---

## JavaScript-Track: Grundkurs
**Zielgruppe:** ab 12 Jahre | **Dauer:** 9 Wochen | **Voraussetzungen:** keine

Systematischer JS-Einstieg im Browser (eigene iframe-Sandbox, kein Setup nötig). **Eigenständig
neben `projekt-js-spielewerkstatt`** — kein Voraussetzungsverhältnis in beide Richtungen, beide
sind unabhängige Einstiegspunkte in den JS-Track (siehe `VISION.md`). Bewusst leichteres Format
als der Python-12-Wochen-Kurs: ein Track ohne Themen-Varianten (Abenteuer/Pferde/Sci-Fi), kein
Glossar/Boss-Quest/Lösungen/Zertifikat — pro Woche nur **Lektion → Debug → Mission**.

### Wochenplan

| Woche | Thema | Lerninhalt |
|-------|-------|------------|
| 1 | JS-Grundlagen | `console.log`, `let`/`const`, Datentypen (number/string/boolean, `typeof`), Rechnen + Template-Literals |
| 2 | Bedingungen | Vergleichsoperatoren, `if`/`else`/`else if`, `&&`/`\|\|`/`!`, verschachtelte Bedingungen |
| 3 | Schleifen | `for`, `while`, `break`/`continue`, Schleife über Strings |
| 4 | Funktionen | `function`, Parameter/Rückgabewert, kurze Einführung Arrow-Functions |
| 5 | Arrays | Array anlegen, Index, `push`/`pop`, `length`, Schleife über Array |
| 6 | Objekte | Objekt-Literale, Properties lesen/schreiben, Methoden in Objekten, Array aus Objekten |
| 7 | DOM & Interaktivität | `querySelector`, Text ändern, `addEventListener` (Klick) — Brücke zu Canvas/Spielen |
| 8 | Objekte als Blaupause | Klassen, `constructor`, Methoden, `this` — bewusst **ohne** Vererbung/Polymorphismus (zu fortgeschritten für den Rahmen, analog zur Kürzung in `python-12-wochen-grundkurs` Woche 11) |
| 9 | Abschlussprojekt | Kombination aus Woche 2–8, inkl. Klassen (z.B. kleine To-Do-Liste oder klickbares Quiz), kein neues Konzept |

### Lernziele
- Variablen, Datentypen, Bedingungen, Schleifen und Funktionen in JavaScript anwenden
- Mit Arrays und Objekten einfache Datensammlungen modellieren
- Eine Webseite über den DOM verändern und auf Klicks reagieren
- Eigene Daten als Klassen (Blaupausen) strukturieren

### Technisch
- **Tool:** eigene iframe-Sandbox (`useJsSandbox.js`, wie `projekt-js-spielewerkstatt`), kein Pyodide
- **Format:** ein Track, kein Themen-Varianten-System, kein Quiz/Zertifikat/PDF
- **Offener technischer Punkt:** Woche 7 (DOM) braucht einen neuen `validation.type` — bisher gibt
  es nur `output_contains`/`variables`/`functionCalls`/`canvas_*`, nichts, das einen DOM-Zustand
  prüft
- **Offener struktureller Punkt:** Mehrwochen-Navigation ist noch nicht entschieden — aktuell ist
  `js-grundkurs-woche1` (unverlinktes Experiment, siehe `HANDOFF.md` 3.42) ein einzelner,
  eigenständiger Content-Ordner mit eigenem Stepper (`JsCourseTour.vue`), gebaut für genau eine
  Woche. Für 9 Wochen braucht es entweder eine Wochen-Auswahl wie beim Python-Kurs
  (`WeekTour.vue`) oder eine andere Lösung — zu klären, sobald Woche 2 umgesetzt wird

---

## Vertiefungen: Spieleprogrammierung Advanced
**Zielgruppe:** ab 14 Jahre | **Dauer:** 10 Wochen

Zwei unabhängige Tracks in unterschiedlichen Sprachen — **keine gemeinsame Voraussetzung**, jeder
Track baut nur auf seiner eigenen Sprache auf (siehe `VISION.md`s Abhängigkeitsprinzip).

### Track A: Python RPG (Pygame + OOP)
**Voraussetzung:** Python 12-Wochen-Grundkurs oder gleichwertig (baut direkt auf Woche 10–11 OOP
auf). Komplexes 2D-Spiel mit Klassen, Inventar und Leveln.

| Woche | Thema |
|-------|-------|
| 1–2 | Pygame Setup, Tilemap, Kamera |
| 3–4 | Spielfigur als Klasse, Animation, Zustandsmaschine |
| 5–6 | Gegner-KI, Kampfsystem, Schaden berechnen |
| 7–8 | Inventar-System, Items, Dictionaries als Spieldaten |
| 9 | Level-Design, Tür & Schlüssel, Level-Wechsel |
| 10 | Speichern & Laden (JSON), eigenes Level bauen |

### Track B: Browser-Spiel (JavaScript + Canvas)
**Voraussetzung:** ein JS-Projekt-Kurs (z.B. `projekt-js-spielewerkstatt`) oder gleichwertige
JS-Grundlagen — **kein Python nötig**. Spiel läuft direkt im Browser – ideal für Schüler die
etwas für das Web bauen wollen. Eigenständig von der kompakten `js-spielewerkstatt`
(Projekt-Kurs, ~6 Lektionen): die Spielewerkstatt ist ein niedrigschwelliger, für sich
abgeschlossener Einstieg; dieser Track hier ist die spätere, deutlich umfangreichere
Vertiefung — beide ergänzen sich, keins ist Voraussetzung für das andere im strengen Sinn,
aber wer schon die Spielewerkstatt gemacht hat, startet hier mit Vorwissen.

| Woche | Thema |
|-------|-------|
| 1–2 | HTML/CSS Grundlagen, Canvas kennenlernen |
| 3–4 | JavaScript Grundlagen (Variablen, Funktionen, Events) |
| 5–6 | Spielschleife, Figur bewegen, Tastatursteuerung |
| 7–8 | Kollision, Gegner, Punkte, Sounds |
| 9 | Spieldesign: Levels, Schwierigkeit, Highscore |
| 10 | Veröffentlichen: Spiel online stellen (GitHub Pages) |

### Lernziele (beide Tracks)
- Komplexere Spielmechanik planen und umsetzen
- Klassen und OOP im Spielkontext anwenden
- Spielzustände und Datenpersistenz
- Eigenes Spiel von Konzept bis zur spielbaren Version

---

## KI-Track: KI-Grundlagen
**Zielgruppe:** ab 14 Jahre | **Dauer:** 8 Wochen | **Voraussetzungen:** Python 12-Wochen-Kurs
(einzige legitime Cross-Track-Voraussetzung, siehe `VISION.md` — ML-Bibliotheken wie
pandas/scikit-learn sind Python)

Einführung in Künstliche Intelligenz – ohne tiefe Mathematik. Fokus auf Konzepte verstehen,
indem die Algorithmen **komplett selbst in reinem Python geschrieben** werden (kein scikit-learn,
kein zusätzliches Paket) — Schüler sehen dadurch wirklich, was beim Lernen passiert, statt eine
Library aufzurufen. Bewusster Verzicht auf Prompting/Chatbot-Nutzung als Kursthema: das bringen
Schüler:innen bereits mit, hier soll verstanden werden, was dahinter passiert. **Kein
Themen-Varianten-Format** (wie `js-grundkurs`) — ein fester, algorithmus-zentrierter Aufbau.

### Wochenplan

| Woche | Thema | Was wird selbst gebaut |
|-------|-------|------------|
| 1 | Was ist KI? | Regelbasiert vs. lernend – an einem einfachen Beispiel gegenübergestellt |
| 2 | Daten sind alles | Eigene kleine Datensätze als Listen/Dictionaries anlegen, Muster von Auge suchen |
| 3 | Nächste Nachbarn (k-NN) | Erster Klassifikator komplett selbst geschrieben: Distanz berechnen, Mehrheitsentscheid |
| 4 | Training & Test | Trainings-/Testdaten trennen, Genauigkeit selbst berechnen, Overfitting an absichtlich zu kleinem Datensatz zeigen |
| 5 | Entscheidungsbäume | Eigener einfacher if/else-Baum aus Daten abgeleitet |
| 6 | Neuronale Netze I | Ein einzelnes Neuron von Hand: Gewichte, Summe, Schwellenwert (Perceptron) |
| 7 | Neuronale Netze II | Kleines Netz mit versteckter Schicht, Gewichte lernen lassen (z.B. XOR oder 3×3-Pixel-Mustererkennung) |
| 8 | Grenzen & Ethik | Bias-Experiment (schiefer Datensatz → unfaires Modell), kurze Einordnung "was macht ChatGPT anders", Datenschutz |

### Lernziele
- Unterschied KI / klassische Programmierung verstehen
- Eigene Datensätze erstellen und aufbereiten
- k-NN, Entscheidungsbaum und ein kleines neuronales Netz von Grund auf selbst implementieren
- Genauigkeit/Overfitting selbst messen und interpretieren
- Ethische Fragen (Bias, Datenschutz) rund um KI diskutieren

### Technisch
- **Keine zusätzlichen Libraries** – reines Python, läuft im nackten Pyodide-Kernel (kein
  scikit-learn/pandas: wasm-Build zieht scipy mit, mehrere zehn MB Download, zu schwer für
  Schul-WLAN/ältere Geräte)
- **Kein eigenes GPU nötig, keine API-Kosten** – alles läuft lokal auf kleinen, selbst erstellten Datensätzen im Browser

---

## Lernpfade

Beispielhafte Wege durch die Tracks — jeder Pfad bleibt innerhalb seiner Sprache, außer beim
KI-Track (siehe `VISION.md`):

```
Python-Interesse, ab 10:
  → Spieleprogrammierung Grundkurs (Python-Track, Pygame Zero)
  → 12-Wochen-Grundkurs (Python-Track)
  → Spieleprogrammierung Advanced, Track A: Python RPG

Python-Interesse, ab 12:
  → 12-Wochen-Grundkurs (Python-Track)
  → Spieleprogrammierung Advanced Track A (Python-Track) oder KI-Grundlagen (KI-Track)

Web/JS-Interesse, ab 12 (kein Python nötig):
  → js-grundkurs (JS-Track, Grundkurs) optional, für mehr Struktur
  → js-spielewerkstatt (JS-Track, Projekt-Kurs) — unabhängig vom Grundkurs, gleichwertiger Einstieg
  → Spieleprogrammierung Advanced, Track B: Browser-Spiel (JS-Track)

KI-Interesse, ab 14:
  → 12-Wochen-Grundkurs (Python-Track) — Pflicht-Voraussetzung
  → KI-Grundlagen (KI-Track)
```

---

## Offene Fragen / Nächste Schritte

- [ ] Entscheidung: Pygame Zero oder anderes Framework für den Spieleprogrammierung-Grundkurs?
- [ ] Technisch: Läuft Pygame Zero in Pyodide/Browser oder braucht es lokale Installation?
- [ ] Spieleprogrammierung Grundkurs: Themen-Varianten bestätigen oder festes Thema ohne Varianten?
- [ ] Reihenfolge/Priorität zwischen KI-Track und weiteren Python-Projekt-Kursen — siehe `todo.md`
      "Nächste Themen".
