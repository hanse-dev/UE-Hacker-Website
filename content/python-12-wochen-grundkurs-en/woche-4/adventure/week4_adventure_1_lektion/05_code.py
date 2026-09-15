# Example 3: For loop with step size
print("=== Example 3: Every other number from 0 to 10 ===")
# range(0, 11, 2) creates: 0, 2, 4, 6, 8, 10
for even in range(0, 11, 2):
    print(f"Even number: {even}")

print("\n=== The step size ===")
print("range(start, end, step) jumps 'step' positions each time")
print("Here: start=0, end=11, step=2 → 0, 2, 4, 6, 8, 10")