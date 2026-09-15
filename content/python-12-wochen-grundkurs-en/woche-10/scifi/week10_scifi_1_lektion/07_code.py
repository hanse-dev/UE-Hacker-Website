# Example 1: Simple constructor
class Android:
    def __init__(self, name):
        self.name = name

# Example 2: Constructor with multiple values
class Planet:
    def __init__(self, name, planet_type, diameter):
        self.name = name
        self.planet_type = planet_type
        self.diameter = diameter

# Example 3: Constructor with default values
class Alien:
    def __init__(self, species="Greys", hp=50):
        self.species = species
        self.hp = hp