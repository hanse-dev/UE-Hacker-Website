import random
import time as t
import string

print(f"Zufall im Bereich: {1 <= random.randint(1, 6) <= 6}")
print(f"Buchstaben: {len(string.ascii_letters)}")
print(f"Zeit vergeht: {t.time() > 0}")
