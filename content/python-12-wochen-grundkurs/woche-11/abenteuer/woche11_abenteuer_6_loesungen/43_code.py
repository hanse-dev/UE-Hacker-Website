class Vorrat:
    def __init__(self, menge):
        self.menge = menge

    def __add__(self, other):
        return Vorrat(self.menge + other.menge)

    def __str__(self):
        return f"Vorrat: {self.menge}"

lager = [Vorrat(10), Vorrat(20), Vorrat(30)]
gesamt = Vorrat(0)
for v in lager:
    gesamt = gesamt + v
print(gesamt)
