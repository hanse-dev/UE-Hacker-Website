class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Werkzeug("Plasmalaser", 50), Werkzeug("Ionenblaster", 35), Werkzeug("Schweißbrenner", 20)]
summe = 0
for g in lager:
    summe += g.wert
print(f"Summe: {summe}")
