bestenliste = {"Mira": 120, "Tom": 90, "Lena": 150}
import json
with open("punkte.json", "w") as f:
    json.dump(bestenliste, f)
with open("punkte.json", "r") as f:
    zurueck = json.load(f)
print(f"Anzahl: {len(zurueck)}")
