# 🚀 AI Module 3: super() and __init__

If the child needs **additional** attributes, it writes its own `__init__`. Then it must **call the parent's** `__init__` – with **`super()`**:

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    def __init__(self, name, armor=30):
        super().__init__(name)
        self.armor = armor

k = BattleRobot("Nova", 45)
print(k.name, k.armor)
```

1. **`super().__init__(name)`** calls the parent constructor (sets `self.name`)
2. After that come the child's **new** attributes
3. With `super().method()` you can also call other methods of the parent, e.g. when overriding

> ⚠️ Without `super().__init__(...)` the parent's attributes are missing!
