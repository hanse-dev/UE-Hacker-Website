def erstelle_quest(name, schwierigkeit):
    return {"name": name, "schwierigkeit": schwierigkeit, "status": "offen"}

quests = []
quests.append(erstelle_quest("Drache besiegen", 1))
quests.append(erstelle_quest("Schatz finden", 2))
quests.append(erstelle_quest("Dorf retten", 3))
print(f"Quest-Anzahl: {len(quests)}")
print(f"Status: {quests[0]['status']}")
