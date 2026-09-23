class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energy = 50

    def attack(self, ziel):
        ziel.energy -= self.level * 5

a = Hero("Aria", 4)
b = Hero("Thorin", 2)
sieger = None
while sieger is None:
    a.attack(b)
    if b.energy <= 0:
        sieger = a
        break
    b.attack(a)
    if a.energy <= 0:
        sieger = b
print(f"Winner: {sieger.name}")
