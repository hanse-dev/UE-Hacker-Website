class Enemy:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def is_defeated(self):
        return self.hp <= 0

foe = Enemy("Dragon", 10, 3)
print(foe.is_defeated())
foe.hp = 0
print(foe.is_defeated())
