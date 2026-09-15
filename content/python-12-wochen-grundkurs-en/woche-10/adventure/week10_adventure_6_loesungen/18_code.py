class Weapon:
    def __init__(self, name, weapon_type, damage):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage

    def display(self):
        print(f"[{self.weapon_type}] {self.name} – Damage: {self.damage}")

    def use(self):
        print(f"{self.name} is used! +{self.damage} damage!")

    # Bonus: upgrade method
    def upgrade(self):
        self.damage += 5
        print(f"{self.name} was upgraded! New damage: {self.damage}")

storage = [
    Weapon("Excalibur", "Sword", 60),
    Weapon("Shadowsong", "Dagger", 35),
    Weapon("Thunderbow", "Bow", 45),
]

print("=== Weapon Storage ===")
for weapon in storage:
    weapon.display()

strongest = max(storage, key=lambda w: w.damage)
print(f"\nStrongest weapon: {strongest.name} ({strongest.damage} damage)")

# Bonus: upgrade
strongest.upgrade()

print("\n=== In Use ===")
for weapon in storage:
    weapon.use()