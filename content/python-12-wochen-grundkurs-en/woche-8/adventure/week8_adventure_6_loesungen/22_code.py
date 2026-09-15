# Step 1: Create heroes
heroes = [
    {"name": "Thorin", "hero_class": "Warrior", "level": 10, "special": "Shield Wall"},
    {"name": "Aria", "hero_class": "Mage", "level": 8, "special": "Fireball"},
    {"name": "Drake", "hero_class": "Warrior", "level": 6, "special": "Storm Strike"},
    {"name": "Lyra", "hero_class": "Archer", "level": 9, "special": "Dead Eye"}
]

# Step 2: Search by class
print("=== HEROES' ARCHIVE ===")
for hero_class in ["Warrior", "Mage"]:
    found = [h for h in heroes if h["hero_class"] == hero_class]
    print(f"\nClass '{hero_class}':")
    for h in found:
        print(f"  {h['name']} (Level {h['level']})")

# Step 3: Leaderboard
best = max(heroes, key=lambda h: h["level"])
print(f"\nBest hero: {best['name']} (Level {best['level']})")
print("\nLeaderboard (by level):")
leaderboard = sorted(heroes, key=lambda h: h["level"], reverse=True)
for i, h in enumerate(leaderboard, 1):
    print(f"  {i}. {h['name']} | Level {h['level']} | {h['hero_class']}")

# Bonus: Last 3 missions as tuple
heroes[0]["missions"] = ("Goblin Camp", "Tower of Light", "Dragon Cave")
print(f"\nBonus – Missions of {heroes[0]['name']}: {heroes[0]['missions']}")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Archivist of the Guild Archive!")
print("⭐ Title received: Master of Profiles")
print()
print("🎊 CONGRATULATIONS! You have mastered Week 8!")
print("📚 Next week: JSON files and I/O!")