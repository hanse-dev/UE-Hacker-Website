import random

# Step 1 – Training plan
def create_training_plan(horse_name, breed, level):
    """Creates a training plan for a horse.
    
    Parameters:
        horse_name (str): Name of the horse
        breed (str): Breed of the horse
        level (int): Training level
    
    Returns:
        dict: Dictionary with name, breed and level
    """
    return {"name": horse_name, "breed": breed, "level": level}

# Step 2 – Energy requirement
def calculate_energy(intensity, duration):
    return intensity * duration

# Step 3 – Training session
def generate_training_session(name, energy):
    return f"{name} completes a session using {energy} energy points."

# Step 4 – Show progress
def show_progress(horse, completed_sessions):
    print("=" * 35)
    print("      TRAINING PROGRESS")
    print("=" * 35)
    print(f"Horse:    {horse['name']}")
    print(f"Breed:    {horse['breed']}")
    print(f"Level:    {horse['level']}")
    print(f"Sessions completed: {completed_sessions}")
    print("=" * 35)

plan = create_training_plan("Storm", "Andalusian", 5)
energy = calculate_energy(8, 4)
session = generate_training_session(plan["name"], energy)
print(session)
show_progress(plan, 12)

# Bonus – weather and ground
def random_conditions():
    weather = random.choice(["Sunshine", "Rain", "Wind"])
    ground = random.choice(["dry", "muddy", "sandy"])
    energy_bonus = {"Rain": 5, "Wind": 3, "Sunshine": 0}
    extra = energy_bonus.get(weather, 0)
    return weather, ground, extra

weather, ground, extra = random_conditions()
print(f"Weather: {weather}, Ground: {ground} → +{extra} energy needed")