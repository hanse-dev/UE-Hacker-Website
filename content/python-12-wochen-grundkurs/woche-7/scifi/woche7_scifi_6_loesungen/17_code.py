import random
import string

zeichen = string.ascii_letters + string.digits
schluessel = "".join([random.choice(zeichen) for i in range(10)])
nur_erlaubt = True
for z in schluessel:
    if z not in zeichen:
        nur_erlaubt = False
print(f"Länge: {len(schluessel)}")
print(f"Nur erlaubte Zeichen: {nur_erlaubt}")
