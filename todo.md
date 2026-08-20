# Todo

## Now
### Website / Frontend
- [x] Das Tabsystem erklären
- [x] "Wie ist der Kurs aufgebaut?" mit den Belohnungen ergänzen
- [x] MissionenPanel: Punkte-Stand nach Browser-Reload prüfen (localStorage?)
- [x] Belohnungen zuklappen
- [x] Woche 1 zuklappen
- [x] Language-Toggle: Phase 4 – Markdown-Content-Dateien auf Englisch übersetzen (26 Dateien)
- [x] Language-Toggle: Phase 5 – rewards-manifest-en.json anlegen
- [x] Language-Toggle: Phase 6 – Notebooks übersetzen (216 Notebooks, ~18 pro Session)


### Inhalte / Notebooks
- [x] Woche 9-12 Debug-Notebooks kurz durchschauen (Aufgaben verständlich?)
- [x] Glossar-Notebooks: Sind alle Begriffe für Anfänger erklärt?
- [x] Branch `splitting` in `main` mergen
- [x] den "python grundlagen interaktiv" kurs in 2 Varianten zu erstellen, 1x kinderfreundlich (in einfacher Sprache), 1x für Jugendliche

### Infrastruktur

- [ ] Docker-Deployment testen (prod-Build auf lokalem Rechner)
- [ ] README.md aktualisieren (neue Struktur erklären)

### Jetzt: Einstufung / Checks (Branch `cursor/python-lernpfad-quiz`)

- [x] Einstufung als eigener Kurs + Check-Tab pro Woche
- [x] Fragen für alle 12 Wochen + Rotation / Multi-Select
- [x] Bei 100%: Projektideen statt Woche-1-Empfehlung
- [x] Deep-Link Einstufung → Kurs lädt Wochen neu
- [x] Playwright-Tests + Pre-commit-Hook
- [x] Alten Lernpfad-Code/Content entfernt
- [ ] Committen und in `main` mergen

### Storytelling-Überarbeitung 12-Wochen-Kurs (Branch `cursor/storytelling-woche7-pilot`)

- [x] Storytelling-Analyse Abenteuer-Variante (alle 12 Wochen) — Befunde siehe unten
- [x] Woche 7 Abenteuer (DE+EN) als Pilot komplett umgebaut: zusammenhängende Szenen statt Schritt-Listen,
      Bibliothekswahl von math-lastig auf random/string/time umgestellt, Debug-Bugs unabhängig vom
      geteilten Kernel-Zustand gemacht, Belohnungstexte an rewards-manifest(.en).json angeglichen
- [x] Pythonia/Pyralia-Namenskonflikt weltweit vereinheitlicht (Woche 1, 10, 12, DE+EN, inkl. Vorlagen
      unter Regeln/)
- [x] Woche 2 Abenteuer (DE+EN) umgebaut: Elementbezug ("Vier magische Elemente") jetzt durchgängig
      eingelöst — Feuer=str, Erde=int, Wasser=float, Luft=bool, "Elementarturm" als Rahmengeschichte
- [x] Woche 3, 4, 5 Abenteuer geprüft: Missionen bereits sinnvolle Szenen mit Zielbezug, Debug-Bugs
      bereits in sich geschlossen — kein Umbau nötig
- [x] Woche 6: Boss-Quest 1+2 Titel/Prämissen ("Zauber-Generator"/"Guilden-Manager") waren wortgleich
      zu Woche 5 kopiert — in DE+EN umbenannt/umthemet ("Schatzkammer-Katalog"/"Tresorwächter")
- [ ] Restliche 6 Wochen Abenteuer (8–12) nach demselben Prinzip überarbeiten/prüfen
- [ ] Pferde- und Sci-Fi-Variante ebenfalls überarbeiten (eigene Metaphern nötig, kein reines Übersetzen)
- [ ] Woche 9: Missionen-Formatierung vereinheitlichen (Nummerierungs-Mischmasch)
- [ ] Woche 10, Boss-Quest 2 ("Zookeeper"): stärker in die Fantasy-Welt einbetten
- [ ] Woche 12, Boss-Quest 5: Textbug "Als Nächstes: Woche – wartet schon!" reparieren (Wochenzahl fehlt)
- [ ] "Gilde-Meister-Urkunde" als Zwischenbelohnung (W6/7/8) vs. Kursabschluss-Titel prüfen — evtl. umbenennen

### Später: Admin-Login (neuer Branch `cursor/admin-login`)

- [x] Neuer Branch von `main` — Plan: [`ACCOUNT-SYNC-PLAN.md`](ACCOUNT-SYNC-PLAN.md)
  - [x] Phase 1: kleine API + Admin (User anlegen)
  - [x] Phase 2: Login + Progress-Sync
  - [x] Phase 3: Notebook-Sync
  - [x] API liefert Static (`dist/`), ein Port / ein Docker-Container `app`
  - **Nicht:** E-Mail-Registrierung / Supabase / öffentliche Sign-up
- [ ] Manuell testen + ggf. committen/PR
