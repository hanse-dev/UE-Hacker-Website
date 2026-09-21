shelves = ["Shelf of Elements", "Shelf of Animals", "Shelf of Stars", "Shelf of Shadows", "Shelf of Heroes"]
import random

chosen = random.choice(shelves)
print(f"Contained: {chosen in shelves}")
