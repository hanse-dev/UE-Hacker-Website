# 🐴 Exercise 6: Objects in Lists

Objects can be collected in **lists** (week 6) just like numbers or text, and looped over with **`for`**:

```python
class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level

gruppe = [Horse("Blitz", 3), Horse("Stella", 8), Horse("Sturm", 5)]
for h in gruppe:
    print(h.name, h.level)

starke = [h.name for h in gruppe if h.level >= 5]
print(starke)
```

1. The list contains **objects**, not text
2. The loop variable `h` is one object each time – `h.name` reads its attribute
3. The list comprehension from week 6 also works with attributes
