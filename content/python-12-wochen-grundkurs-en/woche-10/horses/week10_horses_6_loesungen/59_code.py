class Horse:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def gallop(self, kosten):
        self.energy -= kosten
        if self.energy < 0:
            self.energy = 0

horse = Horse("Blitz")
horse.gallop(40)
horse.gallop(40)
horse.gallop(40)
print(f"Energy: {horse.energy}")
