# Todo

## Jetzt: 10 Verbesserungen in 6 Branches (gruppiert, B→A→E→F→C→D)

Plan-Datei: `~/.claude/plans/scalable-singing-cook.md` (Kontext/Details je Branch).

### Branch `cursor/debug-notebook-safety` (Punkte 5, 6)
- [x] Punkt 5 — Endlosschleifen-Schutz: `usePyodide.js` injiziert per AST-Transformation eine
      Deadline-Prüfung in jede `for`/`while`-Schleife; nach 5 Sekunden wird mit `_CellTimeout`
      (BaseException) abgebrochen und eine freundliche Fehlermeldung gezeigt statt den Tab
      einzufrieren. Bewusst KEIN Web-Worker (hätte `input()` in 65 Notebooks kaputt gemacht, da
      `window.prompt()` im Worker nicht verfügbar ist) — lokal mit CPython getestet (Endlosschleife,
      verschachtelt in Funktionen, geteilte Variablen über Zellen hinweg, NameError/SyntaxError
      bleiben unverändert) und live im Browser verifiziert (Playwright: Abbruch nach ~5s,
      Kernel bleibt danach voll funktionsfähig).
- [x] Punkt 6 — Debug-Ziel benennen: Sci-Fi-Variante komplett (12 Wochen × DE+EN = 24 Dateien,
      72 Bug-Zellen) um eine **Ziel:**/**Goal:**-Zeile ergänzt, die das erwartete Verhalten/die
      erwartete Ausgabe beschreibt, ohne den Bug zu verraten. Stichprobenartig geprüft (Woche 1, 8,
      11) — akkurat und spoilerfrei.
- [x] Dauerhafte Tests ergänzt (waren zunächst nur manuell per Playwright-Skript verifiziert, nicht
      in der Suite): `tests/site.spec.js` → "Debug-Notebook-Sicherheit" (Endlosschleife bricht nach
      3-12s ab, Kernel bleibt danach nutzbar) und `tests/storytelling-content.spec.js` → "Woche 1:
      Debug-Bugs nennen ein Ziel" (Anzahl Ziel-Zeilen == Anzahl Bugs, keine Spoiler-Formulierungen).
      Dabei einen latenten Bug im Test-Helper `openWeek()` gefunden+behoben (ging noch davon aus,
      dass Woche 1 immer aufgeklappt startet).
- [ ] Punkt 6 Fortsetzung: Pferde- und Abenteuer-Variante nach demselben Muster (nicht in dieser
      Sitzung gemacht — nächste Session)

### Branch `cursor/et-fixes` (Punkte 1-4) — noch offen
- [ ] Punkt 1: "Ich weiß es nicht"-Option in `QuizStep.vue`
- [ ] Punkt 2: Erklärung bei Falsch-Antwort ist technisch schon vorhanden (Coverage 100 % in
      `weeks.json`) — nur Wortlaut schärfen
- [ ] Punkt 3: Placement-Scoring lockern (`placementPerWeek` 2→3, eigener `placementPassThreshold`)
- [ ] Punkt 4: Distraktoren in `weeks.json` plausibler machen (erste Charge Wochen 1-4)

### Branch `cursor/kontakt-email` (Punkt 9) — noch offen
- [ ] Footer-Link ergänzen — **braucht die tatsächliche Kontakt-E-Mail-Adresse vom Nutzer**

### Branch `cursor/kurs-caesar-chiffre` (Punkt 10) — noch offen
- [ ] Neuer Projekt-Kurs "Cäsar-Chiffre" mit Deep-Links in Woche 2/4/5 des 12-Wochen-Kurses

### Branch `cursor/interaktiv-klarer` (Punkt 7) — noch offen
- [ ] Gestufter Hinweis in `LessonView.vue` statt sofortigem Preisgeben der erwarteten Ausgabe

### Branch `cursor/text-typo-pass` (Punkt 8) — noch offen
- [ ] `cspell`-Tooling-Pass, dann UI-Texte → Wochenbeschreibungen → Notebook-Inhalte

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
