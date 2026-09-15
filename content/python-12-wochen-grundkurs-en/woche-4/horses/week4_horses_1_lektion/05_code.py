# Example 3: For loop with step size
print("=== Example 3: Every second hurdle ===")
# range(0, 11, 2) creates: 0, 2, 4, 6, 8, 10
for hurdle in range(0, 11, 2):
    print(f"Hurdle {hurdle}: Jumped!")

print("\n=== The step size ===")
print("range(start, end, step) skips hurdles")
print("Here: skip every second hurdle")