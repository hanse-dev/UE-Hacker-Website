def create_member(name, kind, level):
    return {"name": name, "role": kind, "rank": level}

member = create_member("Nova", "Pilot", 4)
print(f"Created: {member['name']}")
print(f"Rank: {member['rank']}")
