class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Schwert("Excalibur", 50), Schwert("Nachtklinge", 35), Schwert("Eisendolch", 20)]
summe = 0
for g in lager:
    summe += g.wert
print(f"Summe: {summe}")
