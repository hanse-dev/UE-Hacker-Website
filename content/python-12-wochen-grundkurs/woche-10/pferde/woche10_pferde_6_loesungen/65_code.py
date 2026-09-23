class Sattel:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Sattel("Turniersattel", 50), Sattel("Reitdecke", 35), Sattel("Halfter", 20)]
for g in lager:
    print(f"{g.name}: {g.wert}")
