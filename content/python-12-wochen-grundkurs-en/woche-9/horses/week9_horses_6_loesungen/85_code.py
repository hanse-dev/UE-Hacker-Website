import json
horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}
def save(data, name):
    with open(name, "w") as f:
        json.dump(data, f)

def load(name):
    with open(name, "r") as f:
        return json.load(f)

save(horse, "horse.json")
loaded = load("horse.json")
print(f"Equal: {loaded == horse}")
