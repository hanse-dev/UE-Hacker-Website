"""### Debug-Quest – Aufgabe 3

🐛 Bug #3 – Ziel: Das Programm soll Rang plus 1: 5 ausgeben. Was ist falsch?

**Erklärung:** CSV liest alle Werte als **Text**. Vor dem Rechnen muss `int()` den Text `\"4\"` in die Zahl 4 umwandeln – sonst gibt es einen `TypeError`."""