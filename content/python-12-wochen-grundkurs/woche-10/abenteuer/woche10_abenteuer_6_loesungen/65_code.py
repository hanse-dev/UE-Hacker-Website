class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Schwert("Excalibur", 50), Schwert("Nachtklinge", 35), Schwert("Eisendolch", 20)]
for g in lager:
    print(f"{g.name}: {g.wert}")
