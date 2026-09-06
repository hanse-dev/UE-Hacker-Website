# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-07  
> **Aktueller Stand:** Alle Branches bis `weeks-json-splitten` (3.5–3.18) sind in `main` gemergt
> (siehe `git log main` für die genaue Reihenfolge), dazwischen auch `dependency-audit-fixes` und
> `vite-major-bump`. Noch **nicht** nach `origin/main` gepusht — Push/Deploy bewusst zurückgestellt,
> siehe Abschnitt 5/7. `weeks-json-splitten` (3.18) ist Schritt 1 eines größeren, laufenden
> Refactorings gegen zu große Dateien — Schritt 2 (CSS-Konsolidierung) ist der nächste.
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
content/python-checks/config.json, week-{N}.json, index.mjs (Node-Loader für Tests)
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
  Projekt-Kurse (Cäsar-Chiffre, künftig `kurs-python-spiele`) könnten später ein eigenes
  Abschluss-Zertifikat bekommen, aber noch nicht angefragt.
- [x] Personalisierte Falsch-Antwort-Erklärungen (3.17, Branch
  `einstufung-personalisierte-erklaerungen`, gemerged) — inkl. Nebenfund/Fix der unübersetzten
  `explanation_en`-Felder

**Alle Branches bis `einstufung-personalisierte-erklaerungen` sind gemergt** (siehe `git log main`
für die genaue Reihenfolge) — noch **nicht** nach `origin/main` gepusht, Push/Server-Deploy
bewusst zurückgestellt (Nutzer will erst später deployen).

**Refactoring (vom Nutzer angestoßen, gegen zu große Dateien):**
- [x] Schritt 1: `weeks.json` pro Woche gesplittet (3.18, Branch `weeks-json-splitten`, gemergt)
- [ ] Schritt 2: CSS-Konsolidierung (doppelte Klassen `.btn-kernel`/`.btn-check`/`.code-editor`/
      `.kernel-status` in LessonView/ProjectCourse/InteractiveCourse/CodeChallenge)
- [ ] Schritt 3: `WeekSection.vue` in Subkomponenten aufteilen (CheatSheetList, VariantSelector)
- [ ] Schritt 4: `LessonView.vue` entflechten (Glossar/Content-Loading → eigenes Composable)
- [ ] Schritt 5: `QuizStep.vue`/`PlacementCourse.vue` ähnlich entflechten
- [ ] Schritt 6: Ternary-Cleanup (97 Inline-`lang === 'en' ? X : Y`) — niedrige Priorität, außer eine
      dritte Sprache kommt konkret dazu (siehe „Überlegungen" unten), dann vorziehen

**Danach — nächste Kurs-Themen, je eigener Branch von `main`:**

1. **`kurs-python-spiele`** — Python Spiele-Werkstatt, `ProjectCourse.vue` schon generalisiert,
   Inhalte (mehrere kleine Projekte wie Cäsar-Chiffre, DE-first) fehlen noch
2. **`kurs-python-projekte`** — „Was kommt danach?“ Projekt-Sprints
3. **`kurs-js-minigames`** *oder* **`kurs-ki-labor`** — Entscheidung beim Start

Nicht mischen; Details/Checkboxen in `todo.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.
Kontakt-E-Mail im Footer wartet noch auf die tatsächliche Adresse vom Nutzer (nicht selbst erfinden).

**Bekannte Altlasten (niedrige Prio):** Notebook-Download-ZIP nur DE; optionale EN-Nachzüge bei neuen Kursen (inkl. Cäsar-Chiffre).

**Überlegungen (noch nicht entschieden):** Nutzer erwägt evtl. eine dritte Sprache neben DE/EN —
noch kein konkretes Ziel. DE/EN ist aktuell hart auf zwei Sprachen verdrahtet (Ternarys, `_en`-Feld-
Suffix, `-en`-Ordner-Suffix), siehe Refactoring-Schritt 6 oben. Keine i18n-Library nötig, falls es
dazu kommt — der bestehende `t()`-Mechanismus reicht, nur der Content ist der eigentliche Aufwand.

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
   Punkte-/Item-System wieder einführen (siehe 3.12)
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`

**Empfohlener nächster Schritt:** `weeks-json-splitten` (3.18) ist fertig, getestet und gemergt.
Refactoring-Schritt 2 (CSS-Konsolidierung, siehe Abschnitt 5) ist der nächste im laufenden Plan.
Weiterhin offen: ob/wann nach `origin/main` gepusht und deployed wird. Falls stattdessen inhaltlich
weitergearbeitet werden soll: `kurs-python-spiele` (Spiele-Werkstatt-Inhalte, bereits begonnen) ist
der nächstliegende Kandidat.
