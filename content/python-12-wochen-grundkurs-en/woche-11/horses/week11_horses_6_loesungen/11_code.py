# Solution suggestion Mission 1 – The Horse Hierarchy

# Step 1: Base class
class Horse:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def neigh(self):
        print(f"{self.name} neighs: NEIIIGH! 🐴")

# Step 2: Child classes
class RidingHorse(Horse):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.discipline = "Dressage"

    def train(self):
        print(f"{self.name} practices {self.discipline} – elegant movements!")

class Coldblood(Horse):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.pulling_force_kg = 1500

    def pull(self):
        print(f"{self.name} pulls up to {self.pulling_force_kg} kg – a strong working horse!")

class Pony(Horse):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.height_cm = 145

    def info(self):
        print(f"{self.name} is a pony with {self.height_cm} cm height.")

# Step 3: Create objects and call methods
valencia = RidingHorse("Valencia", 7, "mare")
valencia.neigh()
valencia.train()

print()
bruno = Coldblood("Bruno", 10, "stallion")
bruno.neigh()
bruno.pull()

print()
stardust = Pony("Stardust", 5, "gelding")
stardust.neigh()
stardust.info()

# Bonus: DressageHorse inherits from RidingHorse
print()
class DressageHorse(RidingHorse):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.discipline = "Grand Prix Dressage"
        self.title = "Champion"

    def gala_performance(self):
        print(f"{self.name}, {self.title}, performs a freestyle at the highest level!")

bella_donna = DressageHorse("Bella Donna", 12, "mare")
bella_donna.neigh()            # inherited from Horse
bella_donna.train()            # inherited from RidingHorse
bella_donna.gala_performance()
