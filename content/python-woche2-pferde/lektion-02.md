# 🚶 Übung 2: Schritt – Text

Jede Information auf dem Reiterhof hat einen **Typ** – genau wie ein Pferd eine von vier Gangarten zeigt. Die vier Hufschlag-Typen:

| Hufschlag-Typ | Gangart | Fachbegriff | Beispiel |
|---------------|---------|------------|---------|
| 🚶 Schritt | ruhig, gleichmäßig | `str` (Text) | `"Thunder"` |
| 🐎 Trab | fest getaktet, zählbar | `int` (Ganzzahl) | `7` |
| 🏇 Galopp | fließend, nie exakt gleich | `float` (Kommazahl) | `4.25` |
| 🦘 Sprung | geschafft oder nicht | `bool` (Wahrheitswert) | `True` / `False` |

> ⚠️ Kommazahlen schreibt Python mit **Punkt**: `3.14`, nicht `3,14`.

Den Typ erkennst du mit der **Funktion `type()`**. Du gibst ihr einen Wert in die Klammern, sie sagt dir den Typ:

```python
pferd_name = "Windsturm"
print(type(pferd_name))   # <class 'str'>
```

Python schreibt `<class '…'>` drumherum – wichtig ist nur das Wort in den Anführungszeichen, z. B. `str`.

## 🚶 Schritt: `str`

Ein **String** ist Text – alles in Anführungszeichen. Schritt ist die Gangart zum Reden und Kommunizieren.

> ⚠️ Auch `"7"` ist ein Text, weil es in Anführungszeichen steht – obwohl darin eine Ziffer liegt!

## 📏 `len()` – die Länge messen

`len()` ist ebenfalls eine Funktion: Du gibst ihr einen Text, und sie liefert dir die **Anzahl der Zeichen** zurück. Leerzeichen zählen mit!

```python
pferd_name = "Luna"
print(len(pferd_name))    # 4
```
