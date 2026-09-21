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

def exhausted(figur):
    return figur.energy == 0

robot = Robot("Nova")
print(exhausted(robot))
robot.work(100)
print(exhausted(robot))
