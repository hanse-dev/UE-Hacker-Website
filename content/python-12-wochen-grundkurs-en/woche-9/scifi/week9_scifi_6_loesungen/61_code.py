import csv
crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
    {"name": "Kai", "role": "Pilot", "rank": 5, "energy": 110},
]
with open("crew.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "role", "rank", "energy"])
    writer.writeheader()
    writer.writerows(crew)
with open("crew.csv", "r") as f:
    rows = list(csv.DictReader(f))
print(f"Rows: {len(rows)}")
