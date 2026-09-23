crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
    {"name": "Kai", "role": "Pilot", "rank": 5, "energy": 110},
]
total = 0
for h in crew:
    total += h["rank"]
average = total / len(crew)
print(f"Average: {average}")
