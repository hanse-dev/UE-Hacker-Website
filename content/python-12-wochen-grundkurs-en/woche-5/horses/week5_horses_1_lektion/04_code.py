# With vs. without parentheses
def greet_ranch():
    """Greets visitors at the riding ranch"""
    print("Welcome to Sunny Valley Riding Ranch!")

# WITH parentheses: function is executed
print("=== With parentheses greet_ranch() ===")
greet_ranch()

# WITHOUT parentheses: only a reference, nothing happens
print("\n=== Without parentheses greet_ranch ===")
print("Type:", type(greet_ranch))
print("(The function was not executed!)")