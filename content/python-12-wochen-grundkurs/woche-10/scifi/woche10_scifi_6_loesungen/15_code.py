class Roboter:
    def __init__(self, name):
        self.name = name
        self.level = 1

    def aktualisiere(self):
        self.level += 1
        print(f"{self.name} bekommt ein Update: Level {self.level}")

roboter = Roboter("Nova")
roboter.aktualisiere()
roboter.aktualisiere()
