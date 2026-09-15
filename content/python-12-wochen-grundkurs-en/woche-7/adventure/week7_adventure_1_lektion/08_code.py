# Example 2: Shelves, scrolls and shuffling
import random

shelves = ["Shelf of the Elements", "Shelf of Beasts", "Shelf of Stars", "Shelf of Shadows", "Shelf of Heroes"]
print(f"All shelves: {shelves}")

# One random shelf
chosen_shelf = random.choice(shelves)
print(f"Your shelf: {chosen_shelf}")

# Draw three distinct scrolls (no repeats!)
drawn_scrolls = random.sample(shelves, 3)
print(f"Drawn scrolls: {drawn_scrolls}")

# Shuffle the order
order = shelves.copy()
random.shuffle(order)
print(f"Shuffled reading order: {order}")
