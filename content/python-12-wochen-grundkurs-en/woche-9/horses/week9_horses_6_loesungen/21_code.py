import json
text = '{"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}'
data = json.loads(text)
print(f"Name: {data['name']}")
print(f"Age plus 1: {data['age'] + 1}")
