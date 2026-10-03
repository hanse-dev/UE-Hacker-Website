import json
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
def lade_sicher(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Leer: {lade_sicher('gibt_es_nicht.json') == {}}")
with open("mitglied.json", "w") as f:
    json.dump(mitglied, f)
print(f"Name: {lade_sicher('mitglied.json')['name']}")
