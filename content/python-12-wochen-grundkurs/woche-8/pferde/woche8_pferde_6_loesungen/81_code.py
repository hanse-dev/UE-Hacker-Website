def erstelle_training(name, schwierigkeit):
    return {"name": name, "schwierigkeit": schwierigkeit, "status": "offen"}

trainings = []
trainings.append(erstelle_training("Springen üben", 1))
trainings.append(erstelle_training("Ausritt planen", 2))
trainings.append(erstelle_training("Fell pflegen", 3))
print(f"Training-Anzahl: {len(trainings)}")
print(f"Status: {trainings[0]['status']}")
