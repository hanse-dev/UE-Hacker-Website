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

def erstelle_figur(name, level):
    return Roboter(name, level)

gruppe = [erstelle_figur("Nova", 2), erstelle_figur("Orbit", 5)]
print(f"Gruppe: {len(gruppe)}")
