# Example 3: Combining lists
treasures = ["Gold", "Silver", "Gems"]
weapons = ["Sword", "Bow", "Axe"]
potions = ["Healing", "Mana", "Strength"]

print("=== Combining Lists ===")
print(f"Treasures: {treasures}")
print(f"Weapons: {weapons}")
print(f"Potions: {potions}")

# Combine with + operator
everything = treasures + weapons + potions
print(f"Everything combined: {everything}")

# Add one list to another with extend()
treasures.extend(weapons)
print(f"Treasures extended: {treasures}")