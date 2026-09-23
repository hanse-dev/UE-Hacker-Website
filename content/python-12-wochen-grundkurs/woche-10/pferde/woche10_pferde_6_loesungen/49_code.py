class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

a = Sattel("Turniersattel", 50)
b = Sattel("Reitdecke", 35)
print(f"Zusammen: {a.wert + b.wert}")
