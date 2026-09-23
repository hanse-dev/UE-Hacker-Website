class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Springpferd(Pferd):
    def laufe(self):
        print(f"{self.name} springt über das Hindernis.")

Pferd("Sturm").laufe()
Springpferd("Stella").laufe()
