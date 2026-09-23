class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

robot = Robot("Nova")
robot.introduce()
