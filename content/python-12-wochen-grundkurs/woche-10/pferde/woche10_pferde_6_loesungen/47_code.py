class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

sattel = Sattel("Turniersattel", 50)
print(f"{sattel.name}: {sattel.wert}")
