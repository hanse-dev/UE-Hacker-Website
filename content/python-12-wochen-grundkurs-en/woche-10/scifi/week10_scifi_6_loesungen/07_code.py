# Problem: Methods always need self as first parameter – without self the method
# cannot access self.designation (it doesn't know which robot is meant).
class Robot:
    def __init__(self, designation):
        self.designation = designation
    
    def move(self):
        print(f"{self.designation} is moving! 🤖")

robot = Robot("R2-D2")
robot.move()