hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
removed = hero.pop("class")
print(f"Removed: {removed}")
del hero["hp"]
print(f"Properties: {len(hero)}")
