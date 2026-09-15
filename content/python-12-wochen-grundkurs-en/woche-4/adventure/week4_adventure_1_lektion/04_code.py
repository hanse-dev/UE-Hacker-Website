# Example 2: For loop with start and end
print("=== Example 2: Counting from 3 to 7 ===")
# range(3, 8) creates the numbers 3, 4, 5, 6, 7 (8 is exclusive!)
for number in range(3, 8):
    print(f"Number: {number}")

print("\n=== Important observation ===")
print("range(start, end) includes start, but not end!")
print("Just like slices: [start:end] is end-exclusive")