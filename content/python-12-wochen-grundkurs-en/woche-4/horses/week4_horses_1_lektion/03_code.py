# Example 1: Simple for loop with range()
print("=== Example 1: 5 laps riding ===")
# range(5) creates the numbers 0, 1, 2, 3, 4
for i in range(5):
    print(f"Lap {i+1}: The horse trots elegantly")

print("\n=== What happens here? ===")
print("1. range(5) creates: [0, 1, 2, 3, 4]")
print("2. i is set to the next element on each pass")
print("3. We print i+1 to count from 1 to 5")
print("4. The loop ends after the last element")