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

### Notebook-Struktur (pro Woche/Thema — 7 Dateien)
`0_glossar` → `1_lektion` → `2_debug` → `3_missionen` → `4_reflexion` → `5_loesungen` → `6_boss`

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

> **Zuletzt aktualisiert:** 2026-06-17
> **Letzter Commit:** `ab99f92` — feat: add teaser view and routing, implement mission panel component

**Was gerade läuft:**
Branch `splitting` baut eine neue Website-Struktur mit Kurs-Übersicht, Teaser-View und Mission-Panel-Komponente. Die Notebook-Inhalte sind vollständig (alle 12 Wochen × 3 Themen × 7 Notebooks = 252 Dateien).

**Bekannte offene Baustellen:**
- Debug Quests noch nicht überprüft
- Mission Panel Komponente neu, noch nicht vollständig getestet

**Workflow:**
1. `docker-compose up dev` starten
2. Weiter an `splitting` Branch arbeiten
3. Am Ende: `git add`, `git commit`, `git push` — dann steht alles auf dem anderen Rechner bereit

---

## Hinweis: Handoff aktualisieren

Am Ende einer produktiven Session kannst du Claude bitten:
> "Aktualisiere den Handoff-Abschnitt in der CLAUDE.md"

Claude fasst dann zusammen was gemacht wurde und was als nächstes ansteht.
