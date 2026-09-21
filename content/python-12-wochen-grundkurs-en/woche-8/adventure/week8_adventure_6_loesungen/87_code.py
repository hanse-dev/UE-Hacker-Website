bag = {"Potion": 3, "Torch": 5, "Rope": 2}
import random

drawn = random.choice(list(bag.keys()))
print(f"Drawn valid: {drawn in bag}")
