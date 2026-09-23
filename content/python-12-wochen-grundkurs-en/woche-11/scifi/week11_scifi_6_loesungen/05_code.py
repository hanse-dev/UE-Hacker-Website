class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class RepairRobot(Robot):
    def arm(self):
        print(f"{self.name} charges the laser.")

k = RepairRobot("Orbit")
k.introduce()
k.arm()
