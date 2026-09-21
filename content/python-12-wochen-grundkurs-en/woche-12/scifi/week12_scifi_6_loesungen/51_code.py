import json
data = {"name": "Mira", "hp": 20}
with open("save.json", "w") as f:
    json.dump(data, f)
print("💾 Saved game of Mira saved.")
