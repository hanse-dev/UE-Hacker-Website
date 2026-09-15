import json

# Write a file
with open("hero.txt", "w") as f:
    f.write("Aria\nLevel 5\n")

# Read a file
with open("hero.txt", "r") as f:
    content = f.read()
print(content)

# Save JSON
hero = {"name": "Aria", "level": 5}
with open("hero.json", "w") as f:
    json.dump(hero, f)

# Load JSON
with open("hero.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])  # Aria
