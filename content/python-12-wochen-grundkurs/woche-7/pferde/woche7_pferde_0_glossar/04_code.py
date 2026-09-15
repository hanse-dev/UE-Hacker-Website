import math
import random

# math-Modul
print(math.sqrt(25))   # 5.0
print(math.floor(3.7)) # 3
print(math.ceil(3.2))  # 4
print(round(math.pi, 2))  # 3.14

# random-Modul
wurf = random.randint(1, 6)
print("Würfel:", wurf)

pferde = ["Bobby", "Blitz", "Moritz"]
print(random.choice(pferde))

random.shuffle(pferde)
print(pferde)
