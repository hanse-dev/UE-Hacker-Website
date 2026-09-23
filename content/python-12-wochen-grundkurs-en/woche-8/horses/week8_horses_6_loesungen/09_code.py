horse = {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120}
removed = horse.pop("breed")
print(f"Removed: {removed}")
del horse["points"]
print(f"Properties: {len(horse)}")
