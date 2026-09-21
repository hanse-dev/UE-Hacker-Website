class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Rennpferd(Pferd):
    def __init__(self, name, tempo=30):
        super().__init__(name)
        self.tempo = tempo

    def laufe(self):
        print(f"{self.name} sprintet über die Bahn.")

class Champion(Rennpferd):
    def laufe(self):
        super().laufe()
        print(f"{self.name} ist ein Meister!")

Champion("Blitz").laufe()
