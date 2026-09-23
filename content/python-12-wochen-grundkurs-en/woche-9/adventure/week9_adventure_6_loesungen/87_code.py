import json
hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
def safe_load(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Empty: {safe_load('does_not_exist.json') == {}}")
with open("hero.json", "w") as f:
    json.dump(hero, f)
print(f"Name: {safe_load('hero.json')['name']}")
