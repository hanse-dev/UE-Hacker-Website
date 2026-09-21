class Robot:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

    def upgrade(self):
        self.level += 1
        print(f"{self.name} gets an upgrade: Level {self.level}")

    def work(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

    def recharge(self, menge):
        self.energy += menge
        if self.energy > 100:
            self.energy = 100

gruppe = [Robot("Nova", 3), Robot("Orbit", 8), Robot("Zeta", 5)]
starke = [h.name for h in gruppe if h.level >= 5]
print(starke)
