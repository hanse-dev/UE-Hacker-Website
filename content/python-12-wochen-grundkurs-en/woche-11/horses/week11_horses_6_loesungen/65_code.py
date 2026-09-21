class Horse:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __lt__(self, other):
        return self.level < other.level

for f in sorted([Horse("Blitz", 5), Horse("Stella", 9), Horse("Sturm", 2)]):
    print(f)
