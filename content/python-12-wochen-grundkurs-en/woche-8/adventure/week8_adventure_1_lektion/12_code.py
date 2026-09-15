# Example 3: Artifact unpacking and methods
hero_data = ("Aria", "Mage", 15, 120)

# Artifact unpacking
name, hero_class, level, hit_points = hero_data
print("=== Artifact Unpacking ===")
print(f"Name: {name}")
print(f"Class: {hero_class}")
print(f"Level: {level}")
print(f"Hit points: {hit_points}")

# Artifact methods
print(f"\nNumber of elements: {len(hero_data)}")
print(f"Index of 'Mage': {hero_data.index('Mage')}")
print(f"Count of 'Mage': {hero_data.count('Mage')}")