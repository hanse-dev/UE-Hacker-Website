class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    def __init__(self, name, armor=30):
        super().__init__(name)
        self.armor = armor

    def work(self):
        print(f"{self.name} fires the laser.")

class Elite(BattleRobot):
    def work(self):
        super().work()
        print(f"{self.name} is a master!")

Elite("Nova").work()
