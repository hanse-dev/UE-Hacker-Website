# ⚔️ Evolution Spell 5: __str__ and __repr__

**Magic methods** have two underscores before and after the name. Python calls them **by itself**. You already know `__init__` – now come the ones for the **text form**:

```python
class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __repr__(self):
        return f"Hero('{self.name}', {self.level})"

k = Hero("Aria", 5)
print(k)
print([k])
```

1. **`__str__`** provides the text for `print(object)` – with **`return`**, not with `print`!
2. **`__repr__`** is the "developer form"; Python uses it e.g. inside lists
3. Without `__str__`, `print(k)` would only show something like `<__main__.Hero object at 0x…>`
