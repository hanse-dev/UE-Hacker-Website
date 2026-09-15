# Example 3: Function without explicit return (None)
def show_inventory():
    """Shows the inventory (returns nothing)"""
    print("Your inventory:")
    print("  - Sword")
    print("  - Shield")
    print("  - Health potion")
    # No return – automatically returns None

print("=== Show Inventory ===")
result = show_inventory()
print(f"Return value: {result}")
print("Functions without return always return None!")