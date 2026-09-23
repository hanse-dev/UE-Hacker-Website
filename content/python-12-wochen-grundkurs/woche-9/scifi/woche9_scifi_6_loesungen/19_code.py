import json
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
text = json.dumps(mitglied)
print(text)
