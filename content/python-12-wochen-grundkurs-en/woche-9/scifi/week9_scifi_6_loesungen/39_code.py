import csv
crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
]
with open("crew.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "role", "rank", "energy"])
    w.writeheader()
    w.writerows(crew)
import json

entries = []
with open("crew.csv", "r") as f:
    for row in csv.DictReader(f):
        row["rank"] = int(row["rank"])
        entries.append(row)
with open("member.json", "w") as f:
    json.dump(entries, f)
with open("member.json", "r") as f:
    loaded = json.load(f)
total = 0
for entry in loaded:
    total += entry["rank"]
print(f"Count: {len(loaded)}")
print(f"Total: {total}")
