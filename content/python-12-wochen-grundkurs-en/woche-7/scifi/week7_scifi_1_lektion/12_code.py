# Example 2: Choosing from lists
import random

print("=== Random Selection from Lists ===")

# Planets in the system
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]
print(f"All planets: {planets}")

# One random planet
target = random.choice(planets)
print(f"Target planet: {target}")

# Three random planets
fleet = random.choices(planets, k=3)
print(f"Fleet targets: {fleet}")

# Shuffle the list
order = planets.copy()
random.shuffle(order)
print(f"Shuffled order: {order}")