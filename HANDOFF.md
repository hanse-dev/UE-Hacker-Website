# Handoff — UE Hacker Website

> **Zuletzt aktualisiert:** 2026-09-03  
> **Aktueller Stand:** `main` enthält PR #1–#3 + Storytelling-Überarbeitung (siehe 3.4). Sieben weitere
> Themen sind fertig auf eigenen Branches, aber noch **nicht** nach `main` gemerged — Merge/Deploy ist
> auf Wunsch des Nutzers bewusst zurückgestellt (siehe 3.5). `wochen-zertifikate` wurde in dieser
> Session final überarbeitet (Zertifikat jetzt komplett von Missionen entkoppelt, 2 Coding-Aufgaben
> pro Woche, alle Belohnungszeilen aus 444 Notebooks entfernt) — Details unten in 3.5, offene
> Anschlussfrage (Merge-Reihenfolge) in Abschnitt 5/7.  
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

### 3.5 Sieben weitere Themen (je eigener Branch, fertig, noch nicht gemerged)

Nutzer-Vorgabe: Branch-Namen jetzt **ohne** `cursor/`-Präfix (wurde nachträglich bei allen Branches
entfernt). Jede Verhaltensänderung hat einen Playwright-Test (WORKFLOW.md-Regel, s.u.). Deploy/Merge
bewusst zurückgestellt — der Nutzer will erst später deployen.

**`debug-notebook-safety`** — Pyodide läuft komplett im Hauptthread (`usePyodide.js`); eine
`while True:`-Zelle würde den Tab einfrieren, ein Web-Worker-Timeout hätte `input()` in 65 Notebooks
kaputt gemacht (Worker hat kein `window.prompt()`). Stattdessen: AST-Injection (`_LoopDeadlineGuard`
in `usePyodide.js`), die in jede `for`/`while`-Schleife eine Deadline-Prüfung einbaut; nach 5s wirft
`_CellTimeout(BaseException)` (bewusst nicht `Exception`, damit generische `except Exception`-Blöcke
in Nutzercode das nicht schlucken). Zusätzlich: 24 Sci-Fi-Debug-Notebooks (12 Wochen × DE+EN) um eine
"Ziel:"-Zeile ergänzt, damit Bug-Zellen ein erkennbares Soll-Verhalten nennen.

**`et-fixes`** — Einstufungstest-Verbesserungen: "Weiß ich nicht"-Option im Quiz (eigene, freundliche
Rückmeldung statt harter Falsch-Wertung-Optik), Einstufung von 2 auf 3 Fragen/Woche mit eigener
`placementPassThreshold: 0.66` (bewusst nicht 0.67 — `2/3 = 0.6666...` liegt SONST unter der Schwelle,
selbst gefunden per `python3 -c "print(2/3>=0.67)"` → `False`), 12 Distraktoren in Wochen 1-4 von
generischem Unsinn zu plausiblen Missverständnissen geschärft.

**`interaktiv-klarer`** — gestufter Hinweis in `LessonView.vue`: beim ersten Fehlversuch nur ein
vager Hinweis, der wörtliche erwartete Teilstring wird erst ab dem zweiten Fehlversuch gezeigt (vorher
wirkte die sofortige wörtliche Anzeige wie Lösungsverrat).

**`text-typo-pass`** — `cspell.json` + `npm run lint:spelling` neu eingerichtet (braucht `"import"`,
nicht nur `"dictionaries"`, sonst 400+ Fehlalarme). Reale Tippfehler gefunden und behoben: britisches
Englisch vereinheitlicht (W12 EN "colors"→"colours"), "Parours"→"Parcours", "pferdbezogene"→
"pferdebezogene", "Pferdname"→"Pferdename", "Futterschip"→"Futterschippe" (auch im Rewards-Manifest),
doppeltes "Du betrittstest"→"Du betrittst" (W1+W10 Sci-Fi).

**`backup-sqlite-db`** — `api/src/scripts/backup-db.js`: sicheres Backup der Live-SQLite-DB per
`VACUUM INTO` (kein `cp`, das bei gleichzeitigen Schreibzugriffen korrumpieren könnte) + Rotation
(`BACKUP_KEEP`, Default 14). `npm run backup:db` (Root + `api/`). Tests mit `node --test` (erste
Tests im `api/`-Ordner).

**`kurs-caesar-chiffre`** — erstes eigenständiges Projekt neben den Wochenkursen (nicht Teil des
12-Wochen- oder Interaktiv-Kurses): `content/caesar-chiffre/` mit 5 Lektionen (ord/chr, Verschieben
mit Modulo, Verschlüsseln-Funktion, Entschlüsseln-Funktion, Brute-Force-Knacker). Neue, schlanke
`src/components/ProjectCourse.vue` (reduzierte Kopie der Nicht-Varianten-Teile von
`InteractiveCourse.vue`, kein Kinder/Jugendliche-Varianten-Selector). Eintrag in `kurse.json` als
`projekt-caesar-chiffre`, verlinkt aus dem 12-Wochen-Kurs. Auf `kurs-python-spiele` wurde
`ProjectCourse.vue` danach generalisiert (`contentPath`-Prop statt fest verdrahteter Konstanten),
damit sich mehrere Projekt-Kurse die Komponente teilen können — das ist bereits committet, die
eigentlichen Spiele-Inhalte für `kurs-python-spiele` fehlen aber noch (siehe todo.md).

**`wochen-zertifikate`** — größere Änderung, vom Nutzer explizit angestoßen: das Punkte-/
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
- [ ] Backup-Skript (`backup-sqlite-db`, siehe 3.5) auf dem Server einrichten, sobald die anderen Branches gemerged sind

**Inhalte**
- Keine offenen Punkte aus der Storytelling-Überarbeitung mehr (siehe 3.4)
- [ ] **Neu gefunden, noch nicht behoben:** Boss-Quest-Lösungscode (`6_loesungen`-Notebooks) und
  Abschluss-Markdown enthalten noch punkte-artige Feier-Texte, z.B. `print("🎉 +400 XP: Boss-Quest
  abgeschlossen!")` und `**Gesammelte XP:** 1500 Punkte`. Das sind **keine** `**Belohnung:**`-Zeilen
  (die wurden in `wochen-zertifikate` bereits vollständig entfernt, siehe 3.5) — das ist Code-Output
  und Abschluss-Prosa, die noch von XP/Punkten erzählt, obwohl es das System nicht mehr gibt. Noch
  nicht mit dem Nutzer geklärt, ob das behoben werden soll (reines Story-Flavor vs. veraltete
  Punkte-Referenz). Vermutlich in denselben 444 Notebooks verstreut wie die entfernten
  Belohnungszeilen — vor dem Fix erst eine Umfangs-Analyse machen (grep nach `XP`, `Gesammelte`,
  `Punkte` in Boss-/Lösungs-Notebooks), dann mit dem Nutzer abstimmen, bevor an allen Dateien geändert
  wird.

**Fertige, ungemergte Branches (siehe 3.5 für Details):** `debug-notebook-safety`, `et-fixes`,
`interaktiv-klarer`, `text-typo-pass`, `backup-sqlite-db`, `kurs-caesar-chiffre`, `wochen-zertifikate`.
Merge/Deploy ist auf Nutzerwunsch bewusst zurückgestellt — nicht ohne Rückfrage mergen. Empfohlene
Merge-Reihenfolge (Details/Begründung siehe 3.5 und todo.md):
`debug-notebook-safety` → `et-fixes` → `interaktiv-klarer` → `text-typo-pass` → `backup-sqlite-db` →
`kurs-caesar-chiffre` → `wochen-zertifikate`. Nach jedem Merge `npm run test:checks` laufen lassen,
bevor der nächste Branch drankommt. **`wochen-zertifikate` ist der umfangreichste Branch** (2 Commits,
Punkte-/Sammelsystem komplett durch Zertifikate ersetzt) — dort am ehesten mit Merge-Konflikten in
`content/python-checks/weeks.json` rechnen (kollidiert mit `et-fixes`' Änderungen an derselben Datei).

**Laufend/als Nächstes:**

1. **`kurs-python-spiele`** — Python Spiele-Werkstatt, `ProjectCourse.vue` schon generalisiert,
   Inhalte (mehrere kleine Projekte wie Cäsar-Chiffre, DE-first) fehlen noch
2. **`kurs-python-projekte`** — „Was kommt danach?“ Projekt-Sprints
3. **`kurs-js-minigames`** *oder* **`kurs-ki-labor`** — Entscheidung beim Start

Branch-Namen jetzt **ohne** `cursor/`-Präfix. Nicht mischen; Details/Checkboxen in `todo.md`.

**Bewusst nicht geplant:** öffentliches Sign-up, Supabase als Pflicht. Kontakt-E-Mail im Footer wartet
noch auf die tatsächliche Adresse vom Nutzer (nicht selbst erfinden).

**Bekannte Altlasten (niedrige Prio):** Notebook-Download-ZIP nur DE; optionale EN-Nachzüge bei neuen Kursen.

---

## 6. Entscheidungen / Konventionen (nicht ohne Rückfrage ändern)

- Ein Thema = ein Branch von `main`, **ohne** `cursor/`-Präfix (`WORKFLOW.md`)
- Jede Verhaltensänderung braucht einen Playwright-Test (`WORKFLOW.md`) — reine Text-/Typo-Korrekturen sind ausgenommen
- Accounts: Admin legt an; `ageGroup` kinder|jugendliche; ein Mensch = ein Account
- Sync: per-key Merge nach `updatedAt`
- Prod: ein Container `app`, Port 8080, API serviert Static
- SQLite bleibt; Node ≥ 22 wegen `node:sqlite`
- Vor Commit: `test:checks`; Auth-Änderungen zusätzlich `test:auth`
- Inhaltsänderungen: `INHALTE.md` Abschnitt 6 (DE/EN, Manifeste, `kurse.json`)
- Missionen/Belohnungen kennen seit `wochen-zertifikate` **keine Punkte/Items mehr** — nur noch
  Zertifikate (siehe 3.5). Nicht versehentlich wieder ein Punktesystem einführen.
- Zertifikat = **nur** Wochen-Check (Quiz + beide Coding-Aufgaben), **ein** Zertifikat pro Woche
  (keine Varianten-Aufteilung). Missionen/Boss-Quests sind reine Übung, keine Voraussetzung — nicht
  versehentlich wieder an Missionen koppeln oder wieder 3 Varianten-Zertifikate einführen.
- Kein lokales Fortschritt-Skript mehr (`scripts/fortschritt.py` entfernt) — Fortschritt-Sync läuft
  über den Account (Login), nicht über CLI-Skript + manuellen JSON-Import. Nicht wieder einführen.

---

## 7. Schnellstart für Claude in der nächsten Session

1. `git checkout main && git pull`  
2. `HANDOFF.md` + `todo.md` + `WORKFLOW.md` lesen  
3. Neues Thema → **neuen** Branch (ohne `cursor/`-Präfix), z.B. `git checkout -b kurs-python-spiele`  
4. Nicht: altes `prod` in Compose erwarten; nicht: Sync so ändern, dass Notebooks wieder voll neu geladen werden bei jedem Apply; nicht: Punkte-/Item-System wieder einführen  
5. Nach Arbeit: `todo.md`/`HANDOFF.md` aktualisieren, testen, PR gegen `main`

**Empfohlener nächster inhaltlicher Schritt:** Der Nutzer wollte als Nächstes entscheiden, ob/wann die
sieben fertigen Branches (3.5) mit der oben genannten Reihenfolge gemerged werden — das war der letzte
offene Punkt am Ende der vorigen Session, noch keine Antwort. Direkt danach fragen. Falls der Nutzer
stattdessen lieber inhaltlich weiterarbeiten will: `kurs-python-spiele` (Spiele-Werkstatt-Inhalte)
oder der neu gefundene XP/Punkte-Text in Boss-Lösungsnotebooks (siehe Abschnitt 5) sind die
nächstliegenden Kandidaten.
