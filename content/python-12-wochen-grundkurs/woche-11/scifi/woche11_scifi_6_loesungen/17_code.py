class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Reparaturroboter(Roboter):
    def __init__(self, name, werkzeuge=50):
        super().__init__(name)
        self.werkzeuge = werkzeuge

k = Reparaturroboter("Orbit")
print(k.name, k.werkzeuge)
