# Example 2: Function with one parameter
def greet_by_name(name):
    """Greets a hero by their name"""
    print(f"Welcome, {name}!")
    print(f"Good luck on your journey, {name}!")

# Call the function with different names
print("=== Different heroes ===")
greet_by_name("Aria")
greet_by_name("Thorin")
greet_by_name("Luna")

print("\n=== What happens here? ===")
print("1. name is a placeholder for the passed value")
print("2. Each call passes a different name")
print("3. The function works with the passed value")