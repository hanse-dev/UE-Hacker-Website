# Example 3: Modifying and extending dictionaries
ship = {
    "name": "Nebula-Explorer",
    "type": "Research",
    "crew": 150
}

print(f"Original: {ship}")

# Change a value
ship["crew"] = 200
print(f"After crew change: {ship}")

# Add a new entry
ship["captain"] = "Captain Alex"
print(f"After adding captain: {ship}")

# Remove an entry
removed = ship.pop("type")
print(f"Removed: {removed}")
print(f"After removal: {ship}")