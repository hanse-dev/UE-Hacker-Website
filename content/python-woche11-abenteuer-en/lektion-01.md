# ⚔️ Evolution Spell 1: Inheritance

Welcome to the **Master Guilds of Pyralia**! Great hero lines pass their abilities on to the next generation – exactly what **inheritance** does in Python.

A **child class** inherits all methods and attributes of its **parent class**. The parent goes in brackets after the name:

```python
class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Warrior(Hero):
    pass

k = Warrior("Aria")
k.introduce()
print(isinstance(k, Hero))
```

1. **`class Warrior(Hero):`** – Warrior inherits everything from Hero
2. `k.introduce()` works although Warrior does **not write it itself**
3. A child class can get **new** methods
4. **`isinstance(object, Class)`** asks: "Does the object belong to this class (or its parents)?"
