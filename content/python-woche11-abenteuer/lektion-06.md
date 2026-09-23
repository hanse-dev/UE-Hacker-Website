# ⚔️ Evolutions-Zauber 6: Vergleichen und sortieren

Mit **`__eq__`** (`==`) und **`__lt__`** (`<`) erklärst du Python, wie **deine** Objekte verglichen werden:

```python
class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

a = Held("Aria", 5)
b = Held("Thorin", 9)
print(a == b)
print(a < b)
for f in sorted([b, a]):
    print(f.name)
```

1. **`__eq__(self, other)`** gibt `True` zurück, wenn zwei Objekte „gleich“ sind
2. **`__lt__(self, other)`** gibt `True` zurück, wenn `self` **kleiner** ist als `other`
3. Mit `__lt__` kann **`sorted()`** (Woche 6) deine Objekte sortieren – ganz ohne extra Regel
