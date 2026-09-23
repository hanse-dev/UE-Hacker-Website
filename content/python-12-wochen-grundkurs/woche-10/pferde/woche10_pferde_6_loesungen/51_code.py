class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

    def info(self):
        return f"{self.name} ({self.wert})"

print(Sattel("Turniersattel", 50).info())
print(Sattel("Reitdecke", 35).info())
