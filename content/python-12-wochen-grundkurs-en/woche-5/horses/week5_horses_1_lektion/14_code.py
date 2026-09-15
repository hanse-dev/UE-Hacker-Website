# Example 1: Different docstring styles
def simple_function():
    """This is a one-line docstring."""
    return "Simple"

def detailed_function(horse_name, training_level):
    """Creates a training description.
    
    Args:
        horse_name (str): The name of the horse
        training_level (int): The training level of the horse
    
    Returns:
        str: A formatted description
    """
    return f"{horse_name} has training level {training_level}."

# Access docstring (this is how it works!)
print("=== Docstring Examples ===")
print(f"Simple docstring: {simple_function.__doc__}")
print()
print(f"Detailed docstring: {detailed_function.__doc__}")