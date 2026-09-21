import random

random.seed(5)
first = random.randint(1, 100)
random.seed(5)
second = random.randint(1, 100)
print(f"Same: {first == second}")
