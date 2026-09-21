class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

    def kraft(self):
        return 10

class Rennpferd(Pferd):
    def __init__(self, name, tempo=30):
        super().__init__(name)
        self.tempo = tempo

    def laufe(self):
        print(f"{self.name} sprintet über die Bahn.")

    def kraft(self):
        return self.tempo

class Springpferd(Pferd):
    def __init__(self, name, hoehe=50):
        super().__init__(name)
        self.hoehe = hoehe

    def laufe(self):
        print(f"{self.name} springt über das Hindernis.")

    def kraft(self):
        return self.hoehe

def los(figur):
    figur.laufe()

for f in [Rennpferd("Blitz"), Springpferd("Stella")]:
    los(f)
