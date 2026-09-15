# Example 1: __str__ and __repr__
class Horse:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"🐴 {self.name} ({self.breed})"

    def __repr__(self):
        return f"Horse('{self.name}', '{self.breed}')"

# Example 2: __len__ and __getitem__
class Herd:
    def __init__(self):
        self.horses = []

    def __len__(self):
        return len(self.horses)

    def __getitem__(self, index):
        return self.horses[index]

    def add_horse(self, horse):
        self.horses.append(horse)

# Example 3: __eq__ and __lt__
class Champion:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __eq__(self, other):
        return self.points == other.points

    def __lt__(self, other):
        return self.points < other.points

    def __str__(self):
        return f"{self.name} ({self.points} points)"
