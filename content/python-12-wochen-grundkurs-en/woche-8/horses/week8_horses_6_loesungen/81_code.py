def create_training(name, difficulty):
    return {"name": name, "difficulty": difficulty, "status": "open"}

trainings = []
trainings.append(create_training("Practice jumping", 1))
trainings.append(create_training("Plan a ride", 2))
trainings.append(create_training("Groom the coat", 3))
print(f"Training count: {len(trainings)}")
print(f"Status: {trainings[0]['status']}")
