import random

random.seed(5)
erste = random.randint(1, 100)
random.seed(5)
zweite = random.randint(1, 100)
print(f"Gleich: {erste == zweite}")
