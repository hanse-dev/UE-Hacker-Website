import json
crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
]
with open("member.json", "w") as f:
    json.dump(crew, f)
import csv

with open("member.json", "r") as f:
    loaded = json.load(f)
with open("crew.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "role", "rank", "energy"])
    writer.writeheader()
    writer.writerows(loaded)
with open("crew.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames
print(f"Rows: {len(rows)}")
print(f"Fields: {fields}")
