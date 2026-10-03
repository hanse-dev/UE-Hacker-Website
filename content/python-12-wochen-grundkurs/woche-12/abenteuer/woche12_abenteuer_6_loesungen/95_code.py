import json

def lade_stand(dateiname):
    try:
        with open(dateiname, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Anzahl: {len(lade_stand('gibtsnicht.json'))}")
