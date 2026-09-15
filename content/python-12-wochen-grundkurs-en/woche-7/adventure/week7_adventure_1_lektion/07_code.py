# Example 1: Consulting the dice oracle
import random

print("=== The Dice Oracle ===")
print(f"Roll 1: {random.randint(1, 6)}")
print(f"Roll 2: {random.randint(1, 6)}")
print(f"Decimal 0-1: {random.random():.3f}")
print(f"Decimal 10-20: {random.uniform(10, 20):.2f}")

# Reproducible with a seed
random.seed(42)
print(f"\nWith seed 42: {random.randint(1, 100)}")
random.seed(42)
print(f"With seed 42 (again): {random.randint(1, 100)} (same result!)")
