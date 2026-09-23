class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    pass

class RepairRobot(Robot):
    pass

k = BattleRobot("Nova")
print(isinstance(k, Robot))
print(isinstance(k, RepairRobot))
