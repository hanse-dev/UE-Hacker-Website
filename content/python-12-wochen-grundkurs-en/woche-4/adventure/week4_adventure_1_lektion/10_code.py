# Example 1: Simple while loop
print("=== Example 1: Counting to 5 ===")
counter = 0
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # IMPORTANT: Increment, otherwise infinite loop!

print("\n=== What happens here? ===")
print("1. counter starts at 0")
print("2. As long as counter <= 5, the code runs")
print("3. counter += 1 increases the value each run")
print("4. At counter = 6 the condition is false → loop ends")