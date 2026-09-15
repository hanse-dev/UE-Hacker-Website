# Argument becomes variable: step by step
def greet_by_name(name):  # "name" is the parameter (placeholder)
    """Greets a hero by their name"""
    # Inside the function, "name" is now a variable with the passed value!
    print(f"In the function: name = '{name}'")
    print(f"Welcome, {name}!")

# When calling: "Aria" is the argument
print("=== Call: greet_by_name('Aria') ===")
greet_by_name("Aria")  # → name becomes "Aria"

print("\n=== Call: greet_by_name('Thorin') ===")
greet_by_name("Thorin")  # → name becomes "Thorin"