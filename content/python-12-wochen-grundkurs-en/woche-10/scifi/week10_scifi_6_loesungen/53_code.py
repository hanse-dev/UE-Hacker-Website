class Robot:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

gruppe = [Robot("Nova", 15), Robot("Orbit", 18), Robot("Zeta", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")
