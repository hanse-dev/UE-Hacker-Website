missions = [["Scan Mission", "Mars", 4], ["Rescue Mission", "Titan", 2], ["Repair Flight", "Station", 3]]
def search_missions(items, term):
    found = []
    for mission in items:
        if term in mission[0]:
            found.append(mission)
    return found

hits = search_missions(missions, "Mission")
print(f"Found: {len(hits)}")
