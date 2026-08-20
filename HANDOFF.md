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
- Pythonia/Pyralia-Namenskonflikt weltweit vereinheitlicht (auf "Pyralia", da in der Mehrheit der Wochen
  etabliert) — betraf Woche 1, 10, 12 (DE+EN, inkl. gecachter Zell-Outputs) sowie die Vorlagen unter
  `Regeln/`
- Woche 2 Abenteuer (DE + EN) umgebaut: "Elementarturm" als Rahmengeschichte, die vier Datentypen jetzt
  explizit als Elemente eingeführt (🔥 Feuer=str, 🪨 Erde=int, 💧 Wasser=float, 💨 Luft=bool), Missionen als
  drei zusammenhängende Prüfungen statt Schritt-Listen
- Woche 3, 4, 5 Abenteuer geprüft und für gut befunden (Missionen sind bereits sinnvolle Szenen,
  Debug-Bugs bereits in sich geschlossen) — kein Umbau nötig, nur verifiziert
- Woche 6 Abenteuer (DE + EN): Boss-Quest 1+2 waren wortwörtlich von Woche 5 kopiert
  ("Zauber-Generator"/"Guilden-Manager") — umbenannt zu "Schatzkammer-Katalog"/"Tresorwächter" mit
  passend umgethemtem Code (Schätze/Tresorfächer statt Zauber/Gildenabteilungen)
- Alle Code-Zellen in den neuen/geänderten Notebooks wurden ausgeführt und verifiziert (auch mit geteiltem
  Namespace, um Kernel-Reihenfolge-Effekte zu simulieren)

**Als Nächstes:**
1. Committen (noch nicht passiert)
2. Mit gleichem Prinzip weitermachen: Woche 8–12 Abenteuer (DE+EN) prüfen/umbauen, dann Pferde/Sci-Fi
3. Bei Weiterarbeit in neuer Session: dieses Vorgehen als Vorlage nehmen — zuerst Ist-Zustand prüfen
   (Missionen schon sinnvolle Szenen? Titel eingelöst? Boss-Quests einzigartig?), nur bei echtem Bedarf
   voll umbauen (Analyse → Story-Konzept → alle 6 Notebook-Typen DE schreiben → Code testen, inkl.
   Debug-Bugs mit geteiltem Kernel-Zustand → EN spiegeln → testen → committen)

**Git-Regel:** Jedes neue Thema = neuer Branch (`cursor/…`). Siehe `WORKFLOW.md`.
