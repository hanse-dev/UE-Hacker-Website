import random
import string

fragment = random.choice(string.ascii_letters)
print(f"Fragment gültig: {fragment in string.ascii_letters}")
print(f"Länge: {len(fragment)}")
