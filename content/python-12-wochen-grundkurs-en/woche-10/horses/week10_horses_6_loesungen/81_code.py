class Horse:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

    def train(self):
        self.level += 1
        print(f"{self.name} trains: Level {self.level}")

    def gallop(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

    def rest(self, menge):
        self.energy += menge
        if self.energy > 100:
            self.energy = 100

gruppe = [Horse("Blitz", 3, 80), Horse("Stella", 8, 30), Horse("Sturm", 5, 60)]
schwach = gruppe[0]
for h in gruppe:
    if h.energy < schwach.energy:
        schwach = h
print(f"Weakest: {schwach.name}")
