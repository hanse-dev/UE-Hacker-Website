import json
hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
with open("hero.json", "w") as f:
    json.dump(hero, f)
with open("hero.json", "r") as f:
    loaded = json.load(f)
print(f"Loaded: {loaded['name']}")
print(f"Equal: {loaded == hero}")
