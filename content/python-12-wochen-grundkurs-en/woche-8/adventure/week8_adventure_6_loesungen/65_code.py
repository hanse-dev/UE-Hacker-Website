treasures = [
    {"name": "Gold crown", "value": 800, "place": "Tower"},
    {"name": "Silver cup", "value": 300, "place": "Cellar"},
    {"name": "Ruby", "value": 650, "place": "Cave"},
]
values = [t["value"] for t in treasures]
values = sorted(values, reverse=True)
print(f"Values: {values}")
