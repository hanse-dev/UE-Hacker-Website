# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-18  
> **Aktueller Stand:** `main` ist auf `origin/main` gepusht, inkl. Branch `experiment-wochen-tour`
> (3.35+3.36, gemergt) — was als unverlinktes Experiment begann, ist jetzt die **echte** Kursseite
> unter `/kurs/python-12-wochen-grundkurs` (alte Akkordeon-UI `WeekSection.vue` + Co. entfernt).
> **Server-Deploy steht noch aus** — Code ist auf GitHub, aber noch nicht auf dem
> Produktions-Server ausgerollt (siehe Abschnitt 4 "Betrieb", Nutzer deployt selbst). **Neu:**
> `VISION.md` (Mission + Track-Modell/langfristige Roadmap über mehrere Sprachen/Themen) angelegt,
> `KURSPLAN.md` erstmals aus `CLAUDE.md` verlinkt und ans Track-Modell angeglichen (3.37, gemergt).
> Darauf aufbauend: `ProjectCourse.vue` generalisiert, neue Projekte-Übersicht mit Filtern unter
> `/projekte`, zwei neue Projekt-Kurse (Morsecode, Zahlen-Detektiv) — Branch
> `kurs-projekte-uebersicht` (3.38, inzwischen gemergt). **Neu:** Login-gated `/profil`-Seite mit
> Abschluss-Abzeichen pro Projekt-Kurs (3.39, Branch `profil-abschluss-badges`), lokal
> fertig/getestet, noch **nicht** gemergt. Dabei auch Projekt-Kurs-Fortschritt erstmals mit dem
> Account synchronisiert (war vorher nur pro Browser gültig).
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

### 3.1 Einstufung & Checks (PR #1) — gemerged

Kurs `python-einstufung`, Fragen in `content/python-checks/weeks.json`, Check-Tab pro Woche,
Deep-Link öffnet den 12-Wochen-Kurs an der richtigen Stelle. Details: `git log` / PR #1.

### 3.2 Admin, Accounts, Sync, Deploy (PR #2) — gemerged

Express+SQLite-API (`api/`, `node:sqlite`, Node ≥ 22), Admin-Login + User-Verwaltung, Learner-Login
mit Progress-Sync (per-Key-Merge nach `updatedAt`, ohne Login bleibt alles lokal), Single-Port-Deploy
(`docker compose up -d --build app` → Service **`app`**, nicht `prod`). Aktuelle Betriebsbefehle stehen
in Abschnitt 4, Details zur Umsetzung: `git log` / PR #2.

### 3.3 Notebook-Sync-Loop-Fix (PR #3) — gemerged

**Gelernte Regel:** Sync darf nach dem Anwenden von Server-Zuständen niemals einen vollen
Notebook-Re-Fetch auslösen — sonst reagiert der Watcher darauf, synct erneut, und es entsteht eine
Endlosschleife (führte zu sichtbarem Blinken bei eingeloggten Nutzern). Sync wendet Zustand seither
nur lokal an, ohne Reload. Details: `git log` / PR #3, `useProgressSync.js`.

### 3.4 Storytelling-Überarbeitung 12-Wochen-Kurs — gemerged

Alle 3 Varianten (Abenteuer/Pferde/Sci-Fi), alle 12 Wochen wurden auf zusammenhängende Szenen statt
Schritt-Listen geprüft und mehrere echte Content-Bugs behoben (kaputter Code, Boss-Quest-Duplikate,
Textfehler) — Details siehe Commit-Historie.

**Gelernte Regeln (weiterhin relevant für Notebook-Arbeit):**
1. Debug-Notebook-Bugs müssen unabhängig vom geteilten Jupyter-Kernel-Zustand sein — ein "vergessener
   Import" wirkt nicht mehr, wenn eine frühere Zelle das Modul schon importiert hat.
2. Debug-Notebook-Kommentare dürfen die Lösung nicht verraten — vage Leitfragen sind ok.
3. Bei jeder Notebook-Änderung: Code-Zellen ausführen und JSON-Validität prüfen, bevor committet wird.

Regressionstests: `tests/storytelling-content.spec.js` (Teil von `npm run test:checks`).

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

### 3.12 Wochen-Zertifikate: Punkte-/Sammelsystem ersetzt (Branch `wochen-zertifikate`)

Größere Änderung, vom Nutzer explizit angestoßen: das Punkte-/
Sammel-Item-System wird komplett durch **Wochen-Zertifikate** ersetzt. Auslöser war der Wunsch, dass
Boss-Quests+Missionen allein ("einfaches Abhaken") zu wenig Aussagekraft haben. Der Nutzer wollte das
Für-und-Wider erst diskutieren, dann kam die Anforderung in zwei Schritten — erst "Quiz + eine
Coding-Aufgabe zusätzlich zu den Missionen", dann (nach weiterem Nachdenken des Nutzers) die deutlich
einfachere Endversion: **Missionen zählen gar nicht mehr fürs Zertifikat.**

Finaler Stand:
- **Ein** Zertifikat pro Woche (keine Varianten-Aufteilung — ein früherer Zwischenstand hatte noch
  Abenteuer-/Pferde-/Sci-Fi-Zertifikate vorgesehen, das wurde verworfen, weil das Zertifikat inhaltlich
  komplett variantenunabhängig ist: Quiz und Coding-Aufgaben sind generisch/geteilt. 3 separate,
  aber immer identisch verliehene Zertifikate hätten keinen Mehrwert gehabt). Verliehen wird es, sobald
  der Wochen-Check bestanden ist — und der besteht aus **Quiz + zwei Coding-Aufgaben** (leicht +
  schwerer, je eine pro Woche, generisch, Pyodide-basiert). Missionen/Boss-Quests bleiben als
  freiwillige Übungs-Checkliste pro Variante bestehen (weiterhin abhakbar in `MissionenPanel.vue`),
  zählen aber nicht mehr als Voraussetzung.
- Punkte/Items sind komplett weg, keine Kompatibilitäts-Schicht. `public/rewards-manifest*.json`
  enthalten nur noch ID-Listen (`missions`, `bossQuests`), keine `points`/`item`-Felder mehr.
- `content/python-checks/weeks.json`: Feld heißt jetzt `codingChallenges` (Array, nicht mehr
  `codingChallenge`-Objekt) — 2 Einträge pro Woche (`instruction(_en)`, `codeTemplate`,
  `validation: {type:'output_contains', expected}`). Alle 12 neuen "schwereren" Aufgaben lokal mit
  `python3` gegen eine Referenzlösung verifiziert, bevor sie geschrieben wurden.
- `useWeekChecks.js`: `codingPassed` ist jetzt ein Objekt `{0: true, 1: true}` (ein Flag pro
  Challenge-Index) statt eines einzelnen Booleans; `isCodingPassedForWeek(week, totalChallenges=2)`
  prüft alle Indizes. `CodeChallenge.vue` bekam eine `challenge-index`-Prop (plus `label`), damit
  `WeekCheckPanel.vue` zwei Instanzen nebeneinander rendern kann (`data-challenge-index="0"/"1"` am
  Root-Element für Tests).
- `useZertifikate.js`: `isCertificateEarned(weekNumber)` prüft nur noch `isWeekCheckPassed()` — Manifest/
  Missionen werden dafür nicht mehr angefasst (Manifest-Zugriff bleibt nur noch für die
  Missionen-Anzeige selbst erhalten). `countCertificates()` ohne Variantenparameter.
- `FortschrittWidget.vue` komplett vereinfacht: keine Varianten-Auswahl/-Tabs mehr, ein einzelnes
  12-Wochen-Zertifikats-Raster statt drei parallele Raster.
- **Alle "\*\*Belohnung(en):\*\*"/"\*\*Reward(s):\*\*"-Zeilen aus allen 444 Notebooks entfernt** — die
  waren nach der Punkte-Entfernung inhaltlich verwaist (nannten XP/Huf-Punkte/Cyber Credits/Items, die
  es im Produkt nicht mehr gibt). Das war technisch aufwändiger als erwartet: Notebooks im Repo
  verwenden mindestens **drei verschiedene JSON-Serialisierungs-Stile** für `cell.source`
  (mehrzeiliges Array mit einem String pro Zeile; ein einzelner String mit eingebetteten `\n`;
  kompaktes Array, mehrere Strings auf einer physischen Zeile) — ein naiver `json.load()` +
  `json.dump()`-Rewrite des ganzen Files hätte in >80% der Fälle die Formatierung anderer,
  unveränderter Stellen zerstört (mit `indent=1`/`2`/`4` verglichen: keines matcht die Originaldatei
  byte-genau). Lösung: nur die betroffenen Zeilen/Werte gezielt per Text-Ersetzung anfassen (nie das
  ganze File neu serialisieren), nach jeder Änderung `json.loads()` zur Validierung, und bei jeder
  entfernten "letztes Array-Element"-Belohnungszeile das jetzt illegale Trailing-Komma vor der
  schließenden Klammer separat reparieren. Nebenbei auch die **"Lernziele"-Checkliste** entschärft:
  das ☐-Symbol ist reiner Unicode-Text (kein `- [ ]` GFM-Task-Listen-Syntax, `marked` rendert es nicht
  interaktiv) — Formulierungen wie "Hake ab, was du schon kannst" / "Wenn du alle Punkte abhaken
  kannst" (DE) bzw. "Check/Tick off..." (EN) täuschten Klickbarkeit vor, die nie existiert hat. Ersetzt
  durch "Überprüfe selbst, ob du diese Fähigkeiten gemeistert hast" / "Check for yourself...".
  Nutzer-Entscheidung dazu: kleiner Text-Fix statt echter interaktiver Checkboxen (das wäre ein
  eigenes, deutlich größeres Feature gewesen).
- **Lokales Fortschritt-Skript entfernt** (`scripts/fortschritt.py`, `scripts/README-fortschritt.md`,
  `scripts/rewards-manifest.json`, sowie die `fortschritt-script.zip`-Bündelung in
  `pack_notebooks.py`): Nutzer-Entscheidung, dass Fortschritt-Sync über den Account (Login, PR #2)
  laufen soll statt über ein CLI-Skript + manuellen JSON-Export/Import für Jupyter/VS-Code-Nutzer.
  Der allgemeine Export/Import-Button in `FortschrittWidget.vue` bleibt bestehen (generisches
  Backup/Restore, nicht exklusiv ans Skript gebunden).
- **Ein Playwright-Bug beim Testen selbst** (nicht im Produktivcode): `passWeek1Quiz()` im Test las
  `.quiz-question`-Anzahl, bevor `loadWeekChecks()` (asynchroner Fetch) fertig war → 0 Fragen erkannt,
  0 Klicks, `.btn-check-quiz` blieb für immer disabled. Fix: `await expect(cards.first()).toBeVisible()`
  vor dem Auslesen der Anzahl ergänzen. Falls an anderer Stelle ein ähnliches Timing-Problem auftaucht
  (Frage-Anzahl 0 trotz sichtbarem Check-Tab): zuerst prüfen, ob auf das Laden gewartet wurde, bevor
  ein Bug in `QuizStep.vue`/`WeekCheckPanel.vue` vermutet wird.
- `content/python-12-wochen-grundkurs(-en)/beschreibung.md`, `INHALTE.md` Abschnitt 4 und die
  betroffenen `progress.*`/`mission.*`-Locale-Texte wurden passend zur neuen Terminologie aktualisiert
  (kein "Punkte sammeln" mehr, kein Verweis mehr auf Missionen als Zertifikats-Voraussetzung).
  `tests/storytelling-content.spec.js`: zwei Tests entfernt, die variantenspezifische
  Belohnungs-Wortwahl prüften (z.B. "Huf-Punkte statt XP") — die geprüfte Textstelle existiert jetzt
  gar nicht mehr, nicht weil der Fix falsch war, sondern weil das Feature (Belohnungszeilen) komplett
  entfernt wurde.

### 3.13 Zertifikat-PDF-Download (gleicher Branch, Nachtrag)

Nutzer-Wunsch nach einem greifbaren Dokument statt nur dem 🎓-Icon im Raster. Jedes verliehene
Wochen-Zertifikat lässt sich jetzt als PDF herunterladen —
mit den Lernzielen der Woche (aus `woche{N}.md`, Abschnitt "Lernziele"/"Learning goals"), Datum, Logo
und einem editierbaren Namensfeld. **Nur sichtbar, wenn ein Account eingeloggt ist** — bei rein
lokalem Fortschritt ohne Login erscheint stattdessen ein Hinweistext. E-Mail-Versand ist bewusst noch
nicht Teil davon (eigenes, späteres Thema — Kontaktweg für Account-Wünsche kommt separat).

- Neue Dependency `pdf-lib` (reines Browser-JS, kein Server-PDF nötig für den Download) — wird per
  dynamischem `import()` erst beim Klick geladen (Vorbild: `useCourseData.js` lädt Content genauso
  lazy), damit das PDF-Feature das Haupt-Bundle nicht aufbläht.
- `useWeeklyContent.js:parseWeekMarkdown` hat jetzt zusätzlich `lernzieleFull` (volle, ungekürzte
  Lernziele-Bullets) neben dem bestehenden `lernziele` (auf 36 Zeichen gekürzte UI-Chips) — die Chips
  waren für ein Zertifikat unbrauchbar ("Text mit `print()` ausgeben" → nur "Text"). `CourseDetail.vue`
  reicht das schon geladene `weeks`-Array jetzt per Prop an `FortschrittWidget.vue` durch.
- **Gelernte Regel:** die Standard-PDF-Fonts (Helvetica) können nur WinAnsi/Windows-1252 kodieren —
  Emoji aus Notebook-/Markdown-Titeln (z.B. das 📚 im Wochentitel-Frontmatter) lassen `pdf-lib` sonst
  mit "WinAnsi cannot encode …" abstürzen. `useCertificatePdf.js:sanitizeForPdfFont` filtert das vorher
  pro Zeichen heraus (testet `font.widthOfTextAtSize` je Unicode-Codepoint). Gilt für jeden Text, der
  aus Content-Dateien statt fest im Code steht.
- Bullet-Listen in `pdf-lib` nicht einzeln zentrieren (`drawText` pro Zeile mit eigener Center-Breite)
  — das ergibt eine optisch zerfranste, unterschiedlich eingerückte Liste. Stattdessen alle Zeilen
  vorab sammeln, per größter Zeilenbreite als Block linksbündig positionieren und den Block als Ganzes
  zentrieren.
- Tests: `tests/zertifikate.spec.js` (ohne Login → kein Download-Button, nur Hinweistext;
  `test:checks`, kein API-Server nötig) + `tests/auth-ui.spec.js` (echter Login über den Test-API-Server
  auf :3011, PDF-Download-Button erscheint erst danach, Playwright fängt den echten `download`-Event ab
  und prüft den Dateinamen; `test:auth`).
- `api/node_modules` fehlte in dieser Arbeitskopie (Express nie installiert) — `cd api && npm install`
  nachgeholt, damit `npm run test:auth` den Test-API-Server überhaupt starten kann.

### 3.14 Punkte-artige Feier-Texte entfernt (Branch `entferne-xp-texte`)

Nachtrag zu `wochen-zertifikate`: die entfernten `**Belohnung:**`-Zeilen waren nicht die einzige
Stelle, die noch vom alten Punktesystem erzählte — Boss-Quest-Lösungscode und Abschluss-Markdown
gaben weiterhin XP/Huf-Punkte/Cyber-Credits-Zahlen aus, die es im Produkt nicht mehr gibt.

**Umfangs-Analyse zuerst** (wie in HANDOFF.md schon vorgemerkt): grep nach `XP`, `Huf-Punkte`,
`Hoof Points`, `Cyber Credits`, `Gesammelte` über alle 444 Notebooks, dann jeder Treffer einzeln
eingeordnet — nicht jede Erwähnung ist ein Überbleibsel:
- **Entfernt (echte Reward-Behauptungen ans reale Publikum):** der Präfix `+400 XP: ` (bzw.
  `Huf-Punkte`/`Hoof Points`/`Cyber Credits`) in den `🎉`-Boss-Quest-Abschluss-Prints — 125
  Notebooks, DE+EN, alle drei Varianten, sowohl `5_boss` (Beispiel-Ausgabe) als auch `6_loesungen`
  (tatsächlicher Lösungscode). Plus drei Einzelfälle: `**Gesammelte XP:** 1500 Punkte` (Woche 1
  Abenteuer Boss), das Versprechen „sammelst du **1000 XP**!" in der Woche-1-Lektion, und
  „…und 500 Huf-Punkte/Hoof Points für den Erstplatzierten" in der Woche-1-Pferde-Siegerehrung
  (DE+EN) — dort blieb nur der Sachpreis (Pokal, Schleife) übrig, die Punktzahl gestrichen.
- **Bewusst NICHT angefasst (fiktive Story-Werte, die die Übung selbst berechnet, keine echte
  Belohnung ans reale Publikum):** `hero_xp`/`erfahrung`-Felder in Helden-Steckbrief-Übungen,
  `reward`/`belohnung`-Tupel in Dict/Tupel-Übungen, die Cyber-Credits-Berechnung einer
  Asteroiden-Bewertungsübung, `erfolgs_xp`/`earned_xp` als Summe über eine selbst gebaute
  Quest-Liste (Listen/Dict-Übung), sowie die `+200 XP`/`-20 HP`/`-10 HP`-Zufallsereignis-Prints in
  Woche 3 (dieselbe Übung nennt Schaden in "HP", das war nie eine reale Platform-Währung — die
  Struktur ist identisch, nur "XP" fällt hier zufällig mit dem alten Currency-Namen zusammen). Die
  Unterscheidung: erzählt die Zeile dem *echten Lernenden*, dass er/sie gerade etwas Reales
  bekommen hat (Session-Abschluss-Feier), oder ist die Zahl nur ein Zwischenwert, den die Übung
  selbst als Programmier-Aufgabe berechnet (Variablen/Listen/Dicts/Summen)?
- Website-Texte (`src/`, `public/*.json`, `beschreibung.md`) waren bereits vollständig sauber —
  dort war schon in `wochen-zertifikate` alles entfernt worden.

**Umsetzung:** Massenänderung per Text-Ersetzung (nicht JSON-Reserialisierung) wie schon beim
`**Belohnung:**`-Cleanup — Regex `(🎉 )\+\d+ (XP|Huf-Punkte|Hoof Points|Cyber Credits): ` → `\1`
für die 125 Boss-Quest-Prints, drei manuelle Einzel-Edits für die restlichen Fälle. Nach jeder
Änderung `json.loads()` zur Validierung (126 Notebooks geprüft, alle valide) sowie `ast.parse()`
auf jede Code-Zelle der geänderten Notebooks (keine Syntaxfehler).

**Getestet:** `npm run test:checks` (43 Tests grün, unverändert — reine Text-/Print-Output-Änderung
ohne Verhaltensänderung, laut `WORKFLOW.md` kein neuer Test nötig).

### 3.15 Einstufungstest: Distraktoren Wochen 5-12 geschärft (Branch `einstufung-distraktoren-w5-12`)

Fortsetzung von 3.6 (`et-fixes` hatte nur Wochen 1-4 gemacht, 12 von 40 Fragen). Jetzt Wochen 5-12
durchgesehen (80 Fragen) — 28 hatten unplausible Falsch-Antworten, die man auch ohne Python-Wissen
ausschließen konnte (z.B. "Nur am Wochenende" bei "Muss man jedes Modul selbst schreiben?", oder
themenfremde Distraktoren wie "Musik abspielen" bei "Wofür ist JSON gut?"). Ersetzt durch nähere
Verwechslungen, die echtes Verständnis brauchen — bevorzugt durch **Vertauschen verwandter
Konzepte**: `json.dumps`/`json.loads` gegeneinander als Distraktor, `append`/`insert(0)`,
`remove(value)`/`pop(index)`, `import math`/`from math import pi`, Radius/Durchmesser bei
`turtle.circle()`. Bereits gute Distraktoren (z.B. `class`/`def`/`for`, `new KlassenName`) bewusst
nicht angefasst.

**Umsetzung:** wie bei den vorherigen JSON-Content-Änderungen keine volle Reserialisierung —
Text-Ersetzung pro Frage, auf den Block zwischen zwei `"id":`-Markern begrenzt (verhindert, dass
generische Wörter wie "Ein Fehler" oder "Ein Modul", die in mehreren Fragen als Distraktor
vorkommen, versehentlich in der falschen Frage landen). `correctIndex` unverändert, nur
Falsch-Antworten getauscht — DE (`options`) und EN (`options_en`) synchron gehalten.

**Getestet:** `npm run test:checks` (43 Tests grün) + Duplikat-Check (kein Options-Array enthält
nach der Änderung zwei identische Einträge, DE wie EN) + manuelle Durchsicht aller 28 geänderten
Fragen, ob ein Distraktor versehentlich auch als "richtig" durchgehen könnte — keine Verhaltens-
änderung, laut `WORKFLOW.md` kein neuer Test nötig (die bestehenden Tests lesen Fragen/Antworten
sowieso dynamisch aus `weeks.json`, nicht hart codiert).

### 3.16 Debug-Notebook-Ziele: Pferde + Abenteuer nachgezogen (Branch `debug-ziele-pferde-abenteuer`)

Fortsetzung von 3.5 (`debug-notebook-safety` hatte nur Sci-Fi gemacht, 24 Dateien). Jetzt Pferde +
Abenteuer, DE + EN, alle 12 Wochen ergänzt — 48 Debug-Notebooks (`2_debug.ipynb`), je 3 Bug-Zellen,
144 `**Ziel:**`/`**Goal:**`-Zeilen insgesamt (nur 3 Bugs pro Notebook, nicht 6 wie ursprünglich
geschätzt).

**Vorgehen:** Erst alle 144 Bug-Code-Zellen gelesen (Pferde/Abenteuer DE komplett, EN stichproben-
artig gegengeprüft) und pro Bug den *beabsichtigten* korrekten Output ermittelt, ohne die Ursache
zu verraten — z.B. bei `koordinaten[0] = 150` (Tupel-Bug, identisch zum Sci-Fi-Beispiel aus 3.5):
"Ziel: Das Programm soll die erste Koordinate auf `150` ändern", nicht "Tupel sind unveränderlich".
Bei zwei Bugs (Woche 5 #1: eine nie aufgerufene Funktion; Woche 9 #3: CSV-Datei, die im Notebook nie
angelegt wird, bevor sie gelesen wird) gibt es keinen sinnvollen "soll X ausgeben"-Satz — dort
generischer formuliert ("soll die Funktion fehlerfrei definieren" bzw. "soll den Inhalt zeilenweise
ausgeben"). Die CSV-Datei-Lücke selbst (fehlende Datei-Erstellung) ist ein separates, vorbestehendes
Content-Problem, nicht Teil dieser Änderung.

**Technisch — drei verschiedene JSON-Stile pro Markdown-Zelle in freier Wildbahn** (analog zur
bereits bekannten Notebook-Serialisierungs-Vielfalt aus `wochen-zertifikate`, siehe 3.12): reiner
String, Array mit einem Element, Array mit einem String pro Zeile. Lösung: unabhängig vom Stil ist
der abschließende Fragesatz ("Was ist falsch? Finde und behebe den Fehler!" bzw. EN-Varianten mit
"bug!"/"error!") immer das letzte Textstück vor dem schließenden Anführungszeichen — die neue
Ziel-Zeile wird einfach dort angehängt (`\n\n**Ziel:** ...`), unabhängig davon, ob dieser String
ein eigenständiger Wert oder das letzte Array-Element ist. Kein Array-Element hinzugefügt, kein
Full-Reserialize.

**Verifiziert:** nicht per `ast.parse()` auf Code-Zellen (die enthalten ja absichtlich kaputten
Code — das hätte 35 erwartete "Fehler" gemeldet, die keine sind), sondern per Zell-für-Zell-Diff
gegen den alten Stand: bestätigt, dass ausschließlich Markdown-Zellen geändert wurden und jede
Änderung eine reine Erweiterung des alten Texts ist (kein Code-Byte angefasst).

**Getestet:** `npm run test:checks` (45 Tests, 2 neu: Pferde- und Abenteuer-Pendant zum
bestehenden Sci-Fi-Ziel-Test in `storytelling-content.spec.js`) + `npm test` (voller Lauf inkl.
`tests/notebooks.spec.js` über alle 12 Wochen × 3 Varianten, 56 Tests grün).

### 3.17 Personalisierte Falsch-Antwort-Erklärungen (Branch `einstufung-personalisierte-erklaerungen`) — gemerged

Jede falsche Antwort einer `multiple_choice`-Frage im Check-Tab/Einstufungstest bekommt jetzt eine
eigene, passende Erklärung (neue Felder `optionExplanations`/`optionExplanations_en` in
`weeks.json`, ausgewertet über `explanationForAnswer()` in `useTaskValidation.js`) statt der einen
geteilten `explanation` für alle falschen Optionen. `multiple_select`-Fragen bleiben bewusst ohne
Personalisierung. **Gelernte Regel:** `shuffleQuestionOptions()` muss Optionstext und zugehörige
Erklärung als Paar mischen, sonst hängt nach dem Shuffle die falsche Erklärung an der falschen
Option. Nebenfund: 119 von 120 `explanation_en`-Felder waren nie übersetzt (identisch zum
deutschen Text) — im selben Zug mitgefixt. Details/Content-Erstellung: `git log`/PR.

### 3.18 Refactoring-Start: `weeks.json` pro Woche aufgeteilt (Branch `weeks-json-splitten`) — gemerged

Erster Schritt eines größeren, vom Nutzer angestoßenen Refactorings gegen zu große Dateien (Analyse
ergab: die meisten großen `.vue`-Components sind zu 40-65% `<style>`-Block, nicht Logik — Composables-
Schicht ist bereits sauber geschichtet). `content/python-checks/weeks.json` (3925 Zeilen, größte
Datei im Repo) war der einzige Content-Bereich, der noch nicht pro Woche gesplittet war.

- **Neu:** `content/python-checks/config.json` (`passThreshold`, `placementPerWeek`,
  `placementPassThreshold`, `weekCheckCount`, `projects`) + `week-1.json`…`week-12.json` (je
  `title`/`title_en`/`questions`/`codingChallenges`). Split per Skript, Round-Trip gegen die alte
  Datei geprüft (`json.load` alt == gemergte neue Dateien, byte-äquivalent auf Datenebene).
- **Zwei Lade-Pfade, weil zwei Laufzeiten:** `useWeekChecks.js` (Browser/Vite) mergt weiterhin per
  `import.meta.glob` + frischem `loader()`-Aufruf pro `loadWeekChecks()`-Call — das war schon vorher
  bewusst so gebaut, damit Content-Edits ohne vollen Seiten-Reload sichtbar werden (HMR-Bypass), und
  musste erhalten bleiben. Für die Playwright-Tests (laufen in Node, nicht im Vite-Dev-Server) neuer
  kleiner Loader `content/python-checks/index.mjs` (reines `fs`/`readdirSync`, kein Vite nötig) —
  ersetzt in den 3 betroffenen Tests (`week-checks.spec.js`, `week-checks-logic.spec.js`,
  `zertifikate.spec.js`) den bisherigen `import ... with { type: 'json' }` auf die alte Einzeldatei.
- **Gelernte Regel:** bei Content, der sowohl im Vite-Dev-Server (Browser) als auch in Node-Tests
  gelesen wird, reicht ein Lade-Mechanismus nicht immer aus — `import.meta.glob` ist Vite-exklusiv,
  ein Node-Test braucht einen eigenen (einfachen) Loader. Beide müssen bei künftigen Schema-Änderungen
  synchron gehalten werden.

**Getestet:** `npm run test:checks` (49 Tests grün) + `npm run test:auth` (13 Tests grün, inkl.
Zertifikat-PDF-Tests, die Wochendaten laden) — alles über echte Chromium-Läufe gegen den Vite-Dev-
Server, keine reine Unit-Verifizierung. Reine Datenumstrukturierung ohne Verhaltensänderung, laut
`WORKFLOW.md` kein neuer Test nötig.

**Offen (nächste Schritte desselben Refactorings, siehe `todo.md`):** CSS-Konsolidierung (doppelte
Klassen wie `.btn-kernel`/`.code-editor` in LessonView/ProjectCourse/InteractiveCourse/CodeChallenge),
`WeekSection.vue`-Aufteilung, `LessonView.vue`/`QuizStep.vue`-Entflechtung, Ternary-Cleanup (97
Inline-`lang === 'en' ? X : Y`).

### 3.19 Refactoring Schritt 2: CSS-Konsolidierung Kurs-Sidebar-Layout (Branch `css-konsolidierung-kurslayout`) — gemerged

`ProjectCourse.vue` ist laut 3.11 eine "reduzierte Kopie" von `InteractiveCourse.vue` — Diff der
kompilierten CSS-Regeln bestätigte: der komplette Sidebar/Lektionsliste/Fortschritt-Block
(`.course-layout`, `.lessons-sidebar`, `.lesson-item`, `.sidebar-actions`, `.btn-export`/`-import`,
`.no-lesson`, die zugehörige `@media (max-width: 768px)`-Regel — ~165 Zeilen) war zwischen beiden
Dateien byte-identisch. In `src/assets/styles/course-layout.css` ausgelagert.

**Gelernte Regel (wichtig, hat den ersten Versuch kaputt gemacht):** `@import 'shared.css';`
**innerhalb** eines `<style scoped>`-Blocks bekommt in diesem Vite-8/`@vitejs/plugin-vue`-6-Setup
einen **eigenen, vom Rest der Datei abweichenden** `data-v-xxxx`-Scope-Hash — die importierten
Regeln matchen dann keine Template-Elemente mehr (per Playwright verifiziert: `getComputedStyle()`
lieferte Default-Werte statt der erwarteten). Lösung: den `@import` in einen **separaten,
UNscoped** `<style>`-Block packen (Vue-SFCs erlauben mehrere `<style>`-Blöcke) — dann gilt er
global, was hier sicher ist, weil alle Klassennamen repo-weit geprüft exklusiv in genau diesen
zwei Components vorkommen. **Ausnahme:** `.loading`/`.error` sind generische Namen, die in ~10
anderen Components mit eigener Bedeutung vorkommen (`PlacementCourse.vue`, `JupyterNotebook.vue`,
`AdminView.vue`, …) — die blieben bewusst als kleine Duplikate in beiden Dateien statt in der
globalen Datei, sonst hätte die globale Regel dort geleakt. **Bei künftigen CSS-Extraktionen:**
vor dem Auslagern grep-prüfen, ob der Klassenname anderswo im Repo mit anderer Bedeutung vorkommt.

**Getestet:** `npm run test:checks` (49 Tests) + `npm run test:auth` (13 Tests) grün. Zusätzlich
Vite-Dev-Server gestartet und per Playwright `getComputedStyle()` auf `.course-layout`/
`.lessons-sidebar`/`.lesson-item` in beiden Kursen verglichen (identische Werte) sowie
Full-Page-Screenshots beider Kurse visuell geprüft — reine CSS-Umstrukturierung ohne
Verhaltensänderung, laut `WORKFLOW.md` kein neuer Test nötig, aber visuelle Verifizierung war hier
nötig, weil Playwrights Funktionstests kein CSS prüfen.

**Ergebnis:** `InteractiveCourse.vue` 547 → 386 Zeilen, `ProjectCourse.vue` 383 → 217 Zeilen (−341
Zeilen Duplikat, jetzt eine gemeinsame 180-Zeilen-Quelle).

**Offen (nächste Schritte):** `.btn-kernel`/`.code-editor`/`.kernel-status`/`.feedback-*` zwischen
`LessonView.vue` und `CodeChallenge.vue` sind NICHT identisch (nur Klassennamen gleich, Werte
unterscheiden sich) — dort lohnt sich vor einer Konsolidierung erst ein Abgleich, ob die
Unterschiede beabsichtigt sind oder Drift. Danach `WeekSection.vue`-Aufteilung, `LessonView.vue`/
`QuizStep.vue`-Entflechtung, Ternary-Cleanup.

### 3.20 Refactoring Schritt 3: `WeekSection.vue` in Subkomponenten aufgeteilt (Branch `weeksection-subkomponenten`) — gemerged

Zwei in sich geschlossene Template-Blöcke aus `WeekSection.vue` (666 Zeilen) ausgelagert:
`CheatSheetList.vue` (der komplette Cheat-Sheet-Akkordeon-Block: Header, Download-Buttons,
Markdown-Vorschau mit allen `:deep()`-Styles) und `VariantSelector.vue` (die 3
Varianten-Buttons). Beide erhalten `week`/`cheat-sheets` als Prop und emittieren nach oben
(`toggle`/`set-variant`) — der Zustand (`week.expandedCheatSheets`, `week.selectedVariant`) bleibt
weiterhin außerhalb von `WeekSection.vue` verwaltet, wie schon vor dem Split (`WeekSection.vue` war
selbst schon nur ein Relay dafür, keine Verhaltensänderung).

**Gelernte Regel:** vor dem Verschieben von CSS-Regeln in eine neue Komponente per Playwright
`getComputedStyle()` auf dem ALTEN Stand geprüft, nicht nur die Selektor-Texte verglichen — dabei
einen bestehenden CSS-"Leak" gefunden: `.cheat-sheet-header h4` bekam über die generische
`.downloads-section h4`-Regel (gedacht für die "Sonstige Downloads"-Liste) zusätzlich
`border-top`/`padding-top`, weil beide Blöcke früher denselben `.downloads-section`-Wrapper und
dieselbe Scope-Datei teilten. Nach dem Split verschwindet dieser Cross-Selector-Effekt automatisch
(andere Komponente, anderer Scope-Hash) — die zwei Werte deshalb explizit in
`CheatSheetList.vue`s eigene `.cheat-sheet-header h4`-Regel übernommen, damit sich am Rendering
nichts ändert. **Bei künftigen Komponenten-Splits:** immer prüfen, ob eine generische Ziel-Regel
(hier `.downloads-section h4`) versehentlich auch Elemente trifft, die mit ausgelagert werden.

**Getestet:** `npm run test:checks` (49) + `npm run test:auth` (13) + `npm test` (60, volle
Notebook-Suite über alle Wochen/Varianten) grün. Zusätzlich per Playwright verifiziert: Varianten-
Umschaltung funktioniert weiter (aktive Klasse + Hintergrundfarbe korrekt), Cheat-Sheet-Akkordeon
öffnet/schließt weiter, Download-Links funktionieren, und der `.cheat-sheet-header h4`-Computed-Style
ist byte-identisch zum Stand vor dem Split.

**Ergebnis:** `WeekSection.vue` 666 → 451 Zeilen, neue `CheatSheetList.vue` (201 Zeilen) und
`VariantSelector.vue` (73 Zeilen).

**Offen (nächste Schritte):** `LessonView.vue`/`QuizStep.vue`-Entflechtung, dann Ternary-Cleanup.

### 3.21 Refactoring Schritt 4: `LessonView.vue` entflechtet (Branch `lessonview-entflechten`) — gemerged

Glossar/Content-Loading (Lektions-Markdown laden, Glossar laden, Tooltip-Spans in Lektionstext und
Aufgabenanweisungen einfügen — `import.meta.glob`-Listen, `loadGlossary`, `loadContent`,
`instructionWithGlossary`, `applyGlossaryTooltips`, `escapeHtml`) aus `LessonView.vue` in ein neues
`src/composables/useLessonContent.js` ausgelagert. Task-Run/Check-State-Machine (der andere,
unabhängige Verantwortungsbereich in derselben Datei) bleibt unverändert in der Komponente.

**Kopplungsdetail:** `isMounted` (verhindert State-Updates nach Unmount) wird von BEIDEN
Verantwortungsbereichen genutzt (Content-Loading UND Task-Run/Check) — bleibt deshalb in
`LessonView.vue` deklariert und wird als Ref-Parameter in `useLessonContent(isMounted)`
hineingereicht, statt eine zweite, separate Unmount-Guard-Instanz im Composable zu duplizieren.

**Getestet:** `npm run test:checks` (49) + `npm run test:auth` (13) grün. Zusätzlich per Playwright
verifiziert: Glossar-Tooltip-Spans (`.glossary-term`) erscheinen weiterhin im gerenderten
Lektionstext mit korrektem `title`-Attribut (Erklärungstext) — das ist der einzige Teil dieser
Änderung, der nicht schon durch bestehende Funktionstests (Interaktiver Kurs, Cäsar-Chiffre)
abgedeckt war.

**Ergebnis:** `LessonView.vue` 684 → 586 Zeilen, neues `useLessonContent.js` (114 Zeilen).

**Offen (nächste Schritte):** `QuizStep.vue`/`PlacementCourse.vue`-Entflechtung, dann Ternary-Cleanup.

### 3.22 Refactoring Schritt 5: `PlacementCourse.vue` — Score-Logik ausgelagert (Branch `quizstep-placementcourse-entflechten`) — gemerged

**Abweichung vom ursprünglichen Plan:** `QuizStep.vue` beim genauen Lesen NICHT gesplittet — anders
als `LessonView.vue` (klar zwei Verantwortungsbereiche: Content-Loading vs. Task-Running) ist
`QuizStep.vue` bereits eine einzige, in sich kohärente Quiz-State-Machine (Antworten, Prüfen,
Feedback-Text — alles hängt zusammen, keine natürliche Trennstelle). Eine erzwungene Aufteilung
hätte nur Code verschoben, ohne echte Kohäsion zu verbessern (CLAUDE.md: keine Abstraktionen ohne
Not). Stattdessen bei `PlacementCourse.vue` eine echte, durch Duplikat-Beseitigung begründete
Extraktion gemacht: `restoreResults()` (gespeichertes Ergebnis → Raster-Zeilen) und `onSubmit()`
(frisch beantwortete Fragen → Raster-Zeilen) berechneten an zwei Stellen dieselbe Zeilenform
(`{weekNumber, title, score, correct, total, ok}`) — jetzt `computePlacementResults()` +
`weekScoresToRows()` in `useWeekChecks.js`, neben den bereits dort vorhandenen
Placement-Funktionen (`getPlacementQuestions` etc.), reine Datentransformation ohne
Vue-Abhängigkeit.

**Getestet:** `npm run test:checks` (49) + `npm run test:auth` (13) grün — inkl. der
Einstufungs-Tests, die genau die geänderten Pfade abdecken (frisches Ergebnis, wiederhergestellter
Zwischenstand, wiederhergestelltes fertiges Ergebnis).

**Ergebnis:** `PlacementCourse.vue` 497 → 463 Zeilen (moderat, weil die Extraktion bewusst klein und
gut begründet gehalten wurde statt forciert). `QuizStep.vue` unverändert (556 Zeilen) — bewusste
Entscheidung, siehe oben.

**Damit ist der Refactoring-Plan im Kern abgeschlossen.** Übrig: Schritt 6 (Ternary-Cleanup, 97
Inline-`lang === 'en' ? X : Y`) — niedrige Priorität, siehe Abschnitt 5/6, nur vorziehen falls eine
dritte Sprache konkret ansteht.

### 3.23 Refactoring Schritt 6: Ternary-Cleanup (Branch `ternary-cleanup`) — gemerged

Alle 97 Inline-`lang === 'en' ? X : Y`-Ternarys über 7 Components (InteractiveCourse.vue,
LessonView.vue, ProjectCourse.vue, CodeChallenge.vue, QuizStep.vue, WeekCheckPanel.vue,
PlacementCourse.vue) auf den bestehenden `t()`-Mechanismus (`useLanguage.js` + `locales/de.js`/
`en.js`) umgestellt. `locales/de.js`/`en.js` von 166 auf 224 Zeilen/Keys gewachsen, komplett
parallel gehalten (Skript-Check: gleiche Key-Menge, keine Duplikate, keine kopierten DE=EN-Werte
außer bewusst identischen Wörtern wie „Check"/„Home").

**Bewusst NICHT migriert (2 Kategorien, klar von echten Text-Ternarys unterschieden):**
1. **Daten-Feld-Auswahl statt UI-Text:** `q.explanation_en`/`q.explanation`,
   `q.question_en`/`q.question`, `challenge.instruction_en`/`instruction` — wählen zwischen zwei
   Content-Feldern eines Objekts (gleiches Muster wie `localizeQuestion()` in `useWeekChecks.js`),
   keine doppelt gepflegte UI-Prosa. Bleiben in den Components, wie auch die bereits vorher
   bestehenden, strukturell identischen Fälle in `CourseDetail.vue`/`Home.vue`
   (`kurs.title_en`/`title`), die nie Teil der 97 waren.
2. **Technische Werte, keine Übersetzung:** `AdminView.vue` (Locale-Code für
   `toLocaleString('en-GB'/'de-DE')`) und `InteractiveCourse.vue` (Ordner-Pfad-Suffix
   `${variant}-en`/`${variant}`) — beides Parameter, keine Prosa.

**Geteilte Keys zwischen Components** (analog zum CSS-Konsolidierungs-Muster aus 3.19): der
komplette "Lektionen-Sidebar"-Text (`lessons.*`) ist identisch zwischen `InteractiveCourse.vue` und
`ProjectCourse.vue` (dieselbe Kopplung wie beim CSS-Block), der "Code-Editor"-Text (`editor.*`,
`jupyter.ready`/`jupyter.noOutput`/`jupyter.unknownError`) identisch zwischen `LessonView.vue` und
`CodeChallenge.vue`. Beide Male eine Quelle statt doppelter Locale-Einträge.

**Gefundene, bewusst nicht angefasste Inkonsistenz:** `LessonView.vue`/`CodeChallenge.vue` nutzten
schon vorher amerikanisches „Initialize Python", während `jupyter.init` (JupyterNotebook.vue)
britisches „Initialise Python" verwendet — passend zum sonst konsequent britischen Englisch im
Kurs (siehe 3.9/3.10). Das ist eine vorbestehende Content-Inkonsistenz, keine durch diesen
Refactor eingeführte — absichtlich nicht "nebenbei" gefixt (Content-Entscheidung, kein
Strukturthema, würde einen eigenen kleinen Fix verdienen statt in einem Struktur-Refactor
mitzulaufen).

**Getestet:** `npm run test:checks` (49) + `npm run test:auth` (13) + `npm test` (60) grün.
Zusätzlich per Playwright gezielt auf Englisch durchgeklickt (Interaktiv-Kurs inkl. Varianten-Karten,
Cäsar-Chiffre, Einstufung inkl. „Ich weiß es nicht"-Rückmeldung, Wochen-Check inkl. Coding-Aufgabe
und volles Falsch-Beantworten-Feedback mit Interpolation) — Automatiktests laufen überwiegend auf
Deutsch, das war der einzige Weg, jede migrierte EN-Zeichenkette tatsächlich gerendert zu sehen.

**Damit ist der komplette Refactoring-Plan (Schritte 1-6) abgeschlossen.**

### 3.24 Curriculum-Lücken 12-Wochen-Kurs, Teil 1: Woche-12-Notebook-Bug (Branch `woche12-turtle-notebook-bug-fix`)

Erster Branch eines mehrteiligen Plans (`~/.claude/plans/joyful-wishing-piglet.md`, Content-Analyse
über alle 12 Wochen hat Reihenfolge-Probleme/Redundanz/Lernziel-Lücken gefunden — siehe `todo.md`
für die vollständige Liste der noch offenen Branches). Dieser Branch behebt einen reinen Bug ohne
inhaltliche Debatte: Woche-12-Lektion (nur Abenteuer, DE+EN — Pferde/Sci-Fi waren nie betroffen)
hatte eine tote `%pip install Tinker`-Zelle (installierte ein unrelated PyPI-Paket, das zufällig
"Tinker" heißt, nicht tkinter — turtle ist ohnehin Standardbibliothek, kein pip nötig) mit
eingebranntem `ModuleNotFoundError`-Output vom Autoren-Rechner. Komplett entfernt statt ersetzt, da
kein nachfolgender Code darauf aufbaute (`from turtle import *` wurde nirgends genutzt, alle
Beispiele machen ihr eigenes `import turtle`). DE-Notebook per Text-Ersetzung + `json.dumps(indent=1)`
bearbeitet (Datei war bereits exakt in diesem Stil serialisiert, verifiziert vor dem Schreiben),
EN-Notebook mit `NotebookEdit`-Tool (Zell-Lösch-Modus). Getestet: `json.loads()` + `ast.parse()` auf
alle verbliebenen Code-Zellen, `npm run test:checks` (49 Tests grün, reine Bug-Fix ohne
Verhaltensänderung, kein neuer Test nötig).

### 3.25 Curriculum-Lücken 12-Wochen-Kurs, Teil 2: Woche 3 (Branch `woche3-bedingungen-luecken`)

Woche 3 kündigte `and`/`or`/`not` und verschachtelte Bedingungen als Lernziele an (`woche3.md`),
lieferte aber nur `and` beiläufig in einem Beispiel — `not`/`or` kamen nirgends als lauffähiger Code
vor, verschachtelte `if`-Strukturen gar nicht. Neue Abschnitte "Zauberformel/Lektion/Systemprotokoll
4: Logische Verknüpfungen" (and/or/not, je ein eigenes Beispiel) und "... 5: Verschachtelte
Bedingungen" (Tür-/Stalltür-/Schleusen-Thema je nach Variante) an alle 6 `1_lektion`-Notebooks
angehängt (3 Varianten × DE/EN) — Glossar hatte `and`/`or`/`not` bereits korrekt definiert, nur die
Lektion nicht. Mit `NotebookEdit`-Tool (Insert-Modus) eingefügt, dadurch minimale Diffs (nur
Anhänge, keine Reformatierung bestehender Zellen). Alle Code-Zellen per `python3 exec()` tatsächlich
ausgeführt (nicht nur `ast.parse()`), um sicherzugehen, dass die Beispiele auch laufen. Getestet:
`npm run test:checks` (49 Tests grün, reine Content-Ergänzung ohne UI-Verhaltensänderung).

### 3.26 Curriculum-Lücken 12-Wochen-Kurs, Teil 3: Woche 4/6 Listen + break/continue (Branch `woche4-woche6-listen-neuordnung`)

**Ausgangslage laut Plan:** Woche 4 nahm Listen (`[]`, `.append()`, `enumerate()`) als Vorgriff auf
Woche 6 vorweg — echte Redundanz, da Woche 6 dieselben Grundlagen nochmal komplett von Null erklärt.
Nutzer-Entscheidung: Listen komplett aus Woche 4 raus, Woche 6 bleibt alleinige Quelle.

**Überraschender Fund währenddessen:** Der ursprüngliche Content-Audit hatte nur die
Abenteuer-Variante geprüft und daraus geschlossen, `break`/`continue` sei in Woche 4 überall
"angekündigt, aber nie geliefert". Tatsächlich ist das nur bei Abenteuer so (liefert `break`/
`continue` stattdessen in Woche 6, "Sammlungs-Zauber 4") — Pferde und Sci-Fi hatten in Woche 4
einen vollständigen, funktionierenden `break`/`continue`-Abschnitt ("Lektion/Systemprotokoll 3"),
dafür in Woche 6 **gar keinen**. Jede Variante lehrt `break`/`continue` also genau einmal, aber an
unterschiedlichen Stellen — ein Verstoß gegen die INHALTE.md-Regel "Konzepte müssen zwischen
Varianten identisch sein". Nutzer-Entscheidung nach Rückfrage: alle Varianten auf **Woche 6**
vereinheitlichen (wie Abenteuer).

**Umsetzung:**
- Woche 4 (alle 3 Varianten × DE/EN): Listen-Vorgriff-Zelle entfernt, `break`/`continue`-Abschnitt
  bei Pferde/Sci-Fi entfernt, Intro-Bullet-Point entsprechend angepasst. Der frei gewordene dritte
  Abschnitt ("Zauberformel/Lektion/Systemprotokoll 3") wurde durch **verschachtelte Schleifen**
  ersetzt (eigenes Lernziel in `woche4.md`, bisher nie eingelöst) — passt inhaltlich besser zum
  Wochenthema als Listen oder break/continue. `woche4.md` (DE+EN) Lernziele angepasst: "Schleifen
  über Strings und Listen" → "Schleifen über Strings", "break und continue" komplett gestrichen.
- Woche 6 (nur Pferde/Sci-Fi × DE/EN — Abenteuer hatte den Abschnitt schon): neuer Abschnitt
  "Sammlungs-Technik/Daten-Sammlung 4: break und continue" nach demselben Muster wie Abenteuer
  ergänzt (Themen-Liste durchsuchen, `break` bei Fund, `continue` bei Ausschluss).
- **Nebenbei gefundener und miterledigter Bug:** Pferdes altes Woche-4-`break`/`continue`-Beispiel
  hatte einen echten `NameError` (`print(f"Übung: {übung}")` referenzierte `übung` mit Ligatur-ü,
  während die Schleifenvariable `uebung` hieß) — verschwindet automatisch, da der ganze Abschnitt
  entfernt wurde, statt ihn zu reparieren und zu verschieben.
- **Nebenfund, nicht in diesem Branch behoben:** Woche 6 Pferde UND Sci-Fi enthalten in ihrem
  letzten Beispiel ("Fortgeschrittene Operationen") ebenfalls eine unerklärte List Comprehension
  (`[d for d in disziplinen if len(d) > 6]` bzw. Sci-Fi-Äquivalent) — analog zum bereits bekannten
  Fall in Woche 8 Abenteuer (siehe `todo.md`, Branch `woche8-list-comprehension-glossar`). Dieser
  Branch sollte beim Abarbeiten auf Woche 6 (alle 3 Varianten) erweitert werden, nicht nur Woche 8.

**Getestet:** `npm run test:checks` (49 Tests) + `npm test` (60 Tests, volle Notebook-Suite über alle
Wochen/Varianten) grün. Alle geänderten/neuen Code-Zellen zusätzlich einzeln per `python3 exec()`
ausgeführt (10 Notebooks, nicht nur `ast.parse()`), um sicherzugehen, dass die neuen
Verschachtelungs- und break/continue-Beispiele tatsächlich laufen.

### 3.27 Curriculum-Lücken 12-Wochen-Kurs, Teil 4: Woche 1 Boolean entfernt (Branch `woche1-boolean-entfernen`)

Boolean wurde in Woche 1 schon als einer von "drei häufigsten Werttypen" genannt (Lektion-Tabelle
+ Beispiel-Code-Zeile + Glossar-Begriff + Glossar-Code-Demo), obwohl Boolean offiziell erst
Woche-2-Thema ist. Nutzer-Entscheidung: komplett entfernen statt behalten — taucht jetzt zum
ersten Mal in Woche 2 als vierter Datentyp auf. "Drei häufigste Werttypen" → "Zwei häufigste
Werttypen" in allen Lektion-Überschriften angepasst. Alle 3 Varianten × DE/EN, je `1_lektion` +
`0_glossar` (12 Dateien). Rein mechanische Content-Korrektur ohne Bezug zu anderen Wochen.

**Getestet:** `npm run test:checks` (49 Tests grün) + alle 12 Notebooks per `json.loads()` validiert
+ alle Code-Zellen per `python3 exec()` tatsächlich ausgeführt (keine Fehler) + grep bestätigt: 0
verbleibende "Boolean"-Erwähnungen in allen 12 Dateien.

### 3.28 Curriculum-Lücken 12-Wochen-Kurs, Teil 5: try/except von Woche 5 nach Woche 8 (Branch `woche5-woche8-tryexcept-verschieben`)

Wieder ein Fund, der nur bei Abenteuer stimmte: `try`/`except` wurde dort in Woche 5
("Zauberformel 4: Fehler abfangen") gelehrt, obwohl es kein Lernziel ist, und in Woche 8 ungeklärt
in der Tupel-Unveränderlichkeits-Demo verwendet. Bei genauerem Hinsehen hatten **Pferde und Sci-Fi
in Woche 5 gar keine try/except-Einführung** — dort gab es also nichts zu verschieben, nur die neue
Erklärung in Woche 8 zu ergänzen. Zusätzlich fiel auf: alle drei Woche-8-Glossare behaupteten in
ihrem "Wiederholung aus Woche 5"-Abschnitt fälschlich, `try`/`except` sei dort schon behandelt
worden — stimmte nur für Abenteuer.

**Umsetzung:**
- Woche 5 Abenteuer (DE+EN): "Zauberformel 4"/"Spell Formula 4" komplett aus Lektion entfernt,
  Glossar-Einträge (`try`, `except`, `ValueError`, `TypeError`) + Code-Demo entfernt. Geprüft:
  keine anderen Woche-5-Dateien (Missionen/Debug/Boss) setzen try/except voraus.
- Woche 8 (alle 3 Varianten × DE/EN): neuer kompakter Abschnitt "🛡️ Fehler abfangen mit
  try/except" direkt vor der bestehenden Tupel-Unveränderlichkeits-Demo eingefügt (nutzt genau den
  `TypeError`-Fall, der dort ohnehin vorkommt, statt die breitere Woche-5-Erklärung mit
  ValueError/ZeroDivisionError zu kopieren). Glossar-Haupttabelle um `try`/`except`-Zeile ergänzt,
  die falsche "Aus Woche 5"-Zeile im Wiederholungs-Abschnitt entfernt (alle 3 Varianten, nicht nur
  Abenteuer).
- `woche8.md` (DE+EN): "Fehler mit try/except abfangen" als Lernziel ergänzt.
- **Nebenfund, nicht in diesem Branch behoben:** Woche 8 Pferde UND Sci-Fi enthalten (wie schon in
  Woche 6, siehe 3.26) je eine unerklärte List Comprehension in ihrem letzten Beispiel — Scope von
  `woche8-list-comprehension-glossar` in `todo.md` entsprechend erweitert.

**Getestet:** Alle 16 betroffenen Notebooks sequenziell mit einem gemeinsamen Namespace ausgeführt
(nicht isoliert pro Zelle — Funktionen aus früheren Zellen müssen in späteren verfügbar sein, wie
im echten Jupyter-Kernel), keine Fehler. `npm test` (60 Tests, volle Suite inkl. Notebook-Checks
über alle Wochen/Varianten) grün.

### 3.29 Curriculum-Lücken 12-Wochen-Kurs, Teil 6: List-Comprehension-Glossareintrag (Branch `woche8-list-comprehension-glossar`)

Ursprünglicher Fund war nur Woche 8 Abenteuer (`[h for h in helden if h['level'] > 14]`
unangekündigt im Lektion-Code). Ein `grep` über alle 444 Notebooks nach dem Muster
`\[\w+ for \w+ in ` zeigte: das Muster kommt in **Lektion**-Dateien nur in Woche 6 Pferde+Sci-Fi
und Woche 8 allen 3 Varianten vor (Woche 6 Abenteuer und Woche 8 selbst nutzen an keiner anderen
Stelle unangekündigt eine List Comprehension). Neuer Begriff "List Comprehension" ans Ende der
Begriffstabelle in allen 10 betroffenen Glossaren (5 Wochen-Varianten-Kombinationen × DE/EN)
ergänzt: `[x for x in liste if x > 5]` / `[x for x in list_ if x > 5]`.

**Bewusst nicht angefasst:** dieselbe grep-Suche fand List Comprehensions auch in vielen
`6_loesungen`-Dateien über mehrere Wochen (6, 8, 9, 12) — Lösungsdateien sind kein primäres
Lehrmittel wie die Lektion (sie zeigen eine mögliche Lösung, keine schrittweise Einführung neuer
Konzepte), dürfen also fortgeschrittenere Syntax enthalten, ohne dass das ein Fehler ist.

**Getestet:** `npm run test:checks` (49 Tests grün, reine Glossar-Ergänzung ohne
Verhaltensänderung) + alle 10 geänderten Dateien per `json.loads()` validiert.

### 3.30 Curriculum-Lücken 12-Wochen-Kurs, Teil 7: math-Modul aufgewertet (Branch `woche7-math-aufwerten`)

Wieder ein Fund, der beim ursprünglichen Audit nur an der Abenteuer-Variante gemessen wurde: dort
war `math` ein "Exkurs (Bonus)" mit dem Hinweis "nicht Teil der Prüfungen dieser Woche", im
Widerspruch zu `woche7.md`s Lernziel "Das math-Modul für komplexe Berechnungen nutzen". Beim
Nachsehen zeigte sich: **Pferde und Sci-Fi hatten `math` nie als Bonus** — beide behandeln es
bereits als vollwertigen zweiten Abschnitt ("Werkzeug-Sammlung 2"/"Modul-Sammlung 2") mit 3
ausführlichen Beispielen (Konstanten + Kreisberechnung, Grundwerkzeuge wie sqrt/pow/ceil/floor,
fortgeschrittene Werkzeuge wie Trigonometrie/Logarithmen/Fakultät/ggT/kgV). Nur Abenteuer hatte
eine einzige, stark verkürzte Bonus-Zelle mit nur `math.pi` und `math.sqrt()`.

**Umsetzung:** Abenteuer-Lektion (DE+EN) auf denselben Umfang wie Pferde/Sci-Fi gebracht — den
"Exkurs (Bonus)"-Abschnitt durch "Kapitel 5: Das math-Modul – Die Rechenkammer" ersetzt (Story-Titel
an Abenteuers Kapitel-Nummerierung angepasst, mathematischer Inhalt identisch zu Pferde/Sci-Fi
übernommen, da rein technisch und nicht variantenspezifisch), Intro-Mission-Bullet ergänzt, Glossar
um die 4 math-Begriffe ergänzt, die Pferde/Sci-Fi schon hatten (`math.sqrt()`, `math.floor()`,
`math.ceil()`, `math.pi`). Pferde/Sci-Fi (DE+EN) unverändert gelassen — waren bereits korrekt.

**Getestet:** `npm run test:checks` (49 Tests grün) + alle 4 geänderten Dateien per `json.loads()`
validiert + Abenteuer-Lektion komplett mit `python3` durchlaufen (gemeinsamer Namespace, `time.sleep`
für den Testlauf übersprungen) — keine Fehler.

### 3.31 Curriculum-Lücken 12-Wochen-Kurs, Teil 8: Woche-11-Lernziele realistisch gekürzt (Branch `woche11-lernziele-anpassen`)

"Design Patterns anwenden" und "Komposition vs. Vererbung verstehen" waren Lernziele in
`woche11.md`, die die (bewusst kurz gehaltene) Lektion nie abdeckt — zu fortgeschritten für den
Rahmen einer Wochenlektion. Nutzer-Entscheidung: streichen statt Content nachliefern.

**Umfang bei genauerem Hinsehen größer als gedacht:** Das Versprechen steckte nicht nur in
`woche11.md`, sondern auch in den Mission-Bullet-Listen aller 6 Lektion-Intros ("Design Patterns
für meisterhafte Architektur"/"...professionelle Zuchtprogramme"/"...skalierbare Architektur", je
DE+EN) sowie in der Selbstcheck-Liste der Missionen-Notebooks von Pferde und Sci-Fi (× DE/EN,
"☐ Design Patterns erkennen und nutzen", "☐ Komposition vs Vererbung unterscheiden") — Abenteuers
Missionen-Notebook hatte diese Checkliste nie. `woche11.md` (DE+EN) Herausforderungs-Absatz von
"Mit Vererbung, Polymorphismus und Patterns..." auf "...und Magic Methods..." angepasst (das sind
die drei Dinge, die die Lektion tatsächlich liefert).

**Getestet:** `npm run test:checks` (49 Tests grün, reine Content-/Lernziel-Korrektur ohne
Verhaltensänderung) + grep über alle 10 geänderten Dateien bestätigt: 0 verbleibende Erwähnungen
von "Design Pattern"/"Komposition"/"composition".

### 3.32 Turtle-Grafik lief nie im Browser — eigener Pyodide-Shim (Branch `turtle-pyodide-shim`)

**Unabhängig vom Curriculum-Lücken-Plan entdeckt**, beim Vorbereiten von `woche12-interaktivitaet`
(Branch 9 des Plans): Bevor ein `onscreenclick`/`onkey`-Beispiel sinnvoll ergänzt werden konnte,
wurde per Playwright geprüft, ob Turtle-Code überhaupt im echten Browser läuft. Ergebnis: **nein** —
`import turtle` schlägt mit `ModuleNotFoundError` fehl, weil Pyodide (hier Version 0.24.1, siehe
`usePyodide.js`) `turtle` aus der Standardbibliothek entfernt hat (basiert auf tkinter, das im
Browser keinen Anzeige-Server hat — offizielle Pyodide-Einschränkung, kein Konfigurationsfehler
dieser Seite). Verifiziert mit einem bereits produktiven, unveränderten Beispiel (nicht nur neuem
Code) — identischer Fehler. **Das bedeutet: die komplette Woche 12 (Turtle Graphics) war für alle
Nutzer:innen die ganze Zeit über nicht lauffähig**, unentdeckt, weil kein bisheriger Test je
echten Turtle-Code im Browser ausgeführt hat (`tests/storytelling-content.spec.js` & Co. prüfen nur
den Text-Inhalt der Notebooks, nie die tatsächliche Code-Ausführung).

**Recherche zu Alternativen** (siehe Konversation, nicht im Repo): `basthon-turtle` (PyPI) und das
archivierte `RaspberryPiFoundation/turtle` wurden geprüft. Beide ungeeignet: Ersteres braucht laut
eigener Doku einen Web Worker für die Pyodide-Integration — inkompatibel mit der bewussten
Architektur-Entscheidung aus 3.5 (kein Web Worker, weil `input()` synchron über `window.prompt()`
laufen muss). Letzteres ist unmaintained (archiviert) und unterstützt explizit keine
Klick-/Tasten-Interaktion. `pygame-ce` wurde ebenfalls geprüft (funktioniert grundsätzlich in
Pyodide ≥0.23), scheidet aber aus: andere API (kein turtle-Ersatz, Content-Rewrite nötig) und
braucht eine async Game-Loop-Architektur, die mit dem bestehenden synchronen
Einmal-Ausführung-pro-Zelle-Modell (inkl. 5s-Loop-Guard aus 3.5) kollidiert — eher Fundament für
den geplanten `kurs-python-spiele` als Fix für Woche 12.

**Umsetzung:** Eigener, selbst geschriebener Python-Shim in `usePyodide.js` (`_install_turtle_shim`,
läuft einmalig beim Kernel-Start), der `sys.modules['turtle']` mit `Turtle`/`Screen`-Klassen belegt,
die direkt auf ein `<canvas>` zeichnen (über Pyodides `js`-Bridge, `from js import document`). Die
Methoden-Oberfläche wurde per grep über alle 444 Notebooks aus `content/python-12-wochen-grundkurs*`
ermittelt (`forward`, `left`/`right`, `penup`/`pendown`, `goto`, `color`/`fillcolor`, `begin_fill`/
`end_fill`, `circle`, `dot`, `write`, `speed`, `shape`, `hideturtle`, `Screen.bgcolor`/`title`/
`setup`/`tracer`/`update`, `onscreenclick`/`onkey`/`listen`) — kein Web Worker, kein externes Paket,
läuft synchron im bestehenden Ausführungsmodell. `JupyterNotebook.vue` bekam einen neuen
`<div class="turtle-canvas-container">` pro Code-Zelle (ID `turtle-{index}`); `runPython()` in
`usePyodide.js` setzt vor der Ausführung `window.__turtleContainerId`, das der Shim ausliest, um
das `<canvas>` im richtigen Zellen-Container zu erzeugen.

**Nebenbei gefundener echter Content-Bug:** Pferde Woche-12-Lösungen (Mission 1, "Dressur-Bahn")
hatte eine tote Schleife `for pos, buchstabe in [(-200, -100, "C"), ...]: pass  # vereinfacht`, die
3er-Tupel in 2 Variablen entpacken wollte — hätte in echtem CPython genauso mit `ValueError: too
many values to unpack` abgebrochen. Offensichtlich ein verworfener erster Entwurf, der nie gelöscht
wurde (die korrekte Version steht direkt darunter). Nur im DE-Notebook, EN war bereits sauber.
Entfernt.

**Bewusst nicht gebaut** (Scope-Grenze für "einfachste lauffähige Lösung"): kein echtes
Klick-/Tasten-Event-Wiring für `onscreenclick`/`onkey` (aktuell nur sichere No-Ops — kein
existierendes Notebook nutzt diese Funktionen wirklich, nur Bonus-Erwähnungen in Missions-Texten;
`woche12-interaktivitaet` aus dem Curriculum-Plan ist damit wieder entblockt und kann das Event-
Wiring bei Bedarf ergänzen); keine Animation/`speed()`-Verzögerung (alles zeichnet sofort); kein
sichtbarer Turtle-Cursor (`shape()` ist kosmetischer No-Op); `tracer(0)`/`screen.update()` sind
No-Ops. Bekannte Konsequenz: die eine Lösungsdatei mit animiertem Pferderennen (Stift oben, nur
Positions-Updates ohne Linien) zeigt dadurch keine sichtbare Bewegung mehr — Ziellinie und
Gewinner-Ausgabe funktionieren trotzdem, kein Kernproblem.

**Getestet:** Alle 3 Varianten × alle 5 Tabs (Lektion/Missionen/Debug/Boss-Quest/Lösungen) per
Playwright durchgeklickt — jede Zelle ausgeführt, keine unerwarteten Fehler (die eine erwartete
Fehlermeldung war der absichtliche Debug-Bug `import Turtle` mit großem T, korrekt reproduziert).
Neue dauerhafte Tests in `tests/site.spec.js` ("Turtle-Grafik im Browser (Pyodide-Shim)"): prüfen
echte Pixel auf dem `<canvas>` (nicht nur "kein Fehler geworfen") — einmal für Linien-Zeichnen,
einmal für `begin_fill()`/`end_fill()`. `npm run test:checks` (51 Tests, 2 neu) + `npm test` (60
Tests) grün.

### 3.33 12-Wochen-Kurs: Umstellung auf Zellen-Format (Branch `12-wochen-kurs-zellen-format`)

**Motivation:** rohes `.ipynb`-JSON ist fragil bei Bulk-Edits (mehrere Serialisierungsstile im
Repo, siehe 3.12/3.16) und erzwingt Jupyter/Pyodide zum Ausführen — kein einfacher Offline-Weg für
Lernende ohne Jupyter-Setup. Erst an der Abenteuer-Variante als Parallel-Experiment erprobt (eigene
Route `/experiment/...`, nicht verlinkt), dann auf Nutzer-Wunsch auf den **kompletten, echten**
Kurs ausgeweitet: alle 3 Varianten × 12 Wochen × 6 Typen × DE/EN = 432 Notebooks.

**Format:** jedes Notebook ist jetzt ein Ordner mit einer `.py`-Datei pro Zelle
(`NN_markdown.py`/`NN_code.py`) statt einer `.ipynb`-Datei — Markdown-Zellen sind ein
alleinstehendes String-Literal (gültiges, wirkungsloses Python), Code-Zellen unverändert. Aus
diesen Zell-Dateien werden bei jedem `npm run dev`/`npm run build` zwei **gitignored** Artefakte
neu erzeugt (`scripts/build_cell_notebooks.py`, Teil der `dev`/`prebuild`-Kette):
`_generated/<name>.ipynb.json` (notebook-förmige JSON fürs Browser-Rendering) und
`_bundle/<name>.py` (alle Zellen zusammengefügt, läuft direkt mit `python3 datei.py` — kein
Jupyter/Pyodide nötig, ersetzt den alten `.ipynb`-Download-Button).

**Migration:** `scripts/migrate_notebooks_to_cells.py` (einmalig, idempotent) hat alle 432
Notebooks in-place ersetzt — pro Datei sofort Byte-für-Byte-Round-Trip verifiziert, danach
zusätzlich unabhängig gegen `git show HEAD:<pfad>` gegengeprüft (0 Abweichungen), erst dann die
alte `.ipynb` gelöscht. **Wichtige Lektion beim Bauen des Skripts:** kein künstliches
Zeilenumbruch-Padding um den Markdown-Text und kein `.rstrip("\n")` bei der Rückwandlung — beides
verändert den extrahierten Wert unmerklich (Markdown ignoriert überzählige Newlines beim Rendern,
daher fällt so ein Fehler beim bloßen Anschauen nicht auf) und hätte den strengen Byte-Vergleich
unbemerkt durchrutschen lassen, wäre die Prüfung nicht bewusst streng gehalten worden.

**Nebenbei gefundener echter Content-Bug** (unabhängig von der Migration, via unerwarteten
`ast.parse()`-Fehlern beim Validitäts-Check aufgefallen): Pferde Woche 11 Lektion hatte 6 Methoden
in 3 Klassen-Beispielen ohne `def`/`self` (`fressen():` statt `def fressen(self):` etc.) — exakt
dasselbe historische Bug-Muster wie bei Sci-Fi Woche 11 (bereits früher gefixt, siehe Pferde-/
Sci-Fi-Analyse in `todo.md`), bei Pferde aber nie behoben. Gefixt, mit gemeinsamem Namespace
ausgeführt verifiziert.

**Browser-Rendering:** `JupyterNotebook.vue` nutzt jetzt CodeMirror 6 statt einer `<textarea>`
(neue `CodeCell.vue`) — Tab-Autocomplete im VS-Code-Stil (offener Vorschlag wird mit Tab
übernommen, sonst rückt Tab ein: `Prec.highest`-Keymap mit `acceptCompletion` vor
`indentWithTab`), 4-Leerzeichen-Einrückung, Mindesthöhe 3 Zeilen pro Zelle (auch leer — eine
Missionen-Platzhalterzelle wie `# Deine Lösung hier:` muss als Coding-Bereich erkennbar bleiben).
Alle bestehenden Produktions-Features aus der alten `JupyterNotebook.vue` blieben erhalten:
localStorage-Persistenz von Zell-Edits (Key = `notebookPath`), `PROGRESS_APPLIED_EVENT`-Sync,
Turtle-Canvas-Container. **Bekannte, akzeptierte Nebenwirkung:** weil `notebookPath` sich durch
die neue URL ändert, verlieren Nutzer:innen mit bereits lokal gespeichertem, unsynctem Zell-Code
diesen einen Zwischenstand beim ersten Besuch nach dem Deploy — betrifft nur unfertigen Code in
einzelnen Zellen, nicht Zertifikate/Fortschritt (laufen unabhängig über `useWeekChecks.js`).

**Design:** von Ad-hoc-Farben (Amber/Blau/Grün aus dem ersten Prototyp) auf die echte Seiten-CI
umgestellt — `--primary-purple`/`--accent-orange`/`--accent-yellow` aus `src/style.css` (bereits
vorher an anderer Stelle im Code etabliert, z.B. `LessonView.vue`s `.btn-kernel`/`.btn-check`).
Wochen-Header in `WeekSection.vue` redesignt: kurzer Titel "Woche N – Thema" (Thema = Teil nach dem
ersten `:` im vollen `week.title`) statt des vollen technischen Titels, Kurzbeschreibung nur im
eingeklappten Zustand (vermeidet Redundanz mit dem bestehenden `week-summary`-Block, der beim
Aufklappen ohnehin erscheint), dezente Lila-Akzentleiste (`border-left`) statt Vollflächen-Invert
beim Aufklappen — eine erste Version mit vollflächigem Lila-Fill wurde explizit als "zu massiv/
überladen" verworfen.

**`useWeeklyContent.js`:** Notebook-Eintrag pro Variante/Typ ist jetzt `{renderUrl, downloadUrl}`
statt einer bloßen URL (zwei getrennte `import.meta.glob`-Quellen: `_generated/*.ipynb.json` fürs
Rendering, `_bundle/*.py` fürs Herunterladen) — `WeekSection.vue` reicht beide getrennt an
`JupyterNotebook.vue` durch (`notebook-path` vs. `notebook-url`).

**Tests:** CodeMirror ist keine `<textarea>` — `.fill()`/`.inputValue()` funktionieren nicht mehr.
`tests/site.spec.js` + `tests/storytelling-content.spec.js` auf neue lokale Helper umgestellt
(`setCodeMirrorContent`/`getCodeCellText`: Klick + Select-All + `page.keyboard.insertText()` statt
`type()` — sonst verdoppelt CodeMirrors Auto-Indent die Einrückung bei literalen `\n` in
mehrzeiligem Test-Code). `tests/zertifikate.spec.js`s `.code-editor`-Treffer gehören zu
`CodeChallenge.vue` (Wochen-Check, eigene Komponente) und waren nicht betroffen.

**Bewusst NICHT Teil dieser Umstellung:** interaktiver Einführungskurs
(`python-grundlagen-interaktiv*`), Cäsar-Chiffre, Wochen-Checks (`CodeChallenge.vue`) — eigene,
unabhängige Editor-Instanzen. Cheat-Sheets (`wissens_cheat_sheet.ipynb`, `gesamtglossar.ipynb`)
bleiben ebenfalls echte `.ipynb`-Dateien (eigene Pipeline, `md_to_cheatsheet_notebook.py`) — beim
Umbau von `scripts/pack_notebooks.py` (jetzt: `_bundle/*.py` statt `*.ipynb`) mussten sie explizit
wieder mit ins ZIP aufgenommen werden, sonst wären sie aus dem Download verschwunden.

**Nachtrag (Kursbeschreibung bereinigt):** beim Durchklicken der Kursseite aufgefallen —
`content/python-12-wochen-grundkurs(-en)/beschreibung.md`s Abschnitt "Einstufung – wo soll ich
starten?" stand fast wortgleich direkt über der separaten `.placement-banner`-Komponente
(`CourseDetail.vue`, Locale-Keys `course.placement.banner`/`.link`), die für `isWeeklyCourse` UND
`isInteractiveCourse` automatisch unter der Beschreibung erscheint — zwei Boxen mit derselben
Aussage hintereinander. Der interaktive Kurs hat diesen Abschnitt in seiner eigenen
`beschreibung.md` nie dupliziert (verlässt sich schon immer nur auf den Banner) — Vorbild für den
Fix: Abschnitt beim 12-Wochen-Kurs entfernt (Banner bleibt einzige Quelle), "Für wen ist der Kurs?"
direkt nach die Zielbeschreibung vorgezogen (Ziel → Zielgruppe → Aufbau als Lesereihenfolge).

### 3.34 Wochen-Check: Variablen-Validierung gegen Hardcoding (Branch `wochencheck-variablen-validierung`)

Nutzer hat beim Ausprobieren selbst herausgefunden, dass sich Coding-Aufgaben, die das Anlegen
bestimmter Variablen verlangen (z.B. "Erstelle eine Variable name..."), durch bloßes Hart-Codieren
der erwarteten Textausgabe umgehen ließen — `useTaskValidation.js`s `validateOutput()` prüfte
ausschließlich `stdout` (`output_contains`/`output_equals`), nie den tatsächlichen Programmzustand.

**Fix:** `validation` kann jetzt optional ein `variables`-Feld haben (`{name: erwarteterWert}`).
`CodeChallenge.vue` liest nach der Ausführung die echten Werte aus `pyodide.globals` (Pyodide fuhrt
Code via `exec(code, globals())` aus, siehe `_run_cell_with_guard` in `usePyodide.js` — der geteilte
Python-Namespace ist deshalb direkt über `pyodide.globals.get(name)` abfragbar) und vergleicht sie
zusätzlich zur Ausgabe. **Wichtige Falle dabei:** die betroffenen Variablennamen müssen vor jedem
Lauf aus dem Namespace gelöscht werden (sonst besteht ein zweiter Versuch fälschlich, weil der alte
Wert aus einem früheren Lauf noch da ist — der Namespace ist über die ganze Seite geteilt) — und
`pyodide.globals.delete(name)` wirft dabei eine Exception, wenn der Name noch nie gesetzt wurde
(der Normalfall beim ersten Versuch), muss also mit try/catch abgefangen werden, sonst bricht
`checkCode()` vorzeitig ab und es erscheint gar kein Feedback (genau daran ist der erste
Implementierungsversuch im eigenen Test gescheitert).

**Nachtrag — alle 24 Coding-Aufgaben durchgesehen:** auf Nachfrage geprüft, ob dieselbe Lücke noch
woanders steckt. Fündig: Woche 3 ("zahl1"/"zahl2", scalar — gleicher Mechanismus wie Nova/alter) und
Woche 8 (beide Aufgaben, "person"/"schueler" — verlangen ein **Dictionary**, kein Skalar). Dafür
`valuesMatch()` in `useTaskValidation.js` um rekursiven Objekt-Vergleich erweitert (erwarteter Wert
als `{"name": "Alex"}` statt Skalar), `CodeChallenge.vue` wandelt den Pyodide-Rückgabewert dafür per
`.toJs({dict_converter: Object.fromEntries})` in ein normales JS-Objekt um (ein dict-PyProxy laesst
sich nicht direkt mit `===` vergleichen). Insgesamt 5 von 24 Aufgaben betroffen — der Rest verlangt
keine explizit benannte Variable in der Aufgabenstellung (nur "berechne X" / "nutze eine Schleife" /
"importiere Y"), dafür bräuchte es einen anderen Mechanismus (Funktions-Re-Test mit neuem Wert für
die beiden Funktionsaufgaben in Woche 5, Modul-Import-Check für Woche 7/12 — noch nicht umgesetzt,
siehe Plan) — bei den restlichen (Woche 2/4/6/9/10/11/12#2) wäre nur AST-Analyse des eingereichten
Codes möglich, das ist fragiler (lehnt valide Alternativlösungen ab) und bewusst zurückgestellt.

**Getestet:** neuer Test in `tests/zertifikate.spec.js` (hart kodierte Ausgabe ohne Variablen schlägt
fehl, dieselbe Aufgabe mit echten Variablen besteht) + Analogtest fürs Dictionary bei Woche 8 +
volle `npm run test:checks`-Suite grün (53 Tests). Woche 3 manuell per Playwright verifiziert.

**Nachtrag 2 — Kategorie B (Funktionsaufgaben, geplant + umgesetzt):** Woche 5 (`verdopple`,
`addiere`) ließ sich mit `variables` nicht sauber fixen, da nur der eine in der Aufgabenstellung
vorgerechnete Aufruf geprüft würde. Neues optionales `functionCalls`-Feld
(`[{name, args, expected}]`): ruft die Funktion nach der Ausführung mit einem **nie genannten**
Eingabewert erneut auf. Deckt nicht nur "keine Funktion geschrieben" auf, sondern auch den
subtileren Fall "Funktion stimmt nur zufällig fürs eine Beispiel" (`zahl + 6` statt `zahl * 2`
ergibt für `verdopple(6)` beide 12, aber nur `*2` stimmt auch für den Re-Test `verdopple(10) == 20`
— genau dieser Fall ist jetzt Teil der Tests). **Wichtige Falle dabei:** der AST-Loop-Guard aus
`usePyodide.js` injiziert Deadline-Checks in jede Schleife der eingereichten Zelle, auch innerhalb
von Funktionskörpern — die Deadline-Variable (`__cell_deadline__`) wird nach dem ursprünglichen Lauf
wieder gelöscht, ein späterer Aufruf einer Funktion mit eigener Schleife würde sonst mit `NameError`
abstürzen. Fix: vor jedem Re-Aufruf defensiv `__cell_deadline__` neu setzen (auch wenn `verdopple`/
`addiere` selbst keine Schleife haben — Absicherung für künftige, ähnlich gebaute Aufgaben). Kleines
Refactoring nebenbei: die `toJs()`-Konvertierung (PyProxy → einfaches JS-Objekt, für `variables` UND
`functionCalls` gebraucht) in eine gemeinsame `toPlainJs()`-Hilfsfunktion in `CodeChallenge.vue`
gezogen, statt sie zweimal zu schreiben.

Plan-Datei für diesen Teil: `~/.claude/plans/lexical-growing-comet.md`.

### 3.35 Experiment: Geführte Wochen-Tour (Branch `experiment-wochen-tour`)

Nutzerwunsch: eine alternative Führung durch den 12-Wochen-Kurs ausprobieren, ohne den bestehenden
Kurs (`/kurs/python-12-wochen-grundkurs`) anzufassen — als unverlinkte Experimentseite (Vorbild:
die früheren `/experiment/...`-Prototypen aus 3.33). Über drei Feedback-Runden gewachsen — hier der
finale Stand, nicht die Zwischenschritte (Tab-Leiste → Kacheln+Kullern-Leiste → Verzweigung +
Zertifikate).

**Route `/experiment/wochen-tour`** (`src/views/experiment/WeekTourView.vue`, nur per direkter URL
erreichbar, kein Nav-Link): vier "Seiten" als Wizard (`phase` ref: `week`|`variant`|`certificates`|
`tour`), Klick auf eine Kachel navigiert sofort weiter.
- **Woche wählen:** 12 große Kacheln, dünn gestrichelt zu einem Pfad verbunden ("Inseln", die man
  bereist). **Erster Versuch (gerade `<polyline>` in Lese-Reihenfolge) sah beim Zeilenumbruch
  kaputt aus** — Nutzer-Feedback: die Linie sprang als lange Diagonale quer durchs Raster (von
  Wochen-Kachel N am Zeilenende zu N+1 am nächsten Zeilenanfang, weit auseinander). Fix: echte
  Schlangen-Anordnung (jede zweite Zeile läuft per explizitem `grid-column`/`grid-row` visuell
  rückwärts, Spaltenzahl live aus `getComputedStyle().gridTemplateColumns` gelesen statt hart
  codiert — wichtig, weil die Spaltenzahl sich je nach Einbettung ändert, siehe unten) plus eine
  Catmull-Rom-Kurve (als kubische Bezier-Segmente ausgegeben) statt gerader Liniensegmente. Jede
  Kachel zeigt ein technisches Themen-Icon (variantenlos, `WEEK_ICONS`-Map nach INHALTE.md
  Abschnitt 3) und ein 🎓-Abzeichen sobald das Zertifikat der Woche verdient ist
  (`useZertifikate().isCertificateEarned`). Zähler + Link zur Zertifikate-Seite.
- **Thema wählen:** bis zu 3 Kacheln (Abenteuer/Pferde/Sci-Fi) — bewusst NICHT `VariantSelector.vue`
  wiederverwendet (das ist für kleine Inline-Buttons gebaut, hier reicht die gleiche Datenbasis
  `hasXVariant`, nur eigenes großes Kachel-Markup).
- **Meine Zertifikate:** wiederverwendet `FortschrittWidget.vue` unverändert (gleiche Datenform
  `weeks`) statt eines eigenen Rasters — visuell bewusst anders (Gold-Gradient) als der Rest der
  Tour, da es 1:1 dieselbe Komponente wie im echten Kurs ist. Neuer additiver Prop `startExpanded`
  (Default `false`, bestehende Nutzung in `CourseDetail.vue` unberührt) sorgt dafür, dass die Seite
  direkt aufgeklappt startet.
- **Tour:** `WeekTourStepper.vue`, siehe unten.

**Fortschritts-Leiste statt Tab-Leiste** (`WeekTourStepper.vue`): Kullern (Kreise) verbunden durch
Linien — Lektion → Debug → Missionen → Extra-Herausforderung → Check (nur vorhandene Schritte,
`4_check` nur wenn `hasWeekCheck()`). Ein Breadcrumb oben ("Woche N: Thema › Variante") erlaubt
jederzeit den Sprung zurück zur Wochen-/Themenwahl (`change-week`/`change-variant`-Events an
`WeekTourView`). Alle Kullern bleiben frei anklickbar (kein Sperren).

**Verzweigung nach den Missionen:** kein automatisches Weiterschalten mehr — ein "Weiter" öffnet
eine Wahl-Kachel-Seite zwischen "🔥 Extra-Herausforderung" (der bisherige Boss-Quest-Schritt,
`5_boss`, **nur hier umbenannt** — der echte Kurs behält "Boss-Quest") und "✅ Check". Beide führen
letztlich zum Check; die Extra-Herausforderung bleibt optional. **Begriffsfindung mit dem Nutzer:**
mehrere Runden Vorschläge (Vertiefung, Herausforderung, Königsdisziplin, Bonusrunde, Feuerprobe, Kür
…) — am Ende eine Kombination aus zweien: "Extra-Herausforderung". Technisch wichtige Umstellung
dafür: die alte `furthestStepIndex`-Schwelle (Fortschritt = "alles bis Index N ist erledigt") ging
von striktem linearem Ablauf aus und wäre bei einer übersprungenen Extra-Herausforderung falsch
gewesen (Check erreichen hätte Boss fälschlich mit ✓ markiert). Ersetzt durch ein `visitedKeys`-
Objekt (welche Schritte *tatsächlich angesehen* wurden) — ein Schritt zeigt nur dann ✓, wenn er
wirklich geöffnet wurde, nicht weil sein Index kleiner als der aktuell erreichte ist. Verifiziert:
"Check" direkt wählen lässt "Extra-Herausforderung" unbesucht (kein ✓).

**Zertifikat-Reveal nach bestandenem Check:** `isWeekCheckPassed(weekNumber)` aus `useWeekChecks.js`
ist reaktiv auf denselben modul-weiten `progress`-Ref, den `WeekCheckPanel.vue`/`CodeChallenge.vue`
beim Bestehen mutieren — kein Extra-Event nötig, ein `computed()` reicht. Reveal zeigt 🎓, Name-Feld
(gleicher `localStorage`-Key `ue-hacker-certificate-name` wie `FortschrittWidget.vue`, damit der
Name geteilt bleibt) und PDF-Download (`downloadCertificatePdf` aus `useCertificatePdf.js`,
login-gated wie im echten Kurs) — komplett wiederverwendete Logik, keine neue PDF-Erzeugung.
Danach eine Wahl "Zur Übersicht" / "Nächste Woche": Letzteres fällt auf die erste verfügbare
Variante zurück, falls die aktuelle Variante in der nächsten Woche fehlt, und wird bei Woche 12
(keine nächste Woche) gar nicht erst angezeigt (`hasNextWeek`-Prop von `WeekTourView` berechnet,
Navigations-Logik inkl. Varianten-Fallback lebt dort, nicht im Stepper).

**Kleines Seitenmenü** (`WeekTourSideMenu.vue`, ein-/ausklappbar über einen neuen Toggle-Button):
Tour-Schritte zum Springen (✓ nach `visitedKeys`, nicht mehr nach Index-Schwelle) + Unterabschnitte
des gerade offenen Schritts (z.B. "Bug #1/#2/#3", "Mission 1/2/3", aus den `##`/`###`-Überschriften
der Notebook-Zellen extrahiert — jede Markdown-Zelle im Zellen-Format, siehe 3.33, beginnt mit genau
einer Überschrift) + Glossar/Lösungen als eigener, nicht gegateter "Nachschlagewerke"-Block. Neue
kleine Composable `useNotebookHeadings.js` lädt dafür dieselbe `renderUrl`-JSON, die
`JupyterNotebook.vue` ohnehin schon rendert (zweiter, unkritischer Fetch derselben kleinen
statischen Datei).

**Eine einzige additive Änderung an einer geteilten Komponente:** `JupyterNotebook.vue`s
`.cell`-Wrapper-Div bekommt zusätzlich `:id="`cell-${index}`"` (vorher keine ID) — ermöglicht dem
Seitenmenü, per `scrollIntoView()` zu einer Zelle zu springen, ohne die 377-Zeilen-Notebook-
Komponente (Kernel-State, Zellen-Persistenz, Turtle-Canvas) zu duplizieren. Reine DOM-ID ohne
Auswirkung auf Aussehen/Verhalten des einzigen bestehenden Verwenders (`WeekSection.vue`).

**Bewusste Vereinfachungen:** keine `localStorage`-Persistenz von Woche/Variante/Schritt (Reload
startet auf der Wochen-Übersicht neu — der Zellen-Bearbeitungsstand einzelner Notebooks bleibt
davon unberührt, der ist bereits unabhängig in `JupyterNotebook.vue` über `notebookPath` geregelt).

**Getestet:** `tests/experiment-wochen-tour.spec.js` (10 Tests: Kachel-Flow, Breadcrumb-Navigation,
Verzweigung Extra-Herausforderung/Check inkl. "bleibt unbesucht bei Direktwahl", **echtes** Bestehen
von Woche 1s Quiz + beiden Coding-Aufgaben inkl. Zertifikat-Reveal und Sprung zur nächsten Woche,
Zertifikat-Abzeichen in Übersicht + Zertifikate-Seite, "Nächste Woche" fehlt bei Woche 12,
Seitenmenü ein-/ausklappen + Unterabschnitt-Sprung + Glossar-Rückkehr) + volle `test:checks`-Suite
(55 bestehende Tests weiterhin grün, deckt u.a. den `FortschrittWidget.vue`-Prop und die additive
Notebook-ID ab) + manuell per Playwright-Skripten End-to-End durchgespielt (nicht nur Screenshots).

Plan-Datei (erste Runde): `~/.claude/plans/twinkly-strolling-lovelace.md`. Die Verzweigung/
Zertifikate/Übersicht-Erweiterungen (zweite Feedback-Runde) liefen ohne eigene Plan-Datei direkt
im Gespräch (kleinere, klar umrissene Ergänzungen auf bestehender Struktur).

### 3.36 Wochen-Tour wird die echte Kursseite (Branch `experiment-wochen-tour`, Fortsetzung von 3.35)

Nutzer-Feedback nach dem Ausprobieren: "sieht super aus, bitte übernehmen und als neuen 12-Wochen-
Kurs verwenden" — die Experimentseite aus 3.35 sollte die **echte, produktive** Kursseite unter
`/kurs/python-12-wochen-grundkurs` ersetzen, nicht mehr nur daneben existieren. Deutlich größer als
der ursprüngliche Aufbau: `WeekSection.vue` (+ `MissionenPanel.vue`/`VariantSelector.vue`/
`CheatSheetList.vue`) war die einzige Quelle für Dinge, die die Tour noch nicht konnte, und mehrere
Stellen im Code zeigten fest auf die alte Seitenstruktur (Deep-Links, 42 von 59 Tests in 6 Dateien).
Vorgehen: erst ein vollständiger Plan zur Freigabe (wie bei 3.35), inkl. eines Explore-Agent-Laufs,
der den genauen Testmigrations-Umfang ermittelt hat, bevor der eigentliche Umbau begann.

**Datei-Umzug** (von "Experiment" zu echtem Code, `git mv` für die Historie): `WeekTourView.vue`
(`src/views/experiment/`) → `WeekTour.vue` (`src/components/` — wird jetzt **eingebettet**, ist kein
Router-Ziel mehr), `WeekTourStepper.vue`/`WeekTourSideMenu.vue`/`useNotebookHeadings.js` aus ihren
`experiment/`-Unterordnern raus in die normalen `components/`/`composables/`-Ordner. Route
`/experiment/wochen-tour` aus `src/router/index.js` entfernt.

**`CourseDetail.vue`:** der `isWeeklyCourse`-Zweig rendert jetzt `<WeekTour />` statt
`<WeekSection v-for>` + `<FortschrittWidget>` — `WeekTour.vue` lädt seine `weeks` weiterhin selbst
und verwaltet Query-Params über `useRoute`/`useRouter` selbst, `CourseDetail.vue` braucht dafür
keine eigene `weeks`-Ref/Deep-Link-Logik mehr (der alte `applyWeekDeepLink()` mit
`document.getElementById('woche-N')`-Scroll-Retry ist komplett weg). Kursbeschreibung,
Einstufungs-Banner, Notebook-Pack-Download und Cäsar-Chiffre-Banner bleiben als Chrome vor der Tour
stehen — funktionieren unverändert, weil sie nicht von `weeks`/Wochen-Deep-Links abhängen. Die
"Wie ist der Kurs aufgebaut"-Erklärbox (`course-structure-tabs`) wurde **inhaltlich neu
geschrieben**: 7 Kacheln (Woche wählen → Thema wählen → Lektion → Debug → Missionen →
Extra-Herausforderung/Check → Zertifikat) statt der alten "7 parallele Tabs"-Erklärung, plus ein
Satz, dass Glossar/Lösungen/Cheat-Sheets jederzeit übers Seitenmenü erreichbar sind. Neue
`course.structure.step.*`-Locale-Keys, die bestehenden `tab.*`-Keys (ohne `.desc`-Suffix) bleiben
unverändert bestehen, weil `WeekTourStepper.vue` sie weiterhin für Schritt-Label braucht.

**Cheat-Sheets + Wochen-ZIP in die Tour integriert** (Nutzer-Entscheidung: kein Feature-Verlust
ggü. der alten Seite): `WeekTourStepper.vue`s bestehender "Nachschlagewerke"-Mechanismus
(`referenceItems`) bekam einen dritten Content-Zweig neben Notebook-Referenz und Check-Panel — Cheat-
Sheets haben kein `renderUrl` (sind bereits fertig von `useWeeklyContent.js` gerendertes
Markdown-HTML), landen also nicht in `JupyterNotebook.vue`, sondern in einem neuen
`<div v-html="activeCheatSheet.content">` mit denselben `.cheat-sheet-markdown`-Stilregeln, die
vorher in `CheatSheetList.vue` standen (übernommen, da diese Komponente sonst wegfällt). Der
Wochen-ZIP-Download (`/wochen-zips/woche-N.zip`, unverändert generierte Datei) sitzt jetzt auf der
Themen-Wahl-Seite in `WeekTour.vue`.

**Rückwärtskompatible Deep-Links, ohne die Linkgeneratoren anzufassen:** `PlacementCourse.vue`
(zwei `router-link`-Stellen) und vier Cäsar-Chiffre-Lektionen verlinken mit dem alten
`?week=N&tab=lektion#woche-N`-Schema — **beide bewusst unverändert gelassen**. `WeekTour.vue`s
`applyDeepLink()` übersetzt `tab=` intern über eine `TAB_TO_STEP`-Map (matcht `WeekSection.vue`s
alte Alias-Logik: `lektion`/`lesson`, `debug`, `missionen`/`missions`, `boss`, `check`,
`loesungen`/`solutions`, `glossar`/`glossary`). Da diese alten Links nie `variant` mitgeben, landen
sie korrekt auf der Themen-Wahl-Seite der richtigen Woche statt direkt in der Lektion — nach der
Themenwahl dann ohnehin auf Lektion (Standard-Einstieg), kein Informationsverlust. Das alte
`#woche-N`-Hash-Ziel existiert in der neuen Seite nicht mehr; Browser ignorieren ein nicht
gefundenes Hash-Ziel stillschweigend.

**Tote alte UI entfernt** (verifiziert: einzige Verwender war `CourseDetail.vue`/`WeekSection.vue`
selbst): `WeekSection.vue`, `MissionenPanel.vue`, `VariantSelector.vue`, `CheatSheetList.vue` +
deren exklusive Locale-Keys (`tab.*.desc`-Varianten, alle `mission.*`-Keys,
`week.noNotebook`/`week.downloads`) — vorher jeweils per grep verifiziert, dass nichts anderes sie
noch braucht.

**Test-Migration — die eigentliche Arbeit dieser Runde:** ein Explore-Agent hat vorab alle sechs
potenziell betroffenen Testdateien durchsucht und exakt beziffert: 42 von 59 Tests hingen an der
alten UI, in zwei Mustern — die Mehrheit (`site.spec.js`, `week-checks.spec.js`,
`zertifikate.spec.js`, `auth-ui.spec.js`) nutzte `?week=N&tab=X#woche-N`-Deep-Links + `#woche-N`-
Scoping (mechanisch auf `?week=N&variant=abenteuer&step=Y` portierbar, Scoping komplett entfallen,
da die neue Seite ohnehin nur eine Woche gleichzeitig zeigt); zwei Dateien
(`storytelling-content.spec.js`, `notebooks.spec.js`) nutzten Akkordeon-Klicks
(`.week-header`/`.variant-btn`/`.tab-btn`), die einer direkten URL-Navigation weichen mussten (das
vereinfacht diese Tests sogar — eine Klick-Kette wird ein einzelner `goto()`). Besonderheiten:
- `site.spec.js` "Missionen-Panel lässt sich aufklappen" entfiel ersatzlos (testete exakt das
  entfernte Widget); `zertifikate.spec.js` "Missionen allein reichen nicht" wurde vereinfacht (die
  Panel-Klick-Interaktion fällt weg, der Kern — Missionen lösen kein Zertifikat aus — bleibt).
- `week-checks.spec.js` "Deep-Link öffnet Woche" — `.tab-btn.active` → `.stepper-step.current`.
- Zwei Tests, die auf `.week-jump`/`.recommend a` (von `PlacementCourse.vue` generiert) klicken,
  bekamen eine **korrekt geänderte** Erwartung: sie landen jetzt auf der Themen-Wahl-Seite statt
  direkt in der Lektion (kein Kompromiss, sondern das tatsächlich neue, gewollte Verhalten).
- Die drei PDF-Tests in `auth-ui.spec.js` + der FortschrittWidget-Test in `zertifikate.spec.js`
  wurden sogar **einfacher**: die neue "Meine Zertifikate"-Seite startet dank `startExpanded` schon
  aufgeklappt, zwei Klicks (`.fortschritt-widget-header`/`.fortschritt-weekly-header`) entfallen.
- `notebooks.spec.js` (größte Einzelbaustelle): der alte Struktur-Smoke-Test (7 Tabs) wurde zu 5
  Stepper-Schritten + Nachschlagewerke-Anzahl: die generierten Tests (Wochen 1/6/12 × 3 Varianten)
  navigieren jetzt direkt per URL zu **jedem** Tour-Schritt, klicken zusätzlich durch die
  Missionen-Verzweigung und jedes Nachschlagewerk (Glossar/Lösungen/Cheat-Sheets) und prüfen `.error`
  bleibt überall unsichtbar — deutlich breitere Abdeckung als vorher (reine Tab-Klicks).
- **Eigener blinder Fleck:** `tests/experiment-wochen-tour.spec.js` selbst testete nach dem Umbau
  weiterhin die jetzt nicht mehr existierende `/experiment/wochen-tour`-Route (fiel erst durch eine
  Vue-Router-Warnung in einem völlig anderen Testlauf auf, nicht durch einen eigenen Testfehler — der
  Datei fehlte im Plan ein Eintrag, weil sie beim Schreiben des Plans nicht als "betroffen" auf dem
  Schirm war). Nach `tests/wochen-tour.spec.js` umbenannt (`git mv`), `TOUR_URL`-Konstante auf die
  echte Kurs-URL umgestellt — Inhalt sonst unverändert übernehmbar.
- **Viewport-abhängiger Test gefixt:** der Schlangen-Pfad-Test aus 3.35 nahm eine feste Spaltenzahl
  (5, wie auf der freistehenden Experimentseite) an — durch die Einbettung in `CourseDetail.vue`
  (Seiten-Header/Nav/Kurstext drumherum) passen bei derselben Fensterbreite jetzt nur noch 4 Spalten
  ins Grid. Test liest die tatsächliche Spaltenzahl aus `getComputedStyle().gridTemplateColumns`
  statt sie anzunehmen, prüft dann generisch "letzte Woche der ersten Zeile" gegen "erste Woche der
  zweiten Zeile" — robust gegen jede tatsächlich gerenderte Spaltenzahl.

**Gelernte Regel für künftige Sessions:** bei Doppel-Server-Setups (normaler Dev-Server auf :5174 +
`playwright.auth.config.js`s eigener Testserver mit `VITE_API_PROXY` auf denselben Port,
`reuseExistingServer: true`) gewinnt ein bereits laufender Server ohne den Proxy-Header — führt zu
`Request failed (502)` in allen Auth-UI-Tests, sieht aus wie ein echter Bug, ist aber nur ein
Port-Konflikt. Vor `npm run test:auth` immer prüfen, ob auf :5174 schon ein "nackter" `vite`-Prozess
läuft (`lsof -nP -iTCP:5174 -sTCP:LISTEN`) und diesen beenden.

**Getestet:** `npm run build` (Produktions-Build ohne Fehler), volle `npm test`-Suite (76 Tests)
grün, `npm run test:auth` (13 Tests) grün, `npm run test:checks` (54 Tests) grün. Manuell per
Playwright-Skripten verifiziert: Cheat-Sheet-Referenz + Wochen-ZIP-Download für eine Woche mit zwei
Cheat-Sheets (Woche 12) und eine mit nur einem (Woche 6), alter Einstufungs-Deep-Link landet auf der
richtigen Themen-Wahl-Seite, ein echter Cäsar-Chiffre-Lektionslink führt zur richtigen Woche.
`grep -rn "WeekSection\|MissionenPanel\|VariantSelector\|CheatSheetList" src` liefert danach nur
noch einen Kommentar-Treffer (der erklärt, dass die Datei entfernt wurde), keine echten
Code-Referenzen mehr.

### 3.37 Vision-Dokument + KURSPLAN.md/todo.md-Abgleich (Branch `vision-roadmap-abgleich`, gemergt)

Neues `VISION.md` (Mission, Kurs-Formate Einstieg/Grundkurs/Projekt-Kurs/Vertiefung, Track-Modell
pro Sprache mit dem Prinzip "Voraussetzung gilt nur innerhalb der eigenen Sprache/des eigenen
Themas" — Ausnahme: KI-Track braucht legitim den Python-Track). `KURSPLAN.md` (bisher nirgends
verlinkt) daran ausgerichtet und erstmals aus `CLAUDE.md` eingebunden — korrigiert dabei eine
falsche Abhängigkeit (JS-Browserspiel-Track verlangte fälschlich den Python-12-Wochen-Kurs).
`todo.md`/`WORKFLOW.md` auf `kurs-js-spielewerkstatt` als nächstes Thema umgestellt.

### 3.38 Projekte-Übersicht mit Filtern + zwei neue Projekt-Kurse (Branch `kurs-projekte-uebersicht`)

`ProjectCourse.vue` war trotz einer gegenteiligen, veralteten Notiz in `todo.md` weiterhin fest auf
Cäsar-Chiffre verdrahtet (`CONTENT_PATH`/`PROGRESS_VARIANT`-Konstanten) — generalisiert auf eine
`contentPath`-Prop, `CourseDetail.vue`s `isProjectCourse` von einem ID-Vergleich auf
`course.type === 'projekt'` umgestellt. Neue Seite `/projekte` (`ProjekteView.vue`) sammelt alle
Projekt-Kurse und filtert nach Sprache, Level, Thema/Tags und Dauer (Dauer wird live aus der
`lessons.json`-Länge berechnet, kein manuell gepflegtes Feld). Projekt-Kurse erscheinen dafür nicht
mehr in `Home.vue`s normaler Kursliste; der 12-Wochen-Kurs-Banner verlinkt jetzt zu `/projekte`
statt fest zu Cäsar-Chiffre. `useLessonContent.js`s bisher pro Kurs gepflegte `import.meta.glob`-
Listen sind jetzt Wildcards (`content/*/*.md` bzw. `content/*/glossary.json`) — ein neuer
Projekt-Kurs braucht damit nur noch einen Content-Ordner + `kurse.json`-Eintrag, keine
Code-Änderung mehr. Zwei neue Projekte ergänzt: `projekt-morsecode` (Einsteiger, 5 Lektionen) und
`projekt-zahlendetektiv` (Fortgeschritten, 5 Lektionen, u.a. Primzahlen-Sieb, Collatz-Vermutung,
Bisektions-Zahlenrater) — alle Code-Beispiele lokal mit `python3` gegenverifiziert. Neue Tests in
`tests/projekte.spec.js` (Kartenanzahl, Level-/Tag-Filter, Reset, Morsecode-Lektion lösen,
Banner-Link); `tests/site.spec.js` an die neue Home-Struktur angepasst (Projekt-Kurse nicht mehr
in `#kurse-uebersicht`, dafür ein `/projekte`-Teaser-Link).

### 3.39 Header-Nav: direkter "Projekte"-Link (Branch `nav-projekte-link`)

Kleine, eigenständige Ergänzung: `App.vue`s Header-Nav hatte neben "Home"/"Kurse" keinen direkten
Link zu `/projekte` — bisher nur über den Teaser auf der Startseite oder den Banner im 12-Wochen-
Kurs erreichbar. Neuer `<router-link to="/projekte">` direkt in der Nav, neue `nav.projects`-Keys.
**Testfalle dabei gefunden:** der bestehende Home-Test prüfte `a[href="/projekte"]` mit
`toBeVisible()` — traf durch den neuen Nav-Link jetzt zwei Elemente (Nav-Link + Teaser-Link) und
verletzte Playwrights Strict-Mode. Fix: auf die schon vorhandene `.projekte-teaser-link`-Klasse
präzisiert, neuer eigener Test für den Nav-Link ergänzt. `npm run test:checks` (60 Tests) grün.

### 3.40 Mein Profil: Abschluss-Abzeichen für Projekt-Kurse (Branch `profil-abschluss-badges`)

Nutzer-Wunsch nach einer leichtgewichtigen Anerkennung für abgeschlossene Projekt-Kurse — explizit
**kein** Zertifikat wie beim 12-Wochen-Kurs (Quiz, PDF, Login-Pflicht wäre inkonsistent mit dem in
`VISION.md` festgehaltenen Projekt-Kurs-Prinzip "kein Zertifikat, niedrige Einstiegshürde"),
sondern ein einfaches Abzeichen im eigenen Profil.

**Neue Seite `/profil`** (`ProfilView.vue`, Login-gated — ohne Account nur ein Hinweistext, analog
zum PDF-Download-Gate aus 3.13): zeigt pro Projekt-Kurs eine Karte mit 🏅 (verdient) oder 🔒
(gesperrt) + Fortschritt (`x/y Lektionen`). Neue Composable `useProjectBadges.js`: lädt
`kurse.json`, filtert `type === 'projekt'`, nutzt für jeden Kurs `useInteractiveProgress` (exakt
derselbe Fortschritts-Mechanismus, den `ProjectCourse.vue` selbst schon nutzt — kein zweites,
paralleles Punktesystem) und `lessons.json`-Länge (gleiches Wildcard-Glob wie `ProjekteView.vue`).
Abzeichen verdient, sobald `completedCount >= totalLessons`. Ein neuer Projekt-Kurs braucht dafür
**keinen** manuellen Eintrag — automatisch erkannt, wie schon bei `/projekte` selbst.

**Wichtiger Nebenfund beim Umsetzen:** Projekt-Kurs-Fortschritt (`ue-hacker-interactive-progress-
<contentPath>`, ein Key pro Kurs) wurde bisher **nie** mit dem Account synchronisiert —
`useProgressSync.js`s `FIXED_SYNC_KEYS` kannte nur `kinder`/`jugendliche` (die Interaktiv-Kurs-
Varianten), nicht die Projekt-Kurse. Ohne Fix wäre "im eigenen Profil" nur pro Browser gültig
gewesen, nicht wirklich am Account hängend. Fix: `isSyncableKey()` prüft jetzt einen Präfix
(`ue-hacker-interactive-progress-`) statt zwei fest eingetragener Keys — deckt automatisch
`kinder`/`jugendliche` UND jeden aktuellen wie künftigen Projekt-Kurs ab, ohne diese Datei je
wieder anfassen zu müssen. Per Playwright verifiziert: `PUT /api/progress` liefert den Projekt-Key
nach Login tatsächlich zurück.

Neuer Nav-Link "Mein Profil" in `App.vue` (nur sichtbar wenn `isLoggedIn`, gleiches Muster wie
`showHomeLink`). Zwei neue Tests in `tests/auth-ui.spec.js` (Login-Pflicht + Abzeichen erscheint
nach vollständigem Kurs, unvollständiger Kurs bleibt gesperrt; Sync-Test). `npm run test:auth`
(15 Tests) + `npm run test:checks` (59 Tests) grün.

**Bewusst nicht gebaut:** kein PDF-Download, kein Quiz, kein Datum/"seit wann verdient" — passend
zur bewusst niedrigen Schwelle des Formats. Eigener Branch von `main` (nicht auf
`kurs-js-spielewerkstatt` aufgesetzt, obwohl dort entwickelt) — das Feature ist unabhängig vom
JS-Kurs und gilt für alle Projekt-Kurse gleichermaßen, siehe WORKFLOW.md "ein Thema = ein Branch".

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
src/components/JupyterNotebook.vue, CodeCell.vue, PlacementCourse.vue, QuizStep.vue
scripts/migrate_notebooks_to_cells.py (einmalig gelaufen), build_cell_notebooks.py (bei jedem
  dev/build), pack_notebooks.py (zippt jetzt _bundle/*.py statt *.ipynb)
public/kurse.json
content/python-checks/config.json, week-{N}.json, index.mjs (Node-Loader für Tests)
.env.example / .env (nie committen)
```

---

## 5. Offene Aufgaben

Siehe auch `todo.md`.

**Aktuell (3.38):** Branch `kurs-projekte-uebersicht` ist lokal fertig und getestet, aber noch
nicht nach `main` gemergt/gepusht — Projekte-Übersicht + zwei neue Projekt-Kurse. Nächster
sinnvoller Schritt danach: `kurs-js-spielewerkstatt` (Plan gespeichert unter
`~/.claude/plans/fizzy-sprouting-quilt.md`) oder weitere Projekt-Kurse (`kurs-python-projekte`,
siehe `todo.md`).

**Betrieb**
- [ ] Server-Deploy: Code ist auf `origin/main`, aber noch nicht auf dem Produktions-Server
      ausgerollt — Nutzer deployt selbst (`git pull` + `docker compose up -d --build app` auf dem
      Server, siehe Abschnitt 4). Dabei auch die `build:cells`-Pipeline prüfen — `npm run build`
      muss `build:cells` vor `pack:notebooks` laufen lassen, sonst fehlen `_generated`/`_bundle`
      im Produktions-Build. Danach im Browser gegenprüfen: `/kurs/python-12-wochen-grundkurs`
      zeigt die neue Wochen-Tour (nicht mehr die alte Akkordeon-Seite).
- [x] SQLite-Backup-Script (`api/src/scripts/backup-db.js`) — siehe Abschnitt 4. Externe
      Sicherung der Backups (z.B. `rsync`/`rclone` auf einen anderen Host) bewusst nicht mitgebaut,
      hängt von der jeweiligen Server-Infrastruktur ab. Auf dem Server noch einzurichten (Cron o.ä.).

**Inhalte**
- Keine offenen Punkte aus der Storytelling-Überarbeitung mehr (siehe 3.4) — "Gilde-Meister-Urkunde" geklärt, kein Bug
- [x] Debug-Notebook-Ziele (3.5): Pferde + Abenteuer nachgezogen (3.16, Branch
  `debug-ziele-pferde-abenteuer`)
- [x] Einstufungstest (3.6): Distraktoren für Wochen 5-12 geschärft (3.15, Branch
  `einstufung-distraktoren-w5-12`)
- Interaktiver Kurs (3.7): "Ausführen vs. Prüfen"-Klarheit und Weiter-Flow noch offen, braucht
  konkretes Nutzer-Feedback (idealerweise Screenshot) bevor daran gearbeitet wird
- Text-Tippfehler-Pass (3.8–3.10): alle 444 Notebooks + Cheat-Sheets/Glossare + UI-Texte +
  Wochenbeschreibungen + `weeks.json` fertig — `.vue`-Dateien und die interaktiven Kurse
  (`python-grundlagen-interaktiv*`, `caesar-chiffre`) noch offen
- Cäsar-Chiffre-Projekt (3.11): EN-Version noch offen (DE-first)
- [x] Punkte-artige Feier-Texte entfernt (3.14, Branch `entferne-xp-texte`) — siehe unten
- Zertifikat-PDF (3.13): E-Mail-Versand eigenes, späteres Thema (hängt an der noch offenen
  Kontakt-E-Mail-Adresse, s.u.). Bewusst nur für den 12-Wochen-Kurs — Interaktiv-Kurs und
  Projekt-Kurse (Cäsar-Chiffre, künftig `kurs-js-spielewerkstatt`) könnten später ein eigenes
  Abschluss-Zertifikat bekommen, aber noch nicht angefragt.
- [x] Personalisierte Falsch-Antwort-Erklärungen (3.17, Branch
  `einstufung-personalisierte-erklaerungen`, gemerged) — inkl. Nebenfund/Fix der unübersetzten
  `explanation_en`-Felder

**`main` ist nach `origin/main` gepusht** (siehe `git log main` für die volle Historie) —
Server-Deploy selbst bewusst weiter zurückgestellt (Nutzer will erst später deployen).

**Refactoring (vom Nutzer angestoßen, gegen zu große Dateien):**
- [x] Schritt 1: `weeks.json` pro Woche gesplittet (3.18, Branch `weeks-json-splitten`, gemergt)
- [x] Schritt 2: CSS-Konsolidierung Kurs-Sidebar-Layout (3.19, Branch
      `css-konsolidierung-kurslayout`, gemergt). `.btn-kernel`/`.btn-check`/`.code-editor`/
      `.kernel-status` (LessonView/CodeChallenge) noch offen — die sind NICHT identisch, erst
      Drift vs. Absicht klären (siehe 3.19 "Offen")
- [x] Schritt 3: `WeekSection.vue` in Subkomponenten aufgeteilt (3.20, Branch
      `weeksection-subkomponenten`, gemergt) — neue `CheatSheetList.vue` + `VariantSelector.vue`
- [x] Schritt 4: `LessonView.vue` entflechtet (3.21, Branch `lessonview-entflechten`, gemergt) —
      Glossar/Content-Loading → neues `useLessonContent.js`
- [x] Schritt 5: `PlacementCourse.vue` Score-Logik ausgelagert (3.22, Branch
      `quizstep-placementcourse-entflechten`, gemergt) — `computePlacementResults`/
      `weekScoresToRows` neu in `useWeekChecks.js`. `QuizStep.vue` bewusst NICHT gesplittet (schon
      kohärent, keine natürliche Trennstelle — siehe 3.22 "Abweichung")
- [x] Schritt 6: Ternary-Cleanup (3.23, Branch `ternary-cleanup`, gemergt) — alle 97 Inline-
      `lang === 'en' ? X : Y` auf den bestehenden `t()`-Mechanismus umgestellt. Bewusst nicht
      migriert: Daten-Feld-Auswahl (`q.explanation_en`/`explanation` etc.) und rein technische
      Ternarys (Locale-Code, Pfad-Suffix) — siehe 3.23 "Bewusst NICHT migriert"

**Refactoring-Plan (Schritte 1-6) ist damit komplett abgeschlossen.**

**Danach — nächste Kurs-Themen, je eigener Branch von `main`:**

1. **`kurs-js-spielewerkstatt`** — JavaScript statt der ursprünglich geplanten Python-Spiele-
   Werkstatt (Pyodides synchrones Ausführungsmodell verträgt keine echte Spiele-Loop, siehe 3.32).
   Vollständiger Implementierungsplan gespeichert unter
   `~/.claude/plans/fizzy-sprouting-quilt.md`.
2. **`kurs-python-projekte`** — „Was kommt danach?“ Projekt-Sprints
3. **`kurs-ki-labor`** — KI-Grundlagen, baut auf dem Python-Track auf

Nicht mischen; Details/Checkboxen in `todo.md`, Gesamt-Roadmap/Track-Modell in `VISION.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.
Kontakt-E-Mail im Footer wartet noch auf die tatsächliche Adresse vom Nutzer (nicht selbst erfinden).

**Bekannte Altlasten (niedrige Prio):** Notebook-Download-ZIP nur DE; optionale EN-Nachzüge bei neuen Kursen (inkl. Cäsar-Chiffre).

**Überlegungen (noch nicht entschieden):** Nutzer erwägt evtl. eine dritte Sprache neben DE/EN —
noch kein konkretes Ziel. Die UI-Ternarys sind seit Refactoring-Schritt 6 (3.23) bereits auf `t()`
umgestellt — dieser Teil ist erledigt. Offen bliebe nur noch der Content: `_en`-Feld-Suffix in
`content/python-checks/week-{N}.json`, `-en`-Ordner-Suffix in `useCourseData.js`. Keine i18n-Library
nötig, falls es dazu kommt — der bestehende `t()`-Mechanismus reicht.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch von `main` (`WORKFLOW.md`) — **kein** Präfix mehr (früher `cursor/…`,
  wurde entfernt)
- Jede Verhaltensänderung braucht einen Playwright-Test (`WORKFLOW.md`) — reine Text-/Typo-Korrekturen sind ausgenommen
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt`
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`; Verhaltensänderungen brauchen
  einen Test in `tests/*.spec.js` bzw. `api/src/scripts/*.test.js` (`WORKFLOW.md`) — nicht nur
  manuell verifizieren
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)
- 12-Wochen-Kurs-Notebooks sind seit 3.33 **kein `.ipynb` mehr** — Zellen-Ordner mit `NN_*.py`-
  Dateien, `_generated`/`_bundle` sind generiert (gitignored, `scripts/build_cell_notebooks.py`).
  Nicht versehentlich wieder rohe `.ipynb`-Dateien als Quelle einführen.
- Missionen/Belohnungen kennen seit `wochen-zertifikate` **keine Punkte/Items mehr** — nur noch
  Zertifikate (siehe 3.12). Nicht versehentlich wieder ein Punktesystem einführen.
- Zertifikat = **nur** Wochen-Check (Quiz + beide Coding-Aufgaben), **ein** Zertifikat pro Woche
  (keine Varianten-Aufteilung). Missionen/Boss-Quests sind reine Übung, keine Voraussetzung — nicht
  versehentlich wieder an Missionen koppeln oder wieder 3 Varianten-Zertifikate einführen.
- Kein lokales Fortschritt-Skript mehr (`scripts/fortschritt.py` entfernt) — Fortschritt-Sync läuft
  über den Account (Login), nicht über CLI-Skript + manuellen JSON-Import. Nicht wieder einführen.
- Zertifikat-PDF-Download ist **login-gated** — ohne Account nur ein Hinweistext, kein Button. Nicht
  versehentlich für alle (auch rein lokalen Fortschritt ohne Login) freischalten.
- Falsch-Antwort-Erklärungen (`optionExplanations`/`optionExplanations_en` in `weeks.json`, siehe
  3.17) gibt es **nur** bei `multiple_choice`-Fragen, bewusst nicht bei `multiple_select` (mehrere
  Antworten können gleichzeitig falsch sein). Beim Hinzufügen neuer Quizfragen dieses Feld mit
  ausfüllen, sonst fällt die UI automatisch auf die geteilte `explanation` zurück (kein Bug, aber
  weniger hilfreich) — und `explanation_en` muss eine echte Übersetzung sein, nicht identisch zu
  `explanation` (Test dafür in `tests/week-checks-logic.spec.js`).

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
   `import.meta.glob(...)`-Pfadlisten in `LessonView.vue` zu erweitern (siehe 3.11); nicht:
   Punkte-/Item-System wieder einführen (siehe 3.12); nicht: `turtle` als echtes Pyodide-Paket
   erwarten oder erneut versuchen zu installieren — es ist bewusst durch einen eigenen Canvas-Shim
   in `usePyodide.js` ersetzt (kein Web Worker, siehe 3.32); nicht: 12-Wochen-Kurs-Notebooks als
   `.ipynb` erwarten — seit 3.33 Zellen-Ordner mit `NN_*.py`-Dateien, `_generated`/`_bundle` sind
   generiert (gitignored) und müssen nicht von Hand gepflegt werden; nicht: `WeekSection.vue`/
   `MissionenPanel.vue`/`VariantSelector.vue`/`CheatSheetList.vue` erwarten oder wieder anlegen —
   seit 3.36 rendert `CourseDetail.vue` für den 12-Wochen-Kurs `WeekTour.vue` (Kachel-Wizard +
   Fortschritts-Leiste), die alte Akkordeon-UI ist entfernt; nicht: `?week=&tab=`-Deep-Links von
   `PlacementCourse.vue`/Cäsar-Chiffre-Lektionen "reparieren" oder auf `?week=&variant=&step=`
   umschreiben — funktionieren bewusst unverändert weiter, `WeekTour.vue` übersetzt intern (3.36)
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`

**Empfohlener nächster Schritt:** Branch `kurs-projekte-uebersicht` (3.38) ist lokal fertig/
getestet — mergen und pushen, sobald abgenommen. Danach: `kurs-js-spielewerkstatt` (JavaScript
statt der ursprünglich geplanten Python-Variante, Plan gespeichert unter
`~/.claude/plans/fizzy-sprouting-quilt.md` — Schritt 1 daraus ist bereits durch 3.38 erledigt) oder
weitere Projekt-Kurse (`kurs-python-projekte`, Infrastruktur existiert bereits seit 3.38). Server-
Deploy von `experiment-wochen-tour` (3.35+3.36) steht weiterhin aus (siehe Abschnitt 5 "Betrieb").
Gesamt-Roadmap/Track-Modell: `VISION.md`. Für neue **Python**-Kurse gilt seit 3.33 die
Zellen-Format-Erfahrung als Referenz, siehe Memory `project_neue-kurse-content-format`.
