def erstelle_quest(name, ziel, schwierigkeit):
    return [name, ziel, schwierigkeit]

quests = []
quests.append(erstelle_quest("Drachenjagd", "Berg", 4))
print(quests[0])
