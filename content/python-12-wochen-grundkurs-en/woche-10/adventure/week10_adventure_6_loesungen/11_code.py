# Step 1: Create class Sword
class Sword:
    def __init__(self, name, damage, material):
        self.name = name
        self.damage = damage
        self.material = material
    
    # Bonus: attack method
    def attack(self):
        return f"{self.name} strikes and deals {self.damage} damage!"

# Step 2: Create first object
excalibur = Sword("Excalibur", 50, "Steel")
print("=== Sword 1 ===")
print(f"Name: {excalibur.name}")
print(f"Damage: {excalibur.damage}")
print(f"Material: {excalibur.material}")
print(excalibur.attack())

# Step 3: Second sword
flame_sword = Sword("Flame Sword", 75, "Dragon Steel")
print("\n=== Sword 2 ===")
print(f"Name: {flame_sword.name}")
print(f"Damage: {flame_sword.damage}")
print(f"Material: {flame_sword.material}")
print(flame_sword.attack())