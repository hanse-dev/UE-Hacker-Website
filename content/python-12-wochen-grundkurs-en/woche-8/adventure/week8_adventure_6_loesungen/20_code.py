# Step 1: Build the dungeon
dungeon = {
    "Level 1": {"monster": "Goblin", "treasure": "Copper Coins", "difficulty": 2},
    "Level 2": {"monster": "Troll", "treasure": "Silver Dagger", "difficulty": 5},
    "Level 3": {"monster": "Dragon", "treasure": "Ruby Crown", "difficulty": 9}
}

# Step 2: Explore the levels
print("=== DUNGEON MANAGER ===")
most_dangerous = max(dungeon, key=lambda e: dungeon[e]["difficulty"])
for level, data in dungeon.items():
    print(f"\n{level}:")
    print(f"  Monster:     {data['monster']}")
    print(f"  Treasure:    {data['treasure']}")
    print(f"  Difficulty:  {data['difficulty']}/10")
print(f"\nMost dangerous level: {most_dangerous}")

# Step 3: Send a hero
hero = {"name": "Thorin", "hero_class": "Warrior", "level": 5}
print(f"\nHero: {hero['name']} (Level {hero['level']})")
print("Accessible levels:")
for level, data in dungeon.items():
    if hero["level"] >= data["difficulty"]:
        print(f"  ✓ {level} (Difficulty {data['difficulty']})")
    else:
        print(f"  ✗ {level} (Difficulty {data['difficulty']}) – too dangerous!")

# Bonus: Level up after each level
print("\nBonus – Level-up after exploration:")
for level in dungeon:
    if hero["level"] >= dungeon[level]["difficulty"]:
        hero["level"] += 1
        print(f"  {level} defeated! New level: {hero['level']}")