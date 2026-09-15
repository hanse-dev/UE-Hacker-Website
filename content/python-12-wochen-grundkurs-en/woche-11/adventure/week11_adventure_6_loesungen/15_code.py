# Solution suggestion Mission 3 – Magical Artefacts

# Step 1: Class Artefact
class Artefact:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    # Step 2: Magic Methods
    def __str__(self):
        return f"✨ {self.name} ({self.type}), Power: {self.power}"

    def __add__(self, other):
        return self.power + other.power

    def __len__(self):
        return self.power

    # Bonus
    def __eq__(self, other):
        return self.power == other.power

    def __lt__(self, other):
        return self.power < other.power

# Step 3: Testing
amulet = Artefact("Amulet of Wisdom", 75, "Jewellery")
staff = Artefact("Staff of Storms", 90, "Weapon")

print(amulet)
print(staff)

combined_power = amulet + staff
print(f"Combined Power: {combined_power}")

print(f"Power of Amulet (len): {len(amulet)}")

print(f"Equal strength? {amulet == staff}")
print(f"Amulet weaker than Staff? {amulet < staff}")
