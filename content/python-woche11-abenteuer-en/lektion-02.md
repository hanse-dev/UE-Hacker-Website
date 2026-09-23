# ⚔️ Evolution Spell 2: Overriding Methods

Sometimes a child should do something **differently** from its parents. Then you write the method with **the same name** again – it **overrides** the inherited one:

```python
class Hero:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def fight(self):
        print(f"{self.name} fights bare-handed.")

class Warrior(Hero):
    def fight(self):
        print(f"{self.name} swings the sword.")

Hero("Aria").fight()
Warrior("Thorin").fight()
```

1. Python always takes the method of the **own** class first
2. If there is none it looks at the **parents**
3. The parent class stays unchanged
