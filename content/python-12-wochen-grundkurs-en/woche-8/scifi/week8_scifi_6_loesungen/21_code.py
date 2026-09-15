# List of mission dictionaries
missions = [
    {"name": "Alpha", "planet": "Kepler-62", "result": "successful", "duration": 30},
    {"name": "Beta", "planet": "Gliese-667", "result": "aborted", "duration": 7},
    {"name": "Gamma", "planet": "Proxima", "result": "successful", "duration": 45},
    {"name": "Delta", "planet": "HD 40307", "result": "successful", "duration": 22},
]

# Search: successful missions
successful = [m for m in missions if m["result"] == "successful"]
print(f"Successful missions: {len(successful)} of {len(missions)}")

# Total duration
total = sum(m["duration"] for m in missions)
print(f"Total duration: {total} days")

# Shortest successful mission
shortest = min(successful, key=lambda m: m["duration"])
print(f"Shortest successful mission: {shortest['name']} ({shortest['duration']} days)")

print()
print("🎉 Boss Quest completed!")
print("🏆 You have defeated the Data Curator of the Infinite Keys!")
print("⭐ Title earned: Master of the Data Archives")