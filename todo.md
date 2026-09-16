# Todo

## Now
### Wochen-Check: Variablen-Validierung (Branch `wochencheck-variablen-validierung`)
- [x] Lücke gefunden: Coding-Aufgaben, die das Anlegen bestimmter Variablen verlangen (z.B.
      "Erstelle eine Variable name..."), ließen sich durch bloßes Hart-Codieren der erwarteten
      Textausgabe umgehen — die Prüfung schaute nur auf `stdout`, nie auf den Programmzustand.
- [x] Neuer optionaler `variables`-Block in `validation` (`useTaskValidation.js`): prüft nach der
      Ausführung echte Werte im Pyodide-Namespace (`pyodide.globals.get(name)`), zusätzlich zur
      bestehenden Ausgabe-Prüfung. `CodeChallenge.vue` löscht die betroffenen Variablennamen vor
      jedem Lauf aus dem (geteilten) Namespace, damit ein alter Wert aus einem früheren Versuch
      nicht fälschlich als "bestanden" durchgeht.
- [x] Alle 24 Coding-Aufgaben (12 Wochen × 2) durchgesehen: 5 verlangen explizit benannte
      Variablen und sind jetzt mit `variables` abgesichert — Woche 1 "Nova"/`level`, Woche 2
      "alter", Woche 3 "zahl1"/"zahl2", Woche 8 "person"/"schueler" (verschachteltes Dictionary,
      siehe unten). Restliche Aufgaben verlangen keine benannte Variable in der Aufgabenstellung,
      daher (noch) kein Fix dafür — siehe Plan für Kategorie B/C unten bzw. `todo.md`-Eintrag.
- [x] `variables` unterstützt jetzt auch verschachtelte Werte (Dictionaries): erwarteter Wert als
      Objekt (`{"person": {"name": "Alex"}}`) statt Skalar → `CodeChallenge.vue` wandelt den
      Pyodide-PyProxy-Rückgabewert per `.toJs({dict_converter: Object.fromEntries})` in ein
      normales JS-Objekt um, `useTaskValidation.js`s `valuesMatch()` vergleicht rekursiv.
- [x] Neue Tests in `tests/zertifikate.spec.js`: hart kodierte Ausgabe ohne die Variablen (Woche 1)
      bzw. ohne das Dictionary (Woche 8) schlägt fehl, dieselbe Aufgabe mit echter Lösung besteht
      weiterhin. Woche 3 manuell verifiziert (gleicher Skalar-Mechanismus wie Woche 1, kein
      zusätzlicher automatisierter Test nötig).
- **Bewusst nicht angefasst:** der interaktive Kurs (`LessonView.vue`) nutzt dieselbe
  `validateOutput()`-Funktion, hat aber keine Aufgabe, die das Anlegen bestimmter Variablen
  verlangt — daher keine Content-Änderung dort nötig, die neue Prüfung steht dort aber genauso
  zur Verfügung, falls später gebraucht.
- [x] **Kategorie B (Funktionsaufgaben):** Woche 5 (`verdopple`, `addiere`) ließ sich mit dem
      `variables`-Mechanismus nicht sauber fixen, da nur der eine vorgerechnete Aufruf geprüft
      würde. Neues optionales `functionCalls`-Feld (`[{name, args, expected}]`): ruft die
      Funktion nach der Ausführung erneut mit einem in der Aufgabenstellung nie genannten Wert
      auf (`verdopple(10)` statt nur `verdopple(6)`) — deckt auch auf, wenn eine Funktion nur
      zufällig für das eine Beispiel stimmt (z.B. `zahl + 6` statt `zahl * 2`, beide ergeben 12
      für `verdopple(6)`, aber nur `*2` stimmt auch für `verdopple(10) == 20`). Getestet: genau
      dieser "zufällig richtig"-Fall schlägt jetzt fehl, echte Lösung besteht weiterhin (beide
      Woche-5-Aufgaben).
- **Kategorie C (Modul-Import-Check, Woche 7/12) und AST-Analyse für den Rest — zurückgestellt,**
  siehe HANDOFF.md 3.34.

### 12-Wochen-Kurs: Zellen-Format-Umstellung (Branch `12-wochen-kurs-zellen-format`)
- [x] Alle 432 Notebooks (3 Varianten × 12 Wochen × 6 Typen × DE/EN) vom `.ipynb`-Format auf
      Zellen-Ordner (`NN_markdown.py`/`NN_code.py`) migriert, byte-exakt gegen `git HEAD`
      verifiziert. Details siehe HANDOFF.md 3.33.
- [x] Permanenter Build-Schritt (`scripts/build_cell_notebooks.py`, gitignored Output), in
      `npm run dev`/`prebuild` eingehängt
- [x] Download-ZIPs (`pack_notebooks.py`) auf `_bundle/*.py` umgestellt, Cheat-Sheets weiterhin
      als `.ipynb` mit im Zip
- [x] `JupyterNotebook.vue`/neue `CodeCell.vue`: CodeMirror 6 mit Autocomplete statt Textarea,
      Marken-CI-Design (Lila/Orange/Gelb)
- [x] `WeekSection.vue`: Wochen-Header redesignt (kurzer Titel + Kurztext, Lila-Akzentleiste)
- [x] `useWeeklyContent.js`: zwei getrennte URLs (`renderUrl`/`downloadUrl`) pro Notebook
- [x] Tests (`site.spec.js`, `storytelling-content.spec.js`) auf CodeMirror-taugliche Helper
      umgestellt
- [x] Nebenbei gefunden und gefixt: Pferde Woche 11 Lektion hatte 6 Methoden ohne `def`/`self`
      (gleiches Bug-Muster wie der frühere Sci-Fi-Fix)
- [x] `npm run test:checks` + `npm test` vollständig grün bestätigt
- [x] Kursbeschreibung (`beschreibung.md`, DE+EN) bereinigt: "Einstufung – wo soll ich starten?"
      war inhaltlich fast wortgleich mit der separaten `.placement-banner`-Komponente, die direkt
      danach auf der Seite erscheint (zwei Boxen mit derselben Aussage hintereinander) — Abschnitt
      entfernt, Banner bleibt die einzige Quelle dafür. "Für wen ist der Kurs?" direkt nach die
      Zielbeschreibung vorgezogen (bessere Reihenfolge: Ziel → Zielgruppe → Aufbau)

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
- [x] `woche8-list-comprehension-glossar` — unerklärte List Comprehension per grep über alle 444
      Notebooks gesucht (nicht nur Woche 8 Abenteuer wie ursprünglich gedacht): betraf Woche 6
      Pferde+Sci-Fi UND Woche 8 alle 3 Varianten (Woche 6 Abenteuer und Woche 8 selbst nutzen sie
      nirgends unangekündigt). Neuer Glossar-Begriff "List Comprehension" in allen 10 betroffenen
      Dateien × DE/EN ergänzt (ans Ende der Begriffstabelle). `6_loesungen`-Dateien bewusst nicht
      angefasst (auch dort List Comprehensions gefunden, aber Lösungsdateien sind kein Lehrmittel
      wie die Lektion, dürfen fortgeschrittenere Varianten zeigen)
- [x] `woche7-math-aufwerten` — wieder ein Fund, der nur bei Abenteuer stimmte: Pferde und Sci-Fi
      hatten `math` schon immer als vollwertigen Abschnitt (nicht als Bonus), nur Abenteuer degradierte
      es zum "Exkurs (Bonus), nicht Teil der Prüfungen". Abenteuer-Lektion (DE+EN) auf denselben
      Umfang wie Pferde/Sci-Fi gebracht (3 Beispiele: Konstanten+Kreisberechnung, Grundwerkzeuge,
      Trigonometrie/Logarithmen/Fakultät), Intro-Mission-Bullet + Glossar (4 neue math-Begriffe)
      ergänzt. Pferde/Sci-Fi unverändert (waren schon korrekt)
- [x] `woche11-lernziele-anpassen` — "Design Patterns"/"Komposition vs. Vererbung" komplett
      gestrichen (zu fortgeschritten für den Rahmen der Lektion): nicht nur `woche11.md`
      (DE+EN), sondern auch die "Design Patterns für ..."-Mission-Bullets in allen 6
      Lektion-Intros (3 Varianten × DE/EN) und die "☐ Design Patterns erkennen"/"☐ Komposition vs
      Vererbung"-Checkliste in den Missionen von Pferde+Sci-Fi (× DE/EN) — Abenteuer-Missionen
      hatten die Checkliste nie. Alle Fundstellen per grep verifiziert, danach 0 verbleibende
      Erwähnungen
- [ ] `woche12-interaktivitaet` — Event-Handling-Beispiel (`onscreenclick`/`onkey`) ergänzen, da
      "Interaktive Grafik erstellen" bisher unerfülltes Lernziel ist. War blockiert durch den
      Turtle-Pyodide-Bug (siehe unten) — jetzt entblockt, da der Shim `onscreenclick`/`onkey`/
      `listen()` bereits als sichere No-Ops unterstützt (nur echtes Event-Wiring fehlt noch)

### Turtle-Grafik lief nie im Browser (Branch `turtle-pyodide-shim`, gemergt)
**Kritischer, unabhängig entdeckter Bug:** Beim Testen von `woche12-interaktivitaet` (s.o.) stellte
sich heraus, dass `import turtle` in der echten Browser-Umgebung (Pyodide 0.24.1) mit
`ModuleNotFoundError` fehlschlägt — Pyodide hat `turtle` aus der Standardbibliothek entfernt
(basiert auf tkinter, das im Browser keinen Anzeige-Server hat). Verifiziert: auch die bereits
produktiven, unveränderten Beispiele (nicht nur meine neuen) schlagen exakt gleich fehl — das war
**für alle Nutzer:innen die ganze Zeit über kaputt**, unentdeckt, weil kein Test je echten
Turtle-Code im Browser ausgeführt hat (nur Text-Inhalt der Notebooks wurde geprüft).
- [x] Eigenen Python-Shim in `usePyodide.js` geschrieben, der `sys.modules['turtle']` mit einer
      eigenen, Canvas-basierten Implementierung belegt (kein externes Paket — siehe Recherche zu
      `basthon-turtle`/RaspberryPiFoundation/pygame-ce, alle brauchten entweder einen Web Worker
      [nicht kompatibel mit der bestehenden `input()`-über-`window.prompt()`-Architektur, siehe
      HANDOFF.md 3.5] oder waren unmaintained/ohne Interaktions-Support). Deckt die komplette,
      per grep über alle 444 Notebooks ermittelte API-Oberfläche ab (Turtle/Screen, forward/left/
      right, penup/pendown, goto, color/fillcolor, begin_fill/end_fill, circle, dot, write, speed,
      shape als No-Op, hideturtle, onscreenclick/onkey/listen als sichere No-Ops).
- [x] `JupyterNotebook.vue`: neuer `<div class="turtle-canvas-container">` pro Code-Zelle, in den
      der Shim bei `turtle.Screen()`/`turtle.Turtle()` ein `<canvas>` zeichnet.
- [x] Dabei einen echten, bisher nie bemerkten Content-Bug gefunden und gefixt: Pferde-Lösungen
      Woche 12 hatte eine tote Schleife, die 3er-Tupel in 2 Variablen entpacken wollte
      (`ValueError: too many values to unpack`) — Überbleibsel eines verworfenen Entwurfs, direkt
      darunter stand schon die korrekte Version. EN-Pendant war bereits sauber.
- [x] Neue dauerhafte Tests in `tests/site.spec.js` ("Turtle-Grafik im Browser (Pyodide-Shim)"):
      prüfen echte Pixel auf dem Canvas (nicht nur "kein Fehler"), einmal für Linien, einmal für
      `begin_fill()`/`end_fill()`.
- Getestet: alle 3 Varianten × Lektion/Missionen/Debug/Boss-Quest/Lösungen manuell per Playwright
  durchgeklickt (kein Fehler außer dem absichtlichen Debug-Bug `import Turtle` mit großem T).
  EN-Inhalte technisch identisch zu DE (gleiche turtle-Aufrufe), nicht separat durchgeklickt.
- **Bewusst nicht gebaut:** echtes Event-Handling für `onscreenclick`/`onkey` (Klick-/Tasten-Reaktion
  im Canvas) — aktuell nutzt kein einziges der 444 Notebooks diese Funktionen wirklich (nur
  Bonus-Erwähnungen in Missions-Texten), daher zurückgestellt für `woche12-interaktivitaet`.
- **Bekannte Vereinfachungen** (bewusst, für "einfachste Lösung, die läuft"): keine Animation/
  `speed()`-Verzögerung (alles zeichnet sofort), kein sichtbarer Turtle-Cursor/keine `shape()`-Grafik,
  `tracer(0)`+`update()` sind No-Ops (ein Beispiel mit animiertem Pferderennen bei ausgehobenem Stift
  zeigt dadurch keine sichtbare Bewegung mehr — nur in einer Lösungsdatei, kein Kernproblem).

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
