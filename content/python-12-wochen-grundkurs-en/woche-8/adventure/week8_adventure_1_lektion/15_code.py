# Example 2: List of profiles
heroes = [
    {
        "name": "Aria",
        "hero_class": "Mage",
        "level": 15,
        "experience": 2500
    },
    {
        "name": "Thorin",
        "hero_class": "Warrior",
        "level": 18,
        "experience": 3200
    },
    {
        "name": "Luna",
        "hero_class": "Rogue",
        "level": 12,
        "experience": 1800
    }
]

print("=== Hero List ===")
for hero in heroes:
    print(f"{hero['name']} - {hero['hero_class']} (Level {hero['level']})")

# Filter by level
strong = [h for h in heroes if h['level'] > 14]
print(f"\nStrong heroes: {[h['name'] for h in strong]}")