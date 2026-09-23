import json
text = '{"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}'
daten = json.loads(text)
print(f"Name: {daten['name']}")
print(f"Alter plus 1: {daten['alter'] + 1}")
