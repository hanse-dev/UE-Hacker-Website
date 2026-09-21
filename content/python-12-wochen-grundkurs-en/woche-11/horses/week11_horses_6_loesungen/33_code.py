class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

a = Horse("Blitz", 5)
print(a == Horse("Stella", 5))
print(a == Horse("Sturm", 8))
