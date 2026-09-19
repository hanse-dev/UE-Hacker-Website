# 🔥 Element 1: Fire – Text (`str`)

The Tower Guardian shows you the four elemental stones. Each has its own **nature** – in Python we call this the **type** of a variable.

| Element | Type | Technical term | Example | Nature |
|---------|------|----------------|---------|--------|
| 🔥 Fire | Text | `str` | `"Fireball"` | spoken words, names, spells |
| 🪨 Earth | Whole number | `int` | `42` | solid and countable – level, gold, points |
| 💧 Water | Decimal number | `float` | `3.14` | flowing, never quite exact – percentages, damage |
| 💨 Air | Truth value | `bool` | `True` / `False` | invisible, either there or not – switches |

We start with **🔥 Fire**: text, or *string*. Anything between quotation marks is Fire.

## Two new spell formulas

Two functions help you to recognise an element:

- `type(x)` – reveals the element (type) of a variable
- `len(x)` – counts the length of a Fire element (the letters of a text)

Remember: a spell formula is cast with **parentheses**, and the ingredient goes inside.

```python
name = "Aria"
print(type(name))   # <class 'str'>  -> Fire element
print(len(name))    # 4
```
