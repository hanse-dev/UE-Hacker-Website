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

def create_figure(name, level):
    return Hero(name, level)

gruppe = [create_figure("Aria", 2), create_figure("Thorin", 5)]
print(f"Group: {len(gruppe)}")
