import json
daten = {"name": "Test"}
text = json.dumps(daten)
ergebnis = json.loads(text)
print("Name:", ergebnis["name"])
