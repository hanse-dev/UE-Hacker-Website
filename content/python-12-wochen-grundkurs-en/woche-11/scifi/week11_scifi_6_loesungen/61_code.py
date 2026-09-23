class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

    def power(self):
        return 10

class BattleRobot(Robot):
    def __init__(self, name, armor=30):
        super().__init__(name)
        self.armor = armor

    def work(self):
        print(f"{self.name} fires the laser.")

    def power(self):
        return self.armor

class RepairRobot(Robot):
    def __init__(self, name, tools=50):
        super().__init__(name)
        self.tools = tools

    def work(self):
        print(f"{self.name} repairs the hull.")

    def power(self):
        return self.tools

team = [BattleRobot("Nova"), RepairRobot("Orbit"), Robot("Zeta")]
def strongest(team):
    beste = team[0]
    for f in team:
        if f.power() > beste.power():
            beste = f
    return beste

print(f"Strongest: {strongest(team).name}")
