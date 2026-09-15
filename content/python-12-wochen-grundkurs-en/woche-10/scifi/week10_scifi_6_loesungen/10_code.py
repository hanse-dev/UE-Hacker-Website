class Robot:
    def __init__(self, id, model, energy, function):
        self.id = id
        self.model = model
        self.energy = energy
        self.function = function

    def status(self):
        print(f"Robot {self.id} | {self.model} | Function: {self.function} | Energy: {self.energy}%")

r1 = Robot("R-001", "ServoX", 90, "Maintenance")
r2 = Robot("R-002", "MediBot", 75, "Medicine")
r3 = Robot("R-003", "CombatX", 100, "Security")

for robot in [r1, r2, r3]:
    robot.status()

print(f"\nR-001 model: {r1.model}")
print(f"R-002 energy: {r2.energy}%")