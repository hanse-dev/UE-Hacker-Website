import json

# Write a file
with open("ship.txt", "w") as f:
    f.write("Enterprise\nClass: Galaxy\n")

# Read a file
with open("ship.txt", "r") as f:
    content = f.read()
print(content)

# Save JSON
ship = {"name": "Enterprise", "crew": 150}
with open("ship.json", "w") as f:
    json.dump(ship, f)

# Load JSON
with open("ship.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])  # Enterprise
