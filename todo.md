# Todo

Erledigtes (frühere Abschnitte "Now" + "Fertige Branches") steht kalt in `docs/archiv/todo-erledigt.md` —
nicht per `@` geladen, nur bei Bedarf lesen. Hier stehen nur **offene** Punkte und die nächsten Themen.

## Offen

- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken) —
      **zurückgestellt** (Nutzer will erst später deployen). Backup-Cron auf dem Server einrichten
      (Befehl siehe HANDOFF.md Abschnitt 4); externe Sicherung der Backups bewusst nicht mitgebaut.
- [ ] Tippfehler-Pass (`cspell`): `.vue`-Prosa (Ternary-/`t()`-Texte) und Interaktiv-/Projekt-Kurse noch
      nicht geprüft.
- [ ] Weitere Sprache neben DE/EN? Noch keine Entscheidung, kein Ziel. UI-Texte laufen bereits über
      `t()` (`locales/de.js`/`en.js`); offen bliebe nur der Content: `_en`-Feld-Suffix in
      `content/python-checks/week-{N}.json`, `-en`-Ordner-Suffix in `useCourseData.js`. Größter
      Aufwand wäre der Content selbst (444 Notebooks × Sprache). Keine neue i18n-Library nötig.
- [ ] `kurs-python-spiele` — Idee verworfen zugunsten von `kurs-js-spielewerkstatt`: Pyodides
      synchrones Ausführungsmodell ist mit einer echten Spiele-Loop unvereinbar (Archiv HANDOFF 3.32).

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2 → 3. Nicht mischen. (Branch-Namen ohne `cursor/`-Präfix.)
Gesamt-Roadmap/Track-Modell (welche Sprache/welches Thema baut auf was auf) siehe `VISION.md`.

### 1. JavaScript-Spielewerkstatt — Branch `kurs-js-spielewerkstatt` ✅ gemergt
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
- [ ] `KURSPLAN.md`/`VISION.md` bei Bedarf nachziehen — bisher keine Abweichung vom dortigen
      Track-Modell nötig (JS-Projekt-Kurs passt unverändert ins bestehende Schema)

### 2. Was kommt danach? Python-Projekt-Sprints — Branch `kurs-python-projekte`
Die Infrastruktur dafür existiert bereits (Branch `kurs-projekte-uebersicht`, s.u.): generalisiertes
`ProjectCourse.vue`, Projekte-Übersicht mit Filtern unter `/projekte`. Ein weiteres Projekt braucht
nur noch einen Content-Ordner + `kurse.json`-Eintrag (siehe `INHALTE.md` §6), keine neue Komponente.
- [ ] 2–3 weitere Projekt-Ideen ausarbeiten (Sprints im Cäsar-Chiffre-Stil, ~5 Lektionen) —
      Ideen-Backlog mit ~40 Vorschlägen (Spiele, Web, KI, Logik, Krypto, Kreativ, Daten) samt
      Reihenfolge-Empfehlung in `PROJEKTIDEEN.md`; beim Umsetzen dort abhaken
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 3. KI-Labor — Branch `kurs-ki-labor`
Baut auf dem Python-Track auf (12-Wochen-Grundkurs), siehe `VISION.md`/`KURSPLAN.md` Kurs 4
"KI-Grundlagen". Breitere Zielgruppe, Fokus auf Prompts/Grenzen/Schul-Nutzen.
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Drittes Thema erst starten, wenn 1 und 2 gemerged sind (oder bewusst parallel nur
wenn Kapazität klar ist).
