class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Rennpferd(Pferd):
    def __init__(self, name, tempo):
        super().__init__(name)
        self.tempo = tempo

k = Rennpferd("Blitz", 30)
print(k.name)
