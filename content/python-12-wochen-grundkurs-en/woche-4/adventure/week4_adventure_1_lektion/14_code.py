# Example 1: The Towers of Repetition
print("=== Searching the three towers ===")
for tower in range(1, 4):
    print(f"Tower {tower}:")
    for floor in range(1, 3):
        print(f"  Floor {floor} is being searched...")

# Example 2: A magical pattern
print("\n=== A pattern of stars ===")
for row in range(3):
    for col in range(4):
        print("⭐", end=" ")
    print()