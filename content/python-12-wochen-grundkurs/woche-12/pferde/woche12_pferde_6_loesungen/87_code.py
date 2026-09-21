bestenliste = {"Mira": 120, "Tom": 90, "Lena": 150}
import json
with open("scores.json", "w") as f:
    json.dump(bestenliste, f)
with open("scores.json", "r") as f:
    back = json.load(f)
print(f"Anzahl: {len(back)}")
