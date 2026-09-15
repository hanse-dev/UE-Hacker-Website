# Example 1: Simple constructor
class Hero:
    def __init__(self, name):
        self.name = name

# Example 2: Constructor with multiple values
class Potion:
    def __init__(self, name, color, strength):
        self.name = name
        self.color = color
        self.strength = strength

# Example 3: Constructor with default values
class Goblin:
    def __init__(self, name="Grog", hp=10):
        self.name = name
        self.hp = hp