class Schwert:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Schwert("Excalibur", 50), Schwert("Nachtklinge", 35), Schwert("Eisendolch", 20)]
beste = lager[0]
for g in lager:
    if g.wert > beste.wert:
        beste = g
print(f"Stärkster: {beste.name}")
