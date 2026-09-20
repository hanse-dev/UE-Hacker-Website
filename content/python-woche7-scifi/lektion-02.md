# 🎲 Modul-Protokoll 2: Zufallszahlen

Das Modul **`random`** liefert Zufall – für Würfel, Glücksspiele und Überraschungen:

```python
import random

wurf = random.randint(1, 6)       # ganze Zahl von 1 bis 6 (beide inklusive)
kommazahl = random.uniform(10, 20)  # Kommazahl zwischen 10 und 20
zahl = random.random()            # Kommazahl zwischen 0 und 1
```

**Reproduzierbarer Zufall:** Mit `random.seed(zahl)` startest du den Zufall an einer festen Stelle. Mit demselben Seed kommen immer **dieselben** Zahlen – praktisch zum Testen.

> 💡 Weil der Zufall bei jedem Lauf anders ist, prüfst du in den Aufgaben **Eigenschaften** (liegt der Wurf zwischen 1 und 6?) statt feste Werte.
