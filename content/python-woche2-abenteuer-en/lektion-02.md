# 🔥🪨💧💨 Spell Formula 2: type() and the Four Elements

The Tower Guardian shows you the four elemental stones. Each has its own **nature** – in Python we call this the **type** of a value.

| Element | Type | Technical term | Example | Nature |
|---------|------|-----------------|---------|--------|
| 🔥 Fire | Text | `str` | `"Fireball"` | spoken words, names, spells |
| 🪨 Earth | Whole number | `int` | `42` | solid and countable – level, gold, points |
| 💧 Water | Decimal number | `float` | `3.14` | flowing, never quite exact – percentages, damage |
| 💨 Air | Truth value | `bool` | `True` / `False` | invisible, only there or not there – switches |

## `type()` – the element finder

`type()` is also a **spell formula (function)**, just like `print()` from Week 1: you call it with parentheses and give it a value inside. It hands you back the type:

```python
name = "Aria"
print(type(name))    # <class 'str'>  -> Fire element
print(type(42))      # <class 'int'>  -> Earth element
```

Note: `type()` only **returns** the type – it only becomes visible once you print it with `print()`.
