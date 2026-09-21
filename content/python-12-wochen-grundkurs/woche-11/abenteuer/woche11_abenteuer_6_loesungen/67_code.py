class Vorrat:
    def __init__(self, menge):
        self.menge = menge

    def __add__(self, other):
        return Vorrat(self.menge + other.menge)

    def __str__(self):
        return f"Vorrat: {self.menge}"

print(Vorrat(15) + Vorrat(25) + Vorrat(5))
