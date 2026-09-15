# Solution Suggestion Boss Quest 3 – The Alien Contact System

# Step 1: Base class
class Alien:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def communicate(self):
        print(f"{self.name} from {self.origin}: [unknown communication]")

    def __str__(self):
        return f"👽 {self.name} | Origin: {self.origin}"

    def __len__(self):
        return len(self.origin)

# Step 2: Alien species
class Zylarian(Alien):
    def communicate(self):
        print(f"{self.name} (Zylarian): 'Zyk-zyh-zyh!' – communicates through light pulses")

class Grolthen(Alien):
    def communicate(self):
        print(f"{self.name} (Grolthen): 'GROMMM!' – deep rumbling, ground vibrations perceptible")

class Silicon(Alien):
    def communicate(self):
        print(f"{self.name} (Silicon): '01001000 01101001' – binary data packets")

class Aethros(Alien):
    def communicate(self):
        print(f"{self.name} (Aethros): [Telepathic waves perceptible – no sound]")

# Step 3: First contact
contacts = [
    Zylarian("Zykla", "Zylaron-5"),
    Grolthen("Grox", "Groltheim"),
    Silicon("Binary-1", "Datacron"),
    Aethros("Ether", "Aether Dimension")
]

print("=== FIRST CONTACT PROTOCOL ===")
for alien in contacts:
    print(alien)                # __str__
    alien.communicate()         # Polymorphism!
    print(f"  Origin name length: {len(alien)}")   # __len__
    print()

print("🎉 Mission complete!")
print("🏆 You have defeated the Construction Master!")
print("⭐ Title earned: Architect of Systems")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 11!")