def erstelle_turnier(name, ort, schwierigkeit):
    return [name, ort, schwierigkeit]

turniere = []
turniere.append(erstelle_turnier("Springturnier", "Halle", 4))
print(turniere[0])
