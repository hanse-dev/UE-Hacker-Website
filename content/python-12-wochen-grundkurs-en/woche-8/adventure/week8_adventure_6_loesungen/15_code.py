# Step 1: Create hero list
heroes = [
    {"name": "Thorin", "hero_class": "Warrior", "level": 8, "experience": 2400},
    {"name": "Aria", "hero_class": "Mage", "level": 6, "experience": 1800},
    {"name": "Lyra", "hero_class": "Archer", "level": 7, "experience": 2100},
]
print("=== HEROES' GUILD ===")
for h in heroes:
    print(f"  {h['name']} | {h['hero_class']} | Level {h['level']}")

# Step 2: Add a member
heroes.append({"name": "Drake", "hero_class": "Warrior", "level": 4, "experience": 900})
print(f"\nMembers after joining: {len(heroes)}")

# Step 3: Search function by class
def search_by_class(hero_list, hero_class):
    return [h for h in hero_list if h["hero_class"] == hero_class]

warriors = search_by_class(heroes, "Warrior")
print("\nAll Warriors:")
for w in warriors:
    print(f"  {w['name']} (Level {w['level']})")

mages = search_by_class(heroes, "Mage")
print("\nAll Mages:")
for m in mages:
    print(f"  {m['name']} (Level {m['level']})")

# Step 4: Average level
average_level = sum(h["level"] for h in heroes) / len(heroes)
print(f"\nAverage guild level: {average_level:.1f}")

# Assign quests
for h in heroes:
    if h["level"] >= 7:
        h["quest"] = "Defeat dragon"
    else:
        h["quest"] = "Clear bandit camp"

print("\nQuest assignment:")
for h in heroes:
    print(f"  {h['name']}: {h['quest']}")

# Bonus: Abilities
heroes[0]["abilities"] = ["Shield Wall", "Berserker", "Iron Will"]
print(f"\nBonus – Abilities of {heroes[0]['name']}: {heroes[0]['abilities']}")