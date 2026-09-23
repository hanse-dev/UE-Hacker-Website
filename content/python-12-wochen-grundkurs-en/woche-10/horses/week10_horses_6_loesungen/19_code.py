class Horse:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def is_tired(self):
        return self.energy < 20

print(Horse("Blitz", 10).is_tired())
print(Horse("Stella", 80).is_tired())
