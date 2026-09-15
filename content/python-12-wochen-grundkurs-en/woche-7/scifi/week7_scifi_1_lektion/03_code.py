# Example 1: Importing modules
# Import the whole module
import math
print(f"Pi from math: {math.pi}")

# Import with alias
import random as r
print(f"Random number: {r.randint(1, 10)}")

# Import only specific functions
from math import sqrt, sin, cos
print(f"Square root of 16: {sqrt(16)}")
print(f"Sine 90°: {sin(1.57)}")
print(f"Cosine 0°: {cos(0)}")