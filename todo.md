# Todo

## Jetzt: 10 Verbesserungen in 6 Branches (gruppiert, B→A→E→F→C→D)

Plan-Datei: `~/.claude/plans/scalable-singing-cook.md` (Kontext/Details je Branch).

### Branch `debug-notebook-safety` (Punkte 5, 6) — eigener Branch, fertig (inkl. nachgereichter
      Tests für Endlosschleifen-Schutz + Debug-Ziele, siehe unten "Testlücke geschlossen")
### Branch `et-fixes` (Punkte 1-4) — eigener Branch, fertig (inkl. nachgereichter Tests für
      "weiß nicht"-Option + Scoring-Schwelle, siehe unten)
### Branch `kontakt-email` (Punkt 9) — zurückgestellt, braucht E-Mail-Adresse vom Nutzer
### Branch `kurs-caesar-chiffre` (Punkt 10) — eigener Branch, fertig (hatte von Anfang an Tests)
### Branch `interaktiv-klarer` (Punkt 7) — eigener Branch, fertig (hatte von Anfang an einen Test)

### Testlücke geschlossen (nachträglich, auf Nutzer-Nachfrage)
- [x] Geprüft, ob alle Änderungen Tests haben: `debug-notebook-safety` (Endlosschleifen-Schutz,
      Debug-Ziele) und `et-fixes` ("weiß nicht"-Option, Scoring-Schwelle) hatten nur manuelle
      Playwright-Verifizierung, keine dauerhaften Tests — auf den jeweiligen Branches nachgereicht
- [x] `WORKFLOW.md` um Abschnitt "Tests für jede Verhaltensänderung" ergänzt, damit das nicht
      wieder passiert (manuelle Verifizierung reicht nicht, jede Verhaltensänderung braucht einen
      Test in `tests/*.spec.js`)

### Branch `text-typo-pass` (Punkt 8) — dieser Branch, Phase 1 von mehreren
- [x] `cspell` als Tooling eingerichtet (`cspell.json`, `npm run lint:spelling`) mit deutschem und
      englischem Wörterbuch (`@cspell/dict-de-de`, `@cspell/dict-en_us`) — dauerhaft nutzbar für
      künftige Content-Reviews
- [x] `src/locales/de.js` + `src/locales/en.js` geprüft: **keine echten Tippfehler gefunden**,
      Texte waren bereits sauber. Ein paar False Positives ins Custom-Dictionary aufgenommen
      (Identifier wie `jupyter`/`scifi`/`appt` in Locale-Keys, sowie bewusst britisches Englisch
      "Initialise"/"practising", konsistent im EN-Text verwendet — keine Inkonsistenz, kein Fix nötig)
- [x] Stichprobe über `.vue`-Komponenten (`src/components/*.vue`, `src/views/*.vue`): dort steckt
      viel Prosa NICHT in `locales/*.js`, sondern direkt als `lang === 'en' ? ... : ...`-Ternary im
      Template. Ergebnis: **ebenfalls keine echten Tippfehler**, aber ~84 False Positives
      (Routen-Segmente wie `kurs`/`woche`/`lektion`, CSS-Klassen, Variablennamen) — cspell kann
      `.vue`-Dateien nicht sauber genug von Code trennen, ohne weitere Konfiguration. Deshalb nicht
      systematisch in `cspell.json` aufgenommen (würde zu viele echte Treffer mit-verstecken).
### Branch `text-typo-pass` — Phase 2 (Wochenbeschreibungen, Einstufung, Notebooks Abenteuer)
- [x] `content/*/beschreibung.md` (alle 11 Dateien) geprüft: **keine Tippfehler gefunden**
- [x] `content/python-checks/weeks.json` geprüft: 38 Treffer, **alle False Positives** (Python-
      Schlüsselwörter/Funktionsnamen in Code-Beispielen wie `elif`/`randint`/`isinstance`, sowie
      Code-Identifier in Beispiel-Strings wie `mein_geheim_modul_xyz`/`datei.txt`) — **keine echten
      Tippfehler**, alle ins Custom-Dictionary aufgenommen
- [x] Neues Skript `scripts/extract_notebook_text.py`: zieht Markdown-Zellen aus `.ipynb`-Dateien in
      `.md`-Dateien, damit `cspell` sie prüfen kann (Code-Zellen bewusst ausgeklammert — sonst zu
      viele Identifier-False-Positives). **Wichtig:** Ausgabeordner muss innerhalb des Repos liegen
      (`cspell` erkennt Pfade außerhalb des Projekt-Roots nicht, `/tmp` funktioniert nicht)
- [x] Abenteuer-Variante komplett geprüft (12 Wochen × 6 Typen × DE+EN = 144 Notebooks, ~150
      einzigartige Kandidatenwörter manuell geprüft): **keine echten Tippfehler** — fast alles Fantasy-Eigennamen/
      -Komposita (Pyralia, Runenschmiede, Tresorwächter, …), Python-Identifier in Code-Beispielen,
      oder korrekte aber seltene deutsche Flexionsformen (z.B. "lesbarere", "primen" — beide
      grammatisch korrekt, einzeln nachgeprüft). Alle False Positives ins Custom-Dictionary
      übernommen (jetzt 159 Wörter in `cspell.json`).
- [x] **Ein echter Fund:** `week12_adventure_1_lektion.ipynb` (EN) nutzte an 4 Stellen amerikanisches
      Englisch ("colors", "colorful") statt des sonst im ganzen EN-Kurs konsequent verwendeten
      britischen Englisch ("colours", "practise", "organised", …) — korrigiert. Method-Referenzen
      wie `.color()`/`.fillcolor()` (Turtle-API, tatsächlich so benannt) bewusst unverändert gelassen.
### Branch `text-typo-pass` — Phase 2 Fortsetzung: Pferde + Sci-Fi (alle 444 Notebooks jetzt geprüft)
- [x] Pferde-Variante komplett geprüft (144 Notebooks DE+EN): **4 echte Tippfehler gefunden und
      korrigiert:**
      - "Parours" → "Parcours" (Woche 11, Missionen)
      - "pferdbezogene" → "pferdebezogene" (Woche 2, Lektion — fehlendes Fugen-e)
      - "Pferdname" → "Pferdename" (Woche 1, Glossar — inkonsistent zu 4 anderen Stellen im
        selben Notebook-Satz, die korrekt "Pferdename(n)" schreiben)
      - "Futterschip" → "Futterschippe" (Woche 3, Missionen **und** `rewards-manifest.json`) —
        aufgelöst über den EN-Manifest-Eintrag "Feed Scoop": kein Sci-Fi-Chip-Wortspiel, sondern
        ein abgeschnittenes "Futterschippe" (Schippe = Scoop). Bewusst NICHT angefasst: "zuviel"
        (Woche 1, Lösungen) — alte Rechtschreibung, weit verbreitet, kein klarer Fehler.
- [x] Sci-Fi-Variante komplett geprüft (144 Notebooks DE+EN): **1 echter Tippfehler, doppelt
      vorhanden:** "Du betrittstest die hochmoderne Raumstation Nebula-7" → "Du betrittst die..."
      in Woche 1 UND Woche 10 (identischer Intro-Text in beiden Lektionen dupliziert). Bewusst
      NICHT angefasst: "statu" in Woche 1 Lösungen — das ist absichtlich der im Debug-Notebook
      erklärte Tippfehler selbst (`status` vs. `statu`), kein echter Fehler zum Fixen.
- [x] Alle 11 Cheat-Sheets (DE, `.md`-Quelle + generierte `.ipynb`) + 11 EN-Cheat-Sheets +
      `turtle_cheat_sheet.md` (DE+EN) + `gesamtglossar.ipynb` geprüft: **keine Tippfehler**, nur
      Turtle-API-Methodennamen (`setheading`, `pencolor`, …) als False Positives.
- **Ergebnis: alle 444 Notebooks des 12-Wochen-Kurses + alle Cheat-Sheets/Glossare jetzt einmal
  komplett auf Tippfehler geprüft.** `cspell.json` enthält jetzt 344 projektspezifische Wörter.
- **Offen für weitere Sessions:**
  - [ ] `.vue`-Dateien sauber prüfbar machen (z.B. gezielte Marker/Konvention für Prosa-Strings,
        oder Ternary-Texte in `locales/*.js` überführen) — dann echte Prosa-Tippfehler dort finden
  - [ ] Interaktive Kurse (`python-grundlagen-interaktiv*`, 5 Ordner) und `caesar-chiffre`
        (Branch `kurs-caesar-chiffre`) noch nicht mit cspell geprüft

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
