class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Rennpferd(Pferd):
    pass

class Springpferd(Pferd):
    pass

k = Rennpferd("Blitz")
print(isinstance(k, Pferd))
print(isinstance(k, Springpferd))
