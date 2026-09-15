# Example 2: Accessing stable cards
horse = {
    "name": "Thunder",
    "breed": "Hanoverian",
    "age": 8,
    "height": 1.72
}

print("=== Horse Access ===")
print(f"Horse name: {horse['name']}")
print(f"Breed: {horse['breed']}")
print(f"Age: {horse['age']} years")
print(f"Height: {horse['height']} m")

# With get() method (safer)
print(f"\nWith get(): {horse.get('name')}")
print(f"Not existing: {horse.get('gender', 'Unknown')}")