class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Sattel("Turniersattel", 50), Sattel("Reitdecke", 35), Sattel("Halfter", 20)]
beste = lager[0]
for g in lager:
    if g.wert > beste.wert:
        beste = g
print(f"Stärkster: {beste.name}")
