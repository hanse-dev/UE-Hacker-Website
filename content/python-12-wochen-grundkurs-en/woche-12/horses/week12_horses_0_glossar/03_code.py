class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Hero:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon("Wooden Sword", 2)  # The hero HAS a weapon

hero = Hero("Mira")
print(f"{hero.name} fights with the {hero.weapon.name} (damage: {hero.weapon.damage})")