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

gruppe = [Hero("Aria", 3, 80), Hero("Thorin", 8, 30), Hero("Luna", 5, 60)]
def count_fit(gruppe):
    anzahl = 0
    for h in gruppe:
        if h.energy > 50:
            anzahl += 1
    return anzahl

print(f"Fit: {count_fit(gruppe)}")
