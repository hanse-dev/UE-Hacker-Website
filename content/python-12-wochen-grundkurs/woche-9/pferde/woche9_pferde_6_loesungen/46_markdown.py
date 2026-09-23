"""### Debug-Quest – Aufgabe 3

🐛 Bug #3 – Ziel: Das Programm soll Alter plus 1: 9 ausgeben. Was ist falsch?

**Erklärung:** CSV liest alle Werte als **Text**. Vor dem Rechnen muss `int()` den Text `\"8\"` in die Zahl 8 umwandeln – sonst gibt es einen `TypeError`."""