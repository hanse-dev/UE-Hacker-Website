crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
    {"name": "Kai", "role": "Pilot", "rank": 5, "energy": 110},
]
rank_values = [h["rank"] for h in crew]
ranking = sorted(rank_values, reverse=True)
best = crew[0]
for h in crew:
    if h["rank"] > best["rank"]:
        best = h
print(f"Best: {best['name']}")
print(f"Ranking: {ranking}")
