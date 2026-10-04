import json
held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
def lade_sicher(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Leer: {lade_sicher('gibt_es_nicht.json') == {}}")
with open("held.json", "w") as f:
    json.dump(held, f)
print(f"Name: {lade_sicher('held.json')['name']}")
