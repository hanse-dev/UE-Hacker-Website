# Example 3: Modifying and extending profiles
hero = {
    "name": "Aria",
    "hero_class": "Mage",
    "level": 15
}

print(f"Original: {hero}")

# Change a value
hero["level"] = 16
print(f"After level-up: {hero}")

# Add a new attribute
hero["mana"] = 80
print(f"After adding mana: {hero}")

# Remove an entry
removed = hero.pop("hero_class")
print(f"Removed: {removed}")
print(f"After removal: {hero}")