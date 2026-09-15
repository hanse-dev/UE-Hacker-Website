# Example 2: Function with one parameter
def greet_rider(name):
    """Greets a rider by name"""
    print(f"Hello {name}!")
    print(f"Good luck with your training, {name}!")

# Call the function with different names
print("=== Different riders ===")
greet_rider("Anna")
greet_rider("Max")
greet_rider("Lena")

print("\n=== What happens here? ===")
print("1. name is a placeholder for the passed value")
print("2. Each call passes a different name")
print("3. The function works with the passed value")