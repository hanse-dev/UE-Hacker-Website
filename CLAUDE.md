# CLAUDE.md — UE Hacker Website

**Einzige Datei, die automatisch in jede Session geladen wird — klein halten (Richtwert < 8 KB),
keine `@`-Imports.** Alles Weitere liegt "kalt" und wird nur bei Bedarf gelesen (Tabelle unten).

## Projekt

Lernplattform für Kinder/Jugendliche (Python, JavaScript, KI). Vue 3 + Vite + Vue Router, CSS ohne
Tailwind, Pyodide im Browser. Ein Node-Prozess (`api/`, Express + SQLite, Node ≥ 22) liefert
`/api/*` und das gebaute Frontend; Docker-Service `app`, Port 8080. Deploy macht der Nutzer selbst.

```
src/{components,views,composables,router}   Frontend
api/src/                                    Express, db.js, routes, scripts/
content/python-woche{N}-{abenteuer|pferde|scifi}[-en]/   12-Wochen-Kurs: lessons.json + *.md
content/python-12-wochen-grundkurs[-en]/    nur noch Glossar/Lösungen als Zellen-Ordner (NN_*.py)
content/python-checks/week-{N}.json         Wochen-Check (Quiz + 2 Coding-Aufgaben)
content/<projekt>/, js-grundkurs-woche{N}/, ki-labor…   übrige Kurse (lessons.json + Markdown)
public/kurse.json                           Kursmetadaten (inkl. title_en/description_en)
tests/*.spec.js                             Playwright
```

Start lokal: `npm run start:all` (Vite :5173 + API :3001) · `npm run start:prod` (Build, alles :8080).

## Tests & Sicherung (immer einhalten)

| Befehl | Wann / was |
|---|---|
| `npm run test:precommit` | läuft automatisch im Pre-commit-Hook: nur die Specs zu den staged Dateien; Kern-Dateien oder unbekannte Dateien → volle Suite |
| `npm run test:checks` | volle Suite (~2 Min); läuft automatisch im Pre-push-Hook, danach `test:devskip` |
| `npm run test:changed [-- --dry-run]` | manuell: Arbeitsverzeichnis + Branch-Diff zu `main` |
| `npm run test:auth` | zusätzlich bei Änderungen an Auth/Admin/Sync (Port 5174, Test-API :3011) |
| `npm --prefix api test` | bei Änderungen an `api/src/scripts/` (Backup) |
| `npm run contract:update` | nach neuen Kursen/Lektionen/Fragen: Fortschritts-Vertrag neu einfrieren, Fixture mitcommitten |
| `npm run lint:spelling:de` | deutscher Content (LanguageTool in Docker), zusätzlich zu cspell |

- **Hooks nie umgehen** (`SKIP_CHECKS=1`, `--no-verify`), außer der Nutzer verlangt es ausdrücklich.
  Hooks liegen in `.githooks/` (`core.hooksPath`, wird von `npm install` gesetzt).
- **Roter Test = nicht committen/pushen.** Ursache beheben; Test nie abschwächen, damit er grün wird.
  Schlägt `progress-contract.spec.js` an: Änderung zurücknehmen oder Migration bauen — nicht einfach
  neu einfrieren.
- Neuer Test muss fehlschlagen, wenn man die Änderung zurücknimmt (einmal gegenprüfen).
- Neue Komponente/Composable/Content-Ordner → Regel in `scripts/test-changed.mjs` (`RULES`) ergänzen.
- Neue Prüf-Logik nur über `useTaskValidation.js` — der Dev-Modus `npm run dev:skip-checks` darf nur
  mit `import.meta.env.DEV` wirken, nie im Produktions-Build.
- Tests schreiben: Kernel über `startKernel()`, Editor über `tests/helpers/codemirror.js`, Lösungen
  über `openSolutionsNotebook()`. Testdatei umbenannt → `package.json`-Skripte prüfen (Playwright
  ignoriert fehlende Dateien stillschweigend).
- Worktrees haben eigene Ports (`worktree.ports.json`); Standard im Haupt-Checkout: 5173/5174 (Web),
  3001/3011 (API). Generierte Dateien stellt `scripts/ensure-test-prereqs.mjs` vor jedem Lauf sicher.
- **Daten:** `.env` (`ADMIN_PASSWORD`) nie committen. SQLite liegt in `api/data/` (gitignored,
  Bind-Mount) — sichern nur per `npm run backup:db` (`VACUUM INTO`), nie `cp`; nie `git clean -fdx`
  ohne Ausschluss von `api/data/`. Env-Änderung → Container neu erstellen, nicht nur rebuilden.
- Nichts Destruktives ohne Rückfrage: kein Force-Push, kein `git reset --hard` auf `main`, kein
  Löschen ungemergter Branches (`git branch -d`, nie `-D`).

## Regeln (Details: `WORKFLOW.md`)

- **Keine Sub-Agenten**, außer der Nutzer verlangt sie ausdrücklich.
- **Neues Thema = neuer Branch im eigenen Worktree:** `npm run worktree:new -- <branch>` (ohne
  Präfix, von `main`). Nie `git checkout -b` im Haupt-Checkout; direkt auf `main` nur kleine,
  abgeschlossene Korrekturen. Nach dem Merge: `npm run worktree:remove -- <branch>` und Branch
  lokal + remote löschen, ohne nachzufragen.
- **Nach jeder abgeschlossenen Einheit sofort committen** (nur zugehörige Dateien), ohne auf
  Aufforderung zu warten. Push/Merge erst, wenn das Thema fertig und getestet ist.
- **Jede Verhaltensänderung braucht einen Playwright-Test** (`tests/*.spec.js`), der ohne die
  Änderung fehlschlägt. Reine Text-/Typo-Korrekturen nicht. Flaky Tests mit `test.skip` + Grund
  abschalten, nicht wiederholen.
- **Auffälligkeiten sofort beheben**; nur was wirklich nicht jetzt geht, kommt mit Datei, Grund und
  Vorschlag in `todo.md`. Nie nur im Bericht erwähnen.
- **Gespeicherter Fortschritt darf nicht brechen:** Ordnernamen, Lektions-/Fragen-/Kurs-IDs,
  Position der Coding-Aufgaben, Storage-Keys/`version` nie umbenennen, umsortieren oder löschen.
  Neue Lektionen nur mit neuer ID. Neue DB-Spalten brauchen `ALTER TABLE` in `api/src/db.js`. Neues
  per `npm run contract:update` einfrieren.
- **Inhalte:** vor jeder Änderung `INHALTE.md` Abschnitt 6 lesen. DE und EN synchron halten, alle
  drei Themen prüfen. Aufgabentext ändern = `lessons.json` **und** Lösungs-Markdown-Zelle; jede
  Lösung per `python3` gegen `expected` laufen lassen. Jede Aufgabe braucht ein `expected`.
- **Verständlichkeit:** neue/geänderte Lektionen (Python 12 Wochen, micro:bit) vor dem Merge mit
  `npm run testkind -- --geaendert --out <scratchpad>/bericht.md` prüfen: „hoch“ beheben, „mittel“ ansehen.
- **Doku nach jedem Commit:** `todo.md` (offene Punkte) und `HANDOFF.md` (Tabelle in Abschnitt 3,
  neue Fallstricke) im selben Commit nachziehen und dabei Erledigtes nach `docs/archiv/` verschieben.
  In diese Datei kommt nur, was in **jeder** Session gebraucht wird.

## Nicht ohne Rückfrage ändern

- Kein Punkte-/Item-System, kein lokales Fortschritt-Skript. Zertifikat = nur Wochen-Check, eines
  pro Woche, PDF-Download nur mit Login.
- Keine `.ipynb` als Quelle; `_generated`/`_bundle`/ZIPs sind generiert und gitignored.
- Accounts legt der Admin an (kein öffentliches Sign-up, kein Mailversand). Login ersetzt den
  lokalen Fortschritt durch den Account-Stand, Seiten-Reload merged nach `updatedAt`.
- `output_contains` prüft tolerant, `output_equals` exakt. Lektionen prüfen nur die Ausgabe,
  Struktur-Checks gibt es nur im Wochen-Check.

## Bei Bedarf lesen (gezielt per `grep`/Abschnitt, nicht ganze Dateien)

| Datei | Wann |
|---|---|
| `HANDOFF.md` → "Gelernte Regeln" | **vor** Änderungen an Pyodide, JS-Sandbox, Vue/CSS, Tests, Sync, Content — nur den passenden Block |
| `HANDOFF.md` Abschnitt 3/4 | Feature-Übersicht (Nummern → Archiv), Docker, Backup, wichtige Pfade |
| `WORKFLOW.md` | Details zu Worktrees/Ports, Hooks, Fortschritts-Vertrag, Doku-Pflege |
| `todo.md` | offene Punkte und bewusste Lücken je Woche; bei Planung und nach jedem Commit |
| `INHALTE.md` | Dateistruktur und Kopplungen; vor jeder Inhaltsänderung |
| `VISION.md`, `KURSPLAN.md`, `PROJEKTIDEEN.md` | Track-Modell, Lehrpläne, Ideen; bei Kurs-Planung |
| `docs/archiv/HANDOFF-historie.md` | "Warum ist das so gebaut?" — `grep -n "^### 3.NN"` |
| `docs/archiv/todo-erledigt.md` | erledigte Aufgaben/Branches |
