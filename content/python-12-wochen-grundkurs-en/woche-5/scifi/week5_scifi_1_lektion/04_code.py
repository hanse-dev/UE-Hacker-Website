# With vs. without parentheses
def system_greeting():
    """Greets visitors on the space station"""
    print("Welcome aboard Nebula-7!")

# WITH parentheses: function is executed
print("=== With parentheses system_greeting() ===")
system_greeting()

# WITHOUT parentheses: only a reference, nothing happens
print("\n=== Without parentheses system_greeting ===")
print("Type:", type(system_greeting))
print("(The function was not executed!)")