# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-03  
> **Aktueller Stand:** `main` enthält jetzt PR #1–#4, die Storytelling-Überarbeitung (3.4), den
> Endlosschleifen-Schutz + Sci-Fi-Debug-Ziele, die Einstufungstest-Fixes (3.5/3.6), den gestuften
> Hinweis im interaktiven Kurs (3.7), den kompletten Text-Tippfehler-Pass (3.8), das
> SQLite-Backup-Script (Abschnitt 4) sowie das neue Cäsar-Chiffre-Projekt (3.11) —
> `debug-notebook-safety`, `et-fixes`, `interaktiv-klarer`, `text-typo-pass`, `backup-sqlite-db`
> und `kurs-caesar-chiffre` sind gerade gemergt worden. Nur noch ein Branch fehlt in dieser
> Session: `wochen-zertifikate`.  
> **Ziel dieser Datei:** Kontext für die nächste Session (Mensch oder Claude), ohne Chat-Historie.

Projekt-Regeln immer mitlesen: `CLAUDE.md`, `WORKFLOW.md`, `INHALTE.md`, `todo.md`.

---

## 1. Was ist das Projekt?

Lernplattform für Kinder/Jugendliche (Python) — Vue 3 + Vite, Notebooks unter `content/`, Docker-Deploy.

**Live/Prod-Modell:** Ein Node-Prozess (`api/`) liefert `/api/*` **und** das gebaute Frontend (`dist/`) auf Port **8080**. Service-Name in Compose: **`app`** (nicht mehr `prod`).

---

## 2. Git / PRs (erledigt)

| PR | Branch | Inhalt |
|----|--------|--------|
| #1 | `python-lernpfad-quiz` | Einstufung + Wochen-Checks, Tests, alter Lernpfad entfernt |
| #2 | `admin-login` | Express+SQLite API, Admin, Login, Progress/Notebook-Sync, Single-Port-Deploy |
| #3 | `fix-notebook-sync-loop` | Hotfix: Notebook-Blink-/Reload-Schleife bei eingeloggt+Sync |

`main` ist der Integrationsstand. Feature-Branches oben sind historisch; neue Arbeit immer **neu von `main`**.

**Lokale uncommittete Docs (Stand dieser Session):** ggf. noch `HANDOFF.md` / `todo.md` / `WORKFLOW.md` dirty — bitte committen, wenn der Handoff final ist.

---

## 3. Was sich geändert hat (Zusammenfassung der großen Features)

### 3.1 Einstufung & Checks (PR #1)

- Kurs `python-einstufung`; Fragen in `content/python-checks/weeks.json`
- Pro Woche Tab **Check**; Multi-Select; gemischte Optionen
- Placement: Fragen pro Woche; bei 100 % Projektideen
- Deep-Link öffnet 12-Wochen-Kurs mit Notebooks
- Playwright: `npm run test:checks` + Pre-commit `.githooks/pre-commit`

### 3.2 Admin, Accounts, Sync, Deploy (PR #2)

**API (`api/`):**
- Express, SQLite über **`node:sqlite`** (Node **≥ 22**, kein better-sqlite3)
- Tabellen: `users`, `progress`
- Admin: `POST /api/admin/login`, CRUD `/api/admin/users` (Bearer Admin-Token)
- Learner: `POST /api/login`, `GET /api/me`, `GET|PUT /api/progress`
- Env: Projektroot `.env` — **`ADMIN_PASSWORD` Pflicht**; geladen **nur beim Prozessstart**
- DB-Datei: `api/data/ue-hacker.sqlite` (gitignored; Volume in Docker)

**Frontend:**
- `/admin` — User anlegen (`kinder` | `jugendliche`)
- Header **Optionen** → Modal: Sprache DE/EN, Konto, Anmelden/Abmelden
- Sync-Keys u.a.: `ue-hacker-fortschritt`, `ue-hacker-week-checks`, Interactive, `ue-hacker-notebook-state-*`
- Merge: pro Key, neueres `updatedAt` gewinnt → lokal + Server (`useProgressSync.js`, `progressMerge.js`)
- Ohne Login: alles bleibt lokal

**Einstufung UX (auch PR #2-Zeitraum):**
- Pro Frage **Prüfen**; Zwischenstand in `placement.session` in week-checks-Storage
- Wird mit Account mitgesynct

**Deploy:**
- `Dockerfile`: Build Frontend → Image mit API + `dist`
- `docker compose up -d --build app` → `:8080`
- **Nicht** mehr: `docker-compose up … prod` (Service existiert nicht → Fehler + Orphans)
- Alte Orphans: `docker compose down --remove-orphans`

### 3.3 Notebook-Sync-Loop-Fix (PR #3) — wichtig

**Symptom:** Auf dem Server blinkte das Notebook ca. jede Sekunde; Network: `.ipynb` + `/api/progress` in Endlosschleife (oft bei **eingeloggt**).

**Ursache:**  
`PROGRESS_APPLIED` → `JupyterNotebook` machte volles `loadNotebook()` (Fetch + `loading`) → Watch speicherte → `touchSyncKey` → Sync → Apply → wieder Event.

**Fix:**
- Sync wendet Notebook-State nur lokal an, **ohne** Re-Fetch / ohne Loading-Blink
- `syncNow` skippt Apply/Put wenn nichts geändert
- `saveState` / Apply schreiben nur bei Inhaltsänderung; `applying`-Flag etwas länger (Tick), damit Vue-Watcher keinen Re-Sync auslösen

Dateien: `src/composables/useProgressSync.js`, `src/components/JupyterNotebook.vue`

**Server nach Merge:** `git pull` auf `main` + `docker compose up -d --build app` + Hard-Reload.

### 3.4 Storytelling-Überarbeitung 12-Wochen-Kurs (alle 3 Varianten, alle 12 Wochen)

**Ziel:** Missionen/Boss-Quests waren oft nur Schritt-Listen mit Deko statt echter Szenen, manche Wochen
lösten ihr eigenes Titelversprechen nicht ein, und es gab mehrere echte Content-Bugs (kaputter Code,
Textfehler, kopierte Boss-Quests). Pro Woche wurde geprüft, ob ein Umbau nötig ist, und nur dort umgebaut,
wo es einen echten Mangel gab.

**Abenteuer-Variante** (zuerst, als Vorlage):
- Woche 7 als Pilot komplett umgebaut: Rahmengeschichte "Der Archivar der Bibliothek von Pyralia" mit
  drei zusammenhängenden Prüfungen statt isolierter Schritt-Listen; Bibliothekswahl von `math`-lastig auf
  `random`/`string`/`time` umgestellt
- Pythonia/Pyralia-Namenskonflikt weltweit vereinheitlicht (auf "Pyralia") — Woche 1, 10, 12 (DE+EN)
  sowie die Vorlagen unter `Regeln/`
- Woche 2 umgebaut: "Elementarturm", vier Datentypen jetzt explizit als Elemente (🔥 Feuer=str,
  🪨 Erde=int, 💧 Wasser=float, 💨 Luft=bool)
- Woche 6: Boss-Quest 1+2 waren wortwörtlich von Woche 5 kopiert — umbenannt/umgethemt
- Woche 8: Debug-Bug #1 hatte keinen Fehler mehr (fehlende schließende Klammer nie entfernt) — repariert
- Woche 9: Missionen-Formatierung vereinheitlicht
- Woche 10: Boss-Quest 2 "Der Zookeeper" (reale Zootiere) zu "Die Kreaturen-Menagerie" umgethemt
- Woche 12: Textbug "Als Nächstes: Woche – wartet schon!" repariert (betraf auch Pferde/Sci-Fi DE)
- Woche 3, 4, 5, 11 geprüft und für gut befunden

**Pferde- und Sci-Fi-Variante** (nach demselben Prinzip, Analyse zuerst per Subagent):
- Sci-Fi Woche 11: kompletter Lektion-Code (DE) war kaputt (fehlendes `def`/`self` bei jeder Methode) —
  an die korrekte EN-Version angeglichen; Weltname vereinheitlicht (Nebula-7 statt "Evolution-Station
  Alpha-7")
- Sci-Fi Woche 8: Debug-Bug #1 hatte keinen Fehler mehr — repariert (DE+EN)
- Sci-Fi Woche 5/6/8: Boss-Quest "Raumstation(s)-Manager" dreifach dupliziert — Woche 6 zu
  "Der Hangar-Verwalter", Woche 8 zu "Die Sensor-Matrix" umgethemt (DE+EN), rewards-manifest angepasst
- Sci-Fi Woche 12: "XP" statt "Cyber Credits" korrigiert
- Sci-Fi Woche 9: f-String-Syntaxrisiko behoben (verschachtelte gleiche Anführungszeichen, vor Python
  3.12 ein SyntaxError)
- Sci-Fi Woche 12: Debug-Bugs entspoilert (Kommentare verrieten die Lösung direkt); Lösungs-Notebook an
  den tatsächlichen Bug angeglichen (war inhaltlich falsch zugeordnet)
- Sci-Fi Woche 5: fehlende Platzhalterkommentare in Boss-Quest-Codezellen ergänzt
- Sci-Fi Woche 7: Missionen enger an eine durchgehende Szene gebunden (Systemchecks/Kalibrierung/
  Erkundungsmission statt lose math/random-Häppchen)
- Pferde Woche 9: Intro wortwörtlich von Woche 8 kopiert — neue Rahmengeschichte "Die Zuchtbücher von
  Sonnental" (DE+EN); Belohnungsitem "Daten-Chip" (eigentlich Sci-Fi-Item) zu "Stammbaum-Urkunde"
  korrigiert
- Pferde Woche 5/8: abgebrochener Satz und mehrfacher "Funktion eine Funktion"-Textbug repariert (DE+EN)
- Pferde Woche 7/8/9: "Sonnentals"-Tippfehler (falsche Genitivform) zu "Sonnental" korrigiert
- Pferde Woche 12: "XP" statt "Huf-Punkte" und Tippfehler "Visualierungsbrett" korrigiert (DE)
- Pferde Woche 12 + Sci-Fi Woche 12 + Abenteuer Woche 12: Debug-Bug-Spoiler-Kommentare entfernt (DE+EN)
- Pferde Woche 2: "Vier Hufschlag-Typen" jetzt benannt (Schritt=str, Trab=int, Galopp=float, Sprung=bool)
- **Nebenfund:** `week5_horses_1_lektion.ipynb` (EN) hatte unescaped Anführungszeichen und war dadurch
  kaputtes JSON (Notebook konnte in der Website nicht laden) — repariert. Repo-weiter Scan aller 444
  Notebooks bestätigt danach: keine weiteren kaputten Dateien.

**Gelernte Regeln:**
1. Debug-Notebook-Bugs müssen unabhängig vom geteilten Jupyter-Kernel-Zustand sein — ein "vergessener
   Import" funktioniert nicht mehr, wenn eine frühere Zelle das Modul schon importiert hat.
2. Debug-Notebook-Kommentare dürfen die Lösung nicht verraten (keine "# Bug: X fehlt!"-Kommentare) —
   vage Leitfragen sind ok ("Was fehlt hier?").
3. Bei jeder Notebook-Änderung: Code-Zellen ausführen/kompilieren (auch mit geteiltem Namespace) und
   JSON-Validität prüfen, bevor committet wird.

**Systemtests:** Die wichtigsten Fixes sind als Playwright-Regressionstests in `tests/storytelling-content.spec.js`
festgehalten (läuft mit in `npm run test:checks`) — prüft u.a. Woche-9-Pferde-Rahmengeschichte,
Hufschlag-Typen-Benennung, Sci-Fi-Woche-11-Code-Korrektheit (def/self), Boss-Quest-Eindeutigkeit
Woche 6/8 Sci-Fi, Cyber-Credits/Huf-Punkte statt XP, und dass Debug-Bugs nicht im Kommentar verraten
werden. Jeder Test wurde gegen eine absichtlich kaputte Kopie verifiziert (schlägt dann fehl).

**Geklärt:** "Gilde-Meister-Urkunde" als Zwischenbelohnung in W6/7/8 (Abenteuer) ist kein Bug — Pferde
("Reitmeister-Urkunde") und Sci-Fi ("Crew-Meister-Urkunde") nutzen dasselbe Muster je 3×, und andere
Items (z.B. "Kristallkugel" 4×, "Quest-Buch" 4×) wiederholen sich im ganzen Kurs genauso. Bewusstes
Belohnungs-Flavor-Muster für die schwierigste Mission der Woche — keine Umbenennung nötig.

### 3.5 Debug-Notebook-Sicherheit: Endlosschleifen-Schutz + Sci-Fi-Debug-Ziele (Branch `debug-notebook-safety`)

**Ausgangslage:** 10 Verbesserungswünsche wurden in 6 Branches gruppiert (Plan-Datei
`~/.claude/plans/scalable-singing-cook.md`), Reihenfolge B→A→E→F→C→D. Dies ist Branch B.

**Endlosschleifen-Schutz (`src/composables/usePyodide.js`):** Python lief bisher komplett
client-seitig via Pyodide direkt auf dem Hauptthread — eine `while True:` in irgendeiner Code-Zelle
(nicht nur Debug-Notebooks) fror den Tab für immer ein, kein Timeout konnte greifen (Event-Loop
selbst blockiert). Lösung: bei der Kernel-Initialisierung wird eine Python-Hilfsfunktion
`_run_cell_with_guard(source, timeout_seconds=5)` registriert, die den Zell-Code per `ast`-Modul
parst und vor jeden `for`/`while`-Schleifenkörper eine Deadline-Prüfung einfügt (`if time.time() >
deadline: raise _CellTimeout()`, `_CellTimeout` erbt bewusst von `BaseException` statt `Exception`,
damit ein normales `except Exception:` sie nicht verschluckt). `runPython()` übergibt den Code jetzt
über `pyodide.globals.set('_cell_source', ...)` statt textueller Einbettung.

**Bewusst KEIN Web Worker:** Die ursprünglich im Plan vorgesehene Web-Worker-Lösung (für "echte"
Unterbrechbarkeit) hätte `input()` kaputt gemacht — 65 Notebooks nutzen `input()` über
`window.prompt()` (synchron, nur auf dem Hauptthread möglich ohne SharedArrayBuffer +
COOP/COEP-Header). Die AST-Guard-Lösung läuft weiter auf dem Hauptthread, braucht keine
Server-/Infra-Änderung und bricht nach 5 Sekunden sauber ab, ohne `input()` zu beeinträchtigen. Das
ist eine bewusste Abweichung vom ursprünglich geschriebenen Plan (dort stand Web Worker) — technisch
überlegen für diesen konkreten Fall, da sie den harten Blocker (`input()`) vermeidet.

**Bekannte Grenze:** Ein `while True: try: ... except: pass` könnte `_CellTimeout` theoretisch
schlucken (bare `except:` fängt auch `BaseException`) und die Schleife liefe weiter — für die
Zielgruppe (Kinder/Jugendliche in strukturierten Debug-Aufgaben) ein sehr unwahrscheinliches Muster,
kein Blocker.

**Getestet:** lokal mit CPython (`test_loop_guard.py`-Äquivalent: normale Zellen, `for`-Schleifen,
Endlosschleife auch verschachtelt in Funktionen, geteilte Variablen über Zellen hinweg bleiben
erhalten, NameError/SyntaxError propagieren weiterhin normal) sowie live im Browser per Playwright
(Debug-Tab, Sci-Fi, Woche 1): `while True: pass` wird nach ~5032ms mit Fehlermeldung abgebrochen,
danach läuft eine normale Zelle sofort wieder korrekt. **Dauerhafter Regressionstest** ergänzt:
`tests/site.spec.js` → Describe „Debug-Notebook-Sicherheit" (prüft Abbruchzeit 3-12s, Fehlertext
und dass der Kernel danach weiter benutzbar bleibt).

**Debug-Ziele (Punkt 6):** Sci-Fi-Variante komplett (12 Wochen × DE+EN = 24 Dateien, 72
Bug-Markdown-Zellen) um eine **Ziel:**/**Goal:**-Zeile ergänzt, die das erwartete Verhalten/die
erwartete Ausgabe beschreibt, ohne den Bug selbst zu verraten (z.B. bei `koordinaten[0] = 150` auf
einem Tupel: "Ziel: Das Programm soll die erste Koordinate auf `150` ändern" — ohne
Tupel-Unveränderlichkeit zu erwähnen). Stichprobenartig gegen den jeweiligen Code-Kontext geprüft
(Woche 1, 8, 11) — akkurat und spoilerfrei; `tests/storytelling-content.spec.js`s
Anti-Spoiler-Test (prüft nur Code-Zellen auf `# Bug:`-Kommentare) bleibt unberührt, da nur
Markdown-Zellen geändert wurden. **Dauerhafter Regressionstest** ergänzt: neuer Test „Woche 1:
Debug-Bugs nennen ein Ziel, ohne den Fehler zu verraten" prüft Anzahl Ziel-Zeilen == Anzahl Bugs
und dass keine typischen Spoiler-Formulierungen vorkommen. Dabei nebenbei einen latenten Bug im
Test-Helper `openWeek()` gefunden und behoben: er ging noch davon aus, dass Woche 1 (Index 0)
immer aufgeklappt startet — das war seit der "Woche 1 zuklappen"-Änderung nicht mehr der Fall,
wurde aber nie bemerkt, weil kein bisheriger Test Woche 1 über diesen Helper geöffnet hatte.

**Offen (nächste Session):** Pferde- und Abenteuer-Variante nach demselben Muster mit Debug-Zielen
ergänzen (im Plan als "danach nachziehen" vorgesehen, nicht in dieser Sitzung geschafft).

### 3.6 Einstufungstest-Fixes (Branch `cursor/et-fixes`)

**Ausgangslage:** 10 Verbesserungswünsche wurden in 6 Branches gruppiert (Plan-Datei
`~/.claude/plans/scalable-singing-cook.md`), Reihenfolge B→A→E→F→C→D. Dies ist Branch A.

- **"Ich weiß es nicht"** (`src/components/QuizStep.vue`): eigener Button pro Frage, setzt die
  Antwort auf einen Sentinel-Wert `DONT_KNOW`, der nie mit einem `correctIndex` übereinstimmt (zählt
  also korrekt als "falsch" für die Bewertung), löst aber eine eigene Rückmeldung aus ("Kein
  Problem — hier ist die Antwort: …") statt der normalen Falsch-Rückmeldung.
- **Erklärung bei Falsch-Antwort:** war technisch schon vorhanden (100 % Coverage: 240
  `explanation`/`explanation_en`-Einträge bei 120 Fragen in `weeks.json`, `optionClass()` hebt die
  richtige Option grün hervor sobald geprüft) — nur der Wortlaut wurde geschärft: falsche Antworten
  zeigen jetzt "Nicht ganz — [Erklärung]" statt der Erklärung ohne Einleitung, damit klar ist, dass
  es sich um eine Korrektur handelt.
- **Placement-Scoring gelockert:** `placementPerWeek` 2→3 (jede Woche hat bereits genau 3
  `inPlacement: true`-Fragen, keine Content-Änderung nötig), neuer eigener Config-Wert
  `placementPassThreshold: 0.66` in `weeks.json` statt des allgemeinen `passThreshold: 0.8` (der für
  die normalen Wochen-Checks unverändert bleibt — `WeekCheckPanel.vue` liest weiter `passThreshold`).
  `PlacementCourse.vue`s `threshold`-Computed liest jetzt `placementPassThreshold ?? passThreshold ?? 0.8`.
  **Vorsicht bei künftigen Threshold-Änderungen:** 2/3 ergibt in JS `0.6666...` — ein Threshold von
  z.B. `0.67` hätte "2 von 3 richtig" fälschlich durchfallen lassen (0.6667 < 0.67); erst beim
  Live-Test im Browser aufgefallen, `0.66` gewählt um sauberen Abstand zu halten.
- **Distraktoren:** für Wochen 1-4 wurden 12 von 40 Fragen mit genuin unplausiblen Falsch-Antworten
  (z.B. "Um den Computer auszuschalten", "Ein Drucker") auf nähere Verwechslungen umgestellt (z.B.
  "Ein fester Wert, der sich nie ändert" für "Was ist eine Variable?"). Bereits gute Distraktoren
  (echte Verwechslungen wie `==`/`=`/`!=` oder `//`/`/*` für Kommentare) wurden bewusst NICHT
  angefasst. Wochen 5-12 sind noch offen (siehe `todo.md`).

**Getestet:** `npm run test:checks` (alle 34 bestehen, inkl. dynamisch mitgehendem
`placementPerWeek`-Test) + live im Browser per Playwright verifiziert. **Dauerhafte Regressionstests
ergänzt** (waren zunächst nur manuell verifiziert, nicht in der Suite): `tests/week-checks.spec.js`
→ „Ich weiß es nicht zeigt eigene Rückmeldung und die richtige Antwort" sowie „2 von 3 richtig pro
Woche reicht (0.66-Schwelle), 1 von 3 nicht" (beantwortet Woche 1 mit 2/3, Woche 2 mit 1/3, Rest
korrekt, prüft `.week-result.ok`/`.review`-Klassen und die angezeigten Bruch-Werte).

### 3.7 Interaktiver Kurs: gestufter Hinweis (Branch `cursor/interaktiv-klarer`)

**Ausgangslage:** 10 Verbesserungswünsche wurden in 6 Branches gruppiert (Plan-Datei
`~/.claude/plans/scalable-singing-cook.md`), Reihenfolge B→A→E→F→C→D. Dies ist Branch C
(Punkt 7 — "Interaktive Session klarer gestalten").

**Umgesetzt:** `LessonView.vue`s `checkTask()` verriet bei falscher Aufgaben-Ausgabe sofort die
wörtliche erwartete Teilzeichenkette ("Erwartet wurde etwas mit: '...'") — wirkte wie
Lösungsverrat. Jetzt gibt es einen neuen `taskAttempts`-Zähler pro Aufgabe: beim ersten Fehlversuch
kommt nur ein sanfter Hinweis ("schau dir deine Ausgabe an und vergleiche sie mit der
Aufgabenstellung"), erst ab dem zweiten Fehlversuch wird die konkrete erwartete Teilzeichenkette
gezeigt (damit niemand dauerhaft feststeckt). Ein Python-Laufzeitfehler (z.B. `NameError`) ist
davon unberührt — der wird weiterhin sofort und vollständig angezeigt, da er selbst die nützliche
Diagnose ist, kein Lösungsverrat.

**Bewusst nicht umgesetzt:** die im Plan genannte "Ausführen vs. Prüfen"-Unterscheidung klarer
machen und der Fortschritts-/Weiter-Flow — das sind subjektive "klarer machen"-Wünsche ohne
konkret benannten Verwirrungspunkt. Braucht erst Rückmeldung vom Nutzer (idealerweise mit
Screenshot), was genau als unklar aufgefallen ist, bevor an der UI weiter herumgebaut wird.

**Getestet:** neuer Playwright-Test in `tests/site.spec.js` (erster Fehlversuch zeigt keine
Erwartung, zweiter schon) + `npm run test:checks` (alle 33 Tests grün) + manuell im Browser
verifiziert.

### 3.8 Text-Tippfehler-Pass, Phase 1: Tooling + UI-Texte (Branch `text-typo-pass`)

**Ausgangslage:** 10 Verbesserungswünsche wurden in 6 Branches gruppiert (Plan-Datei
`~/.claude/plans/scalable-singing-cook.md`), Reihenfolge B→A→E→F→C→D. Dies ist Branch D
(Punkt 8 — "Texte überarbeiten, komplette Seite auf Schreibfehler prüfen"), Phase 1 von mehreren.

**Tooling:** `cspell` + `@cspell/dict-de-de` + `@cspell/dict-en_us` als devDependencies,
`cspell.json` (Config, Custom-Wortliste) + `npm run lint:spelling`. **Wichtig:** externe
Wörterbuch-Pakete müssen über `"import": ["@cspell/dict-de-de/cspell-ext.json", ...]` eingebunden
werden — nur `"dictionaries": ["de-de", "en_us"]` ohne `import` lädt sie NICHT (führte anfangs zu
402 falschen Treffern, weil praktisch jedes deutsche Wort als unbekannt galt).

**Ergebnis UI-Texte:** `src/locales/de.js` + `src/locales/en.js` sind bereits sauber — keine
echten Tippfehler gefunden. Ein paar technische Identifier (`jupyter`, `scifi`, `appt` als Teil von
Locale-Keys) sowie bewusst britisches Englisch ("Initialise", "practising" — konsistent im
EN-Text, kein Stilbruch) sind im Custom-Dictionary vermerkt.

**Wichtige Erkenntnis:** Ein Großteil der tatsächlichen Nutzer-Prosa steckt NICHT in
`src/locales/*.js`, sondern direkt als `lang === 'en' ? '...' : '...'`-Ternarys in den
`.vue`-Dateien (`InteractiveCourse.vue`, `PlacementCourse.vue`, `QuizStep.vue`, `LessonView.vue`,
`Home.vue` etc.). Eine cspell-Stichprobe über `src/components/*.vue` + `src/views/*.vue` fand
ebenfalls keine echten Tippfehler, aber ~84 False Positives (Routen-Segmente wie `kurs`/`woche`/
`lektion`, CSS-Klassennamen, Variablennamen) — cspell trennt Vue-Templates nicht sauber genug von
Prosa. Deshalb **nicht** systematisch ins Custom-Dictionary aufgenommen (würde echte Treffer
mit-verstecken) — braucht für eine spätere Session entweder gezielte Ignore-Patterns oder eine
Vue-spezifische Cspell-Konfiguration.

### 3.9 Text-Tippfehler-Pass, Phase 2: Wochenbeschreibungen, Einstufung, Notebooks Abenteuer

**`content/*/beschreibung.md`** (alle 11 Dateien) und **`content/python-checks/weeks.json`**
(38 Treffer) geprüft — beide **komplett sauber**, die 38 `weeks.json`-Treffer waren durchweg
Python-Schlüsselwörter/Funktionsnamen in Code-Beispielen (`elif`, `randint`, `isinstance`, …) oder
Code-Identifier in Beispiel-Strings (`mein_geheim_modul_xyz`, `datei.txt`).

**Notebooks — neues Skript `scripts/extract_notebook_text.py`:** zieht nur die Markdown-Zellen aus
`.ipynb`-Dateien in `.md`-Dateien (Code-Zellen bewusst ausgeklammert, sonst zu viele
Identifier-False-Positives). **Wichtige Falle:** der Ausgabeordner muss innerhalb des Repos liegen
— `cspell` prüft Pfade außerhalb des erkannten Projekt-Roots nicht (stiller 0-Treffer, kein Fehler),
`/tmp` funktioniert deshalb nicht.

**Abenteuer-Variante komplett geprüft** (144 Notebooks DE+EN, ~150 einzigartige Kandidatenwörter
einzeln nachgeprüft, nicht blind übernommen): **keine echten Tippfehler.** Fast alles waren
Fantasy-Eigennamen/-Komposita (Pyralia, Runenschmiede, Tresorwächter, Gildenarchiv, …),
Python-Identifier in Code-Beispielen, oder seltene aber korrekte deutsche Flexionsformen — z.B.
"lesbarere" (lesbar+er+e, Komparativ + schwache Adjektivendung, korrekt) und "primen" (Dativ/Akk.
Plural von "prim" nach "alle", korrekt) wurden einzeln nachgerechnet, bevor sie als „kein Fehler"
eingestuft wurden. Alle False Positives ins Custom-Dictionary übernommen (`cspell.json`, jetzt
159 Wörter).

**Ein echter Fund:** `week12_adventure_1_lektion.ipynb` (EN) nutzte an 4 Stellen amerikanisches
Englisch ("colors", "colorful") statt des sonst im ganzen EN-Kurs konsequent verwendeten
britischen Englisch (vgl. "colours", "practise", "organised" im Rest des Korpus) — korrigiert.
Bewusst unverändert gelassen: `.color()`/`.fillcolor()` als Turtle-API-Methodennamen-Referenzen
(z.B. im Glossar "Set pen color") — die Methode heißt in Python tatsächlich so, das ist kein
Dialekt-Stilbruch, sondern korrekt zitierter Code.

**Getestet:** `npm run test:checks` (32 Tests grün, unverändert — der Colours-Fix ist eine reine
Text-Korrektur ohne Verhaltensänderung, laut der neuen `WORKFLOW.md`-Regel braucht das keinen
eigenen Test) + manuelle JSON-Validitätsprüfung der geänderten Notebook-Datei.

### 3.10 Text-Tippfehler-Pass, Fortsetzung: Pferde + Sci-Fi — alle 444 Notebooks fertig

Gleiches Verfahren (Skript aus 3.6) auf Pferde- und Sci-Fi-Variante (je 144 Notebooks DE+EN)
angewendet. **Damit sind jetzt alle 444 Notebooks des 12-Wochen-Kurses + alle Cheat-Sheets/Glossare
einmal komplett auf Tippfehler geprüft.**

**Echte Funde (alle einzeln über Kontext verifiziert, nicht blind gefixt):**
- **Pferde Woche 11:** "Parours" → "Parcours" (fehlendes "c")
- **Pferde Woche 2:** "pferdbezogene" → "pferdebezogene" (fehlendes Fugen-e)
- **Pferde Woche 1 (Glossar):** "Pferdname" → "Pferdename" — inkonsistent zu 4 anderen Stellen im
  selben Wochensatz, die korrekt "Pferdename(n)" schreiben
- **Pferde Woche 3 + `rewards-manifest.json`:** "Futterschip" → "Futterschippe" — aufgelöst über
  den EN-Manifest-Eintrag "Feed Scoop" (nicht "Feed Chip"): kein Sci-Fi-Chip-Wortspiel, sondern ein
  abgeschnittenes "Futterschippe". Betraf zwei gekoppelte Dateien (Notebook + Manifest), beide
  angepasst (INHALTE.md-Kopplungsregel für Belohnungsitems).
- **Sci-Fi Woche 1 UND Woche 10** (identischer Intro-Text dupliziert): "Du betrittstest die
  hochmoderne Raumstation Nebula-7" → "Du betrittst die..."

**Bewusst nicht angefasst** (geprüft, aber kein echter Fehler):
- Pferde Woche 1 Lösungen: "zuviel" — alte Rechtschreibung, weit verbreitet, kein klarer Fehler
- Sci-Fi Woche 1 Lösungen: "statu" — das ist der im Debug-Notebook absichtlich erklärte Tippfehler
  selbst (`status` vs. `statu`), kein zu fixender Fehler
- Pferde/Sci-Fi Woche 12: kein US/UK-Englisch-Mix gefunden (anders als bei Abenteuer Woche 12) —
  `color`/`.color()` kam nur in Turtle-API-Method-Referenzen vor, nicht in freier Prosa

Alle 11 DE-Cheat-Sheets (`.md`-Quelle + generierte `.ipynb`), 11 EN-Cheat-Sheets,
`turtle_cheat_sheet.md` (DE+EN) und `gesamtglossar.ipynb` ebenfalls geprüft — sauber, nur
Turtle-API-Methodennamen als False Positives. `cspell.json` enthält jetzt 344 projektspezifische
Wörter.

**Noch offen (nächste Sessions, siehe `todo.md`):**
- `.vue`-Dateien systematisch prüfbar machen
- Interaktive Kurse (`python-grundlagen-interaktiv*`) und `caesar-chiffre` noch nicht geprüft

**Getestet:** `npm run test:checks` (32 Tests grün — alle Fixes sind reine Text-/Content-
Korrekturen ohne Verhaltensänderung, laut `WORKFLOW.md` kein eigener Test nötig) + JSON-Validität
aller 6 geänderten Notebook-Dateien geprüft.

### 3.11 Neues Projekt: Cäsar-Chiffre (Branch `kurs-caesar-chiffre`)

Das erste eigenständige "Projekt" neben den Wochenkursen.

- **Content:** `content/caesar-chiffre/` (neuer Ordner, gleiches Schema wie
  `python-grundlagen-interaktiv-*`: `lessons.json` + `lektion-01..05.md` + `beschreibung.md`).
  5 Lektionen: ord()/chr() → Buchstaben verschieben (Modulo/Wraparound) → Verschlüsselungsfunktion
  → Entschlüsselungsfunktion → Brute-Force-Knacker (probiert alle 26 Verschiebungen). Jede
  Lektion verlinkt im Text auf die passende Woche des 12-Wochen-Kurses (Woche 2 Strings, Woche 4
  Schleifen, Woche 5 Funktionen) über denselben Query-Param-Deep-Link-Mechanismus wie
  `PlacementCourse.vue` (`?week=N&tab=lektion#woche-N`) — als normaler Markdown-Link, löst also
  einen vollen Seiten-Reload statt SPA-Transition aus, funktioniert aber korrekt.
- **Neue Komponente `src/components/ProjectCourse.vue`:** bewusst NICHT `InteractiveCourse.vue`
  wiederverwendet, weil die einen fest eingebauten Kinder/Jugendliche-Varianten-Selector hat, der
  hier nicht passt (nur eine Variante). `ProjectCourse.vue` ist eine reduzierte Kopie ohne
  Varianten-Auswahl, reused aber `LessonView.vue` unverändert.
- **`src/composables/useInteractiveProgress.js`:** bekam einen optionalen zweiten Parameter
  `courseId` (Default bleibt der bisherige Wert, rückwärtskompatibel) — ohne den hätte der
  exportierte Fortschritt für Cäsar-Chiffre fälschlich `courseId: "python-grundlagen-interaktiv"`
  enthalten, da diese Composable bisher hart auf den einen Kurs verdrahtet war.
- **`LessonView.vue`:** `import.meta.glob(...)`-Listen für Lektions-Markdown und Glossar sind
  hart codierte Pfadlisten (Vite braucht statische Glob-Patterns) — `content/caesar-chiffre/*.md`
  wurde dort ergänzt, sonst hätte die neue Lektion nicht geladen werden können. **Wichtig für
  künftige neue Kurse mit `LessonView.vue`:** diese Glob-Liste immer mit erweitern.
- **`kurse.json`:** neuer Eintrag `projekt-caesar-chiffre`. **`Home.vue`:** die Kursliste auf der
  Startseite ist standardmäßig gefiltert (nur 12-Wochen-Kurs + Interaktiv-Kurs erscheinen immer,
  alles andere nur mit Termin in `termine.json`) — `projekt-caesar-chiffre` wurde bewusst zur
  Always-visible-Liste hinzugefügt, damit es wie gewünscht "neben den Wochenkursen" sichtbar ist.
- **Hinweis-Banner im 12-Wochen-Kurs:** neuer `.project-banner`-Block am Ende der Kursseite
  (`CourseDetail.vue`, nur bei `isWeeklyCourse`) verlinkt zum neuen Projekt.
- **Bekannte Einschränkung:** nur deutschsprachiger Content (kein `-en`-Pendant) — im EN-Modus
  fällt `loadCourseData` automatisch auf den DE-Beschreibungstext zurück (nicht ideal, aber
  funktional, konsistent mit "DE-first" bei anderen neuen Kursen laut `todo.md`).

**Getestet:** `npm run test:checks` (2 neue Tests in `tests/site.spec.js` + angepasster
Home-Test, der jetzt 3 statt 2 immer sichtbare Kurskarten erwartet) + manuell per Playwright mit
echtem Pyodide-Lauf durch alle 5 Lektionen (inkl. der Brute-Force-Lektion, die tatsächlich
"projekt" als Klartext ausgibt) sowie Deep-Link-Navigation zu Woche 2 des 12-Wochen-Kurses.

---

## 4. Aktueller technischer Stand

### Start lokal

```bash
cp .env.example .env   # ADMIN_PASSWORD setzen
cd api && npm install && cd .. && npm install
npm run start:all      # Vite :5173 + API :3001 (Proxy /api)
# oder
npm run start:prod     # Build + alles :8080
```

### Docker Prod

```bash
# .env mit ADMIN_PASSWORD
docker compose down --remove-orphans
docker compose up -d --build app
curl -s http://127.0.0.1:8080/api/health
```

SQLite bleibt in `./api/data/` (Volume). Env-Änderung → Container **recreate**, nicht nur rebuild.
Ein `git pull` + `docker compose up -d --build app` lässt Nutzerdaten unangetastet — die DB liegt
als Bind-Mount auf dem Host, nicht im Container, und ist gitignored. **Einzige echte Gefahr:**
`git clean -fdx` im Repo-Verzeichnis würde die ungetrackte `.sqlite`-Datei löschen, weil sie
technisch im Working Tree liegt — nie in einem Deploy-Skript ohne Ausschluss von `api/data/`.

### DB-Backup

`api/src/scripts/backup-db.js` zieht per `VACUUM INTO` eine konsistente Kopie der SQLite-DB (sicher
auch im laufenden Betrieb dank WAL-Modus — ein simples `cp` könnte sonst mitten in einem
Schreibvorgang eine kaputte Kopie erzeugen) und behält per Retention nur die N neuesten Backups
(Default 14, über `BACKUP_KEEP` einstellbar). Landet unter `api/data/backups/` — dank Bind-Mount
automatisch auch auf dem Host sichtbar.

```bash
npm run backup:db                 # lokal (nutzt DATA_DIR/DB_PATH wie die App selbst)
docker compose exec app node src/scripts/backup-db.js   # im laufenden Prod-Container
```

**Empfehlung für den Server:** ein Cron-Job, z.B. täglich um 3 Uhr:
```
0 3 * * * cd /pfad/zum/repo && docker compose exec -T app node src/scripts/backup-db.js >> /var/log/ue-hacker-backup.log 2>&1
```
Die Backups selbst liegen weiterhin auf demselben Server-Volume — für echten Schutz vor
Datenverlust (Festplattendefekt, versehentliches Löschen) zusätzlich regelmäßig extern sichern
(z.B. `rsync`/`rclone` von `api/data/backups/` auf einen anderen Host oder Cloud-Speicher). Das ist
mit den Bordmitteln hier noch nicht abgedeckt — bewusst nicht mitgebaut, da das von der jeweiligen
Server-/Backup-Infrastruktur abhängt.

### Tests

| Command | Inhalt |
|---------|--------|
| `npm run test:checks` | Pre-commit: Logic, Week-Checks/Placement, Site, Merge, Storytelling-Content |
| `npm run test:auth` | API + Admin/Optionen-UI (eigene Config, Test-API :3011) |
| `npm --prefix api test` | Node-Test-Runner: `backup-db.js` (Backup + Retention) |

### Wichtige Pfade

```
api/src/          Express (index, auth, db, routes)
api/src/scripts/  backup-db.js (+ Test) — SQLite-Backup mit Retention
src/views/AdminView.vue
src/App.vue       Optionen-Modal
src/composables/useAuth*.js, useProgressSync.js, useWeekChecks.js
src/components/JupyterNotebook.vue, PlacementCourse.vue, QuizStep.vue
public/kurse.json
content/python-checks/weeks.json
.env.example / .env (nie committen)
```

---

## 5. Offene Aufgaben

Siehe auch `todo.md`.

**Betrieb**
- [ ] Server-Deploy final verifizieren (Service `app`, Orphans weg, Health, Admin-Login, kein
      Notebook-Blinken mehr nach PR #3) — **bewusst zurückgestellt**, Nutzer will erst später
      deployen
- [x] SQLite-Backup-Script (`api/src/scripts/backup-db.js`) — siehe Abschnitt 4. Externe
      Sicherung der Backups (z.B. `rsync`/`rclone` auf einen anderen Host) bewusst nicht mitgebaut,
      hängt von der jeweiligen Server-Infrastruktur ab

**Inhalte**
- Keine offenen Punkte aus der Storytelling-Überarbeitung mehr (siehe 3.4) — "Gilde-Meister-Urkunde" geklärt, kein Bug
- Debug-Notebook-Ziele (3.5): Pferde + Abenteuer noch offen (Sci-Fi fertig)
- Einstufungstest (3.6): Distraktoren für Wochen 5-12 noch offen (Wochen 1-4 fertig)
- Interaktiver Kurs (3.7): "Ausführen vs. Prüfen"-Klarheit und Weiter-Flow noch offen, braucht
  konkretes Nutzer-Feedback (idealerweise Screenshot) bevor daran gearbeitet wird
- Text-Tippfehler-Pass (3.8–3.10): alle 444 Notebooks + Cheat-Sheets/Glossare + UI-Texte +
  Wochenbeschreibungen + `weeks.json` fertig — `.vue`-Dateien und die interaktiven Kurse
  (`python-grundlagen-interaktiv*`, `caesar-chiffre`) noch offen
- Cäsar-Chiffre-Projekt (3.11): EN-Version noch offen (DE-first)

**Branch-Merge läuft gerade (diese Session):** `debug-notebook-safety`, `et-fixes`,
`interaktiv-klarer`, `text-typo-pass`, `backup-sqlite-db` und `kurs-caesar-chiffre` sind soeben
nach `main` gemergt. Nur noch **`wochen-zertifikate`** fehlt in dieser Session. Nach jedem Merge
`npm run test:checks` (und bei Auth-relevanten Branches zusätzlich `npm run test:auth`), bevor der
nächste Branch drankommt. Noch **nicht** nach `origin/main` gepusht.

**Danach — nächste Kurs-Themen, je eigener Branch von `main`:**

1. **`kurs-python-spiele`** — Python Spiele-Werkstatt (Turtle/Textspiele)
2. **`kurs-python-projekte`** — „Was kommt danach?“ Projekt-Sprints
3. **`kurs-js-minigames`** *oder* **`kurs-ki-labor`** — Entscheidung beim Start

Nicht mischen; Details/Checkboxen in `todo.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.
Kontakt-E-Mail im Footer wartet noch auf die tatsächliche Adresse vom Nutzer (nicht selbst erfinden).

**Bekannte Altlasten (niedrige Prio):** Notebook-Download-ZIP nur DE; optionale EN-Nachzüge bei neuen Kursen (inkl. Cäsar-Chiffre).

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch von `main` (`WORKFLOW.md`) — **kein** Präfix mehr (früher `cursor/…`,
  wurde entfernt)
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt`
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`; Verhaltensänderungen brauchen
  einen Test in `tests/*.spec.js` bzw. `api/src/scripts/*.test.js` (`WORKFLOW.md`) — nicht nur
  manuell verifizieren
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)

---

## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`  
2. `HANDOFF.md` + `todo.md` + `WORKFLOW.md` lesen  
3. Neues Thema → **neuen** Branch (ohne Präfix)  
4. Nicht: altes `prod` in Compose erwarten; nicht: Sync so ändern, dass Notebooks wieder voll neu
   geladen werden bei jedem Apply; nicht: Pyodide in einen Web Worker verschieben ohne `input()`
   (65 Notebooks) neu zu lösen (siehe 3.5); nicht: `placementPassThreshold` auf einen Bruch wie `2/3`
   exakt setzen (Floating-Point — siehe 3.6); nicht: `cspell`-Wörterbücher nur über
   `"dictionaries"` ohne `"import"` einbinden (lädt sie nicht, siehe 3.8); nicht:
   `scripts/extract_notebook_text.py` nach `/tmp` ausgeben lassen (cspell sieht Pfade außerhalb
   des Repos nicht, siehe 3.9); nicht: SQLite per `cp` statt `VACUUM INTO` sichern (WAL-Modus,
   siehe Abschnitt 4); nicht: einen neuen `LessonView.vue`-Kurs anlegen, ohne die
   `import.meta.glob(...)`-Pfadlisten in `LessonView.vue` zu erweitern (siehe 3.11)
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`

**Empfohlener nächster Schritt:** Branch-Merge-Kette abschließen (siehe Abschnitt 5) —
nur noch `wochen-zertifikate`, danach `kurs-python-spiele` (Kursgerüst `kurse.json` +
Content-Ordner).
