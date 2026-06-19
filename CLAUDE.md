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

> **Zuletzt aktualisiert:** 2026-06-19
> **Letzter Commit:** feat: translate Week 11 notebooks to English (Phase 6, Session 11/12)

**Was zuletzt gemacht wurde:**
- Woche 11 – alle 18 EN-Notebooks erstellt (adventure, horses, scifi je 6), per parallele Agenten
- Dateien: `content/python-12-wochen-grundkurs-en/woche-11/{adventure,horses,scifi}/week11_*.ipynb`
- Thema Woche 11: OOP Fortgeschritten (Vererbung, Polymorphismus, Magic Methods: __str__, __repr__, __add__, __len__, __eq__)
- Adventure: Master Guilds of Pyralia / LivingBeing→Human→Warrior/Mage, GuildSystem, Polymorphic Arsenal – XP rewards
- Horses: Sonnental Stud Farm / RidingHorse→Thoroughbred/Coldblood, Polymorphic Training, Champion Register – Hoof Points rewards
- Scifi: Nebula-7 / Robot→Android→CombatRobot/MedicalRobot, Polymorphic Weapon System, Spaceship Registry – Cyber Credits rewards

**Bekannte offene Baustellen:**
- Language-Toggle Phase 6: Noch 18 Notebooks (Woche 12 – letzte Session)
- Nächste Session: Woche 12 (adventure, horses, scifi – Abschlussprojekt / Finale)

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
