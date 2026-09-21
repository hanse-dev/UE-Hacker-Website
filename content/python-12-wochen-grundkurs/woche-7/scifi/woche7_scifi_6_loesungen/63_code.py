import random
import string

name = "Nova"
rune = "".join([random.choice(string.ascii_uppercase) for i in range(len(name))])
nur_gross = True
for z in rune:
    if z not in string.ascii_uppercase:
        nur_gross = False
print(f"Länge stimmt: {len(rune) == len(name)}")
print(f"Nur Großbuchstaben: {nur_gross}")
