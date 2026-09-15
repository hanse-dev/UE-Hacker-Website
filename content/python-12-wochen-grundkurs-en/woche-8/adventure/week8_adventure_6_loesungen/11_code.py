# Step 1: Create a hero profile
hero = {
    "name": "Thorin",
    "hero_class": "Warrior",
    "level": 5,
    "hit_points": 120
}
print("Hero Profile:")
print(hero)

# Step 2: Modify and extend values
hero["level"] = 6
hero["mana"] = 80
print(f"\nAfter update: Level {hero['level']}, Mana {hero['mana']}")

# Step 3: Monster list from dictionaries
monsters = [
    {"name": "Goblin", "type": "Weak", "strength": 10},
    {"name": "Troll", "type": "Strong", "strength": 45},
    {"name": "Dragon", "type": "Boss", "strength": 100}
]
print(f"\nMonster list: {monsters}")
print(f"First monster: {monsters[0]['name']}")

# Step 4: Access and output
name = hero["name"]
hero_class = hero.get("hero_class")
print(f"\n=== HERO: {name}, Class: {hero_class}, Level: {hero['level']} ===")

# Bonus: Nested dictionary
hero["equipment"] = {"weapon": "War Hammer", "armor": "Chain Mail"}
print(f"Weapon: {hero['equipment']['weapon']}")