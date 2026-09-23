import json
text = '{"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}'
daten = json.loads(text)
print(f"Name: {daten['name']}")
print(f"Level plus 1: {daten['level'] + 1}")
