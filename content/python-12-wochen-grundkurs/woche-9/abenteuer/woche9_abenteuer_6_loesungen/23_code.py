import json

text = json.dumps({"pos": (3, 4)})
zurueck = json.loads(text)
print(f"Liste: {zurueck['pos'] == [3, 4]}")
print(f"Tupel: {zurueck['pos'] == (3, 4)}")
