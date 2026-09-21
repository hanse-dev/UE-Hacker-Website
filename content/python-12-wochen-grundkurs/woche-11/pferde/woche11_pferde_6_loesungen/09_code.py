class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Rennpferd(Pferd):
    def laufe(self):
        print(f"{self.name} sprintet über die Bahn.")

Rennpferd("Blitz").laufe()
