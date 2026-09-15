# Example 1: Simple constructor
class Horse:
    def __init__(self, name):
        self.name = name

# Example 2: Constructor with multiple values
class Foal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Example 3: Constructor with default values
class Horse:
    def __init__(self, name="Stormy", breed="Pony"):
        self.name = name
        self.breed = breed