# Example 1: Simple while loop
print("=== Example 1: Counting to 10 ===")
counter = 0
while counter <= 10:
    print(f"Hoof beat {counter}")
    counter += 1  # IMPORTANT: count up, otherwise infinite loop!

print("\n=== What happens here? ===")
print("1. counter starts at 0")
print("2. As long as counter <= 10, the code runs")
print("3. counter += 1 increases the value on each pass")
print("4. At counter = 11 the condition becomes false → loop ends")