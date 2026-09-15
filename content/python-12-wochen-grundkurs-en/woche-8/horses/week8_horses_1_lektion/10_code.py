# Example 3: Capsule unpacking and methods
horse_data = ("Thunder", "Hanoverian", 8, 1.72)

# Capsule unpacking
name, breed, age, height = horse_data
print("=== Capsule Unpacking ===")
print(f"Name: {name}")
print(f"Breed: {breed}")
print(f"Age: {age}")
print(f"Height: {height} m")

# Capsule methods
print(f"\nNumber of elements: {len(horse_data)}")
print(f"Index of 'Hanoverian': {horse_data.index('Hanoverian')}")
print(f"Count of 'Hanoverian': {horse_data.count('Hanoverian')}")