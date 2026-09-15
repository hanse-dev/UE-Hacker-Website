# Problem: Class names must start with capital letters
# and methods need self as the first parameter
class Robot:
    def move(self):
        print("Robot is moving")

class Drone(Robot):
    def fly(self):
        print("Drone is flying")

my_drone = Drone()
my_drone.move()