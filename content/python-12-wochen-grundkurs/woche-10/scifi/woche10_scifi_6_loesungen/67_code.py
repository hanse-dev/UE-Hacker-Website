class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Werkzeug("Plasmalaser", 50), Werkzeug("Ionenblaster", 35), Werkzeug("Schweißbrenner", 20)]
beste = lager[0]
for g in lager:
    if g.wert > beste.wert:
        beste = g
print(f"Stärkster: {beste.name}")
