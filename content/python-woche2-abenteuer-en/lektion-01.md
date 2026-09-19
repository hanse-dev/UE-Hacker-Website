# 💎 Week 2: The Four Magical Elements – f-strings

Welcome back, adventurer! At the edge of Pyralia rises the **Elemental Tower** – only those who master all **four elements** may enter. The **Tower Guardian** greets you: *"Every element has its own nature. Confuse them, and your spell will fail."*

**Your mission this week:**
- Learn **f-strings**, the common tongue for speaking about all elements
- Master the four elements: 🔥 Fire (`str`), 🪨 Earth (`int`), 💧 Water (`float`), 💨 Air (`bool`)
- Determine an element with the spell formulas `type()` and `len()`
- Change elements with the conversion spells `int()`, `float()`, `str()` and `bool()`
- Consult the oracle with `input()`

> 💡 **Week 1 recap:** a spell formula is a **function** – you cast it with its name followed by parentheses `()`. This week you will meet several new ones.

## 🗣️ The Common Tongue: f-strings

Before you combine elements, you need a language to talk about them. An **f-string** is the **modern and readable** way to put variables into text. The `f` before the quotation marks tells Python: *"Look inside the curly braces!"*

```python
name = "Aria"
level = 5
print(f"Hello {name}! You are Level {level}!")
```

Inside the curly braces `{}` you can even calculate:

```python
gold = 100
print(f"Your gold: {gold + 25}")
```

| Method | Example | Recommendation |
|--------|---------|----------------|
| `+` concatenation | `"Hello " + name` | works, but numbers need `str()` |
| f-string | `f"Hello {name}"` | shorter, numbers work directly |

> ✅ Use f-strings – they are clearer to read and less error-prone. The `+` method from Week 1 still works, though.
