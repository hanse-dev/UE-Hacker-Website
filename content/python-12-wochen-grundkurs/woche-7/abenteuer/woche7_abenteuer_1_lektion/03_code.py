# Beispiel 1: Module importieren
import random
import time

print(f"Zufallszahl: {random.randint(1, 10)}")

# Mit Spitzname importieren
import random as r
print(f"Nochmal (über Spitzname r): {r.randint(1, 10)}")

# Nur bestimmte Zauber importieren
from string import ascii_letters
print(f"Erste 5 Buchstaben des Runen-Alphabets: {ascii_letters[:5]}")
