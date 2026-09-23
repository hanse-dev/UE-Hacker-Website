class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}.")

    def work(self):
        print(f"{self.name} idles.")

class RepairRobot(Robot):
    def __init__(self, name, tools=50):
        super().__init__(name)
        self.tools = tools

k = RepairRobot("Orbit")
print(k.name, k.tools)
