# Example 2: Comparing different import methods
# Method 1: import math
import math
print("Method 1 - import math:")
print(f"  math.pi: {math.pi}")
print(f"  math.sqrt(25): {math.sqrt(25)}")

# Method 2: import math as m
import math as m
print("\nMethod 2 - import math as m:")
print(f"  m.pi: {m.pi}")
print(f"  m.sqrt(25): {m.sqrt(25)}")

# Method 3: from math import pi, sqrt
from math import pi, sqrt
print("\nMethod 3 - from math import pi, sqrt:")
print(f"  pi: {pi}")
print(f"  sqrt(25): {sqrt(25)}")