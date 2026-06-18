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

**Branch:** `language-toggle`
**Gegenüber `main`:** Language-Toggle-Feature (DE/EN Umschalter in der App).

### Nächste Schritte / Offene Punkte

@todo.md

---

## Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-06-18
> **Letzter Commit:** feat: translate Week 7 notebooks to English (Phase 6, Session 7/12)

**Was zuletzt gemacht wurde:**
- Woche 7 – alle 18 EN-Notebooks erstellt (adventure, horses, scifi je 6), parallel via 3 Agenten
- Dateien: `content/python-12-wochen-grundkurs-en/woche-7/{adventure,horses,scifi}/week7_*.ipynb`
- Thema Woche 7: Module und Bibliotheken (import, from, math, random, Aliasse mit as)
- Adventure: Pyralia magic library / Dice Tower / Magic Oracle / Random Dungeon, XP rewards
- Horses: Sunny Valley Ranch / obstacle names translated, Hoof Points rewards
- Scifi: Nebula-7 / coordinates/distance/sector themes, Cyber Credits rewards

**Bekannte offene Baustellen:**
- Language-Toggle Phase 6: Noch 90 Notebooks (Wochen 8–12, je ~18 pro Session)
- Nächste Session: Woche 8 (adventure, horses, scifi – 3 parallele Agenten)

**Workflow:**
1. `docker-compose up dev` starten
2. Weiter an `language-toggle` Branch arbeiten
3. Am Ende: `git add`, `git commit`, `git push` — dann steht alles auf dem anderen Rechner bereit

---

## Nach jedem Commit

Nach jedem `git commit` prüfen:
- Welche Aufgaben aus `todo.md` wurden durch diesen Commit erledigt?
- Diese Einträge in `todo.md` von `[ ]` auf `[x]` setzen und unter `## Done` verschieben.
- `todo.md` dann mit in den nächsten Commit aufnehmen, oder direkt committen.

---

## Handoff automatisch aktualisieren

**Vor jedem Commit** ohne explizite Aufforderung:
1. Handoff-Abschnitt in dieser Datei aktualisieren (letzter Commit, was wurde gemacht, was ist offen)
2. `todo.md` prüfen und erledigte Punkte markieren
3. `CLAUDE.md` und `todo.md` mit in denselben Commit aufnehmen (kein Extra-Commit)
