class Werkzeug:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert

lager = [Werkzeug("Plasmalaser", 50), Werkzeug("Ionenblaster", 35), Werkzeug("Schweißbrenner", 20)]
for g in lager:
    print(f"{g.name}: {g.wert}")
