# Example 1: Searching in lists
horses = ["Thunder", "Luna", "Storm", "Shadow", "Thunder", "Luna"]

print("=== Searching in Lists ===")
print(f"Horses list: {horses}")

# Find position with index()
position_luna = horses.index("Luna")
print(f"Luna at position: {position_luna}")

# Check if present with in
has_storm = "Storm" in horses
has_bobby = "Bobby" in horses
print(f"Storm present: {has_storm}")
print(f"Bobby present: {has_bobby}")

# Count with count()
count_thunder = horses.count("Thunder")
print(f"Number of Thunder: {count_thunder}")