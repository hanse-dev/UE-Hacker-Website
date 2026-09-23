def erstelle_mission(name, ziel, schwierigkeit):
    return [name, ziel, schwierigkeit]

missionen = []
missionen.append(erstelle_mission("Scan-Mission", "Mars", 4))
print(missionen[0])
