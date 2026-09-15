# Example 1: Simple for loop with range()
print("=== Example 1: Counting from 0 to 4 ===")
# range(5) creates the numbers 0, 1, 2, 3, 4
for i in range(5):
    print(f"Run {i}: The value of i is {i}")

print("\n=== What happens here? ===")
print("1. range(5) creates: [0, 1, 2, 3, 4]")
print("2. i is set to the next element each run")
print("3. The loop ends after the last element")