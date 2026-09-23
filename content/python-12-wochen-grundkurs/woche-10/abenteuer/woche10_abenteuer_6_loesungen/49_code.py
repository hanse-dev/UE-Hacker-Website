class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

a = Schwert("Excalibur", 50)
b = Schwert("Nachtklinge", 35)
print(f"Zusammen: {a.wert + b.wert}")
