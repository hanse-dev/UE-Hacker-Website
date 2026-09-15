# Example 2: Choosing from lists
import random

print("=== Random Selection from Lists ===")

# Horses at the ranch
horses = ["Thunder", "Stormy", "Sunny", "Shadow", "Blaze", "Misty"]
print(f"All horses: {horses}")

# One random horse
target = random.choice(horses)
print(f"Target horse: {target}")

# Three random horses
group = random.choices(horses, k=3)
print(f"Riding group: {group}")

# Shuffle list
order = horses.copy()
random.shuffle(order)
print(f"Shuffled order: {order}")