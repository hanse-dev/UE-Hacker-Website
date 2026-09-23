class Robot:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level})"

    def __lt__(self, other):
        return self.level < other.level

team = [Robot("Nova", 5), Robot("Orbit", 7)]
print("Team: " + ", ".join([str(f) for f in team]))
