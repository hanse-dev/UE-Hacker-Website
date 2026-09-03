# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-03  
> **Aktueller Stand:** Branch `cursor/debug-notebook-safety` (von `main`, enthält PR #1–#4, die
> Storytelling-Überarbeitung (3.4) sowie den Endlosschleifen-Schutz + Sci-Fi-Debug-Ziele (3.5))  
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
| #1 | `cursor/python-lernpfad-quiz` | Einstufung + Wochen-Checks, Tests, alter Lernpfad entfernt |
| #2 | `cursor/admin-login` | Express+SQLite API, Admin, Login, Progress/Notebook-Sync, Single-Port-Deploy |
| #3 | `cursor/fix-notebook-sync-loop` | Hotfix: Notebook-Blink-/Reload-Schleife bei eingeloggt+Sync |

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

### 3.5 Debug-Notebook-Sicherheit: Endlosschleifen-Schutz + Sci-Fi-Debug-Ziele (Branch `cursor/debug-notebook-safety`)

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
danach läuft eine normale Zelle sofort wieder korrekt.

**Debug-Ziele (Punkt 6):** Sci-Fi-Variante komplett (12 Wochen × DE+EN = 24 Dateien, 72
Bug-Markdown-Zellen) um eine **Ziel:**/**Goal:**-Zeile ergänzt, die das erwartete Verhalten/die
erwartete Ausgabe beschreibt, ohne den Bug selbst zu verraten (z.B. bei `koordinaten[0] = 150` auf
einem Tupel: "Ziel: Das Programm soll die erste Koordinate auf `150` ändern" — ohne
Tupel-Unveränderlichkeit zu erwähnen). Stichprobenartig gegen den jeweiligen Code-Kontext geprüft
(Woche 1, 8, 11) — akkurat und spoilerfrei; `tests/storytelling-content.spec.js`s
Anti-Spoiler-Test (prüft nur Code-Zellen auf `# Bug:`-Kommentare) bleibt unberührt, da nur
Markdown-Zellen geändert wurden.

**Offen (nächste Session):** Pferde- und Abenteuer-Variante nach demselben Muster mit Debug-Zielen
ergänzen (im Plan als "danach nachziehen" vorgesehen, nicht in dieser Sitzung geschafft).

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

### Tests

| Command | Inhalt |
|---------|--------|
| `npm run test:checks` | Pre-commit: Logic, Week-Checks/Placement, Site, Merge, Storytelling-Content |
| `npm run test:auth` | API + Admin/Optionen-UI (eigene Config, Test-API :3011) |

### Wichtige Pfade

```
api/src/          Express (index, auth, db, routes)
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
- [ ] Server-Deploy final verifizieren (Service `app`, Orphans weg, Health, Admin-Login, kein Notebook-Blinken mehr nach PR #3)

**Inhalte**
- Keine offenen Punkte aus der Storytelling-Überarbeitung mehr (siehe 3.4) — "Gilde-Meister-Urkunde" geklärt, kein Bug
- Debug-Notebook-Ziele (3.5, Punkt 6): Pferde + Abenteuer noch offen (Sci-Fi fertig)

**Laufend — 10 Verbesserungen in 6 Branches (Reihenfolge B→A→E→F→C→D, siehe `todo.md` + Plan-Datei
`~/.claude/plans/scalable-singing-cook.md`):**

1. **`cursor/debug-notebook-safety`** — ✅ Punkt 5 fertig, Punkt 6 Sci-Fi fertig (Pferde/Abenteuer offen)
2. **`cursor/et-fixes`** — Einstufungstest: "weiß nicht"-Option, Scoring lockern, Distraktoren (offen)
3. **`cursor/kontakt-email`** — Footer-Kontakt-E-Mail (offen, braucht Adresse vom Nutzer)
4. **`cursor/kurs-caesar-chiffre`** — erstes Projekt neben den Wochenkursen (offen)
5. **`cursor/interaktiv-klarer`** — gestufter Hinweis statt Lösungsverrat in `LessonView.vue` (offen)
6. **`cursor/text-typo-pass`** — Rechtschreib-/Text-Pass über die ganze Seite (offen, größter Umfang)

**Danach — nächste Kurs-Themen, je eigener Branch von `main` (Reihenfolge):**

1. **`cursor/kurs-python-spiele`** — Python Spiele-Werkstatt (Turtle/Textspiele)  
2. **`cursor/kurs-python-projekte`** — „Was kommt danach?“ Projekt-Sprints  
3. **`cursor/kurs-js-minigames`** *oder* **`cursor/kurs-ki-labor`** — Entscheidung beim Start  

Nicht mischen; Details/Checkboxen in `todo.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Mailversand/Kontaktformular, Supabase als Pflicht.
(Eine rein statische Kontakt-E-Mail im Footer ist als Branch `cursor/kontakt-email` geplant — kein
Formular, kein Versand, siehe oben.)

**Bekannte Altlasten (niedrige Prio):** Notebook-Download-ZIP nur DE; optionale EN-Nachzüge bei neuen Kursen.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch `cursor/…` von `main` (`WORKFLOW.md`)
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt`
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)

---

## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`  
2. `HANDOFF.md` + `todo.md` + `WORKFLOW.md` lesen  
3. Neues Thema → **neuen** Branch, z.B. `git checkout -b cursor/et-fixes`  
4. Nicht: altes `prod` in Compose erwarten; nicht: Sync so ändern, dass Notebooks wieder voll neu geladen werden bei jedem Apply; nicht: Pyodide in einen Web Worker verschieben ohne `input()` (65 Notebooks) neu zu lösen (siehe 3.5)
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`

**Empfohlener nächster inhaltlicher Schritt:** `cursor/debug-notebook-safety` fertigstellen (PR nach
`main`), dann Branch `cursor/et-fixes` anlegen (Plan-Datei `~/.claude/plans/scalable-singing-cook.md`,
Abschnitt "Branch A"). Erst danach `cursor/kurs-python-spiele` (siehe Abschnitt 5, "Danach").
