import random
import string

characters = string.ascii_letters + string.digits
key = "".join([random.choice(characters) for i in range(10)])
only_allowed = True
for c in key:
    if c not in characters:
        only_allowed = False
print(f"Length: {len(key)}")
print(f"Only allowed characters: {only_allowed}")
