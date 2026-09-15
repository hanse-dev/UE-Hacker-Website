class Horse:
    def __init__(self, name, breed, age, gender):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"I am {self.name}, a {self.breed}, {self.age} years old.")

# Three horses
p1 = Horse("Thunder", "Hanoverian", 6, "Stallion")
p2 = Horse("Luna", "Haflinger", 4, "Mare")
p3 = Horse("Storm", "Arabian", 8, "Gelding")

for horse in [p1, p2, p3]:
    horse.introduce()

print(f"\nThunder's breed: {p1.breed}")
print(f"Luna's age: {p2.age}")