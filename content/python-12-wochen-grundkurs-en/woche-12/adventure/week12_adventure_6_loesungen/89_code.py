import random

def roll():
    return random.randint(1, 6)

ok = True
for i in range(20):
    if not 1 <= roll() <= 6:
        ok = False
print(ok)
