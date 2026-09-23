class Vorrat:
    def __init__(self, menge):
        self.menge = menge

    def __lt__(self, other):
        return self.menge < other.menge

    def __str__(self):
        return f"Vorrat: {self.menge}"

for v in sorted([Vorrat(30), Vorrat(10), Vorrat(20)]):
    print(v)
