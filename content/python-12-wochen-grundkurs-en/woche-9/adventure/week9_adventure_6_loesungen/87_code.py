import json
hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
def save(data, name):
    with open(name, "w") as f:
        json.dump(data, f)

def load(name):
    with open(name, "r") as f:
        return json.load(f)

save(hero, "hero.json")
loaded = load("hero.json")
print(f"Equal: {loaded == hero}")
