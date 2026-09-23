def create_mission(name, goal, difficulty):
    return [name, goal, difficulty]

missions = []
missions.append(create_mission("Scan Mission", "Mars", 4))
print(missions[0])
