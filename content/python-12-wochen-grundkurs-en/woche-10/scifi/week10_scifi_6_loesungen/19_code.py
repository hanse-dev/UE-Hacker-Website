class Robot:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def is_tired(self):
        return self.energy < 20

print(Robot("Nova", 10).is_tired())
print(Robot("Orbit", 80).is_tired())
