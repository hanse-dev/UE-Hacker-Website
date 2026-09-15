# Argument becomes a variable: step by step
def greet_pilot(name):  # "name" is the parameter (placeholder)
    """Greets a pilot by name"""
    # Inside the function, "name" is now a variable with the passed value!
    print(f"Inside the function: name = '{name}'")
    print(f"Hello {name}!")

# At the call: "Alex" is the argument
print("=== Call: greet_pilot('Alex') ===")
greet_pilot("Alex")  # → name becomes "Alex"

print("\n=== Call: greet_pilot('Zara') ===")
greet_pilot("Zara")  # → name becomes "Zara"