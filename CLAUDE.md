# CLAUDE.md — Projektkontext & Session-Handoff

Diese Datei wird automatisch von Claude Code beim Start jeder Session gelesen.
**Aktualisiere den Handoff-Abschnitt am Ende jeder Session und pushe danach.**

---

## Projekt: UE Hacker Website

Lernplattform für Kinder/Jugendliche (Python-Programmierung).
Vue 3 + Vite Frontend, Docker-Deployment (dev: Port 5173, prod: Nginx Port 8080).

### Tech Stack
- **Frontend:** Vue 3, Vue Router, CSS (kein Tailwind)
- **Inhalte:** Jupyter Notebooks (`.ipynb`) im `content/`-Ordner
- **Deployment:** Docker Compose — `docker-compose up dev` / `docker-compose up -d --build prod`

### Projektstruktur
```
src/
  components/    Vue-Komponenten
  views/         Seiten-Views (Router-Targets)
  router/        Vue Router Konfiguration
  composables/   Composition API Utilities
content/
  python-12-wochen-grundkurs/
    woche-{1-12}/
      scifi/     7 Notebooks pro Thema (0_glossar bis 6_boss)
      pferde/
      abenteuer/
```

### Notebook-Struktur (pro Woche/Thema — 6 Dateien)
`0_glossar` → `1_lektion` → `2_debug` → `3_missionen` → `5_boss` → `6_loesungen`

### Kurs-Themen
- **Sci-Fi:** Cyber Credits, Daten-Chip, Crew-Meister-Urkunde
- **Pferde:** Huf-Punkte, Stall-Schlüssel, Reitmeister-Urkunde
- **Abenteuer:** XP, Magischer Beutel, Gilde-Meister-Urkunde

---

## Aktiver Branch & Offene Aufgaben

**Branch:** `splitting`
**Gegenüber `main`:** Neue Content-Struktur mit aufgeteilten Notebooks (7 Dateien/Woche statt monolithisch), KURSPLAN.md, Website-Routing für Kurs-Übersicht.

### Nächste Schritte / Offene Punkte

@todo.md

---

## Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-06-18
> **Letzter Commit:** `7141bd7` — docs: update CLAUDE.md with post-commit todo check rule

**Was diese Session gemacht wurde:**
- Debug-Notebooks repariert: 9 Code-Zellen hatten keine echten Bugs (woche-4 for-Schleife ohne Doppelpunkt, woche-5 fehlender Print für Funktionsobjekt-Bug, woche-10 fehlender `__init__`-Parameter)
- Alle 36 Reflexion-Notebooks gelöscht + Reflexion-Tab aus dem Frontend entfernt
- Reihenfolge Boss-Quest ↔ Lösungen getauscht (Dateien umbenannt: `5_boss`, `6_loesungen`; Frontend-Keys angepasst)
- Alle 36 Lösungsnotebooks mit echten Lösungen befüllt: Missions-Lösungen (kein Platzhalter mehr) + neuer Boss-Quest-Lösungsabschnitt
- Playwright-Tests laufen durch (11/11) nach allen Änderungen

**Notebook-Struktur jetzt:** 6 Dateien pro Woche/Thema:
`0_glossar` → `1_lektion` → `2_debug` → `3_missionen` → `5_boss` → `6_loesungen`

**Bekannte offene Baustellen:**
- Website/Frontend: Tab-System erklären, Belohnungen in Kursaufbau, localStorage für Punkte-Stand, Verlinkung testen, Belohnungen/Woche-1 zuklappen
- Inhalte: Woche 9-12 Debug-Notebooks auf Verständlichkeit prüfen, Glossar-Notebooks auf Anfänger-Tauglichkeit prüfen

**Workflow:**
1. `docker-compose up dev` starten
2. Weiter an `splitting` Branch arbeiten
3. Am Ende: `git add`, `git commit`, `git push` — dann steht alles auf dem anderen Rechner bereit

---

## Nach jedem Commit

Nach jedem `git commit` prüfen:
- Welche Aufgaben aus `todo.md` wurden durch diesen Commit erledigt?
- Diese Einträge in `todo.md` von `[ ]` auf `[x]` setzen und unter `## Done` verschieben.
- `todo.md` dann mit in den nächsten Commit aufnehmen, oder direkt committen.

---

## Hinweis: Handoff aktualisieren

Am Ende einer produktiven Session kannst du Claude bitten:
> "Aktualisiere den Handoff-Abschnitt in der CLAUDE.md"

Claude fasst dann zusammen was gemacht wurde und was als nächstes ansteht.
