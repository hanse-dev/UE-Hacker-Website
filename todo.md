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

### Später: Admin-Login (neuer Branch `cursor/admin-login`)

- [x] Neuer Branch von `main` — Plan: [`ACCOUNT-SYNC-PLAN.md`](ACCOUNT-SYNC-PLAN.md)
  - [x] Phase 1: kleine API + Admin (User anlegen)
  - [x] Phase 2: Login + Progress-Sync
  - [x] Phase 3: Notebook-Sync
  - [x] API liefert Static (`dist/`), ein Port / ein Docker-Container `app`
  - **Nicht:** E-Mail-Registrierung / Supabase / öffentliche Sign-up
- [ ] Manuell testen + ggf. committen/PR
