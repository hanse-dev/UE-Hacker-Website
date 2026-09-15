# Example 2: Accessing list elements
equipment = ["Phaser", "Tricorder", "Communicator", "Med-Kit", "Tool"]

print("=== Equipment Access ===")
print(f"Full equipment: {equipment}")
print(f"First item: {equipment[0]}")
print(f"Second item: {equipment[1]}")
print(f"Last item: {equipment[-1]}")

# Length of the list
print(f"Number of items: {len(equipment)}")

# Slicing
print(f"First 3 items: {equipment[0:3]}")
print(f"Last 2 items: {equipment[-2:]}")