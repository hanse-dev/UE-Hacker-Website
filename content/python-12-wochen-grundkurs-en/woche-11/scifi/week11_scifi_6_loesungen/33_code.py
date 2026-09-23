class Robot:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Robot("Nova", 5)
print(a == Robot("Orbit", 5))
print(a == Robot("Zeta", 8))
