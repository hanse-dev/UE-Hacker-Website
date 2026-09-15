import json

# Write a file
with open("horse.txt", "w") as f:
    f.write("Bobby\n5 years\n")

# Read a file
with open("horse.txt", "r") as f:
    content = f.read()
print(content)

# Save JSON
horse = {"name": "Bobby", "age": 5}
with open("horse.json", "w") as f:
    json.dump(horse, f)

# Load JSON
with open("horse.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])  # Bobby
