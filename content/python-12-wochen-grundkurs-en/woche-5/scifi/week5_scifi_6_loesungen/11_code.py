import random

def greet_crew():
    print("Welcome aboard Nebula-7!")
    print("All systems ready – mission can begin.")

greet_crew()
greet_crew()

def calculate_energy(level, duration):
    return level * duration * 10

def is_system_ready(energy):
    return energy >= 100

energy = calculate_energy(4, 5)
print(f"Calculated energy: {energy} units")

if is_system_ready(energy):
    print("System status: READY")
else:
    print("System status: NOT READY – insufficient energy")

def generate_system_event():
    events = ["Solar Storm", "Sensor Error", "All Stable", "Micrometeorite Alert", "Cooling System Warning"]
    return random.choice(events)

print(f"Current event: {generate_system_event()}")