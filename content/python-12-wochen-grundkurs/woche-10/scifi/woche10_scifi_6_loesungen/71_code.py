class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energie = 50

    def greife_an(self, ziel):
        ziel.energie -= self.level * 5

a = Roboter("Nova", 4)
b = Roboter("Orbit", 2)
a.greife_an(b)
print(f"{b.name}: {b.energie}")
