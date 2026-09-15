# Beispiel 2: Verschiedene Import-Methoden vergleichen
# Methode 1: import math
import math
print("Methode 1 - import math:")
print(f"  math.pi: {math.pi}")
print(f"  math.sqrt(25): {math.sqrt(25)}")

# Methode 2: import math as m
import math as m
print("\nMethode 2 - import math as m:")
print(f"  m.pi: {m.pi}")
print(f"  m.sqrt(25): {m.sqrt(25)}")

# Methode 3: from math import pi, sqrt
from math import pi, sqrt
print("\nMethode 3 - from math import pi, sqrt:")
print(f"  pi: {pi}")
print(f"  sqrt(25): {sqrt(25)}")