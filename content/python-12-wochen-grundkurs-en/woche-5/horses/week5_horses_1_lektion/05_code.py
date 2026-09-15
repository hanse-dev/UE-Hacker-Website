# Argument becomes variable: step by step
def greet_rider(name):  # "name" is the parameter (placeholder)
    """Greets a rider by name"""
    # Inside the function, "name" is now a variable with the passed value!
    print(f"Inside the function: name = '{name}'")
    print(f"Hello {name}!")

# When calling: "Anna" is the argument
print("=== Call: greet_rider('Anna') ===")
greet_rider("Anna")  # → name becomes "Anna"

print("\n=== Call: greet_rider('Max') ===")
greet_rider("Max")  # → name becomes "Max"