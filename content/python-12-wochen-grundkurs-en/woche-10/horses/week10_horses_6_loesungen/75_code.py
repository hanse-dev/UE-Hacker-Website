class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energy = 50

    def attack(self, ziel):
        ziel.energy -= self.level * 5

a = Horse("Blitz", 4)
b = Horse("Stella", 2)
rounds = 0
while a.energy > 0 and b.energy > 0:
    rounds += 1
    a.attack(b)
    if b.energy > 0:
        b.attack(a)
print(f"Rounds: {rounds}")
