# Example 2: For loop with start and end
print("=== Example 2: Hurdles 3 to 7 ===")
# range(3, 8) creates the numbers 3, 4, 5, 6, 7 (8 is exclusive!)
for hurdle in range(3, 8):
    print(f"Hurdle {hurdle}: Jump!")

print("\n=== Important observation ===")
print("range(start, end) includes start, but not end!")
print("Like a riding arena: from 3 up to BEFORE 8")