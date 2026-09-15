# Example 1: Different docstring styles
def simple_function():
    """This is a single-line docstring."""
    return "Simple"

def detailed_function(ship_name, fleet_id):
    """Creates a mission description.
    
    Args:
        ship_name (str): The name of the ship
        fleet_id (int): The fleet ID
    
    Returns:
        str: A formatted description
    """
    return f"{ship_name} belongs to fleet {fleet_id}."

# Accessing a docstring (this is how it works!)
print("=== Docstring Examples ===")
print(f"Simple docstring: {simple_function.__doc__}")
print()
print(f"Detailed docstring: {detailed_function.__doc__}")