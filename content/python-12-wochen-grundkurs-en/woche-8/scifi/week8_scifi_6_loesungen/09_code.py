member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
removed = member.pop("role")
print(f"Removed: {removed}")
del member["energy"]
print(f"Properties: {len(member)}")
