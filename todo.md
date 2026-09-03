# Todo

## Jetzt: 10 Verbesserungen in 6 Branches (gruppiert, B→A→E→F→C→D)

Plan-Datei: `~/.claude/plans/scalable-singing-cook.md` (Kontext/Details je Branch).

### Branch `cursor/debug-notebook-safety` (Punkte 5, 6) — auf eigenem Branch, nicht hier gemergt
- [x] Punkt 5 — Endlosschleifen-Schutz in `usePyodide.js` (AST-Guard, 5s-Timeout)
- [x] Punkt 6 — Sci-Fi-Debug-Notebooks um Ziel-Angaben ergänzt (Pferde/Abenteuer offen)

### Branch `cursor/et-fixes` (Punkte 1-4) — dieser Branch
- [x] Punkt 1: "Ich weiß es nicht"-Option in `QuizStep.vue` — zählt wie falsch, löst eigene
      freundliche Rückmeldung aus ("Kein Problem — hier ist die Antwort: …"), Coverage geprüft
- [x] Punkt 2: Wortlaut bei Falsch-Antwort geschärft ("Nicht ganz — [Erklärung]" statt Erklärung
      ohne Einleitung) — Erklärungs-Feature selbst war schon vorhanden (100 % Coverage in
      `weeks.json`), nur Framing verbessert
- [x] Punkt 3: Placement-Scoring gelockert — `placementPerWeek` 2→3, neuer eigener
      `placementPassThreshold: 0.66` (≈ 2 von 3 richtig reicht) statt dem harten `passThreshold: 0.8`
      der normalen Wochen-Checks (die bleiben unverändert bei 0.8). Live verifiziert: 2/3 richtig
      (67 %) → "ok", 1/3 richtig (33 %) → "review".
- [x] Punkt 4: Distraktoren für Wochen 1-4 (12 von 40 Fragen, die genuin unplausibel waren, z.B.
      "Um den Computer auszuschalten") durch nähere Verwechslungen ersetzt (DE+EN), Rest der
      12 Wochen bewusst nicht angefasst (todo für spätere Session, siehe unten)
- [x] Dauerhafte Tests ergänzt (Punkt 1 + 3 waren zunächst nur manuell per Playwright-Skript
      verifiziert, nicht in der Suite): `tests/week-checks.spec.js` → "Ich weiß es nicht zeigt
      eigene Rückmeldung und die richtige Antwort" sowie "2 von 3 richtig pro Woche reicht
      (0.66-Schwelle), 1 von 3 nicht"

**Offen für später:** Distraktoren für Wochen 5-12 nach demselben Muster (~80 Fragen, nicht in
dieser Sitzung gemacht).

### Branch `cursor/kontakt-email` (Punkt 9) — offen, braucht Kontakt-E-Mail-Adresse vom Nutzer
### Branch `cursor/kurs-caesar-chiffre` (Punkt 10) — offen
### Branch `cursor/interaktiv-klarer` (Punkt 7) — offen
### Branch `cursor/text-typo-pass` (Punkt 8) — offen, größter Umfang

---

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
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken)

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2 → 3. Nicht mischen.

### 1. Python Spiele-Werkstatt — Branch `cursor/kurs-python-spiele`
- [ ] Kursmetadaten in `kurse.json` (+ EN)
- [ ] Content-Struktur (Wochen/Tabs analog bestehender Kurse oder Kurzformat)
- [ ] Turtle-/Textspiele, Level-Ideen, Belohnungen falls passend
- [ ] DE + EN (oder bewusst DE-first, EN nachziehen)
- [ ] Smoke-Test / manuell prüfen → PR nach `main`

### 2. Was kommt danach? Projekt-Sprints — Branch `cursor/kurs-python-projekte`
- [ ] 2–3 feste Projekt-Sprints (je ~2 Wochen Umfang skizzieren)
- [ ] Kursseite + Einstieg von 12-Wochen-Kurs verlinken („Weiter so“)
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 3. JS Mini-Games (Teens) **oder** KI-Labor — Branch wählen:
- **A)** `cursor/kurs-js-minigames` — Browser-Spiele, Canvas/p5, Zielgruppe 13–17
- **B)** `cursor/kurs-ki-labor` — Prompts, Grenzen, Schul-Nutzen (breitere Zielgruppe)
- [ ] Entscheidung A vs B (oder beide nacheinander, je ein Branch)
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Drittes Thema erst starten, wenn 1 und 2 gemerged sind (oder bewusst parallel nur wenn Kapazität klar ist). Default: erst Spiele-Werkstatt, dann Projekt-Sprints, dann A oder B.
