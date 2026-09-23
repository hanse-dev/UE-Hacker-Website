import random
import string

alphabet = string.ascii_letters + string.digits
schluessel = "".join([random.choice(alphabet) for i in range(8)])
nur_erlaubt = True
for z in schluessel:
    if z not in alphabet:
        nur_erlaubt = False
print(f"Länge: {len(schluessel)}")
print(f"Nur erlaubte Zeichen: {nur_erlaubt}")
