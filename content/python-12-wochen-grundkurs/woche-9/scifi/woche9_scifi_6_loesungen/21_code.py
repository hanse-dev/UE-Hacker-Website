import json
text = '{"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}'
daten = json.loads(text)
print(f"Name: {daten['name']}")
print(f"Rang plus 1: {daten['rang'] + 1}")
