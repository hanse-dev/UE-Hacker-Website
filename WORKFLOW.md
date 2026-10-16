# Workflow-Regeln

Diese Datei wird **nicht** automatisch geladen. Die Kurzfassung aller Regeln steht in `CLAUDE.md`;
hier stehen die Details.

## Keine Sub-Agenten (Agent-Tool) für dieses Projekt

**Keine Sub-Agenten spawnen, auch nicht für Recherche/Exploration** — jeder Spawn startet kalt und
kostet Tokens ohne projektspezifischen Nutzen gegenüber sequenzieller Arbeit in der Hauptsession
(Read/Grep/Bash direkt nutzen). Ausnahme nur, wenn der Nutzer explizit einen Sub-Agenten verlangt.

## Git: Ein Thema = ein Branch = ein Worktree

**Immer einen neuen Branch anlegen, wenn ein neues Thema beginnt — und zwar immer in einem eigenen
Worktree** (`npm run worktree:new -- <branch-name>`, siehe nächster Abschnitt), nie per
`git checkout -b`/`git switch` im Haupt-Checkout. Der Haupt-Checkout bleibt auf `main`; dort wird
nur gemergt und es landen höchstens kleine, in sich abgeschlossene Korrekturen direkt auf `main`.
So kann im Worktree ungestört gebaut und getestet werden, ohne eine im Editor offene Session oder
einen laufenden Dev-Server im Haupt-Checkout zu stören.

- **Ohne** Prefix (z.B. `kurs-js-spielewerkstatt`, `admin-login`) — der frühere `cursor/`-Prefix
  wurde nachträglich bei allen Branches entfernt, nicht wieder einführen
- Branch von aktuellem `main` aus starten (Default von `worktree:new`)
- Ein Branch = ein Thema; Admin/Accounts nicht auf dem Lernpfad-Branch mischen
- Nächste Kurs-Themen (geplant): `kurs-js-spielewerkstatt` → `kurs-python-projekte` → `kurs-ki-labor` (siehe `todo.md`, Gesamt-Roadmap in `VISION.md`)
- Erst mergen, wenn das Thema fertig/getestet ist — danach Worktree entfernen
  (`npm run worktree:remove -- <branch-name>`), Branch löschen; neues Thema → neuer Branch + Worktree

## Git-Worktrees für parallele/ungestörte Arbeit

Jeder neue Branch bekommt seinen eigenen Worktree (Pflicht, siehe oben):

```bash
npm run worktree:new -- <branch-name> [-- --from <basis-branch>]   # Default-Basis: main
```

Legt `../UE-Hacker-Website-worktrees/<branch-name>/` an, symlinkt `node_modules`/`api/node_modules`
(kein zweites `npm install`), übernimmt `.env` und vergibt **eigene** Ports (Web-Dev, API,
Playwright-Test-Webserver, Auth-Test-API) über `worktree.ports.json` — `vite.config.js`,
`playwright.config.js` und `playwright.auth.config.js` lesen diese Datei automatisch
(`scripts/worktree-ports.mjs`). Im Haupt-Checkout fehlt die Datei, dort gelten unverändert die
Standardports (5173/5174/3001/3011). `npm run start:all`/`npm run test:checks` funktionieren im
Worktree ohne weitere Anpassung.

Die gitignorten generierten Dateien (Notebook-`_generated`/`_bundle`, Download-ZIPs) stellt
`scripts/ensure-test-prereqs.mjs` vor **jedem** Playwright-Lauf sicher (`globalSetup` in beiden
Playwright-Configs): fehlen sie oder sind sie älter als ihre Quellen, werden sie neu erzeugt. Ein
von Hand per `git worktree add` angelegter Worktree ohne `worktree.ports.json` bricht dort mit
Hinweis ab, statt stillschweigend den Server des Haupt-Checkouts zu testen. Kommt eine neue
generierte/gitignorte Datei dazu, die Tests brauchen, gehört die Prüfung in dieses Skript.

Nach dem Merge: `npm run worktree:remove -- <branch-name>` (entfernt nur den Worktree, den Branch
danach wie gewohnt per `git branch -d` löschen).

## Tests für jede Verhaltensänderung

**Jede Änderung an Logik/Verhalten (nicht reine Text-/Content-Korrekturen) braucht einen
dauerhaften Test in der Playwright-Suite (`tests/*.spec.js`), nicht nur eine manuelle
Verifizierung.** Ein Skript, das einmal im Terminal läuft, oder eine manuelle Browser-Prüfung
zeigt nur, dass es *heute* funktioniert — ohne Test in `test:checks` kann die nächste Änderung
das stillschweigend wieder kaputt machen, ohne dass es auffällt.

- Neuer Bugfix, neue Option/Feature, geänderte Berechnung/Schwelle → passenden Test in einer
  bestehenden `describe()`-Gruppe ergänzen (oder eine neue, wenn thematisch nötig) — Vorbild:
  bestehende Tests in `tests/site.spec.js`, `tests/week-checks.spec.js`,
  `tests/storytelling-content.spec.js`
- Vor dem Commit `npm run test:checks` laufen lassen und sicherstellen, dass der neue Test auch
  wirklich fehlschlägt, wenn man die Änderung rückgängig macht (sonst testet er nichts)
- Reine Content-/Text-Änderungen ohne Verhaltensänderung (Tippfehler, Formulierungen) brauchen
  keinen neuen Test, aber bei Content mit eingebetteter Logik (z. B. Datentypen-Reihenfolge in
  Quizfragen) im Zweifel lieber einen Test ergänzen als weglassen

## Pre-commit/Pre-push Hooks (Checks)

Der volle `test:checks`-Lauf (14 Spec-Dateien, ~2 Minuten) läuft nicht mehr bei jedem Commit,
sondern zweistufig, damit schnelle Zwischen-Commits nicht durch die komplette Suite ausgebremst
werden:

- **Pre-commit:** `npm run test:precommit` → `scripts/test-changed.mjs --staged` mappt die staged
  Dateien auf die betroffenen Specs (z.B. `LessonView.vue` → nur die Python-Lektions-Specs) und
  lässt nur die laufen (meist Sekunden statt Minuten). Passt eine geänderte Datei zu keiner Regel,
  oder gehört sie zu einer als "Kern" markierten Datei (z.B. `useTaskValidation.js`,
  `locales/*.js`, `App.vue`), läuft als Sicherheitsnetz automatisch die volle Suite.
- **Pre-push:** `npm run test:checks` (voll) läuft automatisch vor jedem `git push` — das ist das
  eigentliche Sicherheitsnetz vor dem Merge nach `main`. Danach läuft `npm run test:devskip`
  (~10 s, eigene Config mit drei Servern): der Dev-Modus `npm run dev:skip-checks` muss im
  Dev-Server wirken und darf im Produktions-Build nicht wirken; der Admin-Login ohne Passwort
  (`DEV_SKIP_ADMIN_LOGIN=1`) muss gehen, und mit `NODE_ENV=production` darf die API nicht starten.
- Mapping-Regeln liegen in `scripts/test-changed.mjs` (`RULES`/`CORE_PREFIXES`); bei neuen
  Komponenten/Composables/Content-Ordnern dort eine Regel ergänzen, sonst greift beim nächsten Mal
  nur das Sicherheitsnetz (voller Lauf).
- Manuell: `npm run test:changed` (Arbeitsverzeichnis + Branch-Diff zu `main`, nicht nur staged),
  `npm run test:changed -- --dry-run` zeigt nur, welche Specs laufen würden, ohne sie zu starten.
- Einmalig nach Clone: `npm install` (setzt `core.hooksPath` auf `.githooks`) und ggf. `npx playwright install chromium`
- Überspringen: `SKIP_CHECKS=1 git commit …` / `SKIP_CHECKS=1 git push …` oder `--no-verify`
- Voller Notebook-Test weiterhin manuell: `npm test`

## Auffälligkeiten: fixen oder dokumentieren (gilt auch für Sub-Agenten)

Fällt bei der Arbeit etwas auf (Vorgriff auf spätere Wochen, Inkonsistenz zwischen Varianten/Sprachen,
vereinfachte oder gekürzte Aufgaben, Lücken, Bugs), wird es **nie nur im Bericht erwähnt und dann
liegengelassen**. Entweder:
1. **gleich beheben**, wenn es klar ist und im eigenen Arbeitsbereich liegt (inkl. Lösungs-Notebook,
   Texte, Tests dazu) — oder
2. **dokumentieren**, damit es später überarbeitet werden kann: Eintrag in `todo.md` (Abschnitt
   "Nachbesserungen") mit Fundstelle (Datei), was auffiel, warum es so blieb und Vorschlag zur Lösung.

**Nacharbeiten gleich miterledigen:** Solche Arbeiten (Vorgriffe in die passende spätere Woche nachziehen,
bewusst weggelassene Inhalte wieder aufnehmen, gekürzte Mengen mit den Original-Mengen wiederholen,
generische Namen themenspezifisch machen, veraltete Tests/Doku anpassen) werden **im selben Zug erledigt**,
sobald der Grund dafür bekannt ist — nicht als Punkt in `todo.md` geparkt und später abgefragt. In `todo.md`
kommt nur, was **wirklich nicht jetzt** geht (z.B. hängt von noch nicht umgestellten Wochen ab), mit Begründung.
**Flaky Tests** (einzeln grün, im Volllauf/unter Last rot) werden nicht toleriert oder wiederholt, sondern mit
`test.skip`/`describe.skip` und einem Kommentar zum Grund abgeschaltet.

**Sub-Agenten:** Das Prompt-Briefing muss diese Regel enthalten. Sie fixen, was in ihren eigenen
Dateien liegt, und melden alles andere unter **"Auffälligkeiten (nicht behoben)"** mit Datei, Grund und
Lösungsvorschlag — die aufrufende Session überträgt das in `todo.md` bzw. behebt es selbst. Sie ändern
keine geteilten Dateien (`todo.md`, `HANDOFF.md`, `src/`, `tests/`) selbst.

## Gespeicherter Fortschritt: ein Deploy darf nichts brechen

Fortschritt liegt als JSON-Blob in der Account-Datenbank (`progress.payload`) und im Browser
(localStorage). Er hängt an **Namen und Positionen**, nicht an Texten:

- Content-Ordnername + Lektions-`id` (`completedLessonIds`), Kurs-`id` in `public/kurse.json`
- Wochen-Check: Wochennummer, Fragen-`id`, **Position** der Coding-Aufgabe (`codingPassed[0]`, `[1]`)
- Storage-Keys (`ue-hacker-…`) und `version` in den gespeicherten Daten
- DB-Schema in `api/src/db.js` (`CREATE TABLE IF NOT EXISTS` ändert bestehende Tabellen **nicht**)

Erlaubt ohne Weiteres: Texte, Aufgaben, `expected`, Vorlagen und Lösungen ändern; neue Kurse,
Lektionen, Fragen, Tabellen ergänzen. **Nicht** ohne Migration: Ordner/IDs umbenennen oder löschen,
Lektionen oder Coding-Aufgaben umsortieren/entfernen, Storage-Key oder `version` ändern, eine Spalte
nur ins `CREATE TABLE` schreiben (stattdessen zusätzlich `ALTER TABLE … ADD COLUMN …` in `db.js`).

`tests/progress-contract.spec.js` (Teil von `test:checks`, läuft bei jeder Content-/Storage-/DB-
Änderung im Pre-commit) vergleicht den aktuellen Stand mit dem eingefrorenen in
`tests/fixtures/progress-contract.json`. Schlägt er an: Änderung zurücknehmen **oder** Migration für
bestehende Daten bauen, dann bewusst neu einfrieren mit `npm run contract:update` und die Fixture
mitcommitten. Neue Kurse/Lektionen ebenfalls per `contract:update` aufnehmen, sonst sind sie nicht
geschützt.

## Bei Inhaltsänderungen: Zusammenhänge prüfen

Wann immer du Inhalte änderst (Notebooks, Markdown-Lektionen, JSON-Manifeste), **prüfe immer `INHALTE.md` Abschnitt 6** — dort steht, welche Dateien gleichzeitig angepasst werden müssen.

Kurzübersicht der wichtigsten Kopplungen:
- **Notebook ändern** → DE- und EN-Version synchron halten (`python-12-wochen-grundkurs` ↔ `python-12-wochen-grundkurs-en`)
- **Interaktive Lektion ändern** → alle drei Ordner prüfen (`python-grundlagen-interaktiv`, `-kinder`, `-jugendliche`) — oder bewusst nur eine Variante ändern und das begründen
- **Missionen/Punkte ändern** → `rewards-manifest.json` und `rewards-manifest-en.json`
- **Kursmetadaten ändern** → `public/kurse.json` (inkl. `title_en`, `description_en`) und ggf. `beschreibung.md` in beiden Sprachordnern

## Nach jeder Änderung committen

**Nach jeder abgeschlossenen Änderung sofort einen Commit anlegen** — nicht Änderungen sammeln und
am Ende der Session in einem Riesen-Commit bündeln. Eine "Änderung" ist eine in sich stimmige
Einheit (ein Bugfix, ein Feature-Schritt, eine Content-Korrektur, eine Doku-Umstrukturierung).

- Ein Commit pro Einheit, mit aussagekräftiger Nachricht; nur die dazugehörigen Dateien stagen
  (keine fremden, uncommitteten Änderungen mitnehmen).
- Das gilt auch für Sub-Agenten-Ergebnisse und für Claude Code: nicht auf eine Aufforderung warten.
- Pushen und Mergen nach `main` bleibt davon getrennt (erst wenn das Thema fertig/getestet ist).

## Nach JEDEM Commit: Doku aktualisieren UND aufräumen

**Pflicht bei jedem einzelnen Commit, ohne explizite Aufforderung.** Automatisch in jede Session
geladen wird nur `CLAUDE.md` (ohne `@`-Imports) — dort steht ausschließlich, was in **jeder**
Session gebraucht wird (Richtwert < 8 KB; Test-/Sicherungsregeln bleiben dort bewusst vollständig). Alles andere (`HANDOFF.md`, `todo.md`, `WORKFLOW.md`,
`VISION.md`, `INHALTE.md`, `KURSPLAN.md`, `PROJEKTIDEEN.md`, `docs/archiv/`) wird nur bei Bedarf
gelesen. Die Commit-Historie (`git log`/`git show`) ist die verlässliche Quelle für Details.

Nach jedem `git commit`:

1. **Aktualisieren:** `todo.md` (erledigte Punkte raus, neue offene rein) und `HANDOFF.md`
   (Stand, Tabelle in Abschnitt 3, neue "Gelernte Regel").
2. **Aufräumen, nicht nur ergänzen:** Erledigtes, Doppeltes, Veraltetes sofort entfernen. Auch
   kalte Dateien kosten Tokens, sobald sie gelesen werden — Richtwert `HANDOFF.md` < 25 KB,
   `todo.md` < 10 KB.
   - Während der Arbeit an einem Branch darf der Feature-Abschnitt ausführlich in `HANDOFF.md`
     Abschnitt 3 stehen (als `### 3.NN`).
   - Nach dem Merge nach `main`: den Abschnitt unverändert ans Ende von
     `docs/archiv/HANDOFF-historie.md` verschieben, in `HANDOFF.md` bleibt eine Tabellenzeile plus
     ggf. eine "Gelernte Regel". Erledigte `todo.md`-Blöcke nach `docs/archiv/todo-erledigt.md`.
3. **`CLAUDE.md` nur anfassen, wenn sich eine Regel oder Grundtatsache ändert** — nie als
   Änderungsprotokoll nutzen, keine `@`-Imports wieder einführen.
4. Die aktualisierten Dateien **mit in denselben Commit** aufnehmen — außer das Aufräumen ist die
   einzige Änderung, dann ein eigener Commit.
