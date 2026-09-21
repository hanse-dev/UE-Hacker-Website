class Pferd:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Pferd("Blitz", 5)
print(a == Pferd("Stella", 5))
print(a == Pferd("Sturm", 8))
