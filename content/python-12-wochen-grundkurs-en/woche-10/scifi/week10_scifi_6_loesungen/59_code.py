class Robot:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def work(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

robot = Robot("Nova")
robot.work(40)
robot.work(40)
robot.work(40)
print(f"Energy: {robot.energy}")
