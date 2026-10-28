import random
import string

zeichen = string.ascii_letters + string.digits
schluessel = "".join([random.choice(zeichen) for i in range(10)])
erlaubt = 0
for z in schluessel:
    if z in zeichen:
        erlaubt = erlaubt + 1
print(f"Länge: {len(schluessel)}")
print(f"Nur erlaubte Zeichen: {erlaubt == len(schluessel)}")
print(schluessel)
