class Hero:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

gruppe = [Hero("Aria", 15), Hero("Thorin", 18), Hero("Luna", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")
