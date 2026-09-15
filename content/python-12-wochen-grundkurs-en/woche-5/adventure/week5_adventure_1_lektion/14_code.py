# Example 1: Different docstring styles
def simple_function():
    """This is a one-line docstring."""
    return "Simple"

def detailed_function(name, level):
    """Creates a character description.
    
    Args:
        name (str): The name of the character
        level (int): The level of the character
    
    Returns:
        str: A formatted description
    """
    return f"{name} is a Level {level} character."

# Calling a docstring (this is how it works!)
print("=== Docstring Examples ===")
print(f"Simple docstring: {simple_function.__doc__}")
print()
print(f"Detailed docstring: {detailed_function.__doc__}")