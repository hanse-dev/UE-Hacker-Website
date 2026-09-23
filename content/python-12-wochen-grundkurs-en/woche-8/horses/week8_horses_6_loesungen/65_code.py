trophies = [
    {"name": "Gold cup", "value": 800, "place": "Hall"},
    {"name": "Silver ribbon", "value": 300, "place": "Stable"},
    {"name": "Honor prize", "value": 650, "place": "Arena"},
]
values = [t["value"] for t in trophies]
values = sorted(values, reverse=True)
print(f"Values: {values}")
