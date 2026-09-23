# 🗣️ Spell Formula 1: f-strings

Welcome back, adventurer! At the edge of Pyralia rises the **Elemental Tower** – only those who master all **four elements** may enter. The **Tower Guardian** greets you with a clear statement: *"Every element has its own nature. Confuse them, and your spell will fail."*

Before you combine elements, you need a language to talk about them. An **f-string** is the modern and readable way to put variables into text. The `f` before the quotation marks tells Python: *"Look inside the curly braces!"*

```python
name = "Aria"
level = 5
print(f"Hello {name}! You are Level {level}!")
```

Inside the `{ }` you can even **calculate**:

```python
gold = 100
bonus = 25
print(f"Your gold: {gold + bonus}")
```

| Method | Example | Recommendation |
|--------|---------|-----------------|
| `+` concatenation | `"Hello " + name` | works, needs `str()` for numbers |
| f-string | `f"Hello {name}"` | more modern, shorter, numbers work directly |

> ✅ Use f-strings – they are clearer to read and less error-prone. The `+` method from Week 1 still works, though.
