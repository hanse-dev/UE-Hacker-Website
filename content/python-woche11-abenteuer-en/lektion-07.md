# ⚔️ Evolution Spell 7: Calculating and Counting: __add__ and __len__

Operators and functions like `len()` can also be set up for your own classes:

```python
class Supply:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Supply(self.amount + other.amount)

    def __str__(self):
        return f"Supply: {self.amount}"

a = Supply(10)
b = Supply(20)
print(a + b)

class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

t = Team()
t.mitglieder.append("Aria")
t.mitglieder.append("Thorin")
print(len(t))
```

1. **`__add__(self, other)`** is called for `a + b` and returns a **new** object
2. **`__len__(self)`** is called for `len(object)` and returns a **number**
3. This way your classes behave almost like built-in types
