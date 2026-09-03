# Todo

## Jetzt: vom Nutzer priorisierte Reihenfolge (Deploy bewusst zurückgestellt)

1. [x] **SQLite-Backup-Script** (Branch `backup-sqlite-db`, dieser Branch) — `api/src/scripts/backup-db.js`
       zieht per `VACUUM INTO` eine konsistente Kopie (sicher auch im WAL-Modus/laufenden Betrieb),
       Retention behält die letzten `BACKUP_KEEP` (Default 14) Backups. `npm run backup:db` lokal,
       `docker compose exec app node src/scripts/backup-db.js` in Prod — Cron-Beispiel in
       `HANDOFF.md` Abschnitt 4. Getestet mit `node --test` (4 Tests: Backup-Inhalt, fehlende
       Quelle, Retention, Ignorieren fremder Dateien im Backup-Ordner) + End-to-End-Smoketest der
       CLI mit echten Env-Vars. **Nicht abgedeckt:** externe Sicherung der Backups selbst
       (Server-Ausfall) — hängt von der jeweiligen Infrastruktur ab, bewusst nicht mitgebaut.
2. [ ] **Text-Tippfehler-Pass Phase 2+** (Branch `text-typo-pass` fortsetzen) — `.vue`-Dateien
       systematisch prüfbar machen, dann `content/*/beschreibung.md` + `weeks.json`, dann die 444
       Notebooks (siehe Details weiter unten im bestehenden Abschnitt)
3. [ ] **Neue Kurse**, in dieser Reihenfolge (je eigener Branch, kein `cursor/`-Präfix mehr):
       - `kurs-python-spiele` — Python Spiele-Werkstatt (Turtle/Textspiele)
       - `kurs-python-projekte` — „Was kommt danach?“ Projekt-Sprints
       - `kurs-js-minigames` *oder* `kurs-ki-labor` — Entscheidung beim Start
4. [ ] **Danach erst:** die 6 bereits fertigen Branches (`debug-notebook-safety`, `et-fixes`,
       `kurs-caesar-chiffre`, `interaktiv-klarer`, `text-typo-pass`, `backup-sqlite-db`) mergen und
       Server-Deploy verifizieren; `kontakt-email` fehlt noch die E-Mail-Adresse vom Nutzer

---

## Now
### Website / Frontend
- [x] Das Tabsystem erklären
- [x] "Wie ist der Kurs aufgebaut?" mit den Belohnungen ergänzen
- [x] MissionenPanel: Punkte-Stand nach Browser-Reload prüfen (localStorage?)
- [x] Belohnungen zuklappen
- [x] Woche 1 zuklappen
- [x] Language-Toggle: Phase 4–6 (EN Content, rewards, Notebooks)

### Inhalte / Notebooks
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

### Infrastruktur
- [x] Einstufung / Checks in `main` (PR #1)
- [x] Admin-Login / Progress-Sync in `main` (PR #2)
- [x] Notebook-Sync-Loop-Fix in `main` (PR #3)
- [ ] Docker-Deployment auf Server final verifizieren (`app`, Orphans, `.env`, kein Notebook-Blinken)
      — **zurückgestellt**, siehe "Jetzt"-Abschnitt oben (Nutzer will erst später deployen)

---

## Nächste Themen (je eigener Branch von `main`)

Reihenfolge empfohlen: 1 → 2 → 3. Nicht mischen.

### 1. Python Spiele-Werkstatt — Branch `kurs-python-spiele`
- [ ] Kursmetadaten in `kurse.json` (+ EN)
- [ ] Content-Struktur (Wochen/Tabs analog bestehender Kurse oder Kurzformat)
- [ ] Turtle-/Textspiele, Level-Ideen, Belohnungen falls passend
- [ ] DE + EN (oder bewusst DE-first, EN nachziehen)
- [ ] Smoke-Test / manuell prüfen → PR nach `main`

### 2. Was kommt danach? Projekt-Sprints — Branch `kurs-python-projekte`
- [ ] 2–3 feste Projekt-Sprints (je ~2 Wochen Umfang skizzieren)
- [ ] Kursseite + Einstieg von 12-Wochen-Kurs verlinken („Weiter so“)
- [ ] Projektideen aus Einstufung ggf. hier ausbauen
- [ ] DE (+ EN nach Bedarf)
- [ ] Smoke-Test → PR nach `main`

### 3. JS Mini-Games (Teens) **oder** KI-Labor — Branch wählen:
- **A)** `kurs-js-minigames` — Browser-Spiele, Canvas/p5, Zielgruppe 13–17
- **B)** `kurs-ki-labor` — Prompts, Grenzen, Schul-Nutzen (breitere Zielgruppe)
- [ ] Entscheidung A vs B (oder beide nacheinander, je ein Branch)
- [ ] Kursmetadaten + Content
- [ ] Smoke-Test → PR nach `main`

**Hinweis:** Drittes Thema erst starten, wenn 1 und 2 gemerged sind (oder bewusst parallel nur wenn Kapazität klar ist). Default: erst Spiele-Werkstatt, dann Projekt-Sprints, dann A oder B.
