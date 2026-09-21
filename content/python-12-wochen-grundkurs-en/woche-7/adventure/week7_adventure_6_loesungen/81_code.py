import random

def roll_ability():
    return random.choice(["Fireball", "Lightning", "Healing"])

all_valid = True
for i in range(20):
    if roll_ability() not in ["Fireball", "Lightning", "Healing"]:
        all_valid = False
print(f"All valid: {all_valid}")
