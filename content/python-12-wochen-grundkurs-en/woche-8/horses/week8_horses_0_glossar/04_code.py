# Create a dictionary
horse = {"name": "Bobby", "age": 5, "breed": "Haflinger"}

# Access
print(horse["name"])            # Bobby
print(horse.get("weight", 0))   # 0 (default value)

# Change and delete
horse["age"] = 6
horse.update({"breed": "Andalusian"})
horse.pop("breed")

# Iteration
for key, value in horse.items():
    print(key, "→", value)

# Tuple
coordinate = (10, 20)
x, y = coordinate
print(x, y)  # 10 20
