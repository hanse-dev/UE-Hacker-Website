class Roboter:
    def __init__(self, name):
        self.name = name
        self.siege = 0

    def gewinne(self):
        self.siege += 1

roboter = Roboter("Nova")
roboter.gewinne()
roboter.gewinne()
roboter.gewinne()
print(f"Siege: {roboter.siege}")
