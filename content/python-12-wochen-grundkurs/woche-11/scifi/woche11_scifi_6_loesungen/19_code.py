class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    def __init__(self, name, panzer=30):
        super().__init__(name)
        self.panzer = panzer

    def arbeite(self):
        print(f"{self.name} feuert den Laser ab.")

class Elite(Kampfroboter):
    def arbeite(self):
        super().arbeite()
        print(f"{self.name} ist ein Meister!")

Elite("Nova").arbeite()
