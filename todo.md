# Todo

## Now
### Website / Frontend
- [x] Das Tabsystem erklären
- [x] "Wie ist der Kurs aufgebaut?" mit den Belohnungen ergänzen
- [x] MissionenPanel: Punkte-Stand nach Browser-Reload prüfen (localStorage?)
- [x] Belohnungen zuklappen
- [x] Woche 1 zuklappen
- [x] Language-Toggle: Phase 4–6 (EN Content, rewards, Notebooks)

### Inhalte / Notebooks
- [x] Woche 9-12 Debug-Notebooks kurz durchschauen
- [x] Glossar-Notebooks für Anfänger
- [x] Branch `splitting` in `main` mergen
- [x] Interaktiv-Kurs: Varianten Kinder + Jugendliche
- [x] Storytelling-Überarbeitung Abenteuer-Variante (alle 12 Wochen, DE+EN): zusammenhängende Szenen
      statt Schritt-Listen, Pythonia/Pyralia-Namenskonflikt vereinheitlicht, Woche 2 "vier Elemente"
      jetzt eingelöst, mehrere Bugs behoben (Woche 6 Boss-Quest-Klon, Woche 8 kaputter Debug-Bug,
      Woche 9 Formatierung, Woche 10 Zoo-Thema, Woche 12 Textbug) — Details siehe Commit-Historie
- [x] Pferde- und Sci-Fi-Variante analysiert und dringende Bugs gefixt (DE+EN): Sci-Fi W11 kaputter
      Lektion-Code, W8 kaputter Debug-Bug, W5/6/8 dreifach kopiertes Boss-Quest, W12 XP-statt-Cyber-
      Credits; Pferde W9 Intro-Duplikat von W8, W5/8 Textbugs, W7/8/9 "Sonnentals"-Tippfehler, W12
      XP-statt-Huf-Punkte. Kleinere Fixes: Sci-Fi W9 f-String-Syntaxrisiko, W12 Debug-Spoiler, W5
      fehlende Platzhalter, W7 Missionen enger verknüpft; Pferde W2 Hufschlag-Typen jetzt benannt.
      Nebenbei: eine kaputte JSON-Datei (week5_horses_1_lektion.ipynb EN) gefunden und repariert,
      alle 444 Notebooks im Repo auf valides JSON geprüft.
- [x] "Gilde-Meister-Urkunde" als Zwischenbelohnung (W6/7/8) geprüft: kein Bug — Pferde/Sci-Fi nutzen
      dasselbe Muster (Reitmeister-/Crew-Meister-Urkunde je 3×), und andere Items (Kristallkugel 4×,
      Quest-Buch 4×) wiederholen sich im ganzen Kurs genauso — bewusstes Belohnungs-Flavor-Muster,
      keine Umbenennung nötig

### Infrastruktur
- [x] Einstufung / Checks in `main` (PR #1)
- [x] Admin-Login / Progress-Sync in `main` (PR #2)
- [x] Notebook-Sync-Loop-Fix in `main` (PR #3)
- [x] Backup-Skript für die SQLite-Nutzerdatenbank (Branch `backup-sqlite-db`, VACUUM INTO + Rotation)
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken)

---

## Fertige Branches (noch nicht nach `main` gemerged)

Reihenfolge-Empfehlung fürs Mergen: `debug-notebook-safety` → `et-fixes` → `interaktiv-klarer` →
`text-typo-pass` → `backup-sqlite-db` → `kurs-caesar-chiffre` → `wochen-zertifikate`. Deploy/Merge
bewusst zurückgestellt (siehe HANDOFF.md).

- [x] `debug-notebook-safety` — 5s-Timeout gegen Endlosschleifen in Pyodide-Zellen (AST-Loop-Guard,
      kein Web-Worker nötig), Sci-Fi-Debug-Notebooks (24 Dateien) um Ziel-Angabe ergänzt
- [x] `et-fixes` — "Weiß nicht"-Option im Quiz, Einstufung auf 3 Fragen/Woche mit eigener
      66%-Schwelle, 12 Distraktoren in Wochen 1-4 geschärft
- [x] `interaktiv-klarer` — gestufter Hinweis im interaktiven Kurs (vager Hinweis beim 1. Fehlversuch,
      wörtlicher erwarteter Wert erst ab dem 2.)
- [x] `text-typo-pass` — cspell-Setup (`cspell.json`, `lint:spelling`) + reale Tippfehler behoben
      (Britisches Englisch W12, "Parours"→"Parcours", "Futterschip"→"Futterschippe" u.a.)
- [x] `kurs-caesar-chiffre` — erstes eigenständiges Projekt neben den Wochenkursen (5 Lektionen,
      neue `ProjectCourse.vue`), verlinkt aus dem 12-Wochen-Kurs
- [ ] `kurs-python-spiele` — `ProjectCourse.vue` bereits generalisiert (mehrere Projekt-Kurse teilen
      sich die Komponente), die eigentlichen Spiele-Inhalte (Quiz-Arena, Turtle-Welt, Galgenmännchen)
      noch offen
- [x] `wochen-zertifikate` — Punkte-/Sammelsystem komplett entfernt, ersetzt durch Wochen-Zertifikate:
      Zertifikat pro Woche/Variante nur wenn alle Missionen+Boss-Quests erledigt UND Wochen-Check
      (Quiz + neue generische Coding-Aufgabe pro Woche) bestanden ist. `rewards-manifest*.json` auf
      reine ID-Listen reduziert (keine Punkte/Items mehr), `useFortschritt.js`/`useWeekChecks.js`
      neu geschrieben, neue `useZertifikate.js`. Tests: `tests/zertifikate.spec.js`.

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2 → 3. Nicht mischen. (Branch-Namen ohne `cursor/`-Präfix.)

### 1. Python Spiele-Werkstatt — Branch `kurs-python-spiele` (bereits begonnen, s.o.)
- [x] `ProjectCourse.vue` generalisiert für mehrere Projekt-Kurse
- [ ] Kursmetadaten in `kurse.json` (+ EN)
- [ ] Content-Struktur (mehrere kleine Projekte wie Cäsar-Chiffre, DE-first)
- [ ] Turtle-/Textspiele, Level-Ideen
- [ ] Smoke-Test / manuell prüfen → PR nach `main`

### 2. Was kommt danach? Projekt-Sprints — Branch `kurs-python-projekte`
- [ ] 2–3 feste Projekt-Sprints (je ~2 Wochen Umfang skizzieren)
- [ ] Kursseite + Einstieg von 12-Wochen-Kurs verlinken („Weiter so“)
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 3. JS Mini-Games (Teens) **oder** KI-Labor — Branch wählen:
- **A)** `kurs-js-minigames` — Browser-Spiele, Canvas/p5, Zielgruppe 13–17
- **B)** `kurs-ki-labor` — Prompts, Grenzen, Schul-Nutzen (breitere Zielgruppe)
- [ ] Entscheidung A vs B (oder beide nacheinander, je ein Branch)
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Drittes Thema erst starten, wenn 1 und 2 gemerged sind (oder bewusst parallel nur wenn Kapazität klar ist). Default: erst Spiele-Werkstatt, dann Projekt-Sprints, dann A oder B.
