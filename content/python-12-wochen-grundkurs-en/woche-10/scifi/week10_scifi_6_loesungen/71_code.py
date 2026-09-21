class Robot:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energy = 50

    def attack(self, ziel):
        ziel.energy -= self.level * 5

a = Robot("Nova", 4)
b = Robot("Orbit", 2)
a.attack(b)
print(f"{b.name}: {b.energy}")
