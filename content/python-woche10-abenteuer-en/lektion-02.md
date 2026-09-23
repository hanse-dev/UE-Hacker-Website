# ⚔️ Blueprint Spell 2: The Constructor __init__

Setting every attribute one by one is tedious. The **constructor `__init__`** runs **automatically** when an object is created and receives all starting values:

```python
class Hero:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

a = Hero("Aria")
b = Hero("Thorin", 5)
print(a.name, a.level)
print(b.name, b.level)
```

1. **`self`** is always the first parameter – the object that is being created
2. **`self.name = name`** stores the value **inside the object**
3. **`level=1`** is a **default value** (like with functions in week 5)

> ⚠️ Two underscores before and after `init`: `__init__`.
