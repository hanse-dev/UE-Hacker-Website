class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

    def info(self):
        return f"{self.name} ({self.wert})"

print(Schwert("Excalibur", 50).info())
print(Schwert("Nachtklinge", 35).info())
