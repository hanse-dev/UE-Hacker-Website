# Problem: missing return
def add(a, b):
    result = a + b
    return result  # This was missing!

total = add(5, 3)
print(f"Total: {total}")  # Now prints 8!