treasures = [
    {"name": "Gold crown", "value": 800, "place": "Tower"},
    {"name": "Silver cup", "value": 300, "place": "Cellar"},
    {"name": "Ruby", "value": 650, "place": "Cave"},
]
above = 0
total = 0
for t in treasures:
    if t["value"] > 500:
        above += 1
    total += t["value"]
print(f"Above 500: {above}")
print(f"Total value: {total}")
