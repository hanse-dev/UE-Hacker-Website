# CLAUDE.md — UE Hacker Website

**Einzige Datei, die automatisch in jede Session geladen wird — klein halten (Richtwert < 6 KB),
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

Befehle: `npm run start:all` (Vite :5173 + API :3001) · `npm run test:checks` (voll, ~2 Min) ·
`npm run test:changed` · `npm run test:auth` (Auth/Admin) · `npm --prefix api test`.

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
- SQLite nur per `npm run backup:db` sichern, nie `cp`; nie `git clean -fdx` ohne Ausschluss von
  `api/data/`.

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
