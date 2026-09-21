class Robot:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def upgrade(self):
        self.level += 1
        print(f"{self.name} gets an upgrade: Level {self.level}")

robot = Robot("Nova")
robot.upgrade()
robot.upgrade()
