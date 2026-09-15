class Creature:
    def __init__(self, name, species, favourite_food, food_amount_kg=2):
        self.name = name
        self.species = species
        self.favourite_food = favourite_food
        self.food_amount_kg = food_amount_kg
        self.fullness = 0  # Bonus

    def introduce(self):
        print(f"I am {self.name}, a {self.species}! My favourite food is {self.favourite_food}.")

    def eat(self):
        print(f"{self.name} eats {self.favourite_food}. Nom nom! ({self.food_amount_kg} kg)")

    # Bonus: feed method
    def feed(self, amount):
        self.fullness += amount
        print(f"{self.name} fed: +{amount} kg. Fullness: {self.fullness} kg")

menagerie = [
    Creature("Lumi", "Unicorn", "Moonblossoms", food_amount_kg=3),
    Creature("Griffar", "Griffin", "Stardust", food_amount_kg=5),
    Creature("Ignira", "Phoenix", "Emberberries", food_amount_kg=1),
    Creature("Scalor", "Young dragon", "Crystal ore", food_amount_kg=20),
]

print("=== Magical Creature Menagerie of Pyralia ===")
for creature in menagerie:
    creature.introduce()
    creature.eat()
    print()

big_eater = max(menagerie, key=lambda c: c.food_amount_kg)
print(f"Biggest eater: {big_eater.name} ({big_eater.species}) with {big_eater.food_amount_kg} kg/day")

# Bonus: feeding round
print("\n=== Feeding Round ===")
for creature in menagerie:
    creature.feed(creature.food_amount_kg)
