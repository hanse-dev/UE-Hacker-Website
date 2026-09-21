import json
text = '{"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}'
data = json.loads(text)
print(f"Name: {data['name']}")
print(f"Rank plus 1: {data['rank'] + 1}")
