# Step 1: Ship list
ships = ["Nebula-Explorer", "Star-Fighter", "Nova-Hawk", "Iron-Wing", "Void-Runner"]
print(ships)

# Step 2: Add elements
ships.append("Shadow-Cruiser")
ships.insert(1, "Alpha-Scout")
print(ships)

# Step 3: Remove element
ships.remove("Iron-Wing")
print(ships)

# Step 4: Sort & search
ships.sort()
print(f"Sorted: {ships}")
print(f"Count: {len(ships)}")
if "Nova-Hawk" in ships:
    print(f"Nova-Hawk at index: {ships.index('Nova-Hawk')}")