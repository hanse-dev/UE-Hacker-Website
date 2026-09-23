# Create a dictionary
hero = {"name": "Aria", "level": 5, "gold": 100}

# Access
print(hero["name"])          # Aria
print(hero.get("xp", 0))    # 0 (default value)

# Modify and delete
hero["level"] = 6
hero.pop("gold")

# Iteration
for key, value in hero.items():
    print(key, "→", value)

# Tuple
coordinate = (10, 20)
x, y = coordinate
print(x, y)  # 10 20
