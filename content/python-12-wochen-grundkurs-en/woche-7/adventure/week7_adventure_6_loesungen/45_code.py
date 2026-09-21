import random

rolls = []
for i in range(3):
    rolls.append(random.randint(1, 6))
all_ok = True
for roll in rolls:
    if roll < 1 or roll > 6:
        all_ok = False
print(f"Rolls: {len(rolls)}")
print(f"All in range: {all_ok}")
