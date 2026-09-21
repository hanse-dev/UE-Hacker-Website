class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Springpferd(Pferd):
    def __init__(self, name, hoehe=50):
        super().__init__(name)
        self.hoehe = hoehe

k = Springpferd("Stella")
print(k.name, k.hoehe)
