# Stage 4: Randomness and an enemy
import random

class Enemy:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def is_defeated(self):
        return self.hp <= 0

# Only one room has a real enemy – all the others have none (None)
world["airlock"]["enemy"] = None
world["corridor"]["enemy"] = None
world["lab"]["enemy"] = None
world["reactor"]["enemy"] = Enemy("Maintenance Robot", 15, 6)

def has_item(player, name):
    for item in player.inventory:
        if item.name == name:
            return True
    return False

def fight(player, enemy):
    print(f"⚔️ Fight: {player.name} vs. {enemy.name}!")
    bonus = 3 if has_item(player, "Cutter") else 0
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
            print(f"🎉 You defeated the {enemy.name}!")

# To try it out: a practice fight with a test hero and a practice enemy
testhero = Player("Testhero", "reactor")
fight(testhero, Enemy("Training Maintenance Robot", 15, 6))