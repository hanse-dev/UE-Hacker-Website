# Beispiel 2: Verschiedene Import-Methoden vergleichen
import random
print("Methode 1 - import random:")
print(f"  random.randint(1, 6): {random.randint(1, 6)}")

import random as r
print("\nMethode 2 - import random as r:")
print(f"  r.randint(1, 6): {r.randint(1, 6)}")

from random import randint
print("\nMethode 3 - from random import randint:")
print(f"  randint(1, 6): {randint(1, 6)}")
