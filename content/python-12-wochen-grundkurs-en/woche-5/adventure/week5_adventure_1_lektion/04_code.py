# With vs. without parentheses
def greet_adventurer():
    """Greets a brave adventurer"""
    print("Welcome, brave hero!")

# WITH parentheses: function is executed
print("=== With parentheses greet_adventurer() ===")
greet_adventurer()

# WITHOUT parentheses: just a reference, nothing happens
print("\n=== Without parentheses greet_adventurer ===")
print("Type:", type(greet_adventurer))
print("(The function was not executed!)")