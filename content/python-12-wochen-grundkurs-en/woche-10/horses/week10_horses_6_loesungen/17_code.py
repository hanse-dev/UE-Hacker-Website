class Horse:
    def __init__(self, name, breed, age, energy=100):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy = energy

    def introduce(self):
        print(f"🐴 {self.name} | {self.breed} | {self.age} years | Energy: {self.energy}%")

    def train(self, hours):
        cost = hours * 10
        self.energy = max(0, self.energy - cost)
        print(f"{self.name} trained {hours}h. Energy now: {self.energy}%")

    def rest(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is resting. Energy: {self.energy}%")

thunder = Horse("Thunder", "Hanoverian", 6)
luna = Horse("Luna", "Haflinger", 4)
storm = Horse("Storm", "Arabian", 10)

horses = [thunder, luna, storm]
for h in horses:
    h.introduce()

oldest = max(horses, key=lambda h: h.age)
print(f"\nOldest horse: {oldest.name} ({oldest.age} years)")

thunder.train(3)
thunder.rest()