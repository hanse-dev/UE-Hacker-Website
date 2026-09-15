# Example 3: Function with multiple parameters
def create_character(name, class_, level):
    """Creates a character with name, class and level"""
    print(f"Character created:")
    print(f"  Name: {name}")
    print(f"  Class: {class_}")
    print(f"  Level: {level}")
    print(f"  Status: Ready for adventure!")

# Create different characters
print("=== Character Creation ===")
create_character("Aria", "Mage", 5)
print()
create_character("Thorin", "Warrior", 8)
print()
create_character("Luna", "Rogue", 3)