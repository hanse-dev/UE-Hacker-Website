import json
hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
with open("hero.json", "w") as f:
    json.dump(hero, f)
with open("hero.json", "r") as f:
    data = json.load(f)
data["mana"] = 80
with open("hero.json", "w") as f:
    json.dump(data, f)
with open("hero.json", "r") as f:
    loaded = json.load(f)
print(f"Mana: {loaded['mana']}")
print(f"Properties: {len(loaded)}")
