# Example 2: Accessing profiles
hero = {
    "name": "Aria",
    "hero_class": "Mage",
    "level": 15,
    "hit_points": 120
}

print("=== Reading the Hero Profile ===")
print(f"Hero name: {hero['name']}")
print(f"Class: {hero['hero_class']}")
print(f"Level: {hero['level']}")
print(f"Hit points: {hero['hit_points']}")

# Using the get() method (safer)
print(f"\nWith get(): {hero.get('name')}")
print(f"Non-existent: {hero.get('mana', 'Unknown')}")