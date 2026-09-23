"""### Debug-Quest – Aufgabe 2

🐛 Bug #2 – Ziel: Das Programm soll Blitz ausgeben. Was ist falsch?

**Erklärung:** Ohne `self.` sind `name` und `level` nur lokale Variablen und verschwinden nach `__init__`. Mit `self.name = name` gehören sie zum Objekt."""