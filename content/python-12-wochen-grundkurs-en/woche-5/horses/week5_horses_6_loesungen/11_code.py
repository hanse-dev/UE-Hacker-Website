import random

# Step 1 – Greeting routine
def greet_horse():
    print("Hello, beautiful horse! Ready for training?")
    print("Today will be a great training day!")

greet_horse()
greet_horse()

# Step 2 – Training intensity
def calculate_intensity(level, duration):
    return level * duration * 5

# Step 3 – Training possibility
def is_training_possible(energy):
    return energy >= 50

# Step 4 – Main block
horse_level = 4
duration = 3
energy = 75

intensity = calculate_intensity(horse_level, duration)
print(f"Training intensity: {intensity}")

if is_training_possible(energy):
    print(f"Training possible! Energy: {energy}")
else:
    print("Horse needs a break.")

# Bonus – random training type
def generate_training():
    types = ["Dressage", "Jumping", "Cross-Country", "Galloping", "Trotting"]
    return random.choice(types)

print(f"Today's training: {generate_training()}")