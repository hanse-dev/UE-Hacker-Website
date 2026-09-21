class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __lt__(self, other):
        return self.level < other.level

for f in sorted([Held("Aria", 5), Held("Thorin", 9), Held("Luna", 2)]):
    print(f)
