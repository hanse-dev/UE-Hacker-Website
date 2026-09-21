class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

    def kraft(self):
        return 10

class Kampfroboter(Roboter):
    def __init__(self, name, panzer=30):
        super().__init__(name)
        self.panzer = panzer

    def arbeite(self):
        print(f"{self.name} feuert den Laser ab.")

    def kraft(self):
        return self.panzer

class Reparaturroboter(Roboter):
    def __init__(self, name, werkzeuge=50):
        super().__init__(name)
        self.werkzeuge = werkzeuge

    def arbeite(self):
        print(f"{self.name} repariert die Hülle.")

    def kraft(self):
        return self.werkzeuge

team = [Kampfroboter("Nova", 40), Reparaturroboter("Orbit", 25), Roboter("Zeta")]
anzahl = 0
for f in team:
    if f.kraft() >= 30:
        anzahl += 1
print(f"Anzahl: {anzahl}")
