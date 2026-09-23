class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energy = 50

    def attack(self, ziel):
        ziel.energy -= self.level * 5

a = Horse("Blitz", 4)
b = Horse("Stella", 2)
a.attack(b)
print(f"{b.name}: {b.energy}")
