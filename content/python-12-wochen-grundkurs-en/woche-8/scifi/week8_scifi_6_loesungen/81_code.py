def create_mission(name, difficulty):
    return {"name": name, "difficulty": difficulty, "status": "open"}

missions = []
missions.append(create_mission("Locate the signal", 1))
missions.append(create_mission("Launch the probe", 2))
missions.append(create_mission("Repair the hull", 3))
print(f"Mission count: {len(missions)}")
print(f"Status: {missions[0]['status']}")
