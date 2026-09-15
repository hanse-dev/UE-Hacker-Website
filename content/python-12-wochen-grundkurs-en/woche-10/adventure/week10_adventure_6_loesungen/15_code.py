# Step 1: Create class Dragon
class Dragon:
    def __init__(self, name, age, element):
        self.name = name
        self.age = age
        self.element = element

    # Step 2: Method breathe_fire
    def breathe_fire(self):
        print(f"{self.name} breathes {self.element}: PUFF! 🔥")

    # Bonus: fly method
    def fly(self):
        print(f"{self.name} spreads its wings and takes off! 🐉")

# Step 3: Create two dragons
fire_dragon = Dragon("Smaug", 500, "Fire")
ice_dragon = Dragon("Frostmaw", 300, "Ice")

dragons = [fire_dragon, ice_dragon]

for dragon in dragons:
    print(f"\n=== {dragon.name} ===")
    print(f"Age: {dragon.age} years")
    print(f"Element: {dragon.element}")
    dragon.breathe_fire()
    dragon.fly()