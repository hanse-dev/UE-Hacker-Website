class Pferd:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

gruppe = [Pferd("Blitz", 15), Pferd("Stella", 18), Pferd("Sturm", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")
