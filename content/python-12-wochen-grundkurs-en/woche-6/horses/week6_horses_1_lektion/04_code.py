# Example 2: Accessing list elements
equipment = ["Saddle", "Bridle", "Crop", "Saddle Pad", "Hoof Care"]

print("=== Equipment Access ===")
print(f"All equipment: {equipment}")
print(f"First item: {equipment[0]}")
print(f"Second item: {equipment[1]}")
print(f"Last item: {equipment[-1]}")

# Length of the list
print(f"Number of items: {len(equipment)}")

# Slicing (sections)
print(f"First 3 items: {equipment[0:3]}")
print(f"Last 2 items: {equipment[-2:]}")