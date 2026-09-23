# ⚔️ Blaupausen-Zauber 5: Den Zustand ändern

Ein Objekt **merkt sich** seinen Zustand – auch zwischen zwei Methodenaufrufen. Jede Methode kann ihn verändern:

```python
class Held:
    def __init__(self, name):
        self.name = name
        self.siege = 0

    def gewinne(self):
        self.siege += 1

held = Held("Aria")
held.gewinne()
held.gewinne()
print(held.siege)
```

1. `self.siege = 0` in `__init__` legt den Startwert fest
2. `self.siege += 1` zählt bei jedem Aufruf weiter
3. Jedes Objekt hat **seinen eigenen** Zähler

> 💡 Damit ein Wert nicht zu groß oder zu klein wird, prüfst du ihn mit `if` – wie die energie in Lektion 4.
