# 🐴 Exercise 1: Classes and Objects

Welcome to **Sonnental Riding Ranch**! Every stable has a **stable plan**: from one plan you can create as many horses, saddles and ponies as you like.

With **`class`** you create a blueprint, with **`Horse()`** you build an **object** from it. You attach properties (**attributes**) with a dot:

```python
class Horse:
    pass

horse = Horse()
horse.name = "Blitz"
horse.level = 1
print(horse.name, horse.level)
```

1. **`class Horse:`** – a class name starts with a **capital letter**
2. **`pass`** means "nothing inside yet"
3. **`horse.name = ...`** sets an attribute, **`horse.name`** reads it

> 💡 Every object stands on its own: changing one leaves the other unchanged.
