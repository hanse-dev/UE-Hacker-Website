import random
import time as t
import string

wurf = random.randint(1, 6)
print(f"Zufall im Bereich: {1 <= wurf <= 6}")
print(f"Buchstaben: {len(string.ascii_letters)}")
print(f"Zeit vergeht: {t.time() > 0}")
print(f"Wurf: {wurf}")
