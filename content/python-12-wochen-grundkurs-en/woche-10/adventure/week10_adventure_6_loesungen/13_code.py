# Step 1: Create class Wizard
class Wizard:
    def __init__(self, name, level=1, spell="Fireball", element="Fire"):
        self.name = name
        self.level = level
        self.spell = spell
        self.element = element  # Bonus

# Step 2: Create three wizards
merlin = Wizard("Merlin", level=15, spell="Lightning", element="Lightning")
gandalf = Wizard("Gandalf", level=20, spell="Light", element="Light")
dumbledore = Wizard("Dumbledore", level=18, spell="Expelliarmus", element="Arcane")

wizard_list = [merlin, gandalf, dumbledore]

print("=== Wizards' Guild ===")
for w in wizard_list:
    print(f"{w.name}: Level {w.level} ({w.element})")

# Step 3: Find the strongest
strongest = max(wizard_list, key=lambda w: w.level)
print(f"\nStrongest wizard: {strongest.name} (Level {strongest.level})")