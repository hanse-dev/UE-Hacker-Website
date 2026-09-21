# 🐴 Breeding Exercise 5: __str__ and __repr__

**Magic methods** have two underscores before and after the name. Python calls them **by itself**. You already know `__init__` – now come the ones for the **text form**:

```python
class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __repr__(self):
        return f"Horse('{self.name}', {self.level})"

k = Horse("Blitz", 5)
print(k)
print([k])
```

1. **`__str__`** provides the text for `print(object)` – with **`return`**, not with `print`!
2. **`__repr__`** is the "developer form"; Python uses it e.g. inside lists
3. Without `__str__`, `print(k)` would only show something like `<__main__.Horse object at 0x…>`
