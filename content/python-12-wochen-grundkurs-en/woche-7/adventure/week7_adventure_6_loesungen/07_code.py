import random

all_ok = True
for i in range(20):
    roll = random.randint(1, 6)
    if roll < 1 or roll > 6:
        all_ok = False
print(f"All in range: {all_ok}")
