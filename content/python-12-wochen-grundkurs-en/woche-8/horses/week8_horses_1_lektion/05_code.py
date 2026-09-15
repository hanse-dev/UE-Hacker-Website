# Example 3: Changing and extending stable cards
horse = {
    "name": "Thunder",
    "breed": "Hanoverian",
    "age": 8
}

print(f"Original: {horse}")

# Change a value
horse["age"] = 9
print(f"After birthday: {horse}")

# Add a new element
horse["owner"] = "Anna"
print(f"After adding owner: {horse}")

# Remove an element
removed = horse.pop("breed")
print(f"Removed: {removed}")
print(f"After removal: {horse}")