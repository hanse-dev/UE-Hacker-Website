class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Reparaturroboter(Roboter):
    def arbeite(self):
        print(f"{self.name} repariert die Hülle.")

Roboter("Zeta").arbeite()
Reparaturroboter("Orbit").arbeite()
