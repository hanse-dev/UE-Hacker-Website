import random

def roll_ability():
    return random.choice(["Trot", "Gallop", "Jump"])

all_valid = True
for i in range(20):
    if roll_ability() not in ["Trot", "Gallop", "Jump"]:
        all_valid = False
print(f"All valid: {all_valid}")
