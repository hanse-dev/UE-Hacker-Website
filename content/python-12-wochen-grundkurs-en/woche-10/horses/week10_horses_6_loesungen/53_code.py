class Horse:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

gruppe = [Horse("Blitz", 15), Horse("Stella", 18), Horse("Sturm", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")
