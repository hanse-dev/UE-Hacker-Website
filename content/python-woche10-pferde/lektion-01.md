# 🐴 Übung 1: Klassen und Objekte

Willkommen im **Reiterhof Sonnental**! Für jeden Stall gibt es einen **Stallplan**: Aus einem Plan entstehen beliebig viele Pferde, Sättel und Ponys.

Mit **`class`** legst du eine Blaupause an, mit **`Pferd()`** baust du daraus ein **Objekt**. Eigenschaften (**Attribute**) hängst du mit einem Punkt an:

```python
class Pferd:
    pass

pferd = Pferd()
pferd.name = "Blitz"
pferd.level = 1
print(pferd.name, pferd.level)
```

1. **`class Pferd:`** – der Name einer Klasse beginnt mit einem **Großbuchstaben**
2. **`pass`** heißt: „noch nichts drin“
3. **`pferd.name = ...`** setzt ein Attribut, **`pferd.name`** liest es

> 💡 Jedes Objekt ist eigenständig: Ändert man eines, bleibt das andere unverändert.
