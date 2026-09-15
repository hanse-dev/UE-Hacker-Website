# Step 1: Create horse list
horses = ["Thunder", "Luna", "Storm", "Bella", "Midnight"]
print(horses)

# Step 2: Add horses
horses.append("Silver")
horses.insert(2, "Star")
print(horses)

# Step 3: Remove a horse
horses.remove("Storm")
print(horses)

# Step 4: Sort and search
horses.sort()
print(horses)
print(f"Number of horses: {len(horses)}")
if "Luna" in horses:
    print(f"Luna is at position {horses.index('Luna')}")