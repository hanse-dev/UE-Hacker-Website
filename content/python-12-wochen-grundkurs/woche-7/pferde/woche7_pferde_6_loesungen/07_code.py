import random

alle_ok = True
for i in range(20):
    wurf = random.randint(1, 6)
    if wurf < 1 or wurf > 6:
        alle_ok = False
print(f"Alle im Bereich: {alle_ok}")
