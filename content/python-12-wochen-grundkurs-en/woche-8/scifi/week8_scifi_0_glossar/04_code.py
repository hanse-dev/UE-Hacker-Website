# Create a dictionary
ship = {"name": "Enterprise", "crew": 150, "class": "Galaxy"}

# Access
print(ship["name"])            # Enterprise
print(ship.get("weapons", 0))  # 0 (default value)

# Modify and delete
ship["crew"] = 160
ship.update({"class": "Sovereign"})
ship.pop("class")

# Iteration
for key, value in ship.items():
    print(key, "→", value)

# Tuple
coordinate = (10, 20)
x, y = coordinate
print(x, y)  # 10 20
