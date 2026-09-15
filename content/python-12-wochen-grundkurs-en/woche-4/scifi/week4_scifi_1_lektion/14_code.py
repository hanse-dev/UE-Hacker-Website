# Example 1: The sector scans
print("=== Scanning all decks ===")
for deck in range(1, 4):
    print(f"Deck {deck}:")
    for room in range(1, 3):
        print(f"  Room {room} is being scanned...")

# Example 2: A hologram pattern
print("\n=== A hologram pattern ===")
for row in range(3):
    for col in range(4):
        print("✨", end=" ")
    print()