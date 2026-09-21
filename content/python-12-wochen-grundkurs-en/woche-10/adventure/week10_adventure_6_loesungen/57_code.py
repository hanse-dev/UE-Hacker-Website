class Hero:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

    def train(self):
        self.level += 1
        print(f"{self.name} trains: Level {self.level}")

    def fight(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

    def rest(self, menge):
        self.energy += menge
        if self.energy > 100:
            self.energy = 100

gruppe = [Hero("Aria", 15), Hero("Thorin", 18), Hero("Luna", 12)]
for h in gruppe:
    h.train()
summe = 0
for h in gruppe:
    summe += h.level
print(f"Sum: {summe}")
