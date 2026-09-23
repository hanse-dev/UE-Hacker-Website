class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Springpferd(Pferd):
    def starte(self):
        print(f"{self.name} startet aus der Box.")

k = Springpferd("Stella")
k.stelle_vor()
k.starte()
