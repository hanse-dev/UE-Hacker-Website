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
  python-12-wochen-grundkurs/        ← DE Notebooks
    woche-{1-12}/
      abenteuer/ pferde/ scifi/      ← je 6 .ipynb pro Variante
  python-12-wochen-grundkurs-en/     ← EN Notebooks (gleiche Struktur)
    woche-{1-12}/
      adventure/ horses/ scifi/
  python-grundlagen-interaktiv-kinder/      ← Interaktiv, 8–12 Jahre
  python-grundlagen-interaktiv-jugendliche/ ← Interaktiv, 13–17 Jahre
public/
  kurse.json                         ← Kursmetadaten (title, title_en, …)
  rewards-manifest.json              ← Belohnungen DE
  rewards-manifest-en.json           ← Belohnungen EN
```

> Vollständige Dateistruktur und Zusammenhänge zwischen Sprachen/Varianten: @INHALTE.md

### Notebook-Struktur (pro Woche/Thema — 6 Dateien)
`0_glossar` → `1_lektion` → `2_debug` → `3_missionen` → `5_boss` → `6_loesungen`

### Kurs-Themen
- **Sci-Fi:** Cyber Credits, Daten-Chip, Crew-Meister-Urkunde
- **Pferde:** Huf-Punkte, Stall-Schlüssel, Reitmeister-Urkunde
- **Abenteuer:** XP, Magischer Beutel, Gilde-Meister-Urkunde

---

## Aktiver Branch & Offene Aufgaben

**Branch:** `main`

### Nächste Schritte / Offene Punkte

@todo.md

---

## Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-06-23
> **Letzter Commit:** `5c23de9` — feat: merge language-toggle branch — full DE/EN toggle

**Was zuletzt gemacht wurde:**
- `language-toggle` Branch vollständig in `main` gemergt (alle 6 Phasen)
- Interaktiven Einführungskurs (`python-grundlagen-interaktiv`) in 2 Varianten aufgeteilt:
  - `content/python-grundlagen-interaktiv-kinder/` — Zielgruppe 8–12 Jahre (Tier-/Spielbeispiele, Code-Templates, 2 Aufgaben/Lektion)
  - `content/python-grundlagen-interaktiv-jugendliche/` — Zielgruppe 13–17 Jahre (App-/Alltag-Beispiele, leere Templates, 3 Aufgaben mit Bonus)
- `InteractiveCourse.vue` komplett neu: Variantenauswahl-Screen, dynamisches Laden per `import.meta.glob`, Mobile-Layout mit Toggle-Button
- `LessonView.vue`: `variant`-Prop, dynamische Glossar-/Lesson-Loader, Bonus-Badge
- `useInteractiveProgress.js`: Per-Variante State-Map mit eigenem localStorage-Slot
- Mobile-Bugs behoben: Sidebar-Overlay-Fix (CSS-Kaskade), Grid-Row-Sizing, Code-Textarea overflow
- `INHALTE.md` neu erstellt: Referenzdokument für alle Inhaltsdateien und ihre Zusammenhänge

**Bekannte offene Baustellen:**
- Docker prod-Build noch nicht getestet
- README.md noch nicht aktualisiert
- Notebook-Download-ZIP ist nur DE (kein EN-Zip)
- EN-Titeln für Wochen 5–12 in `INHALTE.md` noch mit Platzhaltern (aus Notebooks nachlesen)

**Workflow:**
1. `./node_modules/.bin/vite --port 5173` starten (kein Docker auf diesem Rechner)
2. Weiter auf `main` arbeiten
3. Am Ende: `git add`, `git commit`, `git push`

---

## Bei Inhaltsänderungen: Zusammenhänge prüfen

Wann immer du Inhalte änderst (Notebooks, Markdown-Lektionen, JSON-Manifeste), **prüfe immer `INHALTE.md` Abschnitt 6** — dort steht, welche Dateien gleichzeitig angepasst werden müssen.

Kurzübersicht der wichtigsten Kopplungen:
- **Notebook ändern** → DE- und EN-Version synchron halten (`python-12-wochen-grundkurs` ↔ `python-12-wochen-grundkurs-en`)
- **Interaktive Lektion ändern** → alle drei Ordner prüfen (`python-grundlagen-interaktiv`, `-kinder`, `-jugendliche`) — oder bewusst nur eine Variante ändern und das begründen
- **Missionen/Punkte ändern** → `rewards-manifest.json` und `rewards-manifest-en.json`
- **Kursmetadaten ändern** → `public/kurse.json` (inkl. `title_en`, `description_en`) und ggf. `beschreibung.md` in beiden Sprachordnern

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
