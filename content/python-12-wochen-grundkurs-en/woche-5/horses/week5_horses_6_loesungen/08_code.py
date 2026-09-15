# Problem: missing return
def add_training_units(units1, units2):
    total = units1 + units2
    return total  # This was missing!

total_training = add_training_units(5, 3)
print(f"Total training: {total_training}")  # Now prints 8!