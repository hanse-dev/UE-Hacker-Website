# Solution suggestion Boss Quest 3 – The Polymorphic Animal System

# Step 1: Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a general noise...")

    def __str__(self):
        return f"Animal: {self.name}"

    def __len__(self):
        return len(self.name)

# Step 2: Animal types
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name}: WOOF WOOF! 🐕")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}: Meow~ 🐱")

class Dragon(Animal):
    def make_sound(self):
        print(f"{self.name}: ROOOAAAAR! 🐉 *Fire*")

class Owl(Animal):
    def make_sound(self):
        print(f"{self.name}: Hoo hoo~ 🦉")

# Step 3: Animal Parade
animals = [
    Dog("Bello"),
    Cat("Whiskers"),
    Dragon("Infernox"),
    Owl("Minerva")
]

print("=== ANIMAL PARADE ===")
for animal in animals:
    print(animal)              # __str__
    animal.make_sound()        # Polymorphism!
    print(f"  Name length: {len(animal)}")   # __len__
    print()

print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Archmage!")
print("⭐ Title earned: Master of the OOP Arts")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 11!")
