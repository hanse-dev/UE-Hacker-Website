# Todo — erledigt (kalt)

Ausgelagert aus `todo.md` (frühere Abschnitte "Now" und "Fertige Branches"). Nicht per `@` importiert, nur bei Bedarf lesen.

## Now

### JS-Grundkurs (Branch `js-grundkurs-woche1-experiment`)
Curriculum-Plan siehe `KURSPLAN.md` "JavaScript-Track: Grundkurs" (9 Wochen, leichtes Format).
- [x] Mehrwochen-Architektur (Wochenauswahl `JsGrundkursTour.vue`, `?week=`-Deep-Link, freie
      Wochen-Navigation, `JsCourseTour.vue` um `weekLabel`-Prop erweitert) — siehe HANDOFF.md 3.43
- [x] Woche 1: JS-Grundlagen (siehe HANDOFF.md 3.42)
- [x] Woche 2: Bedingungen (siehe HANDOFF.md 3.43)
- [x] Woche 3: Schleifen (siehe HANDOFF.md 3.43 Nachtrag)
- [x] Woche 4: Funktionen (siehe HANDOFF.md 3.43 Nachtrag) — führt `functionCalls`-Hidden-Tests
      ein; dabei gefundene Sandbox-Einschränkung für Woche 9 relevant (s.u.)
- [x] Woche 5: Arrays (siehe HANDOFF.md 3.43 Nachtrag) — **Achtung:** `variables`/
      `functionCalls.expected` können kein Array als erwarteten Wert nutzen (`valuesMatch()`
      vergleicht Arrays nur per `===`, nie inhaltlich — würde selbst bei korrekter Lösung immer
      fehlschlagen). Nur Skalare validieren, die aus einem Array abgeleitet sind (Summe, Anzahl,
      Element). Ein Array als reines Funktions-**Argument** ist dagegen unproblematisch.
- [x] Woche 6: Objekte (siehe HANDOFF.md 3.43 Nachtrag) — Objekte unterstützen (anders als Arrays)
      die rekursive `variables`/`functionCalls`-Prüfung ganz normal, ein Objekt-Literal darf also
      direkt als erwarteter Wert genutzt werden.
- [x] Woche 7: DOM & Interaktivität (siehe HANDOFF.md 3.43 Nachtrag) — neue `validation.type`-Werte
      `dom_text`/`dom_click_text` (Feld `text`, bewusst nicht `expected` — siehe HANDOFF.md),
      festes DOM-Übungs-Markup `#dom-uebung` in `useJsSandbox.js`. Dabei einen echten Bug gefunden:
      Canvas + DOM-Markup gleichzeitig im iframe sprengte die feste 300px-Höhe — gelöst mit zwei
      srcdoc-Varianten (`domMode`-Prop, durchgereicht bis `JsSandboxFrame.vue`), `js-spielewerkstatt`
      unverändert (Default `false`).
- [x] Woche 8: Objekte als Blaupause (Klassen, siehe HANDOFF.md 3.43 Nachtrag) — bestätigt: keine
      `functionCalls`-Hidden-Tests auf Klassen-Methoden möglich (wie in Woche 4 vorhergesagt),
      `variables`-Checks auf ganze Instanzen funktionieren aber (JSON.stringify einer Instanz
      enthält nur Properties, keine Prototyp-Methoden). **Ursprünglich Woche 9**, auf Nutzer-Wunsch
      mit dem Abschlussprojekt getauscht (siehe HANDOFF.md 3.43 Nachtrag "Woche 8 ↔ 9 getauscht") —
      ein Abschlussprojekt sollte alles einschließen können, auch Klassen.
- [x] Woche 9: Abschlussprojekt (siehe HANDOFF.md 3.43 Nachtrag) — Mini-Quiz kombiniert Wochen 2-8,
      inkl. einer eigenen `Frage`-Klasse für das Fragen-Array, bewusst kein neues Konzept.
- [x] Auf der Seite eingebunden (siehe HANDOFF.md 3.43 Nachtrag "auf der Seite eingebunden") —
      echter `kurse.json`-Eintrag `js-grundkurs`, `/kurs/js-grundkurs` über `CourseDetail.vue`
      (neuer `isJsGrundkurs`-Zweig), in der Startseiten-Kursübersicht sichtbar. Kein
      `/experiment/...`-Pfad mehr, `src/views/experiment/` entfernt (Dateien nach
      `src/components/` verschoben). **Der komplette 9-Wochen-Plan aus KURSPLAN.md ist damit
      fertig und live im normalen Kurs-Menü** — kein offener Punkt mehr zu diesem Thema.
- [x] Homepage konsistenter gestaltet (siehe HANDOFF.md 3.44) — Format-Badges auf Kurskarten
      (`kurse.json`-Feld `format`), Projekte-Teaser/Unterstützer auf einheitliche Karten-Optik
      umgestellt, Hero auf 2 sprachneutrale CTAs ("Zu den Kursen"/"Zu den Projekten") reduziert,
      Einstufungstest-Hinweis von dort in die Kursübersicht verschoben.
- [x] `/projekte`-Filterleiste gruppiert (siehe HANDOFF.md 3.44 Nachtrag) — eigene Überschrift
      "Filtern nach" + Reset-Button rechtsbündig, Grid statt freiem Wrap, Icons pro Kategorie.

*(Sonst nichts weiter offen — `kurs-projekte-uebersicht`, `kurs-js-spielewerkstatt`,
`profil-abschluss-badges` und `nav-projekte-link` sind alle nach `main` gemergt, siehe
"Fertige Branches" unten. Server-Deploy steht noch aus, siehe HANDOFF.md Abschnitt 5 "Betrieb".)*

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
- [x] `woche12-abschlussprojekt` (Branch `woche12-abschlussprojekt`) — ersetzt das geplante
      `woche12-interaktivitaet`: Turtle komplett aus dem Grundkurs entfernt (passte nicht mehr zum
      Rest, lief zudem nie nativ im Browser). Woche 12 ist jetzt ein **Abschlussprojekt Text-Adventure**
      (je Variante eine eigene Geschichte: Drachenhöhle / Reiterhof bei Nacht / Notfall auf Nebula-7),
      wendet alles aus Woche 1–11 an, einziger neuer Begriff: Komposition ("hat ein"). Alle 3
      Varianten × DE/EN, neue Wochen-Checks, Turtle-Distraktoren in Woche 5/9/11 ersetzt. Details
      siehe HANDOFF.md 3.46. Der Turtle-Shim bleibt bewusst im Code (für das Backlog-Projekt
      "Turtle-Mandala", siehe `PROJEKTIDEEN.md`).

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
- [ ] `kurs-python-spiele` — Idee verworfen zugunsten von `kurs-js-spielewerkstatt` (s.u. "Nächste
      Themen"): Pyodides synchrones Ausführungsmodell ist mit einer echten Spiele-Loop
      unvereinbar (siehe HANDOFF.md 3.32).
- [x] `kurs-projekte-uebersicht` — `ProjectCourse.vue` generalisiert (`contentPath`-Prop statt
      hart codiertem Cäsar-Chiffre, `kurse.json`-`type`-Feld statt ID-Vergleich in
      `CourseDetail.vue`), neue Projekte-Übersicht mit Filtern (Sprache/Level/Thema/Dauer) unter
      `/projekte` (`ProjekteView.vue`), zwei neue Projekt-Kurse (`projekt-morsecode`,
      `projekt-zahlendetektiv`). Projekt-Kurse erscheinen nicht mehr auf der Startseite, sondern
      nur noch gesammelt unter `/projekte`; der 12-Wochen-Kurs-Banner verlinkt jetzt dorthin statt
      fest zu Cäsar-Chiffre. `useLessonContent.js`-Globs auf Wildcard umgestellt (kein manuelles
      Nachtragen pro neuem Projekt-Kurs mehr nötig). Details siehe `INHALTE.md` §6.
- [x] `kurs-js-spielewerkstatt` (HANDOFF.md 3.39, gemergt) — erster JS- statt
      Python-Projekt-Kurs: neue iframe-Sandbox (`useJsSandbox.js`/`JsSandboxFrame.vue`, kein
      Pyodide, kein Web Worker), `JsLessonView.vue` als JS-Pendant zu `LessonView.vue`, neue
      `engine`-Prop an `ProjectCourse.vue`. Sechs Lektionen "Fang den Ball". Details siehe
      HANDOFF.md 3.39.
- [x] `wochencheck-variablen-validierung` (HANDOFF.md 3.34, gemergt) — Coding-Aufgaben ließen sich
      durch Hart-Codieren der erwarteten Textausgabe umgehen (Prüfung schaute nur auf `stdout`).
      Neue optionale `variables`-/`functionCalls`-Felder in `validation` prüfen zusätzlich echte
      Werte im Pyodide-Namespace bzw. rufen Funktionen mit einem nie genannten Wert erneut auf.
      5 von 24 Coding-Aufgaben betroffen und abgesichert (Kategorie C/AST-Analyse zurückgestellt).
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
- [x] `experiment-wochen-tour` (HANDOFF.md 3.35+3.36, gemergt) — begann als unverlinktes Experiment
      (Kachel-Auswahl Woche→Thema, Fortschritts-Leiste, Verzweigung Missionen→Extra-Herausforderung/
      Check, Zertifikat-Reveal, Wochen-Übersicht mit Themen-Icons + verbindendem Pfad), wurde nach
      Nutzer-Feedback zur **echten** Kursseite unter `/kurs/python-12-wochen-grundkurs` — alte
      Akkordeon-UI (`WeekSection.vue`, `MissionenPanel.vue`, `VariantSelector.vue`,
      `CheatSheetList.vue`) entfernt, 42 von 59 betroffene Tests in 6 Dateien portiert. Cheat-Sheets
      + Wochen-ZIP-Download mit übernommen, alte `?week=&tab=`-Deep-Links (Einstufung,
      Cäsar-Chiffre) funktionieren unverändert weiter (intern übersetzt). Details: Plan-Datei
      `~/.claude/plans/twinkly-strolling-lovelace.md`.
- [x] `profil-abschluss-badges` (HANDOFF.md 3.41, gemergt) —
      neue Login-gated Seite `/profil` mit Abschluss-Abzeichen pro Projekt-Kurs (🏅/🔒, kein
      Zertifikat/PDF/Quiz — bewusst leichtgewichtig, passend zum Projekt-Kurs-Format aus
      `VISION.md`). Neue `useProjectBadges.js`, nutzt denselben Fortschritts-Mechanismus wie
      `ProjectCourse.vue` selbst. Nebenbei gefunden: Projekt-Kurs-Fortschritt wurde nie mit dem
      Account synchronisiert — `useProgressSync.js` auf Präfix-Erkennung umgestellt, deckt jetzt
      automatisch jeden (auch künftigen) Projekt-Kurs ab.
- [x] `nav-projekte-link` (HANDOFF.md 3.40, gemergt) — direkter "Projekte"-Link im Header neben
      "Kurse", bisher nur über Teaser/Banner erreichbar.

---


## Lektions-Format Woche 1–12 — abgeschlossene Nachbesserungen

Ausgelagert aus `todo.md` am 2026-09-23 (Kontext-Hygiene: erledigte Punkte kosten Tokens in jeder
Session, siehe WORKFLOW.md "HANDOFF.md aufräumen"). Offene Reste stehen weiter in `todo.md`.

- [x] Glossar-Notebooks (`0_glossar`) Woche 3–12 an die Lektionen angeglichen: Vorgriffe entfernt (Woche 4 Listen/`append`/Index, Woche 5 `try`/`except` in Pferde+Sci-Fi, Woche 8 `.update()`), Wiederholungs-Verweise korrigiert (Woche 5–7, 9), Woche-6-Tabelle repariert und um Listen ergänzt, Woche 10 Doppelzeile; Test `Glossare: keine Vorgriffe` in `tests/storytelling-content.spec.js`. Bewusst gelassen: `snake_case`/Algorithmus/Instanz (Konzepte ohne eigene Aufgabe), Woche 7 Pferde/Sci-Fi mit kleinerer Begriffsliste als Abenteuer.

### 12-Wochen-Kurs: Lektions-Format (Branch `python-woche1-lektionen-format`)
- [x] Woche 1 + 2 (Abenteuer, Pferde, Sci-Fi; DE + EN) als Einzel-Lektionen im JS-Kurs-Format (siehe HANDOFF.md 3.47)
- [x] Woche 4 (Schleifen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.48).
- [x] Woche 4: DE/EN-Struktur angeglichen (Abenteuer 8, Pferde 7, Sci-Fi 7 Lektionen; IDs/Aufgaben identisch, EN/DE jeweils als Übersetzung der größeren Fassung)
- [x] Woche 5 (Funktionen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.49), ohne Sub-Agenten aus einer Datenquelle pro Thema erzeugt
- [x] Woche 6 (Listen; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.50): 9 Lektionen, Debug, 3 Missionen, 3 Extra-Herausforderungen je Thema, DE = EN; enthält die nachgezogenen Vorgriffe (Listen, `append`, `break`/`continue`, Funktionen mit Listen)
- [x] Woche 7 (Module; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.51): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN; Zufalls-Aufgaben prüfen Eigenschaften statt fester Werte; nimmt die Woche-4/5-Vorgriffe mit `random`, `%` und Feld auf (Extra-Herausforderung 4)
- [x] Woche 8 (Dictionaries/Tupel; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.52): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN; enthält die nachgezogenen Dictionary-/`try/except`-Vorgriffe aus Woche 5/6
- [x] Woche 9 (JSON und Dateien; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.53): 7 Lektionen, Debug, 3 Missionen, 4 Extra-Herausforderungen je Thema, DE = EN
- [x] Woche 10 (OOP Grundlagen), Woche 11 (OOP Fortgeschritten), Woche 12 (Text-Adventure-Abschlussprojekt; Abenteuer, Pferde, Sci-Fi; DE + EN) im Lektions-Format (siehe HANDOFF.md 3.54): je 7 Lektionen/Etappen, Debug, 3 Missionen, 4 Extra-Herausforderungen, DE = EN
- [x] Lösungs-Notebooks passen zu den Aufgaben (aus Referenzlösungen erzeugt, siehe Abschnitt „Lösungen“ oben). Glossar: siehe offener Punkt „Glossar-Notebooks“.

#### Woche 4
- [x] Glossar (Woche 4) bereinigt. Lernziele-Checklisten der Original-Missionen (Woche 4: Listen/`append`/Index/`break`/`continue`; Woche 5: `try/except`) bereinigt. Offen blieb damals: die Original-Missionen/-Boss-Notebooks selbst enthielten Listen-Aufgaben (Bonus/Boss), lagen nur noch im ZIP — seit 3.55 sind die alten Notebooks ganz entfernt, der ZIP-Download wird aus dem Lektions-Format generiert.
- [x] `end=""` ist jetzt in Pferde DE/EN und Sci-Fi EN Lektion 7 erklärt; mehrzeilige `expected` mit `\n` (82 Aufgaben) in der App per Wegwerf-Test bestätigt.
- [x] Pferde DE Boss 3: "Noch 1 Runden" (Plural bei 1) — kosmetisch, DE+`expected` gemeinsam geändert.

#### Woche 3 (Angleichung DE/EN)
- [x] Pferde DE `boss-03`: Anweisung nennt "Kein Turniersieg", `expected` ist "Kein Turniersieg." (mit Punkt) — DE + EN vereinheitlicht.
- [x] Sci-Fi DE/EN `boss-03`: "Gesamtpunkte: 320 und Erfolgsquote: 80.0%" — "in zwei Zeilen" ergänzt.
- [x] Lösungs-Notebooks passen zu den Aufgaben (aus Referenzlösungen erzeugt).

#### Woche 5 (Funktionen)
- [x] `LessonView` prüfte nur die Ausgabe: erledigt über `validation.codeContains` (Woche 3–12 automatisch aus der Aufgabenstellung abgeleitet, siehe INHALTE.md); hart codiertes `print` besteht dort nicht mehr.
- [x] Lösungs-Notebooks Woche 5 passen zu den Aufgaben.

#### Woche 6 (Listen)
- [x] Aus dem Original wieder aufgenommen: Slicing (`[0:3]`, `[-2:]`, `[1::2]`), `extend()`, `sorted(set(...))`, `sorted(..., key=len)`, `.upper()` in der List Comprehension (je eine Zusatzaufgabe in Lektion 2/3/5/6/9).
- [x] Woche-2-Extras (8 Truhen/Säcke/Module, 5 Zauber/Übungen/KI-Modelle) und Woche-4-Mengen (Zahlen 1–20 gerade/rückwärts, sortierte Ereignis-Liste) mit den vollen Original-Mengen als Extra-Herausforderung 4 "Wiederholung" nachgezogen.
- [x] Boss 3 themenspezifisch benannt (Pferde `erstelle_turnier`/`turniere`, Sci-Fi `erstelle_mission`/`missionen`).
- [x] Woche-4-Vorgriffe mit `random`, `%` und dem 8×8-Feld sind in Woche 7 (Extra-Herausforderung 4) nachgezogen (Zufallswerte/-ereignisse/-weg, Primzahlen bis 100, Schachbrett, Figur über das Feld).
- [x] Dictionaries aus den Originalen sind in Woche 8 (Extra-Herausforderung 4) als Wiederholung nachgezogen.
- [x] Lösungs-Notebooks Woche 6 passen zu den Aufgaben.

#### Woche 7 (Module)
- [x] Lösungs-Notebooks Woche 7 passen zu den Aufgaben.

#### Woche 1–2
- [x] `max()` (kam in Woche 2 Abenteuer DE/EN Boss 1 und Pferde EN Boss 1 als Vorgriff vor) durch Vergleich mit `>` ersetzt (Lektions-JSON, Boss-Text, Lösungs-Notebook)
- [x] `//`, `%`, `**` (nur Sci-Fi EN Woche 2 Lektion 6, im Original und in allen anderen Themen nicht) entfernt
- [x] Woche 3: DE/EN je Thema angeglichen (Abenteuer 7 Lektionen + 4 Bugs, Pferde/Sci-Fi 6 Lektionen; IDs/Aufgaben DE = EN, Sci-Fi 4 Bugs, Pferde 3), Struktur per Skript + `python-lektionen-format.spec.js` geprüft
- [x] Alte Notebooks (Lektion/Debug/Missionen/Boss) aller Wochen entfernt (waren nicht mehr in der Tour, nur noch ZIP-Download-Quelle). ZIP-Download baut jetzt `scripts/build_lesson_bundle.py` direkt aus dem Lektions-Format + Referenzlösungen: eine lauffähige `.py`-Datei je Woche/Variante/Sprache (Glossar, Lektionen, Debug, Missionen, Extra-Herausforderungen inkl. Lösungen), DE **und** EN (vorher nur DE). `scripts/pack_notebooks.py` neu geschrieben, `NOTEBOOK_TYPES` in `useWeeklyContent.js` auf `0_glossar`/`6_loesungen` reduziert, veraltete Tests (`notebooks.spec.js`, `wochen-tour.spec.js`, `storytelling-content.spec.js`) auf das Lektions-Format umgestellt. Dabei gefunden und mitbehoben: `JsCourseTour.vue` sprang beim Öffnen von Glossar/Lösungen mitten in einer Lektion zurück auf Lektion 1 (Komponente wird beim Referenz-Wechsel neu gemountet) — startet jetzt bei der ersten noch offenen Lektion.
- [x] `input()`-Aufgaben (Woche 1, 2) prüfen jetzt mit `validation.stdin` und der daraus berechneten Ausgabe statt nur festen Textteilen.
- [x] Woche 2 DE/EN angeglichen (Branch `python-lektionen-nacharbeiten`): Abenteuer + Pferde (größere
      Fassung als Referenz), Sci-Fi ausnahmsweise umgekehrt (EN war größer — 7 Lektionen/46 Aufgaben —
      DE wurde an EN angeglichen). Sci-Fi: `lessons.json` + alle `.md`-Dateien neu geschrieben,
      39 Referenzlösungen (Beispiel-Aufgaben ausgenommen) einzeln mit `python3` gegen `validation`
      geprüft, `woche2_scifi_6_loesungen`-Zellenordner neu erzeugt, `build:cells`/
      `python-lektionen-format.spec.js`/`build_lesson_bundle.py` grün, `npm run test:checks` voll
      grün (340 Tests).

#### Woche 8 (Dictionaries/Tupel)
- [x] `dict`/`try`-Struktur: `try`/`except`, `def`, `json.*`, `csv.*` werden über `validation.codeContains` geprüft (siehe Woche 5); `dict` selbst nicht (kein eindeutiger Baustein).
- [x] Lösungs-Notebooks Woche 8 passen zu den Aufgaben.

#### Woche 10–12 (OOP, Text-Adventure)
- [x] Struktur (`class`, `super()`, Magic Methods, `isinstance`) wird über `validation.codeContains` geprüft; Rest-Lücke: Bausteine in Texten/Kommentaren zählen nicht als Umgehung, aber `print("class")` zählt als Vorkommen (bewusst einfach).
- [x] Lösungs-Notebooks Woche 10–12 sind aus den Referenzlösungen der Aufgaben neu erzeugt (eine Zelle je Aufgabe, Debug mit Erklärung). Offen blieb nur das Glossar von Woche 10–12 (erwähnt teils Themen der Original-Aufgaben).
- [x] `tests/storytelling-content.spec.js` liest aus dem Lektions-Format (Woche 5/8/9/11/12) statt aus den entfernten alten Notebook-Quelldateien.

#### Woche 9 (JSON und Dateien)
- [x] Lösungs-Notebooks Woche 9 passen zu den Aufgaben.

### JavaScript-Spielewerkstatt — Branch `kurs-js-spielewerkstatt` ✅ gemergt
Ersetzt die frühere Idee einer Python-Spiele-Werkstatt: Pyodides synchrones "einmal ausführen"-
Modell ist mit einer echten Spiele-Loop (requestAnimationFrame, laufende Tasten-/Maus-Events)
unvereinbar (siehe HANDOFF.md 3.32) — daher JavaScript statt Python, mit einer neuen
iframe-Sandbox-Ausführungsumgebung. Kompaktes Projekt (6 Lektionen, wie Cäsar-Chiffre), erstes
Spiel "Fang den Ball". Details siehe HANDOFF.md 3.39.
- [x] Neue JS-Sandbox-Ausführungsumgebung (`useJsSandbox.js`, iframe-basiert, kein Worker)
- [x] `engine`-Prop an `ProjectCourse.vue`/`CourseDetail.vue` ergänzt (Default `'pyodide'`)
- [x] Kursmetadaten in `kurse.json` (`engine: "js-sandbox"`, `language: "javascript"`, `level`,
      neuer Tag `spiele` im Projekte-Filter-Vokabular, inkl. neuer `projectTag.spiele`-Locale-Keys)
- [x] Content: 6 Lektionen "Fang den Ball" (DE-first, kein `-en`-Ordner wie Cäsar-Chiffre)
- [x] Playwright-Tests (`tests/js-spielewerkstatt.spec.js`, 12 Tests) + `tests/projekte.spec.js`
      angepasst → volle `test:checks`-Suite grün.
- [x] `KURSPLAN.md`/`VISION.md` geprüft — keine Abweichung vom dortigen Track-Modell nötig (JS-Projekt-Kurs passt unverändert ins bestehende Schema)
