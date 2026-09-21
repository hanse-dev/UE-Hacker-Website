shelves = ["Shelf of Elements", "Shelf of Animals", "Shelf of Stars", "Shelf of Shadows", "Shelf of Heroes"]
import random

drawn = random.sample(shelves, 3)
random.shuffle(drawn)
print(f"Count: {len(drawn)}")
print(f"Different: {len(set(drawn)) == 3}")
