import json
pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}
def lade_sicher(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Leer: {lade_sicher('gibt_es_nicht.json') == {}}")
with open("pferd.json", "w") as f:
    json.dump(pferd, f)
print(f"Name: {lade_sicher('pferd.json')['name']}")
