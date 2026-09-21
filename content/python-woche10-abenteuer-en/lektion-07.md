# ⚔️ Blueprint Spell 7: Passing Objects to Functions

Functions can also take **objects**. The object is **not copied** – the function works with **the same** object:

```python
class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

a = Hero("Aria", 1)
b = a          # two names, one object!
b.level = 10
print(a.level)

def promote(figure):
    figure.level += 1

promote(a)
print(a.level)
```

1. `b = a` does **not** create a new object, just a second name
2. Whatever you change through `b` you also see at `a`
3. That is why `promote(a)` changes the real object – without `return`
