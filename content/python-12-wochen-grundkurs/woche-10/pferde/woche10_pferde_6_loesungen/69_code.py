class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Sattel("Turniersattel", 50), Sattel("Reitdecke", 35), Sattel("Halfter", 20)]
summe = 0
for g in lager:
    summe += g.wert
print(f"Summe: {summe}")
