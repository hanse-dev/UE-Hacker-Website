# 🐴 Breeding Exercise 2: Overriding Methods

Sometimes a child should do something **differently** from its parents. Then you write the method with **the same name** again – it **overrides** the inherited one:

```python
class Horse:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def run(self):
        print(f"{self.name} trots gently.")

class Racehorse(Horse):
    def run(self):
        print(f"{self.name} sprints down the track.")

Horse("Blitz").run()
Racehorse("Stella").run()
```

1. Python always takes the method of the **own** class first
2. If there is none it looks at the **parents**
3. The parent class stays unchanged
