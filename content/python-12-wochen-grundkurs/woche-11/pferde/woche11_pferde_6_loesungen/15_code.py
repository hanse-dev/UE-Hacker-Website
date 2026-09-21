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

k = Rennpferd("Blitz", 45)
print(k.name, k.tempo)
