# Example 1: Generating random numbers
import random

print("=== Random Numbers ===")

# Integers
print(f"Random number 1-6: {random.randint(1, 6)}")
print(f"Random number 0-100: {random.randint(0, 100)}")

# Floats
print(f"Random number 0-1: {random.random():.3f}")
print(f"Random number 10-20: {random.uniform(10, 20):.2f}")

# Reproducible with seeds
random.seed(42)
print(f"With seed 42: {random.randint(1, 100)}")
random.seed(42)
print(f"With seed 42: {random.randint(1, 100)} (same result!)")