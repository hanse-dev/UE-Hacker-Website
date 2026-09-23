class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    def lade_waffe(self):
        print("lädt den Laser.")

k = Kampfroboter("Nova")
k.stelle_vor()
