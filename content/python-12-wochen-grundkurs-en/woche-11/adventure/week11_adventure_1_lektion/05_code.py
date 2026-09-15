# Example 1: Method polymorphism
class Swordsman:
    def attack(self):
        print("Strike with the sword! ⚔️")

class Mage:
    def attack(self):
        print("Fireball thrown! 🔥")

class Archer:
    def attack(self):
        print("Arrow fired! 🏹")

# Example 2: Polymorphic function
def battle(character):
    character.attack()

# Example 3: Operator polymorphism
class GoldCoin:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return GoldCoin(self.value + other.value)
    
    def __str__(self):
        return f"{self.value} Gold Coins"
