# Todo

## Now
### Website / Frontend
- [x] Das Tabsystem erklären
- [x] "Wie ist der Kurs aufgebaut?" mit den Belohnungen ergänzen
- [x] MissionenPanel: Punkte-Stand nach Browser-Reload prüfen (localStorage?)
- [x] Belohnungen zuklappen
- [x] Woche 1 zuklappen
- [x] Language-Toggle: Phase 4–6 (EN Content, rewards, Notebooks)
- [x] Interaktiver Kurs: gestufter Hinweis in `LessonView.vue` (erster Fehlversuch nur vager Hinweis,
      wörtlicher erwarteter Wert erst ab dem zweiten) — **bewusst zurückgestellt:** "Ausführen vs.
      Prüfen"-Unterscheidung klarer machen und den Fortschritts-/Weiter-Flow überarbeiten; brauchte
      konkretes Nutzer-Feedback, nicht blind umsetzen
- [x] Einstufungstest: Distraktoren für Wochen 5-12 geschärft (Branch
      `einstufung-distraktoren-w5-12`) — 28 von 80 Fragen hatten unplausible Falsch-Antworten
      (z.B. "Nur am Wochenende" bei "Muss man jedes Modul selbst schreiben?"), auf nähere
      Verwechslungen umgestellt (z.B. json.dumps/json.loads gegeneinander vertauscht als
      Distraktor). Schon gute Distraktoren unangetastet gelassen, DE+EN synchron.
- [x] Einstufungstest/Check-Tab: personalisierte Falsch-Antwort-Erklärungen (Branch
      `einstufung-personalisierte-erklaerungen`, gemergt) — statt einer geteilten
      Erklärung für alle falschen Antworten einer Frage bekommt jetzt jede falsche Antwort ihre
      eigene, passende Erklärung (z.B. `print[Hi]` bekommt "eckige statt runde Klammern, Anführungs-
      zeichen fehlen" statt fälschlich "muss klein geschrieben werden"). Nebenbei gefunden und
      mitgefixt: 119 von 120 `explanation_en`-Feldern waren nie übersetzt worden. Details siehe
      HANDOFF.md 3.17.

### Curriculum-Lücken 12-Wochen-Kurs (Plan: `~/.claude/plans/joyful-wishing-piglet.md`)
Content-Analyse hat Reihenfolge-Probleme, Redundanz und Lernziel-Lücken im 12-Wochen-Kurs gefunden.
Je ein Branch pro Punkt, empfohlene Reihenfolge:
- [x] `woche12-turtle-notebook-bug-fix` — kaputte `%pip install Tinker`-Zelle in Woche-12-Lektion
      entfernen (falscher Paketname + eingebrannter Fehler-Output). Betraf nur Abenteuer (DE+EN,
      Pferde/Sci-Fi waren sauber): Zelle war komplett tot (nachfolgende Zellen machen ihr eigenes
      `import turtle`, `from turtle import *` wurde nirgends genutzt), daher ganz entfernt statt
      ersetzt. Zusätzlich im DE-Notebook einen zweiten eingebrannten `ModuleNotFoundError:
      No module named '_tkinter'`-Output (an der direkt folgenden `import turtle`-Zelle, vom
      Autoren-Rechner ohne Tk-Unterstützung) geleert.
- [x] `woche3-bedingungen-luecken` — `not`/`or` als lauffähigen Code ergänzt (neue Zauberformel/
      Lektion/Systemprotokoll 4 "Logische Verknüpfungen"), echtes Verschachtelungsbeispiel (neue
      Nummer 5, `if` in `if`, Tür-/Stalltür-/Schleusen-Thema je Variante). Alle 3 Varianten × DE/EN,
      lokal mit `python3` ausgeführt (kein Syntax-/Laufzeitfehler)
- [x] `woche4-woche6-listen-neuordnung` — Listen/`enumerate()` komplett aus Woche 4 raus (war
      Redundanz mit Woche 6), Woche 4 bekommt stattdessen einen neuen Abschnitt "Verschachtelte
      Schleifen" (eigenes, bisher nie eingelöstes Lernziel). Dabei entdeckt: `break`/`continue` war
      NICHT bei allen Varianten in Woche 4 unfertig — nur Abenteuer liefert es erst in Woche 6,
      Pferde/Sci-Fi hatten es schon in Woche 4 (dafür nie in Woche 6). Nutzer-Entscheidung: alle auf
      Woche 6 vereinheitlicht (wie Abenteuer) — `break`/`continue`-Abschnitt bei Pferde/Sci-Fi aus
      Woche 4 raus, dafür neu in Woche 6 ergänzt. `woche4.md` DE+EN Lernziele angepasst. Nebenbei
      einen echten `NameError`-Bug in Pferdes altem Woche-4-Beispiel gefunden (verschwand mit der
      Entfernung des Abschnitts). Details siehe HANDOFF.md 3.26.
- [x] `woche1-boolean-entfernen` — Boolean-Erwähnung aus Woche 1 raus (Lektion-Tabelle "drei" → "zwei
      häufigste Werttypen", Beispiel-Code-Zeile, Glossar-Begriff + Glossar-Code-Demo), taucht jetzt
      erstmals in Woche 2 als vierter Datentyp auf. Alle 3 Varianten × DE/EN, `1_lektion` + `0_glossar`
- [x] `woche5-woche8-tryexcept-verschieben` — `try`/`except` von Woche 5 nach Woche 8 verschoben.
      Überraschender Fund: nur Abenteuer lehrte try/except in Woche 5 ("Zauberformel 4") — Pferde/
      Sci-Fi hatten dort NIE eine try/except-Einführung, obwohl ihr Woche-8-Glossar fälschlich
      "Wiederholung aus Woche 5: try/except" behauptete. Für Pferde/Sci-Fi gab es also gar nichts zu
      verschieben, nur die neue Einführung in Woche 8 zu ergänzen (kein Vorwissen vorausgesetzt).
      Woche 8 (alle 3 Varianten × DE/EN): neuer Mini-Abschnitt "🛡️ Fehler abfangen mit try/except"
      direkt vor der Tupel-Unveränderlichkeits-Demo, Glossar-Haupttabelle um `try`/`except`-Zeile
      ergänzt, die falsche "Aus Woche 5"-Wiederholungszeile entfernt. `woche8.md` DE+EN Lernziel
      ergänzt. Woche 5 Abenteuer: "Zauberformel 4" komplett entfernt (Lektion + Glossar). Alle 16
      betroffenen Notebooks sequenziell (ein gemeinsamer Namespace, wie im echten Kernel) mit
      `python3` durchlaufen — keine Fehler.
- [ ] `woche8-list-comprehension-glossar` — unerklärte List Comprehension aus dem Lektion-Code im
      Glossar erklären. **Scope jetzt zweimal erweitert:** betrifft nicht nur Woche 8 Abenteuer,
      sondern auch Woche 8 Pferde + Sci-Fi (`[p for p in pferde if ...]` / `[m for m in crew if
      ...]`, bei `woche5-woche8-tryexcept-verschieben` entdeckt) UND Woche 6 Pferde + Sci-Fi
      (gleiches Muster, bei `woche4-woche6-listen-neuordnung` entdeckt) — alle Fundstellen im
      selben Branch mitnehmen (Woche 8 Abenteuer bereits bekannt, Woche 8 DE-Glossare in diesem
      Branch schon leicht verändert — auf Merge-Reihenfolge achten)
- [ ] `woche7-math-aufwerten` — `math`-Modul vom optionalen Bonus-Exkurs zu vollwertigem
      Lektionsinhalt aufwerten (Widerspruch zu `woche7.md`-Lernziel auflösen)
- [ ] `woche11-lernziele-anpassen` — "Design Patterns"/"Komposition vs. Vererbung" aus
      `woche11.md`-Lernzielen streichen (zu fortgeschritten für den Rahmen der Lektion)
- [ ] `woche12-interaktivitaet` — Event-Handling-Beispiel (`onscreenclick`/`onkey`) ergänzen, da
      "Interaktive Grafik erstellen" bisher unerfülltes Lernziel ist

### Inhalte / Notebooks
- [x] Neues Projekt "Cäsar-Chiffre" (`kurs-caesar-chiffre`, `projekt-caesar-chiffre`): 5 Lektionen
      (ord/chr → Verschieben mit Wraparound → Verschlüsseln-Funktion → Entschlüsseln-Funktion →
      Brute-Force-Knacker), eigene schlanke Komponente `ProjectCourse.vue` (kein Varianten-Selector),
      Deep-Links aus Woche 2/4/5 des 12-Wochen-Kurses, sichtbar auf der Startseite. Bewusst nur
      DE-Content (EN-Nachzug offen). Tests in `tests/site.spec.js`.
- [x] Text-Tippfehler-Pass über die ganze Seite (`text-typo-pass`): `cspell`-Tooling eingerichtet
      (`cspell.json`, `npm run lint:spelling`), alle 444 Notebooks + Cheat-Sheets/Glossare geprüft,
      6 echte Tippfehler gefunden und korrigiert (u.a. "Parours"→"Parcours",
      "Futterschip"→"Futterschippe", britisches Englisch in Woche 12 EN). Details siehe HANDOFF.md
      3.8. **Offen:** `.vue`-Prosa (Ternary-Texte) und die Interaktiv-/Cäsar-Chiffre-Kurse sind noch
      nicht mit cspell geprüft.
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

### Überlegungen (noch nicht entschieden)
- [ ] Weitere Sprache neben DE/EN? Noch keine Entscheidung, kein Ziel. Falls das kommt: die 97
      Inline-Ternarys `lang === 'en' ? X : Y` in `.vue`-Dateien sind seit dem `ternary-cleanup`-
      Refactoring (HANDOFF.md 3.23) bereits auf den `t()`-Mechanismus umgestellt — dieser Teil ist
      also schon erledigt. Offen bleibt der Content: `_en`-Feld-Suffix in `content/python-checks/
      week-{N}.json`, `-en`-Ordner-Suffix in `useCourseData.js`. Größter Aufwandstreiber wäre der
      Content selbst (444 Notebooks × Sprache), nicht mehr die UI-Technik. Keine neue i18n-Library
      nötig.

### Infrastruktur
- [x] Einstufung / Checks in `main` (PR #1)
- [x] Admin-Login / Progress-Sync in `main` (PR #2)
- [x] Notebook-Sync-Loop-Fix in `main` (PR #3)
- [x] SQLite-Backup-Script (`backup-sqlite-db`): `api/src/scripts/backup-db.js` zieht per
      `VACUUM INTO` eine konsistente Kopie (sicher auch im WAL-Modus/laufenden Betrieb), Retention
      behält die letzten `BACKUP_KEEP` (Default 14) Backups. `npm run backup:db` lokal,
      `docker compose exec app node src/scripts/backup-db.js` in Prod. Getestet mit `node --test`
      (4 Tests). Nicht abgedeckt: externe Sicherung der Backups selbst — hängt von der
      Infrastruktur ab, bewusst nicht mitgebaut.
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken)
      — **zurückgestellt** (Nutzer will erst später deployen)

---

## Fertige Branches (alle nach `main` gemerged)

Alle sieben Branches sind in dieser Session in der Reihenfolge `debug-notebook-safety` → `et-fixes`
→ `interaktiv-klarer` → `text-typo-pass` → `backup-sqlite-db` → `kurs-caesar-chiffre` →
`wochen-zertifikate` nach `main` gemergt worden. Noch **nicht** nach `origin/main` gepusht — Push
und Server-Deploy bewusst zurückgestellt (siehe HANDOFF.md).

- [x] `debug-notebook-safety` — 5s-Timeout gegen Endlosschleifen in Pyodide-Zellen (AST-Loop-Guard,
      kein Web-Worker nötig), Sci-Fi-Debug-Notebooks (24 Dateien) um Ziel-Angabe ergänzt
- [x] Debug-Notebook-Ziele auch für Pferde + Abenteuer nachgezogen (Branch
      `debug-ziele-pferde-abenteuer`) — 48 Dateien (Pferde/Abenteuer × DE/EN × 12 Wochen), 144
      "**Ziel:**"/"**Goal:**"-Zeilen ergänzt, nur Markdown-Zellen geändert, Bug-Code unangetastet.
      Neue Tests: `storytelling-content.spec.js` Woche-1-Ziel-Check für Pferde + Abenteuer
      (analog zum bestehenden Sci-Fi-Test).
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
- [x] `wochen-zertifikate` (HANDOFF.md 3.12) — Punkte-/Sammelsystem komplett entfernt, ersetzt durch Wochen-Zertifikate:
      **ein** Zertifikat pro Woche (keine Varianten-Aufteilung mehr), verliehen sobald der Wochen-Check
      bestanden ist — Quiz **plus zwei** Coding-Aufgaben (leicht + schwerer). Missionen/Boss-Quests
      bleiben als freiwillige Übungs-Checkliste pro Variante bestehen, zählen aber nicht mehr fürs
      Zertifikat (Nutzer-Entscheidung: reines Abhaken war nicht aussagekräftig genug).
      `rewards-manifest*.json` auf reine ID-Listen reduziert (keine Punkte/Items mehr),
      `useFortschritt.js`/`useWeekChecks.js` neu geschrieben, neue `useZertifikate.js`.
      `content/python-checks/weeks.json`: `codingChallenge` (1) → `codingChallenges` (Array, 2 Einträge)
      pro Woche, alle 12 neuen "schwereren" Aufgaben lokal mit `python3` verifiziert.
      Alle "**Belohnung(en):**"-Zeilen aus allen 444 Notebooks entfernt (waren nach der Punkte-
      Entfernung inhaltlich verwaist), dabei auch die "Lernziele"-Checkliste entschärft: das ☐-Symbol
      ist reiner Text (kein echtes Interaktionselement in `marked`), Formulierungen wie "Hake ab" /
      "Check off" wurden durch "Überprüfe selbst" / "Check for yourself" ersetzt, um keine Klickbarkeit
      vorzutäuschen. Lokales Fortschritt-Skript (`scripts/fortschritt.py` + `README-fortschritt.md`)
      komplett entfernt — Fortschritt läuft jetzt über den Account (Login/Sync), nicht mehr über
      manuellen JSON-Export/Import von einem CLI-Skript. Tests: `tests/zertifikate.spec.js`.
- [x] Zertifikat-PDF (Download, nur mit Account): pro verliehenem Wochen-Zertifikat ein
      herunterladbares PDF mit den Lernzielen der Woche, editierbarem Namensfeld, nur sichtbar wenn
      eingeloggt. E-Mail-Versand bewusst zurückgestellt (eigenes, späteres Thema). Details siehe
      HANDOFF.md 3.13.
- [x] `entferne-xp-texte` (HANDOFF.md 3.14, gemergt) — letzte Überbleibsel des
      alten Punktesystems entfernt: Präfix `+400 XP:`/`Huf-Punkte`/`Hoof Points`/`Cyber Credits` aus
      125 Boss-Quest-Feier-Prints (DE+EN, alle Varianten) gestrichen, plus drei Einzelfälle
      (`**Gesammelte XP:** 1500 Punkte`, "sammelst du 1000 XP"-Versprechen, Huf-Punkte in der
      Pferde-Siegerehrung Woche 1). Fiktive Story-Werte, die eine Übung selbst berechnet
      (Helden-Steckbriefe, Quest-Listen-Summen, Cyber-Credits-Rechenübung, HP-Zufallsereignisse),
      bewusst nicht angefasst — keine echte Belohnungsbehauptung ans reale Publikum.
- [x] `weeks-json-splitten` (HANDOFF.md 3.18, gemergt) — Refactoring Schritt 1:
      `content/python-checks/weeks.json` (3925 Zeilen, größte Datei im Repo) in `config.json` +
      `week-1.json`…`week-12.json` aufgeteilt, Round-Trip gegen alte Datei verifiziert. Neuer
      Node-Loader `content/python-checks/index.mjs` für die 3 betroffenen Tests (Vite-Browser-Seite
      nutzt weiter `import.meta.glob` in `useWeekChecks.js`, jetzt über mehrere Dateien gemerged).
- [x] `css-konsolidierung-kurslayout` (HANDOFF.md 3.19, gemergt) — Refactoring Schritt 2: den
      kompletten Sidebar/Lektionsliste-CSS-Block (~165 Zeilen, byte-identisch dupliziert zwischen
      `InteractiveCourse.vue` und `ProjectCourse.vue`) nach `src/assets/styles/course-layout.css`
      ausgelagert. `InteractiveCourse.vue` 547→386, `ProjectCourse.vue` 383→217 Zeilen. Per
      Playwright visuell verifiziert (`getComputedStyle()` + Screenshots), da CSS-Änderungen von
      den Funktionstests nicht erfasst werden.
- [x] `weeksection-subkomponenten` (HANDOFF.md 3.20, gemergt) — Refactoring Schritt 3: den
      Cheat-Sheet-Akkordeon-Block und die Varianten-Buttons aus `WeekSection.vue` in neue
      `CheatSheetList.vue`/`VariantSelector.vue` ausgelagert. `WeekSection.vue` 666→451 Zeilen.
      Dabei einen bestehenden CSS-Leak gefunden (`.cheat-sheet-header h4` bekam Border/Padding über
      eine generische Nachbar-Regel) und explizit in der neuen Komponente nachgebildet, damit sich
      am Rendering nichts ändert.
- [x] `lessonview-entflechten` (HANDOFF.md 3.21, gemergt) — Refactoring Schritt 4: Glossar/
      Content-Loading (Lektions-Markdown/Glossar laden, Tooltip-Spans einfügen) aus
      `LessonView.vue` in neues `src/composables/useLessonContent.js` ausgelagert, Task-Run/Check
      bleibt unverändert in der Komponente. `LessonView.vue` 684→586 Zeilen. Per Playwright
      verifiziert, dass Glossar-Tooltips weiterhin korrekt im Lektionstext erscheinen.
- [x] `quizstep-placementcourse-entflechten` (HANDOFF.md 3.22, gemergt) — Refactoring Schritt 5:
      `QuizStep.vue` bewusst NICHT gesplittet (beim genauen Lesen schon kohärent, keine natürliche
      Trennstelle wie bei LessonView.vue — keine erzwungene Abstraktion). Stattdessen bei
      `PlacementCourse.vue` echtes Duplikat beseitigt: `computePlacementResults`/`weekScoresToRows`
      neu in `useWeekChecks.js`, ersetzen zwei Stellen, die dieselbe Score-Zeilenform bauten.
      Refactoring-Plan damit im Kern abgeschlossen, nur Schritt 6 (Ternary-Cleanup) offen.
- [x] `ternary-cleanup` (HANDOFF.md 3.23, gemergt) — Refactoring Schritt 6: alle 97 Inline-
      `lang === 'en' ? X : Y`-Ternarys über 7 Components auf den bestehenden `t()`-Mechanismus
      (`locales/de.js`/`en.js`, jetzt 224 statt 166 Keys) umgestellt. Bewusst nicht migriert:
      Daten-Feld-Auswahl (`q.explanation_en`/`explanation` etc. — kein doppelt gepflegter UI-Text)
      und rein technische Ternarys (Locale-Code für `toLocaleString()`, Ordner-Pfad-Suffix). Geteilte
      Locale-Keys zwischen InteractiveCourse.vue/ProjectCourse.vue (`lessons.*`) und LessonView.vue/
      CodeChallenge.vue (`editor.*`) analog zum CSS-Konsolidierungs-Muster aus Schritt 2. Per
      Playwright auf Englisch durchgeklickt (Automatiktests laufen überwiegend auf Deutsch). Damit
      ist der komplette Refactoring-Plan (Schritte 1-6) abgeschlossen.

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
