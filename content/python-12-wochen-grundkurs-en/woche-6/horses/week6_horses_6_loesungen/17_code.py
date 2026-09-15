def generate_training(horse_type, difficulty):
    beginner = ["Warm-Up", "Walk", "Trot"]
    intermediate = ["Canter", "Dressage", "Poles"]
    advanced = ["Show Jumping", "Vaulting", "Pirouette"]
    training = list(beginner)
    if difficulty >= 2:
        training += intermediate
    if difficulty >= 3:
        training += advanced
    return [f"{horse_type}-{t}" for t in training]

plan_a = generate_training("Warmblood", 2)
plan_b = generate_training("Pony", 3)
print(f"Warmblood plan: {plan_a}")
print(f"Pony plan: {plan_b}")

# Filter: only units with "Dressage" or "Pirouette"
dressage = [t for t in plan_b if "Dressage" in t or "Pirouette" in t]
print(f"Dressage units: {dressage}")