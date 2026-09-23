import random

def wuerfle():
    return random.randint(1, 6)

ok = True
for i in range(20):
    if not 1 <= wuerfle() <= 6:
        ok = False
print(ok)
