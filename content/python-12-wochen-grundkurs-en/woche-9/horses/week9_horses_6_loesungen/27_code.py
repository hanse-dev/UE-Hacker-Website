import json
horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}
with open("horse.json", "w") as f:
    json.dump(horse, f)
with open("horse.json", "r") as f:
    data = json.load(f)
data["age"] += 1
with open("horse.json", "w") as f:
    json.dump(data, f)
with open("horse.json", "r") as f:
    loaded = json.load(f)
print(f"Age: {loaded['age']}")
