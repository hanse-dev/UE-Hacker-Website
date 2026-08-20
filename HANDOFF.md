# Handoff-Notizen (für den nächsten Rechner)

> **Zuletzt aktualisiert:** 2026-08-20
> **Aktueller Branch (WIP):** `cursor/storytelling-woche7-pilot` — Storytelling-Überarbeitung 12-Wochen-Kurs

**Was zuletzt gemacht wurde:**
- Storytelling-Analyse der Abenteuer-Variante (alle 12 Wochen) — siehe `todo.md` für die Befundliste
- Woche 7 Abenteuer (DE + EN) als Pilot komplett umgebaut: Rahmengeschichte "Der Archivar der Bibliothek
  von Pyralia" mit drei zusammenhängenden Prüfungen statt isolierter Schritt-Listen; Bibliothekswahl von
  `math`-lastig auf `random`/`string`/`time` umgestellt (math nur noch optionaler Bonus-Exkurs)
- Debug-Notebook-Regel gelernt: Bugs müssen unabhängig vom geteilten Jupyter-Kernel-Zustand sein (z.B.
  "vergessener Import" funktioniert nicht mehr, wenn eine frühere Zelle das Modul schon importiert hat)
- Belohnungstexte in Woche 7 an `rewards-manifest.json` / `-en.json` angeglichen (waren vorher an 2 Stellen
  inkonsistent: Boss-Quest 2 und 3 Item-Namen)
- Alle Code-Zellen in den neuen Notebooks wurden ausgeführt und verifiziert (auch mit geteiltem
  Namespace, um Kernel-Reihenfolge-Effekte zu simulieren)

**Als Nächstes:**
1. Committen (noch nicht passiert)
2. Mit dem Nutzer abstimmen, wie es weitergeht — offene Optionen in `todo.md` unter
   "Storytelling-Überarbeitung": restliche 11 Wochen Abenteuer, dann Pferde/Sci-Fi, oder erst die
   günstigen Quick-Fixes (Pythonia/Pyralia-Namenskonflikt, Woche 12 Textbug, Woche 2 Elementbezug)

**Git-Regel:** Jedes neue Thema = neuer Branch (`cursor/…`). Siehe `WORKFLOW.md`.
