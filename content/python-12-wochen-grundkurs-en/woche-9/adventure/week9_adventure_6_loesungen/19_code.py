import json
hero = {"name": "Aria", "class": "Mage", "level": 15, "hp": 120}
text = json.dumps(hero)
print(text)
