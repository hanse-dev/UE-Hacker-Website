horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
    {"name": "Wind", "breed": "Hanoverian", "age": 7, "points": 110},
]
total = 0
for h in horses:
    total += h["age"]
average = total / len(horses)
print(f"Average: {average}")
