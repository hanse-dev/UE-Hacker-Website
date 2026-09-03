# Todo

## Jetzt: 10 Verbesserungen in 6 Branches (gruppiert, B→A→E→F→C→D)

Plan-Datei: `~/.claude/plans/scalable-singing-cook.md` (Kontext/Details je Branch).

### Branch `cursor/debug-notebook-safety` (Punkte 5, 6) — eigener Branch
- [x] Punkt 5 — Endlosschleifen-Schutz in `usePyodide.js` (AST-Guard, 5s-Timeout)
- [x] Punkt 6 — Sci-Fi-Debug-Notebooks um Ziel-Angaben ergänzt (Pferde/Abenteuer offen)

### Branch `cursor/et-fixes` (Punkte 1-4) — eigener Branch
- [x] Alle 4 Punkte fertig: "weiß nicht"-Option, Wortlaut, Scoring (placementPerWeek 3,
      placementPassThreshold 0.66), Distraktoren Wochen 1-4 (Wochen 5-12 offen)

### Branch `cursor/kontakt-email` (Punkt 9) — zurückgestellt
- [ ] Braucht die tatsächliche Kontakt-E-Mail-Adresse vom Nutzer, dann Footer-Link ergänzen

### Branch `cursor/kurs-caesar-chiffre` (Punkt 10) — dieser Branch
- [x] Neuer Kurs `projekt-caesar-chiffre`: 5 Lektionen (ord/chr → Verschieben mit Wraparound →
      Verschlüsseln-Funktion → Entschlüsseln-Funktion → Brute-Force-Knacker), reuse von
      `LessonView.vue` über neue schlanke Komponente `ProjectCourse.vue` (kein Varianten-Selector,
      anders als `InteractiveCourse.vue`)
- [x] Deep-Links aus den Lektionstexten in Woche 2/4/5 des 12-Wochen-Kurses (bestehender
      Query-Param-Mechanismus aus `PlacementCourse.vue` wiederverwendet)
- [x] Sichtbar auf der Startseite (Home.vue-Filter erweitert) und als Hinweis-Banner am Ende des
      12-Wochen-Kurses
- [x] `useInteractiveProgress.js` um optionalen `courseId`-Parameter erweitert (verhindert
      falsches `courseId`-Feld im exportierten Fortschritt, wenn dieselbe Composable für einen
      zweiten Kurs wiederverwendet wird)
- [x] Playwright-Tests ergänzt (`tests/site.spec.js`), End-to-End manuell mit echtem Pyodide-Lauf
      durch alle 5 Lektionen verifiziert (inkl. Brute-Force-Ausgabe "projekt")
- **Bekannte Einschränkung:** nur DE-Content (kein EN), bewusst DE-first wie andere neue Kurse in
  der Planung — EN-Nachzug offen für später

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
