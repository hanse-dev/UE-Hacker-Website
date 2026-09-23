class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class BattleRobot(Robot):
    def __init__(self, name, armor):
        super().__init__(name)
        self.armor = armor

k = BattleRobot("Nova", 30)
print(k.name)
