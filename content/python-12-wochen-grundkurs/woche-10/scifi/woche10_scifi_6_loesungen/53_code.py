class Roboter:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

gruppe = [Roboter("Nova", 15), Roboter("Orbit", 18), Roboter("Zeta", 12)]
for h in gruppe:
    print(f"{h.name}: {h.level}")
