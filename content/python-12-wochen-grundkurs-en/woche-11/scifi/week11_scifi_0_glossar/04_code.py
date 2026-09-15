class Spaceship:
    def __init__(self, name):
        self.name = name

    def ability(self):
        return "Flies through space"

    def __str__(self):
        return f"Ship: {self.name}"

# Inheritance
class Warship(Spaceship):
    def __init__(self, name, weapons):
        super().__init__(name)
        self.weapons = weapons

    def ability(self):   # Polymorphism
        return f"Fights with {self.weapons} weapons!"

enterprise = Spaceship("Enterprise")
defiant = Warship("Defiant", weapons=12)

print(enterprise)                  # Ship: Enterprise
print(enterprise.ability())        # Flies through space
print(defiant.ability())           # Fights with 12 weapons!