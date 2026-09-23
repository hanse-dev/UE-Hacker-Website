# ⚔️ Blueprint Spell 3: Methods and self

A **method** is a function **inside** a class. It can use the object through **`self`**:

```python
class Hero:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

hero = Hero("Aria")
hero.introduce()
```

1. The method is **indented** inside the class and has **`self`** as its first parameter
2. When calling it you write **`hero.introduce()`** – Python fills in `self` itself
3. With **`self.name`** the method reaches the attributes of **this** object

> 💡 Python translates `hero.introduce()` into `Hero.introduce(hero)`.
