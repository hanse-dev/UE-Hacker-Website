# Example 1: __str__ and __repr__
class Spaceship:
    def __init__(self, name, ship_class):
        self.name = name
        self.ship_class = ship_class

    def __str__(self):
        return f"🚀 {self.name} ({self.ship_class})"

    def __repr__(self):
        return f"Spaceship('{self.name}', '{self.ship_class}')"

# Example 2: __len__ and __getitem__
class Fleet:
    def __init__(self):
        self.ships = []

    def __len__(self):
        return len(self.ships)

    def __getitem__(self, index):
        return self.ships[index]

    def add_ship(self, ship):
        self.ships.append(ship)

# Example 3: __eq__ and __lt__
class Planet:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __eq__(self, other):
        return self.population == other.population

    def __lt__(self, other):
        return self.population < other.population

    def __str__(self):
        return f"{self.name} ({self.population} inhabitants)"