# Solution suggestion Boss Quest 3 – The Stable Residents System

# Step 1: Base class
class StableResident:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} makes a sound...")

    def __str__(self):
        return f"Stable resident: {self.name}"

    def __len__(self):
        return len(self.name)

# Step 2: Derive animals
class StableHorse(StableResident):
    def make_sound(self):
        print(f"{self.name} (Horse): NEIIIGH! 🐴")

class StableDog(StableResident):
    def make_sound(self):
        print(f"{self.name} (Dog): WOOF WOOF! 🐕")

class StableCat(StableResident):
    def make_sound(self):
        print(f"{self.name} (Cat): Meow~ 🐱")

class StableChicken(StableResident):
    def make_sound(self):
        print(f"{self.name} (Chicken): CLUCK CLUCK! 🐔")

# Step 3: Morning round
stable = [
    StableHorse("Stardust"),
    StableDog("Rex"),
    StableCat("Mimi"),
    StableChicken("Henrietta")
]

print("=== MORNING ROUND IN THE STABLE ===")
for animal in stable:
    print(animal)              # __str__
    animal.make_sound()        # Polymorphism!
    print(f"  Name length: {len(animal)}")   # __len__
    print()

print("🎉 Challenge completed!")
print("🏆 You have defeated the Master Breeder!")
print("⭐ Title earned: Master of Horse OOP")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 11!")
