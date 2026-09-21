# 🚀 AI Module 1: Inheritance

Welcome to the **AI Lab of Space Station Nebula-7**! New robot models inherit the abilities of their predecessors – exactly what **inheritance** does in Python.

A **child class** inherits all methods and attributes of its **parent class**. The parent goes in brackets after the name:

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    pass

k = BattleRobot("Nova")
k.introduce()
print(isinstance(k, Robot))
```

1. **`class BattleRobot(Robot):`** – BattleRobot inherits everything from Robot
2. `k.introduce()` works although BattleRobot does **not write it itself**
3. A child class can get **new** methods
4. **`isinstance(object, Class)`** asks: "Does the object belong to this class (or its parents)?"
