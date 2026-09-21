class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Roboter("Nova", 5)
print(a == Roboter("Orbit", 5))
print(a == Roboter("Zeta", 8))
