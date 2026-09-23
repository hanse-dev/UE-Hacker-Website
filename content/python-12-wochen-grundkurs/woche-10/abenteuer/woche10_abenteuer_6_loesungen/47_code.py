class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

schwert = Schwert("Excalibur", 50)
print(f"{schwert.name}: {schwert.wert}")
