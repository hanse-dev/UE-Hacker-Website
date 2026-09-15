def generate_training_name(horse_type, difficulty):
    return f"{horse_type.upper()}-L{difficulty}"

def calculate_intensity(duration, horse_type):
    factors = {"Sport Horse": 1.4, "Leisure Horse": 0.8, "Race Horse": 1.8}
    factor = factors.get(horse_type, 1.0)
    return min(100, int(duration * factor * 5))

def create_training(horse_type, difficulty, duration):
    name = generate_training_name(horse_type, difficulty)
    intensity = calculate_intensity(duration, horse_type)
    return {"name": name, "type": horse_type, "difficulty": difficulty, "intensity": intensity}

training_plan = []

def save_training(plan, training):
    plan.append(training)

save_training(training_plan, create_training("Sport Horse", 3, 6))
save_training(training_plan, create_training("Leisure Horse", 1, 4))
save_training(training_plan, create_training("Race Horse", 5, 8))
save_training(training_plan, create_training("Sport Horse", 2, 5))
save_training(training_plan, create_training("Leisure Horse", 2, 3))

print("=== TRAINING PLAN ===")
for t in training_plan:
    print(f"{t['name']} – Type: {t['type']}, Level: {t['difficulty']}, Intensity: {t['intensity']}")

total = sum(t["intensity"] for t in training_plan)
print(f"\nTraining count: {len(training_plan)}")
print(f"Average intensity: {total // len(training_plan)}")

print("\n--- Sorted by intensity ---")
for t in sorted(training_plan, key=lambda x: x["intensity"], reverse=True):
    print(f"  {t['name']}: {t['intensity']}")