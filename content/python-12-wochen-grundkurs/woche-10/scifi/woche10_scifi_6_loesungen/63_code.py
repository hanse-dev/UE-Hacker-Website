class Roboter:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

    def aktualisiere(self):
        self.level += 1
        print(f"{self.name} bekommt ein Update: Level {self.level}")

    def arbeite(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

    def lade_auf(self, menge):
        self.energie += menge
        if self.energie > 100:
            self.energie = 100

roboter = Roboter("Nova")
runden = 0
while roboter.energie > 0:
    roboter.arbeite(30)
    runden += 1
print(f"Runden: {runden}")
