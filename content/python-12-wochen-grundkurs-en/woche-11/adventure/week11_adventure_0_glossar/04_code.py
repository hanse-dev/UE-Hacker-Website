class Hero:
    def __init__(self, name):
        self.name = name

    def ability(self):
        return "Fights with a sword"

    def __str__(self):
        return f"Hero: {self.name}"

# Inheritance
class Mage(Hero):
    def __init__(self, name, mana):
        super().__init__(name)
        self.mana = mana

    def ability(self):   # Polymorphism
        return f"Casts spells (Mana: {self.mana})"

aria = Hero("Aria")
gandalf = Mage("Gandalf", mana=100)

print(aria)                  # Hero: Aria
print(aria.ability())        # Fights with a sword
print(gandalf.ability())     # Casts spells (Mana: 100)
