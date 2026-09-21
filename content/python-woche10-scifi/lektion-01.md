# 🚀 System-Protokoll 1: Klassen und Objekte

Willkommen auf der **Raumstation Nebula-7**! Jede Maschine wird nach einer **Blaupause** gebaut: Aus einer Blaupause entstehen beliebig viele Roboter und Werkzeuge.

Mit **`class`** legst du eine Blaupause an, mit **`Roboter()`** baust du daraus ein **Objekt**. Eigenschaften (**Attribute**) hängst du mit einem Punkt an:

```python
class Roboter:
    pass

roboter = Roboter()
roboter.name = "Nova"
roboter.level = 1
print(roboter.name, roboter.level)
```

1. **`class Roboter:`** – der Name einer Klasse beginnt mit einem **Großbuchstaben**
2. **`pass`** heißt: „noch nichts drin“
3. **`roboter.name = ...`** setzt ein Attribut, **`roboter.name`** liest es

> 💡 Jedes Objekt ist eigenständig: Ändert man eines, bleibt das andere unverändert.
