# Example 1: Simple while loop
print("=== Example 1: Scanning up to 10 ===")
scan = 0
while scan <= 10:
    print(f"Scan {scan}: Data received")
    scan += 1  # IMPORTANT: Increment, otherwise infinite loop!

print("\n=== What happens here? ===")
print("1. scan starts at 0")
print("2. As long as scan <= 10, the code runs")
print("3. scan += 1 increases the value on each pass")
print("4. At scan = 11 the condition is false → loop ends")