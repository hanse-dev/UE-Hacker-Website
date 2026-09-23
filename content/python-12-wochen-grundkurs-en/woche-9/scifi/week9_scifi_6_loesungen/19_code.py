import json
member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
text = json.dumps(member)
print(text)
