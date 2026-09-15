hero = {
    "name": "Aria",
    "hero_class": "Mage",
    "level": 15,
    "hit_points": 120
}

# .keys() – keys only
print("Attributes:", list(hero.keys()))

# .values() – values only
print("Values:", list(hero.values()))

# .items() – key + value
print("\n=== Hero Profile ===")
for attribute, value in hero.items():
    print(f"  {attribute}: {value}")
