# Example 1: The training weeks
print("=== Going through the training plan ===")
for week in range(1, 4):
    print(f"Training week {week}:")
    for session in range(1, 3):
        print(f"  Session {session} is being completed...")

# Example 2: A pattern of hoofprints
print("\n=== A pattern of hoofprints ===")
for row in range(3):
    for col in range(4):
        print("🐴", end=" ")
    print()