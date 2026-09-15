class Horse:
    def __init__(self, name, breed="Unknown"):
        self.name = name
        self.breed = breed
        self.fitness = 0

    def introduce(self):
        print(f"I am {self.name}, a {self.breed}!")

    def train(self):
        self.fitness += 10
        print(f"{self.name} is training! Fitness now: {self.fitness}")

# Create objects
horse1 = Horse("Bobby")
horse2 = Horse("Blitz", breed="Haflinger")

horse1.introduce()   # I am Bobby, a Unknown!
horse1.train()       # Bobby is training! Fitness now: 10
print(horse2.breed)  # Haflinger
