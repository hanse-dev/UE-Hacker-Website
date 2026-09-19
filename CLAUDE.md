# CLAUDE.md — Projektkontext & Session-Handoff

Diese Datei wird automatisch von Claude Code beim Start jeder Session gelesen.

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

### Notebook-Struktur (pro Woche/Thema — 6 Ordner)
`0_glossar` → `1_lektion` → `2_debug` → `3_missionen` → `5_boss` → `6_loesungen`

Seit der Zellen-Format-Umstellung ist jedes Notebook ein Ordner mit einer `.py`-Datei pro Zelle
(`NN_markdown.py`/`NN_code.py`), kein `.ipynb` mehr. Details: `INHALTE.md` Abschnitt 2.

### Kurs-Themen
- **Sci-Fi:** Cyber Credits, Daten-Chip, Crew-Meister-Urkunde
- **Pferde:** Huf-Punkte, Stall-Schlüssel, Reitmeister-Urkunde
- **Abenteuer:** XP, Magischer Beutel, Gilde-Meister-Urkunde

---

## Vision & Gesamt-Roadmap

@VISION.md

---

## Offene Aufgaben

@todo.md

---

## Bei Bedarf lesen (nicht automatisch geladen — hält den Start-Kontext klein)

- `INHALTE.md` — Dateistruktur/Kopplungen; **vor jeder Inhaltsänderung** (Notebooks, Lektionen, Manifeste, `kurse.json`) lesen
- `KURSPLAN.md` — Lehrpläne der einzelnen Kurse; bei Curriculum-/Kurs-Planung
- `PROJEKTIDEEN.md` — Ideen-Backlog für neue Projekt-Kurse
- `docs/archiv/HANDOFF-historie.md` — ausführliche Feature-Historie (Abschnitte 3.1–3.46), z.B. `grep -n "^### 3.32"`;
  nur bei Fragen "warum ist das so gebaut?"
- `docs/archiv/todo-erledigt.md` — erledigte Aufgaben/Branches

---

## Aktueller Stand & Workflow

@HANDOFF.md

---

## Regeln für diese Session

@WORKFLOW.md
