# 🚀 AI Module 2: Overriding Methods

Sometimes a child should do something **differently** from its parents. Then you write the method with **the same name** again – it **overrides** the inherited one:

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    def work(self):
        print(f"{self.name} fires the laser.")

Robot("Nova").work()
BattleRobot("Orbit").work()
```

1. Python always takes the method of the **own** class first
2. If there is none it looks at the **parents**
3. The parent class stays unchanged
