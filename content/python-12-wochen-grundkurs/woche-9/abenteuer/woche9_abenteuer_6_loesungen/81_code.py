import json
quests = [
    {"name": "Drache besiegen", "schwierigkeit": 1, "status": "offen"},
    {"name": "Schatz finden", "schwierigkeit": 2, "status": "offen"},
    {"name": "Dorf retten", "schwierigkeit": 3, "status": "offen"},
]
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    geladen = json.load(f)
print(f"Quest-Anzahl: {len(geladen)}")
print(f"Status: {geladen[0]['status']}")
