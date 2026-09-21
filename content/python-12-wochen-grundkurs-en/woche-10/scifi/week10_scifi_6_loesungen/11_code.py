class Robot:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name}, Level {self.level}.")

robot = Robot("Nova", 2)
robot.introduce()
