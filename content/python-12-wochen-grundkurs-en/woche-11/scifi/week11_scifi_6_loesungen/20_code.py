# Solution Suggestion Boss Quest 2 – The Robot Family

# Step 1: Base class
class Robot:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def task(self):
        print(f"{self.name} performs a general task. (Energy: {self.energy})")

    def __str__(self):
        return f"🤖 {self.name} | Energy: {self.energy}"

    def __eq__(self, other):
        return self.energy == other.energy

# Step 2: Types
class CombatRobot(Robot):
    def task(self):
        print(f"{self.name} (Combat): Neutralizing enemies! RATATATATA! (Energy -{15})")
        self.energy -= 15

class HealingRobot(Robot):
    def task(self):
        print(f"{self.name} (Healing): Repairing injuries and stabilizing vital signs. (Energy -{5})")
        self.energy -= 5

class ExplorationRobot(Robot):
    def task(self):
        print(f"{self.name} (Exploration): Scanning sector and updating map data. (Energy -{8})")
        self.energy -= 8

# Step 3: Deployment
titan = CombatRobot("Titan", 100)
medix = HealingRobot("Medix", 100)
explorer = ExplorationRobot("Explorer", 100)

print("=== ROBOT DEPLOYMENT ===")
for robot in [titan, medix, explorer]:
    print(robot)          # __str__
    robot.task()
    print(f"  Remaining energy: {robot.energy}")
    print()

print(f"Titan and Medix same energy? {titan == medix}")