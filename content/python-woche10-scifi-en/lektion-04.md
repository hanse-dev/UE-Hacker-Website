# 🚀 System Protocol 4: Methods with Parameters and return

Like functions, methods take **parameters** and can give something back with **`return`**:

```python
class Robot:
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy

    def work(self, kosten):
        self.energy -= kosten

    def is_tired(self):
        return self.energy < 20

robot = Robot("Nova")
robot.work(30)
print(robot.energy)
print(robot.is_tired())
```

1. After `self` come your own parameters (here `kosten`)
2. The method **changes** the object: `self.energy -= kosten`
3. **`return`** gives a value back, e.g. `True` or `False`
