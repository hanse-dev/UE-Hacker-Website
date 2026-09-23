trophies = [
    {"name": "Gold cup", "value": 800, "place": "Hall"},
    {"name": "Silver ribbon", "value": 300, "place": "Stable"},
    {"name": "Honor prize", "value": 650, "place": "Arena"},
]
above = 0
total = 0
for t in trophies:
    if t["value"] > 500:
        above += 1
    total += t["value"]
print(f"Above 500: {above}")
print(f"Total value: {total}")
