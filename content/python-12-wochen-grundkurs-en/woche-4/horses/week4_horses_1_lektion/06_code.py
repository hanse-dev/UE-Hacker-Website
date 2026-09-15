# Example 4: For loop over a string
print("=== Example 4: Letters of a horse name ===")
name = "Thunder"
print(f"The horse name is: {name}")
print("Letter by letter:")

for letter in name:
    print(f"  - {letter}")

print("\n=== What happens here? ===")
print("String is treated as a sequence of letters")
print("Each letter is looped through individually")