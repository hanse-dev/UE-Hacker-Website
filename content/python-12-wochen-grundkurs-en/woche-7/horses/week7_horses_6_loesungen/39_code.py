import random
import time as t
import string

print(f"Random in range: {1 <= random.randint(1, 6) <= 6}")
print(f"Letters: {len(string.ascii_letters)}")
print(f"Time passes: {t.time() > 0}")
