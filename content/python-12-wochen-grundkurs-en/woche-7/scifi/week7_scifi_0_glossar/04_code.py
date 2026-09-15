import math
import random

# math module
print(math.sqrt(25))   # 5.0
print(math.floor(3.7)) # 3
print(math.ceil(3.2))  # 4
print(round(math.pi, 2))  # 3.14

# random module
roll = random.randint(1, 6)
print("Dice:", roll)

planets = ["Mars", "Venus", "Jupiter"]
print(random.choice(planets))

random.shuffle(planets)
print(planets)
