import json

def lade_stand(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Anzahl: {len(lade_stand('gibtsnicht.json'))}")
