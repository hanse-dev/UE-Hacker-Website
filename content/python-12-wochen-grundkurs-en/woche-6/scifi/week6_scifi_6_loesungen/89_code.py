missions = [["Scan Mission", "Mars", 4], ["Rescue Mission", "Titan", 2], ["Repair Flight", "Station", 3]]
def mission_statistics(items):
    count = 0
    hard = 0
    for mission in items:
        count += 1
        if mission[2] < 3:
            continue
        hard += 1
    print(f"Missions: {count}")
    print(f"Hard missions: {hard}")

mission_statistics(missions)
