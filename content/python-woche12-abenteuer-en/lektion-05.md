# ⚔️ Stage 5: Enemy and Fight

*Knowledge from week 7 + 11: modules and methods*

The class `Enemy` gets a method `is_defeated()`. The module `random` (week 7) rolls the damage:

```python
import random

class Enemy:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def is_defeated(self):
        return self.hp <= 0

world["entrance"]["enemy"] = None
world["hall"]["enemy"] = None
world["spring"]["enemy"] = None
world["treasury"]["enemy"] = Enemy("Dragon", 15, 6)

def has_item(player, name):
    for item in player.inventory:
        if item.name == name:
            return True
    return False

def fight(player, enemy):
    print(f"⚔️ Fight: {player.name} against {enemy.name}!")
    bonus = 3 if has_item(player, "Sword") else 0
    while player.hp > 0 and not enemy.is_defeated():
        damage = random.randint(1, 6) + bonus
        enemy.hp -= damage
        print(f"   You hit for {damage} damage. ({enemy.name}: {max(enemy.hp, 0)} HP)")
        if enemy.is_defeated():
            break
        counter = random.randint(1, enemy.strength)
        player.hp -= counter
        print(f"   {enemy.name} hits you for {counter}. ({player.name}: {max(player.hp, 0)} HP)")
    return player.hp > 0

def check_enemy(player):
    enemy = world[player.position]["enemy"]
    if enemy is not None and not enemy.is_defeated():
        if fight(player, enemy):
            print(f"🎉 {enemy.name} was defeated!")
```

1. The player strikes: 1 to 6 damage, with Sword **+3**
2. If the enemy is still alive it strikes back
3. A `while` loop repeats this until one has no hit points left

Rooms without an enemy have `None` ("nothing").
