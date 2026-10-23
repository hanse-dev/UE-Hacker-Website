"""### Debug-Quest – Aufgabe 3

🐛 Bug #3 – Ziel: Das Programm soll Level plus 1: 16 ausgeben. Was ist falsch? Repariere den Code im Editor, bis das Ziel erreicht ist.

**Erklärung:** CSV liest alle Werte als **Text**. Vor dem Rechnen muss `int()` den Text `\"15\"` in die Zahl 15 umwandeln – sonst gibt es einen `TypeError`."""