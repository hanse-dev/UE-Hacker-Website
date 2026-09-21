# 🐴 Breeding Exercise 1: Inheritance

Welcome to the **Sonnental Breeding Centre**! Noble horse lines pass their abilities on to the foals – exactly what **inheritance** does in Python.

A **child class** inherits all methods and attributes of its **parent class**. The parent goes in brackets after the name:

```python
class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Racehorse(Horse):
    pass

k = Racehorse("Blitz")
k.introduce()
print(isinstance(k, Horse))
```

1. **`class Racehorse(Horse):`** – Racehorse inherits everything from Horse
2. `k.introduce()` works although Racehorse does **not write it itself**
3. A child class can get **new** methods
4. **`isinstance(object, Class)`** asks: "Does the object belong to this class (or its parents)?"
