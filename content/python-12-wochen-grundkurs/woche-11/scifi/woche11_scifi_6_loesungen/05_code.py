class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Reparaturroboter(Roboter):
    def hole_werkzeug(self):
        print(f"{self.name} holt den Schraubenschlüssel.")

k = Reparaturroboter("Orbit")
k.stelle_vor()
k.hole_werkzeug()
