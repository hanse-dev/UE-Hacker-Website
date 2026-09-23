import random
import string

alphabet = string.ascii_letters + string.digits
key = "".join([random.choice(alphabet) for i in range(8)])
only_allowed = True
for c in key:
    if c not in alphabet:
        only_allowed = False
print(f"Length: {len(key)}")
print(f"Only allowed characters: {only_allowed}")
