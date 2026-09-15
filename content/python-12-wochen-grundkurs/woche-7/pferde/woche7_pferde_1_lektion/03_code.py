# Beispiel 1: Module importieren
# Ganzes Modul importieren
import math
print(f"Pi aus math: {math.pi}")

# Mit Alias importieren
import random as r
print(f"Zufallszahl: {r.randint(1, 10)}")

# Nur bestimmte Werkzeuge importieren
from math import sqrt, sin, cos
print(f"Wurzel aus 16: {sqrt(16)}")
print(f"Sinus 90°: {sin(1.57)}")
print(f"Kosinus 0°: {cos(0)}")