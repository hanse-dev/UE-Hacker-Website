# ⚔️ Blueprint Spell 5: Changing the State

An object **remembers** its state – even between two method calls. Every method can change it:

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def win(self):
        self.wins += 1

hero = Hero("Aria")
hero.win()
hero.win()
print(hero.wins)
```

1. `self.wins = 0` in `__init__` sets the starting value
2. `self.wins += 1` keeps counting with every call
3. Every object has **its own** counter

> 💡 To keep a value from getting too big or too small you check it with `if` – like the energy in lesson 4.
