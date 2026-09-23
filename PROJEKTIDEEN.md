# PROJEKTIDEEN.md — Ideen-Backlog für Projekt-Kurse

Sammlung von Projekt-Ideen (Stand 2026-09-19), aus der wir nach und nach Projekt-Kurse
(`type: "projekt"`, ~5 Lektionen, siehe `INHALTE.md` §6) ausarbeiten. Kurzfristige Planung steht
in `todo.md`, das Format-/Track-Modell in `VISION.md`.

**Legende:** `[ ]` Idee · `[~]` in Arbeit (Branch) · `[x]` umgesetzt.
**Engine:** 🐍 Python/Pyodide (synchron, kein Spiele-Loop) · 🟨 JS-Sandbox (Canvas/DOM, rAF möglich).
**Alter:** Richtwert für die Zielgruppe.

Schon umgesetzt (nicht mehr hier): Cäsar-Chiffre, Morsecode, Zahlen-Detektiv, JS-Spielewerkstatt,
Vigenère-Chiffre, Snake, Text-Adventure.

## Empfohlene Reihenfolge (Vorschlag)
1. ~~Vigenère-Chiffre~~ ✅ umgesetzt
2. ~~Snake~~ ✅ umgesetzt
3. ~~Text-Adventure~~ ✅ umgesetzt

---

## 🎮 Spiele
- [x] **Snake** 🟨 — Segmente als Liste, Wachsen beim Fressen, Game-Over bei Selbstkollision. Ab 12.
- [ ] **Flappy-Klon** 🟨 — Schwerkraft + Sprung per Taste, Röhren als Array aus Objekten. Ab 12.
- [ ] **Space Invaders light** 🟨 — Gegner-Raster, Schüsse, Kollision; gut als Klassen-Übung. Ab 13.
- [ ] **Memory** 🟨 — Karten aufdecken/vergleichen, Zustandsmaschine, auch per DOM ohne Canvas. Ab 9.
- [x] **Text-Adventure** 🐍 — Räume als Dictionary, Inventar als Liste, mehrere Enden; Themen-Varianten möglich. Ab 10.

## 🌐 Web (DOM)
- [ ] **To-do-Liste** 🟨 — hinzufügen, abhaken, löschen; klassischer Anschluss an Woche 7. Ab 12.
- [ ] **Quiz-Generator** 🟨 — Fragen als Array von Objekten, Punktestand, Auswertung. Ab 11.
- [ ] **Farbmischer** 🟨 — R/G/B-Regler ändern live Hintergrund + Hex-Code. Ab 10.
- [ ] **Countdown & Stoppuhr** 🟨 — `setInterval`, Rundenzeiten als Liste. Ab 12.
- [ ] **Wetter/Zufalls-Zitat per API** 🟨 — `fetch`; **Achtung:** Sandbox hat opake Origin, braucht
      erst eine Erweiterung/Prüfung. Ab 14.

## 🤖 KI / ML (Voraussetzung: Python-Grundkurs, siehe `VISION.md`)
- [ ] **Tier-Klassifikator per k-NN** 🐍 — Merkmale (Gewicht/Größe), ohne Bibliotheken (~10 Zeilen). Ab 13.
- [ ] **Spam-Filter (Naive Bayes light)** 🐍 — Wörter zählen, eigene Trainings-Mails. Ab 14.
- [ ] **Regel-Chatbot (ELIZA)** 🐍 — Muster + Antwortvorlagen; Diskussion "Ist das KI?". Ab 12.
- [ ] **Tic-Tac-Toe mit Minimax** 🐍 — Baumsuche, unbesiegbarer Gegner. Ab 15.
- [ ] **Bias-Experiment** 🐍 — Mini-Datensatz mit schiefer Verteilung, Modell entscheidet unfair; Ethik-Diskussion. Ab 14.

## 🧩 Logik & Knobeln
- [ ] **Sudoku-Prüfer** 🐍 — gültig/ungültig, verschachtelte Schleifen + Mengen. Ab 13.
- [ ] **Türme von Hanoi** 🐍 — Rekursion, anfassbar. Ab 14.
- [ ] **Labyrinth-Löser** 🐍 — Breitensuche auf Gitter aus Listen, ASCII-Ausgabe. Ab 14.
- [ ] **Mastermind** 🐍 — Computer rät den Code mit Strategie statt Zufall. Ab 12.
- [ ] **Wolf, Ziege, Kohl** 🐍 — Zustandsraum-Rätsel per Programm lösen. Ab 11.

## 🔐 Krypto & Sicherheit
- [x] **Vigenère-Chiffre** 🐍 — Schlüsselwort, logischer Nachfolger von Cäsar. Ab 13.
- [ ] **Passwort-Stärke-Checker** 🐍 — Brute-Force-Dauer, Rechnen mit Möglichkeiten. Ab 12.
- [ ] **XOR-Geheimschrift** 🐍 — Bits verstehen, Ver-/Entschlüsseln mit derselben Funktion. Ab 15.
- [ ] **Häufigkeitsanalyse** 🐍 — Cäsar-Nachricht ohne Schlüssel knacken. Ab 14.
- [ ] **Prüfziffern (ISBN/IBAN)** 🐍 — wie Barcodes Fehler erkennen. Ab 13.

## 🎨 Kreativ & Generativ
- [ ] **Turtle-Mandala** 🐍 — Schleifen + Winkel (nutzt den Turtle-Shim aus `usePyodide.js`). Ab 10.
- [ ] **Pixel-Art-Editor** 🟨 — Raster anklicken, Farbe wählen, als Array speichern. Ab 11.
- [ ] **Fantasie-Namensgenerator** 🐍 — Drachen-/Pferdenamen aus Silben. Ab 8.
- [ ] **Musik-Loop / Beat-Sequencer** 🟨 — Web Audio, Töne per Klick. Ab 13.
- [ ] **Game of Life** 🟨/🐍 — einfache Regeln, faszinierendes Verhalten. Ab 13.

## 📊 Daten & Alltag
- [ ] **Taschengeld-Rechner** 🐍 — Sparziel, Wochen bis zum Ziel, Text-Diagramm. Ab 10.
- [ ] **Vokabeltrainer** 🐍 — Dictionary + Zufallsabfrage, Ergebnisse als JSON. Ab 11.
- [ ] **Klassen-Umfrage auswerten** 🐍 — eigene Daten zählen, Balken mit `#`. Ab 12.
- [ ] **Würfel-Statistik** 🐍 — 10.000 Würfe, Gesetz der großen Zahlen. Ab 11.
- [ ] **Stundenplan-Generator** 🐍 — Dictionaries + Listen kombinieren. Ab 12.

---

## Beim Ausarbeiten beachten
- Neuer Branch von `main` pro Projekt (`WORKFLOW.md`), Ablauf laut `INHALTE.md` §6 ("Projekt-Kurs
  hinzufügen"): Content-Ordner + `kurse.json`-Eintrag, sonst keine Code-Änderung.
- Neue Tags (z.B. `spiele` existiert schon) brauchen `projectTag.<slug>` in `de.js`/`en.js`.
- JS-Projekte: keine geteilten Namespaces zwischen Aufgaben; `functionCalls` nur auf
  `function`-Deklarationen/`var` möglich, nicht auf `const`/`let`/`class` (siehe HANDOFF 3.43);
  Arrays lassen sich nicht als erwarteter Wert validieren.
- Python-Projekte: keine Spiele-Loops (Pyodide synchron, 5s-Loop-Guard).
- Nach dem Umsetzen hier `[x]` setzen.
