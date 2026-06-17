# Kursplan – Übersicht aller Kurse

Vier Kurse mit aufeinander aufbauendem Lernpfad. Zielgruppe: Kinder und Jugendliche ohne Vorkenntnisse.

```
Ab 10  →  Spieleprogrammierung Grundkurs       8 Wochen   (Pygame Zero)
Ab 12  →  Python 12-Wochen-Grundkurs          12 Wochen   ✅ vorhanden
Ab 14  →  Spieleprogrammierung Advanced       10 Wochen   (Python RPG oder Browser-Spiel)
Ab 14  →  KI-Grundlagen                        8 Wochen   (ML mit Python)
```

---

## Kurs 1 – Spieleprogrammierung Grundkurs
**Zielgruppe:** ab 10 Jahre | **Dauer:** 8 Wochen | **Voraussetzungen:** keine

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

## Kurs 2 – Python 12-Wochen-Grundkurs
**Zielgruppe:** ab 12 Jahre | **Dauer:** 12 Wochen | **Voraussetzungen:** keine

✅ **Bereits vollständig vorhanden.** Siehe `content/python-12-wochen-grundkurs/`.

Kurzbeschreibung: Systematischer Python-Einstieg mit Gamification. Drei parallele Themen-Varianten
(Abenteuer, Pferde, SciFi). 7 Notebooks pro Woche (Glossar, Lektion, Debug, Missionen, Reflexion, Lösungen, Boss-Quest).

Abgedeckte Themen: print/Variablen → Strings → Bedingungen → Schleifen → Funktionen →
Listen → Module → Dictionaries → Dateien → OOP → Vererbung → Turtle-Grafik

---

## Kurs 3 – Spieleprogrammierung Advanced
**Zielgruppe:** ab 14 Jahre | **Dauer:** 10 Wochen | **Voraussetzungen:** Python 12-Wochen-Kurs oder gleichwertig

Zwei wählbare Tracks. Schüler entscheiden sich zu Beginn für einen Track und bleiben dabei.

### Track A: Python RPG (Pygame + OOP)
Baut direkt auf Woche 10–11 (OOP) des Grundkurses auf. Komplexes 2D-Spiel mit Klassen, Inventar und Leveln.

| Woche | Thema |
|-------|-------|
| 1–2 | Pygame Setup, Tilemap, Kamera |
| 3–4 | Spielfigur als Klasse, Animation, Zustandsmaschine |
| 5–6 | Gegner-KI, Kampfsystem, Schaden berechnen |
| 7–8 | Inventar-System, Items, Dictionaries als Spieldaten |
| 9 | Level-Design, Tür & Schlüssel, Level-Wechsel |
| 10 | Speichern & Laden (JSON), eigenes Level bauen |

### Track B: Browser-Spiel (JavaScript + Canvas)
Kein Python nötig. Spiel läuft direkt im Browser – ideal für Schüler die etwas für das Web bauen wollen.

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

## Kurs 4 – KI-Grundlagen
**Zielgruppe:** ab 14 Jahre | **Dauer:** 8 Wochen | **Voraussetzungen:** Python 12-Wochen-Kurs

Einführung in Künstliche Intelligenz – ohne tiefe Mathematik. Fokus auf Konzepte verstehen,
ausprobieren und reflektieren. Schüler trainieren eigene Modelle und sehen was KI kann und nicht kann.

### Themen-Varianten
- 🗺️ **Abenteuer:** KI-Orakel vorhersagt Dungeon-Ausgänge, KI erkennt Monster-Typen
- 🐴 **Pferde:** KI erkennt Gangarten, sagt Siegchancen voraus, empfiehlt Futterpläne
- 🚀 **Sci-Fi:** KI navigiert Raumschiff, erkennt Alien-Signale, klassifiziert Planeten

### Wochenplan

| Woche | Thema | Lerninhalt |
|-------|-------|------------|
| 1 | Was ist KI? | KI vs. Programmierung, Anwendungen, Chancen & Grenzen |
| 2 | Daten sind alles | Datensätze verstehen, bereinigen, visualisieren (pandas, matplotlib) |
| 3 | Klassifikation | KI lernt unterscheiden – k-Nearest-Neighbors intuitiv erklärt |
| 4 | Training & Test | Overfitting, Trainings-/Testdaten, Genauigkeit messen |
| 5 | Entscheidungsbäume | Decision Trees visuell, eigener Classifier |
| 6 | Neuronale Netze | Wie ein Netz "denkt" – visuell ohne tiefe Mathematik |
| 7 | Sprachverarbeitung | Texte klassifizieren, einfacher Spam-Filter |
| 8 | KI & Ethik | Bias, Fairness, Datenschutz – Was darf KI, was nicht? |

### Lernziele
- Unterschied KI / klassische Programmierung verstehen
- Eigene Datensätze erstellen und aufbereiten
- Einfache ML-Modelle trainieren und evaluieren (scikit-learn)
- Ergebnisse visualisieren und interpretieren
- Ethische Fragen rund um KI diskutieren

### Technisch
- **Libraries:** pandas, matplotlib, scikit-learn
- **Kein eigenes GPU nötig** – alles läuft auf kleinen Datensätzen lokal
- Pyodide im Browser möglich für einfache Beispiele, komplexere Modelle lokal

---

## Lernpfade

```
Keine Vorkenntnisse, ab 10:
  → Spieleprogrammierung Grundkurs (Kurs 1)
  → Python 12-Wochen-Grundkurs (Kurs 2)
  → Spieleprogrammierung Advanced (Kurs 3, Track A)

Keine Vorkenntnisse, ab 12:
  → Python 12-Wochen-Grundkurs (Kurs 2)
  → Spieleprogrammierung Advanced (Kurs 3) oder KI-Grundlagen (Kurs 4)

Web-Interesse, ab 14:
  → Python 12-Wochen-Grundkurs (Kurs 2)  [optional]
  → Spieleprogrammierung Advanced, Track B: Browser-Spiel (Kurs 3)

KI-Interesse, ab 14:
  → Python 12-Wochen-Grundkurs (Kurs 2)
  → KI-Grundlagen (Kurs 4)
```

---

## Offene Fragen / Nächste Schritte

- [ ] Entscheidung: Pygame Zero oder anderes Framework für Kurs 1?
- [ ] Entscheidung: Track A oder Track B zuerst für Kurs 3 — oder beide parallel?
- [ ] Technisch: Läuft Pygame Zero in Pyodide/Browser oder braucht es lokale Installation?
- [ ] Kurs 1: Themen-Varianten bestätigen oder festes Thema ohne Varianten?
- [ ] Kurs 4: Datensätze vorbereiten (eigene oder öffentliche wie Iris, Titanic)?
