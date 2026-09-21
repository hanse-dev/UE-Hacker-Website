import random
import string

name = "Nova"
rune = "".join([random.choice(string.ascii_uppercase) for i in range(len(name))])
only_capitals = True
for c in rune:
    if c not in string.ascii_uppercase:
        only_capitals = False
print(f"Length matches: {len(rune) == len(name)}")
print(f"Only capitals: {only_capitals}")
