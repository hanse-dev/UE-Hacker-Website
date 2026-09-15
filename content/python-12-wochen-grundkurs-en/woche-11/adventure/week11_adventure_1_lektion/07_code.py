# Example 1: __str__ and __repr__
class MagicPotion:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def __str__(self):
        return f"🧪 {self.name} ({self.colour})"
    
    def __repr__(self):
        return f"MagicPotion('{self.name}', '{self.colour}')"

# Example 2: __len__ and __getitem__
class Inventory:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def add(self, item):
        self.items.append(item)

# Example 3: __eq__ and __lt__
class Hero:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
    
    def __eq__(self, other):
        return self.strength == other.strength
    
    def __lt__(self, other):
        return self.strength < other.strength
    
    def __str__(self):
        return f"{self.name} (Strength: {self.strength})"
