import json
horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}
text = json.dumps(horse)
print(text)
