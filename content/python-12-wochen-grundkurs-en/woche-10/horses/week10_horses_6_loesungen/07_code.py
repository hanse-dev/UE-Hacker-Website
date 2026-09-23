class Horse:
    def __init__(self, name, level=1, energy=100):
        self.name = name
        self.level = level
        self.energy = energy

horse = Horse("Blitz", 4)
print(f"{horse.name} {horse.level} {horse.energy}")
