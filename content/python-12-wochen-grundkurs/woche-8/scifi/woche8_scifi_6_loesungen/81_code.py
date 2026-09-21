def erstelle_mission(name, schwierigkeit):
    return {"name": name, "schwierigkeit": schwierigkeit, "status": "offen"}

missionen = []
missionen.append(erstelle_mission("Signal orten", 1))
missionen.append(erstelle_mission("Sonde starten", 2))
missionen.append(erstelle_mission("Hülle reparieren", 3))
print(f"Mission-Anzahl: {len(missionen)}")
print(f"Status: {missionen[0]['status']}")
