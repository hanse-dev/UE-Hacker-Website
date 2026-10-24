import random
import string

alphabet = string.ascii_letters + string.digits
schluessel = "".join([random.choice(alphabet) for i in range(8)])
erlaubt = 0
for z in schluessel:
    if z in alphabet:
        erlaubt = erlaubt + 1
print(f"Länge: {len(schluessel)}")
print(f"Nur erlaubte Zeichen: {erlaubt == len(schluessel)}")
print(schluessel)
