# Solution suggestion Boss Quest 2 – The Horse Family

# Step 1: Base class
class Horse:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def run(self):
        print(f"{self.name} runs – steady gallop. (Energy: {self.energy})")

    def __str__(self):
        return f"🐴 {self.name} | Energy: {self.energy}"

    def __eq__(self, other):
        return self.energy == other.energy

# Step 2: Breeds
class Haflinger(Horse):
    def run(self):
        print(f"{self.name} (Haflinger): Endurance mountain ride, safe and reliable! (Energy -{5})")
        self.energy -= 5

class Arab(Horse):
    def run(self):
        print(f"{self.name} (Arab): Lightning-fast sprint, springy gaits! (Energy -{12})")
        self.energy -= 12

class Andalusian(Horse):
    def run(self):
        print(f"{self.name} (Andalusian): Elegant rocking swing, majestic movements! (Energy -{8})")
        self.energy -= 8

# Step 3: Race
goldi = Haflinger("Goldi", 100)
rashid = Arab("Rashid", 100)
conquistador = Andalusian("Conquistador", 100)

print("=== HORSE RACE ===")
for horse in [goldi, rashid, conquistador]:
    print(horse)        # __str__
    horse.run()
    print(f"  Remaining energy: {horse.energy}")
    print()

print(f"Goldi and Rashid same energy? {goldi == rashid}")
