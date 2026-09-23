horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
    {"name": "Wind", "breed": "Hanoverian", "age": 7, "points": 110},
]
age_values = [h["age"] for h in horses]
ranking = sorted(age_values, reverse=True)
best = horses[0]
for h in horses:
    if h["age"] > best["age"]:
        best = h
print(f"Best: {best['name']}")
print(f"Ranking: {ranking}")
