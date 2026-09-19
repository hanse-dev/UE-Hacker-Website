# 📟 Systemprotokoll 7: Verschachtelte Schleifen – der Zeit-in-der-Zeit-Zyklus

Eine Schleife kann **eine weitere Schleife** enthalten – das nennt man Verschachtelung. Die innere Schleife läuft bei **jedem einzelnen Durchlauf** der äußeren komplett durch.

```python
for deck in range(1, 4):
    print(f"Deck {deck}:")
    for raum in range(1, 3):
        print(f"  Raum {raum} wird gescannt...")
```

Hier läuft der innere Code 3 × 2 = 6-mal. Jede weitere Verschachtelungsebene braucht **eine Einrückung mehr**.

Ein schöner Trick für Muster: `print("✨", end="")` gibt ohne Zeilenumbruch aus – normalerweise beendet `print()` jede Zeile mit einem Umbruch, und `end=""` unterdrückt ihn. Mit `end=" "` hängt `print` stattdessen ein Leerzeichen an. Ein leeres `print()` am Ende jeder Reihe beginnt dann eine neue Zeile.
