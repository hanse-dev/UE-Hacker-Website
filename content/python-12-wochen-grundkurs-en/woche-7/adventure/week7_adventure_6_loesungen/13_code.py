import random

# Step 1: Consult the dice oracle
rolls = [random.randint(1, 6) for _ in range(3)]
print("=== The Dice Oracle ===")
print(f"Rolls: {rolls}")

# Step 2: Choose a shelf
shelves = ["Shelf of the Elements", "Shelf of Beasts", "Shelf of Stars", "Shelf of Shadows", "Shelf of Heroes"]
chosen_shelf = random.choice(shelves)
print(f"\nYour shelf: {chosen_shelf}")

# Step 3: Draw scrolls
scrolls = ["Scroll of Fire", "Scroll of Wind", "Scroll of Stars", "Scroll of Shadow", "Scroll of Earth", "Scroll of Ice"]
drawn = random.sample(scrolls, 3)
print(f"\nDrawn scrolls: {drawn}")

# Step 4: Shuffle the reading order
random.shuffle(drawn)
print(f"Reading order: {drawn}")

# Bonus: average of the rolls
average = round(sum(rolls) / len(rolls), 2)
print(f"\nAverage roll: {average}")
