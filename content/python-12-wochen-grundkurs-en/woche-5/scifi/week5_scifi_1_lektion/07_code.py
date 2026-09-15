# Example 2: Function with one parameter
def greet_pilot(name):
    """Greets a pilot by name"""
    print(f"Hello {name}!")
    print(f"Good luck on your mission, {name}!")

# Call the function with different names
print("=== Various Pilots ===")
greet_pilot("Alex")
greet_pilot("Zara")
greet_pilot("Nova")

print("\n=== What happens here? ===")
print("1. name is a placeholder for the passed value")
print("2. Each call passes a different name")
print("3. The function works with the passed value")