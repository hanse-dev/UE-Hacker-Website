# 🐴 Breeding Exercise 6: Comparing and Sorting

With **`__eq__`** (`==`) and **`__lt__`** (`<`) you tell Python how **your** objects are compared:

```python
class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

a = Horse("Blitz", 5)
b = Horse("Stella", 9)
print(a == b)
print(a < b)
for f in sorted([b, a]):
    print(f.name)
```

1. **`__eq__(self, other)`** returns `True` if two objects are "equal"
2. **`__lt__(self, other)`** returns `True` if `self` is **smaller** than `other`
3. With `__lt__` **`sorted()`** (week 6) can sort your objects – without any extra rule
