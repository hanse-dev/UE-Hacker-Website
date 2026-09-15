# Example 3: Tuple unpacking and methods
ship_data = ("Nebula-Explorer", "Research", 150, 0.8)

# Tuple unpacking
name, type_, crew, speed = ship_data
print("=== Tuple Unpacking ===")
print(f"Name: {name}")
print(f"Type: {type_}")
print(f"Crew: {crew}")
print(f"Speed: {speed}")

# Tuple methods
print(f"\nNumber of elements: {len(ship_data)}")
print(f"Index of 'Research': {ship_data.index('Research')}")
print(f"Count of 'Research': {ship_data.count('Research')}")