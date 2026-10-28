# ⭐⭐⭐⭐⭐ Extra-Herausforderung 4: Die große Zufallsprobe

> ⚠️ Schwieriger! Die Extra-Herausforderungen kombinieren alles aus dieser Woche (auch Funktionen aus Woche 5 und Listen aus Woche 6) – sie sind freiwillig.

Die Bordintelligenz prüft dich noch einmal – diesmal mit dem **Zufall** aus dieser Woche (Messwerte, Ereignisse, Zeit-Sprünge), dem **Rest-Operator** für Primzahlen und dem Holodeck-Schachbrett.

**Neu in dieser Herausforderung:**

- **Schleife in einer Schleife:** Eine `for`-Schleife darf in einer anderen stehen. Die innere läuft bei jedem Durchlauf der äußeren einmal ganz durch:

```python
for zeile in range(2):
    for spalte in range(3):
        print(zeile, spalte)
```

  Das gibt 6 Zeilen aus: `0 0`, `0 1`, `0 2`, `1 0`, `1 1`, `1 2`.
- **`while True`** läuft immer weiter – bis ein `break` die Schleife beendet.

**Bonus (freiwillig, ohne Prüfung):** Erweitere den Zufallsweg um eine zweite Richtung (hoch und runter) und speichere beide Koordinaten.
