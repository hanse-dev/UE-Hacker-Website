# Example 3: For loop with step size
print("=== Example 3: Every Second Sector ===")
# range(0, 11, 2) generates: 0, 2, 4, 6, 8, 10
for sector in range(0, 11, 2):
    print(f"Sector {sector}: Reinforcement activated")

print("\n=== The step size ===")
print("range(start, end, step) skips sectors")
print("Here: skip every other sector")