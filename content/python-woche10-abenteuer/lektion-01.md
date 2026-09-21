# ⚔️ Blaupausen-Zauber 1: Klassen und Objekte

Willkommen in den **Handwerkszünften von Pyralia**! Hier liegen magische **Blaupausen**: Aus einer Blaupause schmiedet man beliebig viele Helden, Schwerter und Drachen.

Mit **`class`** legst du eine Blaupause an, mit **`Held()`** baust du daraus ein **Objekt**. Eigenschaften (**Attribute**) hängst du mit einem Punkt an:

```python
class Held:
    pass

held = Held()
held.name = "Aria"
held.level = 1
print(held.name, held.level)
```

1. **`class Held:`** – der Name einer Klasse beginnt mit einem **Großbuchstaben**
2. **`pass`** heißt: „noch nichts drin“
3. **`held.name = ...`** setzt ein Attribut, **`held.name`** liest es

> 💡 Jedes Objekt ist eigenständig: Ändert man eines, bleibt das andere unverändert.
