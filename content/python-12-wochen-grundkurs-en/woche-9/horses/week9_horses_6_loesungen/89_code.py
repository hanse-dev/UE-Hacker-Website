import json
horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}
def safe_load(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Empty: {safe_load('does_not_exist.json') == {}}")
with open("horse.json", "w") as f:
    json.dump(horse, f)
print(f"Name: {safe_load('horse.json')['name']}")
