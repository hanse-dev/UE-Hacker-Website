# 🚶 Übung 2: Schritt – Text

Jede Information im Reiterhof hat einen **Typ** – genau wie ein Pferd eine von vier Gangarten zeigt. Die vier Hufschlag-Typen:

| Hufschlag-Typ | Gangart | Fachbegriff | Beispiel |
|---------------|---------|------------|---------|
| 🚶 Schritt | ruhig, gleichmäßig | `str` (Text) | `"Thunder"` |
| 🐎 Trab | fest getaktet, zählbar | `int` (Ganzzahl) | `7` |
| 🏇 Galopp | fließend, nie exakt gleich | `float` (Kommazahl) | `4.25` |
| 🦘 Sprung | geschafft oder nicht | `bool` (Wahrheitswert) | `True` / `False` |

Den Typ erkennst du mit der **Funktion `type()`**. Du gibst ihr einen Wert in die Klammern, sie sagt dir den Typ:

```python
pferd_name = "Windsturm"
print(type(pferd_name))   # <class 'str'>
```

## 🚶 Schritt: `str`

Ein **String** ist Text – alles in Anführungszeichen. Schritt ist die Gangart zum Reden und Kommunizieren.

> ⚠️ Auch `"7"` ist ein Text, weil es in Anführungszeichen steht – obwohl darin eine Ziffer liegt!
