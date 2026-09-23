import json
text = '{"name": "Aria", "class": "Mage", "level": 15, "hp": 120}'
data = json.loads(text)
print(f"Name: {data['name']}")
print(f"Level plus 1: {data['level'] + 1}")
