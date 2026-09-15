# Step 1: Profile dictionary
profile = {
    "name": "Captain Zara",
    "rank": "Commander",
    "department": "Command",
    "speciality": "Tactics & Navigation"
}
print("=== Profile ===")
for k, v in profile.items():
    print(f"  {k}: {v}")

# Step 2: Crew list
crew_list = [
    {"name": "Captain Zara", "rank": "Commander", "department": "Command", "speciality": "Tactics"},
    {"name": "Dr. Orion", "rank": "Doctor", "department": "Medical", "speciality": "Xenobiology"},
    {"name": "Tech Maya", "rank": "Engineer", "department": "Engineering", "speciality": "Propulsion"},
]

print("\n=== All Profiles ===")
for m in crew_list:
    print(f"  {m['name']} – {m['rank']} ({m['speciality']})")