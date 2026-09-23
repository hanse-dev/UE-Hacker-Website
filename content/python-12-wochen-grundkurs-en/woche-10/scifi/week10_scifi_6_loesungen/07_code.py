class Robot:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

robot = Robot("Nova", 4)
print(f"{robot.name} {robot.level} {robot.energy}")
