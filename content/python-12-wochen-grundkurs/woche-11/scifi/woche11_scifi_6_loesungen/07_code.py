class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    pass

class Reparaturroboter(Roboter):
    pass

k = Kampfroboter("Nova")
print(isinstance(k, Roboter))
print(isinstance(k, Reparaturroboter))
