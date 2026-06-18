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
> **Letzter Commit:** `b558cfb` — feat: swap Boss-Quest and Lösungen order

**Was zuletzt gemacht wurde:**
- Alle 36 Glossar-Notebooks durchgesehen: anfängerfreundlich und konsistent
- Woche 11 (×3): doppelte Tabellenzeilen für Polymorphismus und Vererbung entfernt
- Woche 10 Pferde: `trainieren()` war ein No-op (`self.rasse = self.rasse`) → durch sinnvollen `fitness`-Counter ersetzt
- Tab-System erklärt: einmalig oben auf der Kursseite als `<h2>Wie ist der Kurs aufgebaut?</h2>` mit 6-Tab-Grid (Icon + Titel + Beschreibung); Tooltip auf jedem Tab-Button

**Bekannte offene Baustellen:**
- Website/Frontend: localStorage für Punkte-Stand, Verlinkung testen, Belohnungen/Woche-1 zuklappen
- Mission Panel Komponente neu, noch nicht vollständig getestet

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

## Handoff automatisch aktualisieren

**Vor jedem Commit** ohne explizite Aufforderung:
1. Handoff-Abschnitt in dieser Datei aktualisieren (letzter Commit, was wurde gemacht, was ist offen)
2. `todo.md` prüfen und erledigte Punkte markieren
3. `CLAUDE.md` und `todo.md` mit in denselben Commit aufnehmen (kein Extra-Commit)
