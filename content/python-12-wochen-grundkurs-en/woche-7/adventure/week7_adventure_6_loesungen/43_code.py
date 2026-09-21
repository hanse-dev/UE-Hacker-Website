import random
import string

fragment = random.choice(string.ascii_letters)
print(f"Fragment valid: {fragment in string.ascii_letters}")
print(f"Length: {len(fragment)}")
