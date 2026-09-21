# ⚔️ Blueprint Spell 1: Classes and Objects

Welcome to the **Craft Guilds of Pyralia**! Magic **blueprints** lie here: from one blueprint you can forge as many heroes, swords and dragons as you like.

With **`class`** you create a blueprint, with **`Hero()`** you build an **object** from it. You attach properties (**attributes**) with a dot:

```python
class Hero:
    pass

hero = Hero()
hero.name = "Aria"
hero.level = 1
print(hero.name, hero.level)
```

1. **`class Hero:`** – a class name starts with a **capital letter**
2. **`pass`** means "nothing inside yet"
3. **`hero.name = ...`** sets an attribute, **`hero.name`** reads it

> 💡 Every object stands on its own: changing one leaves the other unchanged.
