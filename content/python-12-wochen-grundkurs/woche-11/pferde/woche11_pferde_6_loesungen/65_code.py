class Pferd:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __lt__(self, other):
        return self.level < other.level

for f in sorted([Pferd("Blitz", 5), Pferd("Stella", 9), Pferd("Sturm", 2)]):
    print(f)
