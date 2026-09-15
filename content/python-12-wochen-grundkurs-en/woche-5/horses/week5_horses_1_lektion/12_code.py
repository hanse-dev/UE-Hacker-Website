# Example 3: Function without explicit return (None)
def show_equipment():
    """Shows the standard equipment (returns nothing)"""
    print("Your equipment:")
    print("  - Saddle")
    print("  - Bridle")
    print("  - Riding crop")
    # No return – automatically returns None

print("=== Show Equipment ===")
result = show_equipment()
print(f"Return value: {result}")
print("Functions without return always return None!")