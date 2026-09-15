# Example 1: Simple inheritance
class LivingBeing:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} breathes")

class Human(LivingBeing):
    def speak(self):
        print(f"{self.name} speaks")

# Example 2: Overriding methods
class Warrior(LivingBeing):
    def breathe(self):
        print(f"{self.name} breathes like a fighter!")
    
    def fight(self):
        print(f"{self.name} draws their sword!")

# Example 3: Using super()
class Mage(LivingBeing):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana
    
    def cast_spell(self):
        print(f"{self.name} casts a spell with {self.mana} Mana!")
