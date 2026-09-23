import json
held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
text = json.dumps(held)
print(text)
