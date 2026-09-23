class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class RepairRobot(Robot):
    def work(self):
        print(f"{self.name} repairs the hull.")

Robot("Zeta").work()
RepairRobot("Orbit").work()
