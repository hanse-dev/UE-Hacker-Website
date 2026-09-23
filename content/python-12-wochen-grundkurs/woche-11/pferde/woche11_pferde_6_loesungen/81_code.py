class Vorrat:
    def __init__(self, menge):
        self.menge = menge

    def __add__(self, other):
        return Vorrat(self.menge + other.menge)

    def __eq__(self, other):
        return self.menge == other.menge

print(Vorrat(10) + Vorrat(40) == Vorrat(50))
